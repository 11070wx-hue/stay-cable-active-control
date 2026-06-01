# Security Policy

## Supported project status

This is an early-stage open-source academic research repository. The codebase is
maintained for reproducible numerical simulation, documentation, and research
use.

## Reporting a vulnerability

If you find a security issue, unsafe dependency, or risky automation pattern in
this repository, please open a GitHub issue with a clear description. If the
issue could expose sensitive information or directly affect users, avoid posting
exploit details publicly and contact the maintainer through the GitHub profile
or a private security advisory if that option is available.

Please include:

- affected file or dependency;
- steps to reproduce the issue;
- possible impact;
- suggested mitigation, if known.

## Security goals

The project aims to keep the repository safe for researchers and students by:

- avoiding hard-coded credentials or tokens;
- keeping dependencies minimal and documented;
- reviewing automation scripts before use;
- avoiding unsafe file-system or shell operations;
- separating research data from source code when needed.

## Scope

This policy covers repository code, examples, documentation, dependency files,
and CI workflows. It does not cover third-party software beyond the dependency
declarations used by this repository.
