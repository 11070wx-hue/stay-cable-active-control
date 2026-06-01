"""Reduced stay-cable vibration model.

This module provides a compact single-degree-of-freedom model that can be used
for open-loop simulation and controller prototyping. The model is intentionally
small so that examples are reproducible and easy to inspect.
"""

from dataclasses import dataclass
from typing import Sequence

import numpy as np


@dataclass(frozen=True)
class CableParameters:
    """Physical and reduced-order parameters for a single-mode cable model."""

    omega: float = 1.6425        # rad/s, first modal circular frequency
    xi: float = 0.001            # damping ratio
    beta2: float = 0.0           # quadratic nonlinear coefficient
    beta3: float = 0.0           # cubic nonlinear coefficient
    excitation_amp: float = 0.02 # equivalent excitation amplitude
    excitation_freq: float = 1.6425 # rad/s


def cable_state_rhs(t: float, state: Sequence[float], params: CableParameters, control_force: float = 0.0) -> np.ndarray:
    """Return the state derivative of the reduced cable model.

    State vector: [modal_displacement, modal_velocity].
    The forcing and control terms are normalized generalized quantities.
    """

    y, y_dot = state
    external_force = params.excitation_amp * np.cos(params.excitation_freq * t)
    y_ddot = (
        -2.0 * params.xi * params.omega * y_dot
        - params.omega**2 * y
        - params.beta2 * y**2
        - params.beta3 * y**3
        + external_force
        + control_force
    )
    return np.array([y_dot, y_ddot], dtype=float)
