"""Run a reproducible open-loop and LQR stay-cable benchmark."""

from pathlib import Path

import numpy as np

from stay_cable_control import lqr_benchmark, open_loop_benchmark, rms_displacement
from stay_cable_control.simulation import peak_displacement


def write_summary(output_path: Path, rows: list[tuple[str, float, float]]) -> None:
    """Write a small CSV summary that can be compared across runs."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["case,rms_displacement,peak_displacement"]
    lines.extend(f"{name},{rms:.8f},{peak:.8f}" for name, rms, peak in rows)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    open_loop = open_loop_benchmark(duration=20.0)
    controlled = lqr_benchmark(duration=20.0)
    rows = [
        ("open_loop", rms_displacement(open_loop), peak_displacement(open_loop)),
        ("lqr_controlled", rms_displacement(controlled), peak_displacement(controlled)),
    ]
    write_summary(Path("results/open_loop_summary.csv"), rows)

    for name, rms, peak in rows:
        print(f"{name}: rms={rms:.6f}, peak={peak:.6f}")
    improvement = 1.0 - rows[1][1] / rows[0][1]
    print(f"rms_reduction={100.0 * np.clip(improvement, -1.0, 1.0):.2f}%")


if __name__ == "__main__":
    main()
