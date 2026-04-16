# llm-knowledge-base (arturseo-geo)

**Source:** https://github.com/arturseo-geo/llm-knowledge-base
**Stars:** 26 | **License:** MIT

## Description

Standardized schema and workflow for building LLM-compiled personal knowledge bases. Adds a learning layer that Karpathy's original workflow omits: flashcards, spaced repetition, gap tracking, and Socratic Q&A.

## Core Features

**Schema & Structure:**
- `AGENTS.md` spec defining directory layouts, frontmatter standards, compilation workflows
- Three index files: `_index.md`, `_concepts.md`, `_graph.md`
- Sandbox-first promotion model preventing quality degradation

**Learning Layer:**
- Automated flashcard generation on concept create/update
- Spaced repetition queue (simplified FSRS algorithm)
- Gap tracking for open questions and weak spots
- Socratic Q&A mode (LLM quizzes users against wiki)

**Knowledge Organization:**
```
raw/ → [LLM compile] → wiki/ → [query/output] → reports/slides/figures
                        ↓
                      learning/ (review queue, flashcards, gaps)
```

**Quality Rules:**
- No orphaned articles (detected via linting)
- Confidence thresholds for graph promotion
- Contradictory articles quarantined
- Citation tracking with no hallucinated sources

## Architecture — Two-Vault Setup

- Agent vault: Full schema, LLM-generated content
- Personal vault: Human-only notes (preserves signal-to-noise)

## What Makes It Unique

- Learning layer with spaced repetition (unique among LLM wiki implementations)
- Sandbox-first promotion model
- Finetune path: flashcard Q&A pairs for supervised fine-tuning
- Two-vault contamination prevention
- Schema versioned (1.1.0) with breaking-change major increments
- Haiku-optimized linting for cost efficiency
