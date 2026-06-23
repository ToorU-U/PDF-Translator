# Agent Development Guide

This file defines how AI agents collaborate on this repository. Project requirements and architecture belong in `docs/`.

## Git Workflow

- Inspect `git status` and relevant diffs before editing or staging.
- Preserve unrelated user changes and stage only files in the agreed scope.
- Do not change remotes or rewrite shared history without explicit approval.
- Commit and push only when the user explicitly requests publication.

## Branch Strategy

- Start each feature or maintenance task from the current default branch unless directed otherwise.
- Use a short-lived branch named `codex/<concise-description>`.
- Keep one coherent change set per branch; do not mix unrelated work.

## Commit Strategy

- Make focused commits that leave the repository in a reviewable state.
- Use concise, imperative commit messages that describe the completed change.
- Review the staged diff before committing and never include generated or unrelated files by accident.

## PR Strategy

- Push the feature branch with upstream tracking.
- Open a Draft PR unless the user explicitly requests a ready-for-review PR.
- Summarize what changed, why it changed, its impact, and the validation performed.
- Keep the PR limited to the stated task.

## Review Workflow

- Run checks appropriate to the change before requesting review.
- Report failed or skipped checks honestly.
- At a requested review gate, stop after opening the Draft PR and wait for feedback.
- Address review comments in focused follow-up commits; do not begin the next milestone without approval.

## Communication Rules

- State scope, assumptions, and material risks clearly.
- Give concise progress updates while working and a self-contained completion summary.
- Ask before taking actions that expand scope, discard work, rewrite history, or change external state beyond the request.
- Never claim that work, validation, publication, or review is complete unless it has succeeded.

## Development Session Checklist

### Start

- [ ] Read the repository documentation relevant to the task.
- [ ] Inspect the current branch, working tree, and recent history.
- [ ] Confirm the requested scope and identify unrelated local changes.

### During development

- [ ] Keep changes focused on the requested outcome.
- [ ] Follow existing conventions and update documentation when responsibilities change.
- [ ] Run proportionate checks and review the resulting diff.

### Finish

- [ ] Confirm the working tree contains only expected changes.
- [ ] Commit, push, and open a Draft PR only when requested.
- [ ] Report the branch, commit, PR, and validation status.
- [ ] Stop at any requested review gate.
