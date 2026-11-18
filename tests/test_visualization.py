import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PropTest_Visualization import plot_chamber_pressure, plot_thrust

def test_visualization_smoke():
    dict1 = {
        "timestamp_s": 0,
        "chamber_pressure_pa": 1e5,
        "thrust_n": 0
    }
    dict2 = {
        "timestamp_s": 1,
        "chamber_pressure_pa": 5e5,
        "thrust_n": 100
    }
    dict3 = {
        "timestamp_s": 2,
        "chamber_pressure_pa": 1e5,
        "thrust_n": 0
    }

    si_samples = [dict1, dict2, dict3]

    plt.close('all')
    plot_chamber_pressure(si_samples)
    plot_thrust(si_samples)
    assert len(plt.get_fignums()) == 2
    plt.close('all')