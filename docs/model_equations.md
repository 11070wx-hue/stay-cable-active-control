# Model Equations

The first public benchmark uses a reduced single-mode stay-cable model. It is
intended for algorithm comparison and controller prototyping, not final bridge
design.

## State

The state is

```text
x = [q, q_dot]
```

where `q` is normalized modal displacement and `q_dot` is normalized modal
velocity.

## Normalized equation

```text
q_ddot + 2*xi*omega*q_dot
      + (omega^2 - a_p*cos(theta*t))*q
      + beta_2*q^2 + beta_3*q^3
    = f*cos(theta*t) + b*u
```

Parameters:

- `omega`: first modal circular frequency in rad/s.
- `xi`: modal damping ratio.
- `a_p`: parametric stiffness excitation amplitude.
- `theta`: excitation circular frequency in rad/s.
- `beta_2`, `beta_3`: reduced nonlinear stiffness coefficients.
- `f`: additive harmonic generalized force amplitude.
- `b`: actuator gain.
- `u`: active-control command.

The Python implementation is in `src/stay_cable_control/models.py`; the MATLAB
implementation is in `src/matlab/cable_state_rhs.m`.

## Current assumptions

- Single dominant cable mode.
- Normalized generalized coordinates.
- No sensor dynamics or control delay in the first benchmark.
- Additive and parametric excitation are deterministic harmonics.
- LQR is designed from the constant zero-state linearization.

These assumptions are intentionally narrow so the first benchmark is auditable.
The roadmap tracks extensions for constrained MPC, output feedback, uncertainty,
and multimodal models.
