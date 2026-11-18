# PropTest
[Original Project Requirements](Requirements.md)

## Program Overview
PropTest analyzes time-series rocket-engine test data from a CSV file. The main script reads the bundled `fake_test_data.csv` and converts chamber pressure from psi and thrust from lbf to SI units before analysis. It prints peak chamber pressure, peak thrust, average thrust, total impulse, and burn duration to the terminal. It also plots chamber pressure and thrust versus time.

## Quick Start
With Python installed, open a terminal in the repository folder and run:

```powershell
python -m pip install matplotlib
python PropTest_Main.py
```

The sample prints five metrics.
Close the chamber pressure plot to see the thrust plot.

## CSV Input Format

| Required header | Measurement | Unit |
| --- | --- | --- |
| `timestamp_s` | Time | s |
| `chamber_pressure_psi` | Chamber Pressure | psi |
| `thrust_lbf` | Thrust | lbf |

- Timestamps must be nonnegative and strictly increasing
- Minimum two samples required for analysis
- Bundled `fake_test_data.csv` includes fuel pressure and oxidizer pressure data that the loader currently ignores
- To try your own data, change the filename in `PropTest_Main.py` to point to your own CSV
