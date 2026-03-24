# Copilot Instructions for Gilded Rose Refactoring Kata

## Project Context
- This repository contains many language variants; for this lab, prioritize the Python implementation under `python/`.
- We are refactoring legacy code in `python/gilded_rose.py` using test-driven development.
- Keep behavior compatible with existing tests unless the user explicitly asks to change requirements.

## Primary Goals
- Make code easier to change (ETC): modular, readable, and maintainable.
- Prefer small safe refactors over large rewrites.
- Preserve item rules from the Gilded Rose requirements.

## Development Rules
- Do not modify the `Item` data shape unless explicitly requested.
- Prefer design patterns that reduce nested conditionals (Strategy is preferred in this kata).
- Keep quality bounds consistent:
  - Normal bounds are `0..50`.
  - `Sulfuras` remains `80` and does not change.
- Keep changes focused and minimal per step.

## Testing Expectations
- Before changes: add/adjust tests in `python/tests/test_gilded_rose.py`.
- During changes: run a narrow scope test first, then full test suite.
- After changes: run all tests via `python -m unittest` from the `python/` directory.

## Output Expectations for Copilot
- When suggesting code, include:
  1. A short rationale (1-3 bullets)
  2. Exact files to edit
  3. Small patch-style steps
- Avoid introducing new dependencies for this Python kata.
- If uncertain, ask one concise clarifying question instead of guessing.
