"""Baseline active-control laws for the reduced stay-cable model."""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np
from scipy.linalg import solve_continuous_are

from .models import CableParameters, linear_state_matrix


def lqr_gain(
    params: CableParameters,
    q_weight: float = 20.0,
    velocity_weight: float = 2.0,
    control_weight: float = 1.0,
) -> np.ndarray:
    """Return a continuous-time LQR gain for the linearized cable model."""

    if control_weight <= 0.0:
        raise ValueError("control_weight must be positive")
    if params.actuator_gain == 0.0:
        raise ValueError("actuator_gain must be nonzero for LQR design")

    a_matrix = linear_state_matrix(params)
    b_matrix = np.array([[0.0], [params.actuator_gain]], dtype=float)
    q_matrix = np.diag([q_weight, velocity_weight])
    r_matrix = np.array([[control_weight]], dtype=float)
    riccati = solve_continuous_are(a_matrix, b_matrix, q_matrix, r_matrix)
    gain = np.linalg.solve(r_matrix, b_matrix.T @ riccati)
    return gain.reshape(2)


def linear_feedback_control(
    gain: Sequence[float],
    reference: Sequence[float] | None = None,
    saturation: float | None = None,
):
    """Build a callable ``u(t, x)`` that applies ``u = -K(x - r)``."""

    gain_vector = np.asarray(gain, dtype=float)
    reference_vector = np.zeros(2, dtype=float) if reference is None else np.asarray(reference, dtype=float)

    if gain_vector.shape != (2,):
        raise ValueError("gain must contain two entries")
    if reference_vector.shape != (2,):
        raise ValueError("reference must contain two entries")
    if saturation is not None and saturation <= 0.0:
        raise ValueError("saturation must be positive when provided")

    def control(_t: float, state: np.ndarray) -> float:
        value = -float(gain_vector @ (np.asarray(state, dtype=float) - reference_vector))
        if saturation is None:
            return value
        return float(np.clip(value, -saturation, saturation))

    return control


def zero_control(_t: float, _state: np.ndarray) -> float:
    """Return zero control input for open-loop simulations."""

    return 0.0
