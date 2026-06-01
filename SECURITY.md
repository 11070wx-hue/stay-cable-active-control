# Security Policy

## Supported project status

This is an early-stage open-source academic research repository. The codebase is maintained for reproducible numerical simulation, documentation, and research use.

## Reporting a vulnerability

If you find a security issue, unsafe dependency, or risky automation pattern in this repository, please open a GitHub issue with a clear description. Avoid publishing sensitive exploit details in public issue text if the issue could affect users directly.

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

This policy covers repository code, examples, documentation, dependency files, and future CI workflows. It does not cover third-party software beyond the dependency declarations used by this repository.
