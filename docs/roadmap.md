# Roadmap

This roadmap describes the intended development path for the repository.

## Stage 1: Reproducible baseline

- Maintain a clear repository structure.
- Provide small MATLAB and Python examples.
- Document all model assumptions and units.
- Keep dependencies minimal.

## Stage 2: Baseline active control

- Add an LQR controller for the reduced cable model.
- Add controller comparison metrics such as peak displacement, RMS displacement, and maximum control force.
- Add scripts for open-loop and closed-loop comparison.

## Stage 3: Constrained MPC

- Add linear MPC examples with input-force constraints.
- Add control-rate constraints.
- Compare constrained MPC with unconstrained LQR under identical disturbance cases.

## Stage 4: Output-feedback control

- Add Kalman filtering or extended Kalman filtering for partial-state measurement.
- Couple state estimation with MPC.
- Study the influence of sensor noise and incomplete measurement.

## Stage 5: Robustness and uncertainty

- Add parameter perturbation scripts.
- Study damping, stiffness, and nonlinear coefficient uncertainty.
- Build reproducible benchmark cases.

## Stage 6: Higher-fidelity models

- Extend from single-mode to multimodal reduced models.
- Prepare interfaces for finite-difference or finite-element data.
- Prepare experimental-data input templates for future laboratory validation.
