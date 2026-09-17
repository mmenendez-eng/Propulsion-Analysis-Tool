from PropTest_CSVPipeline import load_csv
from PropTest_UnitConversion import convert_samples_to_si
from PropTest_Analysis import (
    peak_chamber_pressure,
    peak_thrust,
    average_thrust,
    total_impulse,
    burn_duration,
)

if __name__ == "__main__":
    test_samples = load_csv("fake_test_data.csv")
    si_samples = convert_samples_to_si(test_samples)

    peak_pressure = peak_chamber_pressure(si_samples)
    peak_thrust_value = peak_thrust(si_samples)
    average_thrust_value = average_thrust(si_samples)
    total_impulse_value = total_impulse(si_samples)
    burn_duration_value = burn_duration(si_samples, 100.0)

    print('PropTest Analysis Results')
    print('-------------------------')
    print(f"Peak Pressure: {peak_pressure/1e6:.3f} MPa")
    print(f"Peak Thrust: {peak_thrust_value:.2f} N")
    print(f"Average Thrust: {average_thrust_value:.2f} N")
    print(f"Total Impulse: {total_impulse_value:.2f} N.s")
    print(f"Burn Duration: {burn_duration_value:.2f} s")