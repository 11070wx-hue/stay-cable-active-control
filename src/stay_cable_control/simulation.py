"""Simulation helpers for stay-cable benchmark cases."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np
from scipy.integrate import solve_ivp

from .models import CableParameters, ControlInput, cable_state_rhs, evaluate_control


@dataclass(frozen=True)
class SimulationResult:
    """Container for a time history and the evaluated control signal."""

    time: np.ndarray
    state: np.ndarray
    control: np.ndarray

    @property
    def displacement(self) -> np.ndarray:
        """Return modal displacement samples."""

        return self.state[0]

    @property
    def velocity(self) -> np.ndarray:
        """Return modal velocity samples."""

        return self.state[1]


def simulate(
    params: CableParameters,
    initial_state: Sequence[float],
    t_span: tuple[float, float] = (0.0, 30.0),
    t_eval: np.ndarray | None = None,
    control: ControlInput = 0.0,
    max_step: float = 0.02,
    rtol: float = 1e-8,
    atol: float = 1e-10,
) -> SimulationResult:
    """Integrate the cable model and return displacement, velocity, and control."""

    if t_eval is None:
        t_eval = np.linspace(t_span[0], t_span[1], 1501)

    def rhs(t: float, state: np.ndarray) -> np.ndarray:
        return cable_state_rhs(t, state, params=params, control_force=control)

    solution = solve_ivp(
        rhs,
        t_span,
        np.asarray(initial_state, dtype=float),
        t_eval=t_eval,
        max_step=max_step,
        rtol=rtol,
        atol=atol,
    )
    if not solution.success:
        raise RuntimeError(f"Simulation failed: {solution.message}")

    control_values = np.array(
        [evaluate_control(control, t, solution.y[:, index]) for index, t in enumerate(solution.t)],
        dtype=float,
    )
    return SimulationResult(time=solution.t, state=solution.y, control=control_values)


def rms_displacement(result: SimulationResult) -> float:
    """Return root-mean-square modal displacement."""

    return float(np.sqrt(np.mean(result.displacement**2)))


def peak_displacement(result: SimulationResult) -> float:
    """Return peak absolute modal displacement."""

    return float(np.max(np.abs(result.displacement)))
