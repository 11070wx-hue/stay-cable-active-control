"""Open-loop simulation demo for the reduced stay-cable model."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src" / "python"))

from cable_model import CableParameters, cable_state_rhs


def main() -> None:
    """Run a reproducible open-loop simulation."""

    params = CableParameters()
    t_span = (0.0, 120.0)
    t_eval = [0.05 * i for i in range(int(t_span[1] / 0.05) + 1)]
    initial_state = [0.02, 0.0]

    solution = solve_ivp(
        fun=lambda t, x: cable_state_rhs(t, x, params),
        t_span=t_span,
        y0=initial_state,
        t_eval=t_eval,
        rtol=1e-8,
        atol=1e-10,
    )

    if not solution.success:
        raise RuntimeError(solution.message)

    plt.figure()
    plt.plot(solution.t, solution.y[0])
    plt.xlabel("Time (s)")
    plt.ylabel("Modal displacement")
    plt.title("Open-loop stay-cable response")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
