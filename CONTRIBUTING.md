# Contributing

Contributions are welcome if they improve reproducibility, clarity, numerical correctness, or documentation.

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
5. Do not commit private data, credentials, or unpublished experimental data without permission.

## Pull request checklist

Before opening a pull request, please check that:

- the code runs from the repository root;
- required dependencies are documented;
- scripts use clear parameter names and units;
- new examples include a short explanation;
- large generated result files are not committed unless necessary.
