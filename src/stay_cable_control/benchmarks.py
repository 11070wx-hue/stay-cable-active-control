"""Reproducible benchmark cases used by examples and tests."""

from __future__ import annotations

import numpy as np

from .controllers import linear_feedback_control, lqr_gain
from .models import CableParameters
from .simulation import SimulationResult, simulate


def benchmark_parameters() -> CableParameters:
    """Return the default benchmark parameter set."""

    return CableParameters(
        omega=1.6425,
        damping_ratio=0.003,
        cubic_stiffness=0.08,
        parametric_stiffness=0.0,
        excitation_amplitude=0.02,
        excitation_frequency=1.6425,
        actuator_gain=1.0,
    )


def open_loop_benchmark(duration: float = 30.0) -> SimulationResult:
    """Run the open-loop single-mode benchmark."""

    params = benchmark_parameters()
    t_eval = np.linspace(0.0, duration, int(duration * 50) + 1)
    return simulate(params=params, initial_state=(0.02, 0.0), t_span=(0.0, duration), t_eval=t_eval)


def lqr_benchmark(duration: float = 30.0, saturation: float = 0.25) -> SimulationResult:
    """Run an LQR-controlled benchmark with actuator saturation."""

    params = benchmark_parameters()
    gain = lqr_gain(params, q_weight=30.0, velocity_weight=4.0, control_weight=1.0)
    control = linear_feedback_control(gain, saturation=saturation)
    t_eval = np.linspace(0.0, duration, int(duration * 50) + 1)
    return simulate(
        params=params,
        initial_state=(0.02, 0.0),
        t_span=(0.0, duration),
        t_eval=t_eval,
        control=control,
    )
