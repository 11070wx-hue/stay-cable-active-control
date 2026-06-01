"""Research tools for reduced-order stay-cable active vibration control."""

from .benchmarks import lqr_benchmark, open_loop_benchmark
from .controllers import linear_feedback_control, lqr_gain, zero_control
from .models import CableParameters, cable_state_rhs, linear_state_matrix
from .simulation import SimulationResult, rms_displacement, simulate

__all__ = [
    "CableParameters",
    "SimulationResult",
    "cable_state_rhs",
    "linear_feedback_control",
    "linear_state_matrix",
    "lqr_benchmark",
    "lqr_gain",
    "open_loop_benchmark",
    "rms_displacement",
    "simulate",
    "zero_control",
]
