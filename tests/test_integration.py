from PropTest_CSVPipeline import load_csv
from PropTest_UnitConversion import convert_samples_to_si
from PropTest_Analysis import total_impulse, peak_thrust, peak_chamber_pressure
import pytest

def test_csv_to_si_analysis(tmp_path):
    csv_path = tmp_path / "test_data.csv"
    csv_path.write_text("""timestamp_s,chamber_pressure_psi,thrust_lbf
0,0,0
1,100,100
2,100,100
3,0,0""")

    raw_samples = load_csv(csv_path)
    si_samples = convert_samples_to_si(raw_samples)
    calculated_impulse = total_impulse(si_samples)
    assert abs(calculated_impulse - 889.6443) <= 1e-2

    calculated_peak_thrust = peak_thrust(si_samples)
    calculated_peak_pressure = peak_chamber_pressure(si_samples)
    assert abs(calculated_peak_thrust - 444.8221615) <= 1e-2
    assert abs(calculated_peak_pressure - 689475.7293) <= 1e-2

def test_invalid_csv_integration(tmp_path):
    csv_path = tmp_path / "test_data.csv"
    csv_path.write_text("""timestamp_s,chamber_pressure_psi,thrust_lbf
0,0,0
1,100,INVALID
2,100,100
3,0,0""")

    with pytest.raises(ValueError,match="Invalid thrust_lbf value"):
        load_csv(csv_path)