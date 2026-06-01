# Model Notes

## Purpose

This document records the current modeling assumptions used in the repository. The aim is to keep the numerical examples transparent and reproducible.

## Reduced single-mode model

The initial examples use a reduced single-degree-of-freedom modal equation for stay-cable vibration:

```text
y_ddot + 2 xi omega y_dot + omega^2 y + beta2 y^2 + beta3 y^3 = f(t) + u(t)
```

where:

- `y` is the generalized modal displacement;
- `omega` is the first modal circular frequency;
- `xi` is the damping ratio;
- `beta2` and `beta3` represent reduced nonlinear stiffness terms;
- `f(t)` is a normalized external excitation;
- `u(t)` is a normalized generalized active control force.

## Why start from a reduced model?

A reduced model is useful for early controller verification because it makes the influence of controller structure, actuator constraints, state estimation, and parameter uncertainty easier to inspect. It is not a substitute for a full cable or cable-bridge model.

## Planned extensions

- Replace placeholder coefficients with documented cable parameters.
- Add parametric excitation terms for main-resonance studies.
- Add LQR, constrained MPC, and output-feedback MPC examples.
- Add uncertainty scans and reproducibility scripts for benchmark figures.
- Extend from single-mode dynamics to reduced multimodal models.
