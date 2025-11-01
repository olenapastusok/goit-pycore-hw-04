## Repo snapshot

This repository contains small, single-file Python exercises organized under `Exercise 1/` through `Exercise 4/`.
Each exercise is a standalone script with any input data kept in the same folder (for example `Exercise 1/month_salary.txt`, `Exercise 2/information_about_cats.txt`).

## What the AI agent should know

- Purpose: these are educational/homework scripts — changes should preserve the script entrypoint (`main.py`) and the text-file inputs unless you intend to modify behavior and update README.
- Structure: each exercise folder is a self-contained script+data pair. There is no package layout, no tests, and no requirements file.
- Runtime: scripts are plain Python (standard library). Run with the system Python (e.g. `python3 Exercise 1/main.py`). If you add external deps, add a `requirements.txt` and update `README.md`.

## Patterns and examples to reference

- File I/O: scripts read local text files in their folder. Example: `Exercise 1/month_salary.txt` is read by `Exercise 1/main.py`.
- Single-file entrypoint: each exercise uses a `main.py`; preserve that entrypoint when editing or adding features.
- Visualization: `Exercise 3/visualization.py` contains plotting logic — avoid changing data file locations; prefer adding parameters to control behaviour rather than hard-coding new paths.

## Developer workflows (how to run and verify quickly)

- Run a script locally: `python3 Exercise X/main.py` (replace X with 1..4).
- Inspect or modify input data in the same folder (e.g., `Exercise 2/information_about_cats.txt`) when testing changes.
- No CI/tests present — for any change that affects outputs, run the corresponding `main.py` manually to verify.

## Conventions and expectations for PRs

- Keep changes minimal and well-scoped: these are exercise solutions. If you refactor, keep behaviour identical unless the PR explicitly states a behavior change.
- Add `requirements.txt` only if you introduce third-party packages and document how to create a virtualenv in `README.md`.

## Integration points and external deps

- There are no external services or APIs. Communication patterns are local file IO and stdout. Treat input files in each `Exercise` folder as part of the contract.

## Helpful pointers for edits

- When changing how a script reads a file, update the sample data file in the same folder and add a short note to `README.md` describing the new behaviour.
- Preserve UTF-8 file handling when reading/writing text files (use explicit encoding if adding code).
- If you add tests, place them in a new top-level `tests/` folder and keep them simple (pytest-compatible) and include instructions in `README.md`.

---

If any of these points are unclear or you want the instructions to be more prescriptive (for example, adding a standard venv setup or test runner), tell me which parts you want expanded and I will update this file.
