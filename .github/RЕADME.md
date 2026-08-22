# About the `.github` Folder

> [!IMPORTANT]
> Do **not** modify or delete the `.github/` folder or any files in it. This
> folder is for repository administration. It is not part of the student
> procedures for this assignment.

## What Is Here?

This repository uses `.github/` for GitHub-specific configuration:

- `ISSUE_TEMPLATE/` — forms for reporting a repository problem or requesting
  an improvement
- `ci/` — validation scripts used by the active Assignment Checks workflow
- `workflows/tests.yml` — active repository and assignment-artifact checks
- `workflows/external-links.yml` — manual and scheduled external Markdown link
  checking
- `workflows/tests.yml.disabled` — intentionally disabled optional Python
  practice tests
- `social-preview.png` — the repository social preview image

These files support the repository itself. They are not assignment deliverables.

## Automated Repository Checks

The active **Assignment Checks** workflow runs when changes are pushed to the
repository. It validates the repository structure and the basic
completion state of the graded pseudocode without grading the quality of the
student's design.

The optional Python program and optional acceptance tests are **not required**
for the Module Four Assignment check.

The **External Links** workflow checks external links in Markdown files. Its
weekly scheduled run is limited to the canonical `GC-STEM` course repository
so personal repositories created from the template do not each run a weekly
external-link crawl. The workflow can still be run manually when needed.

## Issue or Assignment Question?

Use a GitHub Issue for a technical problem with the provided repository,
documentation, starter files, or course tools.

Do **not** use an Issue to request or post a completed solution to the graded
pseudocode.

Questions about assignment requirements, grading, submissions, deadlines,
accommodations, or instructor feedback belong with your instructor in D2L
Brightspace.
