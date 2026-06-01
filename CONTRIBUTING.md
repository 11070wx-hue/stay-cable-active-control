# Contributing

Contributions are welcome if they improve reproducibility, clarity, numerical
correctness, or documentation.

## Development setup

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

The Python package is intentionally small. Please keep examples runnable from a
fresh checkout and keep generated data out of commits unless the file is a small
summary needed for a documented benchmark.

## Preferred contributions

- corrected model equations or implementation details;
- MATLAB/Python examples that can be reproduced from a clean checkout;
- documentation for parameters, assumptions, and references;
- tests for numerical functions;
- improvements to code safety and maintainability.

## Development principles

1. Keep examples small and reproducible.
2. Document physical units for every parameter.
3. Separate model equations, controller design, and plotting scripts.
4. Avoid undocumented hard-coded constants.
5. Do not commit private data, credentials, or unpublished experimental data
   without permission.

## Pull request checklist

Before opening a pull request, please check that:

- the code runs from the repository root;
- required dependencies are documented;
- `python -m pytest` passes when Python code changes;
- scripts use clear parameter names and units;
- new examples include a short explanation;
- large generated result files are not committed unless necessary.

## Review expectations

For model or controller changes, please explain:

- which equation, assumption, or numerical method changed;
- how the change was verified;
- whether MATLAB and Python examples should remain equivalent;
- whether the change affects published benchmark numbers.

Small documentation-only pull requests are welcome and do not need a new test.
