# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository

A personal collection of standalone LeetCode/NeetCode solutions in Python. There is no build system, package manifest, test suite, or linter; each file is self-contained and run directly (e.g. `python3 "python/strings+arrays/two_sum.py"`).

## Layout

- `python/` — Python solutions, grouped by topic subfolder:
  - `strings+arrays/` — general string/array problems (flat), named in snake_case without a number (`two_sum.py`, `robots.py`).
  - `Hash Map - Cannonocal Key/` — hash-map problems that group by a canonical key, split into `Easy/` and `Medium/`. Files are prefixed with the LeetCode number (`242_valid_anagram.py`, `49_group_anagrams.py`).

## Conventions

- Files in `strings+arrays/` begin with a docstring header: Description (with difficulty `Category : easy`), Constraints, Input/Output, and Examples, followed by the solution. Some files (e.g. `robots.py`) use `#` comments instead, with a `# Solution ---` separator before the code.
- Files in `Hash Map - Cannonocal Key/` use a docstring with `Title`, `Description`, `Examples`, `Constraints`, and `Pseudocode` sections, followed by the solution.
- Match the style of neighbouring files when adding a new solution.
