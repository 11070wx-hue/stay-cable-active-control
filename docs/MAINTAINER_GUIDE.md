# Maintainer Guide

This project is maintained as open academic research software for stay-cable
vibration control. The goal is to make numerical work easier to inspect, reuse,
and improve.

## Maintenance priorities

1. Keep examples runnable from a clean checkout.
2. Keep model equations and code implementations aligned.
3. Add tests before expanding shared control or simulation utilities.
4. Review dependency changes for security and reproducibility.
5. Keep issues small enough for students or external contributors to pick up.

## Issue triage

- `bug`: incorrect behavior, failed reproducibility, or broken examples.
- `documentation`: unclear equations, assumptions, installation, or usage.
- `enhancement`: new controller, benchmark, or quality-of-life improvement.
- `good first issue`: small documentation, test, or example task.

When a bug report changes benchmark behavior, ask for the environment, command,
parameter set, expected result, and observed result.

## Use of automation

Automation may be used for:

- dependency and CI review;
- checking for unsafe patterns or accidental credentials;
- drafting tests and documentation;
- reviewing numerical-code readability;
- summarizing issue and pull-request history.

Automation should not be used to fabricate results, citations, users, or
validation claims. Engineering claims should remain traceable to code,
benchmarks, documentation, or published references.

## Release checklist

1. Confirm `python -m pytest` passes locally and in GitHub Actions.
2. Run the Python and MATLAB examples.
3. Update `CITATION.cff` version/date when publishing a release.
4. Update `docs/ROADMAP.md`.
5. Tag the release only after benchmark changes are documented.
