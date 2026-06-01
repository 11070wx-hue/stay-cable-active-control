import numpy as np

from stay_cable_control import CableParameters, cable_state_rhs, linear_feedback_control, lqr_gain
from stay_cable_control.benchmarks import lqr_benchmark, open_loop_benchmark
from stay_cable_control.models import linear_state_matrix
from stay_cable_control.simulation import rms_displacement, simulate


def test_rhs_matches_linear_stiffness_without_excitation():
    params = CableParameters(
        omega=2.0,
        damping_ratio=0.05,
        cubic_stiffness=0.0,
        excitation_amplitude=0.0,
    )

    derivative = cable_state_rhs(0.0, [0.5, 0.0], params)

    np.testing.assert_allclose(derivative, [0.0, -2.0], atol=1e-12)


def test_simulation_returns_requested_time_grid():
    params = CableParameters(excitation_amplitude=0.0, damping_ratio=0.02)
    t_eval = np.linspace(0.0, 1.0, 21)

    result = simulate(params=params, initial_state=(0.01, 0.0), t_span=(0.0, 1.0), t_eval=t_eval)

    assert result.state.shape == (2, 21)
    np.testing.assert_allclose(result.time, t_eval)


def test_lqr_gain_stabilizes_linearized_model():
    params = CableParameters(damping_ratio=0.001)
    gain = lqr_gain(params)
    closed_loop = linear_state_matrix(params) - np.array([[0.0], [params.actuator_gain]]) @ gain.reshape(1, 2)

    assert gain.shape == (2,)
    assert np.all(np.real(np.linalg.eigvals(closed_loop)) < 0.0)


def test_lqr_benchmark_reduces_rms_displacement():
    open_loop = open_loop_benchmark(duration=8.0)
    controlled = lqr_benchmark(duration=8.0)

    assert rms_displacement(controlled) < rms_displacement(open_loop)


def test_linear_feedback_saturation_limits_command():
    control = linear_feedback_control([10.0, 0.0], saturation=0.25)

    assert control(0.0, np.array([1.0, 0.0])) == -0.25
