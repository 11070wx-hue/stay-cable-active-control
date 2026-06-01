# Stay Cable Active Control

[![Python CI](https://github.com/11070wx-hue/stay-cable-active-control/actions/workflows/python-ci.yml/badge.svg)](https://github.com/11070wx-hue/stay-cable-active-control/actions/workflows/python-ci.yml)

Open-source MATLAB/Python research code for active vibration control of stay
cables. The project provides small, inspectable benchmark models for nonlinear
cable dynamics, controller prototyping, state estimation, and reproducible
structural-control studies.

This repository is early-stage research software. It is not a certified bridge
design tool, but it is maintained as a transparent baseline that other students
and researchers can run, audit, and extend.

## Why this project matters

Stay cables are long, flexible, lightly damped structural members. Their
vibration control is difficult because of nonlinear dynamics, parametric
excitation, uncertain parameters, actuator limits, time delay, and incomplete
state measurement. Published control methods are often hard to compare because
model assumptions, parameter choices, and numerical workflows are scattered
across papers or private scripts.

This repository addresses that gap by keeping reduced-order models, examples,
tests, documentation, and planned benchmarks in one public place.

## Current modules

- Reduced nonlinear single-mode stay-cable model with additive and parametric
  excitation terms.
- Python simulation helpers based on `scipy.integrate.solve_ivp`.
- Continuous-time LQR baseline controller for the linearized model.
- Reproducible Python and MATLAB open-loop examples.
- Pytest coverage for dynamics, simulation, and controller behavior.
- GitHub Actions workflow for Python tests on every push and pull request.

## Repository structure

```text
stay-cable-active-control/
|-- .github/                  # CI workflow and issue templates
|-- docs/                     # Equations, maintenance notes, roadmap
|-- examples/
|   |-- matlab/               # MATLAB runnable examples
|   `-- python/               # Python runnable examples
|-- results/                  # Small generated summaries; no large raw data
|-- src/
|   |-- matlab/               # MATLAB model functions
|   |-- python/               # Backward-compatible early module path
|   `-- stay_cable_control/   # Installable Python package
|-- tests/                    # Python regression tests
|-- CITATION.cff
|-- CONTRIBUTING.md
|-- LICENSE
|-- SECURITY.md
|-- pyproject.toml
`-- README.md
```

## Quick start: Python

```bash
python -m pip install -e ".[dev]"
python -m pytest
python examples/python/run_open_loop_demo.py
```

The example writes a small CSV summary to `results/open_loop_summary.csv` and
prints the open-loop and LQR-controlled displacement metrics.

## Quick start: MATLAB

Open MATLAB at the repository root and run:

```matlab
run('examples/matlab/run_open_loop_demo.m');
```

## Documentation

- [Model equations](docs/model_equations.md)
- [Reproducibility guide](docs/reproducibility.md)
- [Roadmap](docs/roadmap.md)
- [Maintainer guide](docs/MAINTAINER_GUIDE.md)

## Maintainer focus

The maintainer is currently using this repository to support graduate research
on active control of stay-cable vibration in bridge engineering. Near-term work
prioritizes reproducible examples, model documentation, constrained MPC,
Kalman-filter-based output feedback, uncertainty benchmarks, and safe automation
for code review and maintenance.

Security and quality work are tracked through `SECURITY.md`, GitHub Issues,
pytest, and the Python CI workflow. Contributions that improve correctness,
documentation, tests, or reproducibility are welcome.

## License

This project is released under the MIT License.

## Citation

If this repository supports your academic work, please cite it using the
metadata in `CITATION.cff`.
