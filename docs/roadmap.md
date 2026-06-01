# Roadmap

This roadmap tracks real maintenance work for the public repository. Dates are
targets and may shift as research priorities change.

## 0.1 - Public reproducible baseline

Status: in progress.

- [x] Public MIT-licensed repository.
- [x] Installable Python package.
- [x] Reduced nonlinear single-mode model.
- [x] LQR baseline example.
- [x] MATLAB open-loop parity example.
- [x] Pytest regression tests.
- [x] GitHub Actions CI for Python.
- [ ] First tagged release after CI is green on GitHub.

## 0.2 - Constrained control benchmarks

Target: June-July 2026.

- Add linear MPC example with actuator saturation.
- Add constrained MPC benchmark metrics.
- Document cost functions, constraints, and solver settings.
- Add tests for controller output dimensions and saturation behavior.

## 0.3 - Output feedback

Target: July-August 2026.

- Add Kalman filter and extended Kalman filter examples.
- Add partial-measurement benchmark cases.
- Document observability assumptions and measurement noise parameters.

## 0.4 - Robustness and uncertainty

Target: August-September 2026.

- Add parameter-uncertainty sweeps.
- Add disturbance benchmark cases.
- Add result-summary comparison scripts.
- Document expected failure modes and numerical tolerances.

## Later work

- Nonlinear MPC prototype.
- Reduced-order multimodal cable model.
- Time-delay and actuator dynamics.
- Experimental-data interface for future laboratory validation.
