---
mode: agent
description: Perform one safe refactor step for a Gilded Rose item type
---

# Refactor One Step (Gilded Rose)

You are helping refactor the Python Gilded Rose kata with TDD discipline.

## Inputs
- Item focus: `${input:itemType}`
- Optional failing test name: `${input:testName}`

## Constraints
- Only edit files under `python/` unless explicitly requested.
- Keep changes small and reversible.
- Preserve current behavior for all unaffected item types.
- Do not add third-party dependencies.

## Required Workflow
1. Identify one smallest safe code change for `${input:itemType}`.
2. Propose (or update) one focused test in `python/tests/test_gilded_rose.py`.
3. Implement the minimal code change in `python/gilded_rose.py`.
4. Explain how the change improves maintainability (design pattern or separation of concerns).
5. Provide commands to run:
   - single target test (if provided)
   - full suite: `python -m unittest`

## Output Format
- **Target**: item type and expected behavior
- **Test change**: what test is added/updated
- **Code change**: exact modification summary
- **Why this helps ETC**: 2-4 bullets
- **Run commands**: copy-paste commands
