import matplotlib.pyplot as plt

from PropTest_CSVPipeline import load_csv
from PropTest_UnitConversion import convert_samples_to_si

def plot_chamber_pressure(samples):
    timestamps = []
    pressures = []

    for sample in samples:
        timestamps.append(sample["timestamp_s"])
        pressures.append(sample["chamber_pressure_pa"] / 1e6)

    peak_pressure = max(pressures)

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, pressures, marker="o", markersize=4, label="Chamber Pressure")
    plt.axhline(y=peak_pressure, color="red", linestyle="--", label=f"Peak Pressure: {peak_pressure:.3f} MPa")
    plt.xlabel("Time (s)")
    plt.ylabel("Chamber Pressure (MPa)")
    plt.title("Chamber Pressure vs. Time")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    # plt.savefig("chamber_pressure.png", dpi=300)
    plt.show()

def plot_thrust(samples):
    timestamps = []
    thrust_values = []

    for sample in samples:
        timestamps.append(sample["timestamp_s"])
        thrust_values.append(sample["thrust_n"])

    peak_thrust = max(thrust_values)

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, thrust_values, marker="o", markersize=4, label="Thrust")
    plt.axhline(y=peak_thrust, color="red", linestyle="--", label=f"Peak Thrust: {peak_thrust:.2f} N")
    plt.xlabel("Time (s)")
    plt.ylabel("Thrust (N)")
    plt.title("Thrust vs. Time")

    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    # plt.savefig("thrust.png", dpi=300)
    plt.show()
    
if __name__ == "__main__":
    samples = load_csv("fake_test_data.csv")
    si_samples = convert_samples_to_si(samples)

    plot_chamber_pressure(si_samples)
    plot_thrust(si_samples)