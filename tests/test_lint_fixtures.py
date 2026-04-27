from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Callable


REPO_ROOT = Path(__file__).resolve().parents[1]
LINT = REPO_ROOT / "wiki-base/scripts/wiki-lint.py"


def run_lint(vault: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(LINT), "--vault", str(vault), *args],
        check=False,
        text=True,
        capture_output=True,
    )


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def replace_in(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise AssertionError(f"fixture text not found in {path}: {old!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def make_clean_vault(root: Path) -> Path:
    raw_body = "Fixture source body.\n"
    raw_hash = hashlib.sha256(raw_body.encode("utf-8")).hexdigest()
    write(root / "raw/test-source.md", raw_body)

    write(
        root / "wiki/sources/Test Source.md",
        f"""---
type: source-summary
raw_path: "raw/test-source.md"
raw_hash: "{raw_hash}"
sources: []
created: "2026-04-21"
updated: "2026-04-21"
status: current
tags: []
---

> [!tldr]
> Test source fixture.

## Key Takeaways

> [!source]
> Fixture source body.
""",
    )
    write(
        root / "wiki/entities/Test Entity.md",
        """---
type: entity
entity_type: "tool"
aliases:
  - TE
sources:
  - "[[Test Source]]"
created: "2026-04-21"
updated: "2026-04-21"
status: current
tags: []
---

> [!tldr]
> Test entity fixture.

## Overview

> [!source]
> Test entity appears in [[Test Source]].
""",
    )
    write(
        root / "wiki/concepts/Test Concept.md",
        """---
type: concept
sources:
  - "[[Test Source]]"
created: "2026-04-21"
updated: "2026-04-21"
status: current
tags: []
---

> [!tldr]
> Test concept summarizes the fixture.

## Key Claims

> [!source]
> Fixture claim cites [[Test Source]].

> [!analysis]
> The fixture links [[Test Entity]] because the source names it.
""",
    )
    write(
        root / "wiki/index.md",
        """# Wiki Index

## Entities
- [[Test Entity]] (1) - Test entity fixture.

## Concepts
- [[Test Concept]] (1) - Test concept summarizes the fixture.

## Sources
- [[Test Source]] (0) - Test source fixture.

## Comparisons
""",
    )
    write(root / "wiki/log.md", "# Wiki Log\n")
    write(root / "wiki/conventions.md", "# Wiki Conventions\n")
    return root


class LintFixtureTests(unittest.TestCase):
    def assert_finding(
        self,
        mutate: Callable[[Path], None],
        category: str,
        *lint_args: str,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            vault = make_clean_vault(Path(tmpdir))
            mutate(vault)
            result = run_lint(vault, *lint_args)
            output = result.stdout + result.stderr
            self.assertNotEqual(result.returncode, 0, output)
            self.assertIn(f"## {category}", output)

    def test_clean_fixture_passes_real_linter(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            vault = make_clean_vault(Path(tmpdir))
            result = run_lint(vault)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_frontmatter_defect_is_reported(self) -> None:
        self.assert_finding(
            lambda v: replace_in(
                v / "wiki/concepts/Test Concept.md",
                "status: current\n",
                "",
            ),
            "frontmatter",
            "--category",
            "frontmatter",
        )

    def test_tldr_defect_is_reported(self) -> None:
        self.assert_finding(
            lambda v: replace_in(
                v / "wiki/concepts/Test Concept.md",
                "> [!tldr]\n> Test concept summarizes the fixture.\n",
                "Test concept summary without a callout.\n",
            ),
            "tldr",
        )

    def test_filename_defect_is_reported(self) -> None:
        def mutate(vault: Path) -> None:
            (vault / "wiki/concepts/Test Concept.md").rename(
                vault / "wiki/concepts/test concept.md"
            )

        self.assert_finding(mutate, "filename", "--category", "filenames")

    def test_unresolved_wikilink_defect_is_reported(self) -> None:
        self.assert_finding(
            lambda v: replace_in(
                v / "wiki/concepts/Test Concept.md",
                "> The fixture links [[Test Entity]] because the source names it.\n",
                "> The fixture links [[Missing Page]] because the source names it.\n",
            ),
            "unresolved-link",
            "--category",
            "wikilinks",
        )

    def test_missing_index_entry_is_reported(self) -> None:
        self.assert_finding(
            lambda v: replace_in(
                v / "wiki/index.md",
                "- [[Test Concept]] (1) - Test concept summarizes the fixture.\n\n",
                "",
            ),
            "index",
            "--category",
            "index",
        )

    def test_dead_index_entry_is_reported(self) -> None:
        self.assert_finding(
            lambda v: replace_in(
                v / "wiki/index.md",
                "## Comparisons\n",
                "## Comparisons\n- [[Ghost Page]] (0) - Missing.\n",
            ),
            "index",
            "--category",
            "index",
        )

    def test_index_source_count_mismatch_is_reported(self) -> None:
        self.assert_finding(
            lambda v: replace_in(
                v / "wiki/index.md",
                "- [[Test Concept]] (1) - Test concept summarizes the fixture.",
                "- [[Test Concept]] (2) - Test concept summarizes the fixture.",
            ),
            "index",
            "--category",
            "index",
        )

    def test_index_tldr_mismatch_is_reported(self) -> None:
        self.assert_finding(
            lambda v: replace_in(
                v / "wiki/index.md",
                "Test concept summarizes the fixture.",
                "Different TLDR.",
            ),
            "index",
            "--category",
            "index",
        )

    def test_sources_invariant_defect_is_reported(self) -> None:
        def mutate(vault: Path) -> None:
            replace_in(
                vault / "wiki/concepts/Test Concept.md",
                'sources:\n  - "[[Test Source]]"\n',
                "sources: []\n",
            )
            replace_in(
                vault / "wiki/index.md",
                "- [[Test Concept]] (1) - Test concept summarizes the fixture.",
                "- [[Test Concept]] (0) - Test concept summarizes the fixture.",
            )

        self.assert_finding(mutate, "sources-invariant", "--category", "sources-invariant")

    def test_alias_collision_defect_is_reported(self) -> None:
        self.assert_finding(
            lambda v: replace_in(
                v / "wiki/entities/Test Entity.md",
                "  - TE\n",
                "  - TE\n  - Test Concept\n",
            ),
            "aliases",
            "--category",
            "aliases",
        )

    def test_hash_drift_defect_is_reported(self) -> None:
        self.assert_finding(
            lambda v: write(v / "raw/test-source.md", "Changed source body.\n"),
            "hash-drift",
            "--category",
            "hash-drift",
        )

    def test_bare_claim_defect_is_reported(self) -> None:
        self.assert_finding(
            lambda v: replace_in(
                v / "wiki/concepts/Test Concept.md",
                "## Key Claims\n",
                "## Key Claims\n\nThis untyped paragraph states a factual claim outside a callout.\n",
            ),
            "bare-claim-candidate",
            "--category",
            "bare-claims",
        )

    def test_rebuild_index_regenerates_cache(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            vault = make_clean_vault(Path(tmpdir))
            write(vault / "wiki/index.md", "# Wiki Index\n\n## Entities\n")

            rebuilt = run_lint(vault, "--rebuild-index")
            self.assertEqual(rebuilt.returncode, 0, rebuilt.stdout + rebuilt.stderr)

            index = (vault / "wiki/index.md").read_text(encoding="utf-8")
            self.assertIn("[[Test Entity]] (1)", index)
            self.assertIn("[[Test Concept]] (1)", index)
            self.assertIn("[[Test Source]] (0)", index)

            result = run_lint(vault)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_briefing_output_shape(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            vault = make_clean_vault(Path(tmpdir))
            write(
                vault / "wiki/dashboard.md",
                """---
type: meta
sources: []
created: "2026-04-20"
updated: "2026-04-20"
status: current
tags: []
---

> [!tldr]
> Dashboard.
""",
            )
            write(
                vault / "wiki/log.md",
                "# Wiki Log\n\n"
                "### [2026-04-21] ingest | Fixture source\n"
                "### [2026-04-22] query | Fixture question\n",
            )
            write(
                vault / "wiki/backlog.md",
                """---
type: meta
sources: []
created: "2026-04-21"
updated: "2026-04-21"
status: current
tags: []
---

> [!tldr]
> Backlog.

## Open

| # | Question or claim | Surfaced from | Priority | Review By | Status |
|---|-------------------|---------------|----------|-----------|--------|
| 1 | Fixture gap | [[Test Concept]] | high | 2026-04-30 | open |
""",
            )
            write(
                vault / "wiki/handoff.md",
                """---
type: meta
sources: []
created: "2026-04-21"
updated: "2026-04-21"
status: current
tags: []
---

> [!tldr]
> Handoff.

## Last Session

### [2026-04-22] fixture work
- Worked on: fixture.

## In Progress

*Nothing in progress.*

## Blocked

*Nothing blocked.*

## Open Questions

*No open questions.*
""",
            )

            before = {
                path.relative_to(vault): path.read_bytes()
                for path in vault.rglob("*")
                if path.is_file()
            }
            result = run_lint(vault, "--briefing")
            after = {
                path.relative_to(vault): path.read_bytes()
                for path in vault.rglob("*")
                if path.is_file()
            }

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(before, after)
            self.assertIn("wiki-briefing:", result.stdout)
            self.assertIn("- pages:", result.stdout)
            self.assertIn("- recent ingests/queries:", result.stdout)
            self.assertIn("[2026-04-21] ingest | Fixture source", result.stdout)
            self.assertIn("dashboard freshness: stale", result.stdout)
            self.assertIn("- backlog:", result.stdout)
            self.assertIn("Fixture gap", result.stdout)
            self.assertIn("- handoff:", result.stdout)
            self.assertIn("Last Session:", result.stdout)

    def test_briefing_reports_template_dashboard_date(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            vault = make_clean_vault(Path(tmpdir))
            write(
                vault / "wiki/dashboard.md",
                """---
type: meta
sources: []
created: "{{date}}"
updated: "{{date}}"
status: current
tags: []
---

> [!tldr]
> Dashboard.
""",
            )

            result = run_lint(vault, "--briefing")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("dashboard freshness: template", result.stdout)
            self.assertIn("{{date}} placeholder", result.stdout)


if __name__ == "__main__":
    unittest.main()
