"""Reduced-order stay-cable dynamics.

The model is intentionally compact: it is a transparent single-mode benchmark
for controller prototyping, not a certified bridge design model.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Sequence

import numpy as np

ControlInput = float | Callable[[float, np.ndarray], float]


@dataclass(frozen=True)
class CableParameters:
    """Physical and reduced-order parameters for a single-mode cable model.

    Attributes:
        omega: First modal circular frequency in rad/s.
        damping_ratio: Modal damping ratio.
        quadratic_stiffness: Normalized quadratic nonlinear stiffness.
        cubic_stiffness: Normalized cubic nonlinear stiffness.
        parametric_stiffness: Amplitude of time-varying stiffness excitation.
        excitation_amplitude: Additive generalized harmonic excitation.
        excitation_frequency: Excitation circular frequency in rad/s.
        actuator_gain: Normalized gain from control input to modal acceleration.
    """

    omega: float = 1.6425
    damping_ratio: float = 0.001
    quadratic_stiffness: float = 0.0
    cubic_stiffness: float = 0.05
    parametric_stiffness: float = 0.0
    excitation_amplitude: float = 0.02
    excitation_frequency: float = 1.6425
    actuator_gain: float = 1.0

    @property
    def damping(self) -> float:
        """Return the linear viscous damping coefficient in modal coordinates."""

        return 2.0 * self.damping_ratio * self.omega


def evaluate_control(control: ControlInput, t: float, state: np.ndarray) -> float:
    """Return a scalar control value from a constant or callable input."""

    if callable(control):
        return float(control(t, state))
    return float(control)


def cable_state_rhs(
    t: float,
    state: Sequence[float],
    params: CableParameters,
    control_force: ControlInput = 0.0,
) -> np.ndarray:
    """Return the state derivative of the reduced cable model.

    State vector: ``[modal_displacement, modal_velocity]``.

    The normalized equation is
    ``q_ddot + 2*xi*omega*q_dot + (omega^2 - a_p*cos(theta*t))*q
    + beta_2*q^2 + beta_3*q^3 = f*cos(theta*t) + b*u``.
    """

    q, q_dot = np.asarray(state, dtype=float)
    control = evaluate_control(control_force, t, np.array([q, q_dot], dtype=float))
    harmonic_force = params.excitation_amplitude * np.cos(params.excitation_frequency * t)
    parametric_term = params.parametric_stiffness * np.cos(params.excitation_frequency * t) * q
    q_ddot = (
        -params.damping * q_dot
        - params.omega**2 * q
        - params.quadratic_stiffness * q**2
        - params.cubic_stiffness * q**3
        + parametric_term
        + harmonic_force
        + params.actuator_gain * control
    )
    return np.array([q_dot, q_ddot], dtype=float)


def linear_state_matrix(params: CableParameters) -> np.ndarray:
    """Return the constant open-loop linearization around the zero state."""

    return np.array(
        [
            [0.0, 1.0],
            [-params.omega**2, -params.damping],
        ],
        dtype=float,
    )
