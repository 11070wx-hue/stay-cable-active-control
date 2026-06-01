# Stay Cable Active Control

Open-source MATLAB/Python research code for active vibration control of stay cables. The repository is intended to support reproducible academic studies on nonlinear cable dynamics, active control algorithms, constrained control, and state estimation.

## Scope

This project focuses on numerical models and control workflows for stay-cable vibration control in bridge engineering. The initial codebase starts from a reduced single-mode cable model and will be extended toward constrained MPC, output-feedback control, robust/data-driven control, and experimental validation scripts.

The current repository is early-stage but structured for continuous maintenance and reproducible research.

## Current and planned modules

- Nonlinear single-mode stay-cable vibration model with parametric excitation.
- Open-loop simulation examples in MATLAB and Python.
- LQR baseline controller for comparison studies.
- Linear MPC and constrained MPC examples.
- Kalman filtering / extended Kalman filtering for partial-state measurement.
- Parameter-uncertainty and robustness test scripts.
- Documentation for model equations, assumptions, and reproducibility.

## Repository structure

```text
stay-cable-active-control/
├── src/
│   ├── matlab/          # MATLAB model and control functions
│   └── python/          # Python model and simulation functions
├── examples/
│   ├── matlab/          # MATLAB runnable examples
│   └── python/          # Python runnable examples
├── docs/                # Model notes, roadmap, and implementation details
├── results/             # Placeholder for reproducible figures and benchmark outputs
├── SECURITY.md          # Security and responsible disclosure policy
├── CONTRIBUTING.md      # Contribution guide
├── CITATION.cff         # Citation metadata
├── requirements.txt     # Python dependencies
└── README.md
```

## Quick start: Python

```bash
pip install -r requirements.txt
python examples/python/run_open_loop_demo.py
```

## Quick start: MATLAB

Open MATLAB at the repository root and run:

```matlab
addpath(genpath('src/matlab'));
run('examples/matlab/run_open_loop_demo.m');
```

## Scientific positioning

Stay cables are long, flexible, lightly damped structural members. Their vibration control is difficult because of nonlinear dynamics, modal coupling, uncertain parameters, actuator limits, time delay, and incomplete state measurement. This repository is designed to provide a transparent computational baseline for testing active control strategies under these constraints.

The project does not claim to be a validated engineering design tool at this stage. It is a research codebase for reproducible algorithm development.

## Roadmap

1. Implement and document the reduced nonlinear single-mode cable equation.
2. Add LQR and constrained linear MPC baselines.
3. Add Kalman-filter-based output-feedback MPC.
4. Add uncertainty and disturbance benchmark cases.
5. Extend to nonlinear MPC and reduced-order multimodal cable models.
6. Prepare experimental-data interfaces for future laboratory validation.

## License

This project is released under the MIT License.

## Citation

If this repository supports your academic work, please cite it using the metadata in `CITATION.cff`.
