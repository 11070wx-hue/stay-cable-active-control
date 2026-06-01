# Reproducibility Guide

## Python environment

Use Python 3.10 or newer:

```bash
python -m pip install -e ".[dev]"
python -m pytest
python examples/python/run_open_loop_demo.py
```

The example writes `results/open_loop_summary.csv`. The file is a small summary
of RMS and peak displacement for the open-loop and LQR-controlled benchmark.

## MATLAB environment

From the repository root:

```matlab
run('examples/matlab/run_open_loop_demo.m');
```

The MATLAB example uses `ode45` and the same parameter defaults as the Python
model where practical.

## Benchmark policy

- Commit source code, tests, equations, and small tabular summaries.
- Do not commit large raw sweeps, private experimental data, or unpublished
  measurement files.
- Document every benchmark parameter and unit.
- Keep controller examples separated from model equations.

## Verification checklist

Before publishing new benchmark results:

1. Run `python -m pytest`.
2. Run the relevant example from a clean checkout.
3. Record parameter changes in the script or documentation.
4. Explain whether MATLAB and Python results are expected to match exactly or
   only qualitatively.
