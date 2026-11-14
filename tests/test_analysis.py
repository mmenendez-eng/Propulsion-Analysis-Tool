from PropTest_Analysis import burn_duration, average_thrust,peak_chamber_pressure, total_impulse, peak_thrust
import pytest
from PropTest_CSVPipeline import load_csv


def test_total_impulse():
    dict1 = {
        "timestamp_s": 0,
        "thrust_n": 0
            }
    dict2 = {
        "timestamp_s": 1,
        "thrust_n": 100
            }
    dict3 = {
        "timestamp_s": 2,
        "thrust_n": 100
            }
    dict4 = {
        "timestamp_s": 3,
        "thrust_n": 0
            }

    test_samples = [dict1, dict2, dict3, dict4]

    calculated_impulse = total_impulse(test_samples)

    assert abs(calculated_impulse - 200) <= 1e-2

def test_peak_thrust():
    dict1 = {
        "timestamp_s": 0,
        "thrust_n": 0
            }
    dict2 = {
        "timestamp_s": 1,
        "thrust_n": 100
            }
    dict3 = {
        "timestamp_s": 2,
        "thrust_n": 100
            }
    dict4 = {
        "timestamp_s": 3,
        "thrust_n": 0
            }

    test_samples = [dict1, dict2, dict3, dict4]

    calculated_peak_thrust = peak_thrust(test_samples)

    assert abs(calculated_peak_thrust - 100) <= 1e-2

def test_peak_pressure():
    dict1 = {
        "timestamp_s": 0,
        "chamber_pressure_pa": 0
            }
    dict2 = {
        "timestamp_s": 1,
        "chamber_pressure_pa": 100
            }
    dict3 = {
        "timestamp_s": 2,
        "chamber_pressure_pa": 100
            }
    dict4 = {
        "timestamp_s": 3,
        "chamber_pressure_pa": 0
            }

    test_samples = [dict1, dict2, dict3, dict4]

    calculated_peak_pressure = peak_chamber_pressure(test_samples)

    assert abs(calculated_peak_pressure - 100) <= 1e-2

def test_average_thrust():
    dict1 = {
        "timestamp_s": 0,
        "thrust_n": 0
            }
    dict2 = {
        "timestamp_s": 1,
        "thrust_n": 100
            }
    dict3 = {
        "timestamp_s": 2,
        "thrust_n": 100
            }
    dict4 = {
        "timestamp_s": 3,
        "thrust_n": 0
            }

    test_samples = [dict1, dict2, dict3, dict4]

    calculated_average_thrust = average_thrust(test_samples)

    assert abs(calculated_average_thrust - 50) <= 1e-2

def test_burn_duration():
    dict1 = {
        "timestamp_s": 0,
        "thrust_n": 0
            }
    dict2 = {
        "timestamp_s": 0.5,
        "thrust_n": 50
            }
    dict3 = {
        "timestamp_s": 1,
        "thrust_n": 150
            }
    dict4 = {
        "timestamp_s": 1.5,
        "thrust_n": 200
            }
    dict5 = {
        "timestamp_s": 2.0,
        "thrust_n": 150
            }
    dict6 = {
        "timestamp_s": 2.5,
        "thrust_n": 50
            }
    dict7 = {
        "timestamp_s": 3.0,
        "thrust_n": 0
            }
    test_samples = [dict1, dict2, dict3, dict4, dict5, dict6, dict7]

    calculated_burn_duration = burn_duration(test_samples, 100)

    assert abs(calculated_burn_duration - 1.0) <= 1e-2

def test_peak_thrust_empty():
    test_samples = []

    with pytest.raises(ValueError):
        result = peak_thrust(test_samples)

def test_total_impulse_single_sample():
    dict1 = {
        "timestamp_s": 0,
        "thrust_n": 100
            }

    test_samples = [dict1]

    with pytest.raises(ValueError):
        result = total_impulse(test_samples)

def test_total_impulse_duplicate_timestamps():
    dict1 = {
        "timestamp_s": 0,
        "thrust_n": 100
            }
    dict2 = {
        "timestamp_s": 0,
        "thrust_n": 200
            }

    test_samples = [dict1, dict2]

    with pytest.raises(ValueError):
        result = total_impulse(test_samples)

def test_total_impulse_decreasing_timestamps():
    dict1 = {
        "timestamp_s": 0,
        "thrust_n": 100
            }
    dict2 = {
        "timestamp_s": 2,
        "thrust_n": 200
            }
    dict3 = {
        "timestamp_s": 1,
        "thrust_n": 150
            }

    test_samples = [dict1, dict2, dict3]

    with pytest.raises(ValueError):
        result = total_impulse(test_samples)

def test_load_csv_missing_column(tmp_path):
    file_path = tmp_path / "example.csv"

    file_path.write_text("timestamp_s,thrust_lbf\n0,0\n0.1,100\n0.2,200")

    with pytest.raises(ValueError):
        load_csv(file_path)

def test_load_csv_invalid_pressure(tmp_path):
    file_path = tmp_path / "example.csv"
    file_path.write_text("timestamp_s,chamber_pressure_psi,thrust_lbf\n" \
        "0,14.7,0\n" \
        "0.1,150.0,100\n" \
        "0.2,200,200\n" \
        "0.3,ERROR,300")
    
    with pytest.raises(ValueError, match="Invalid chamber_pressure_psi"):
        load_csv(file_path)

def test_load_csv_invalid_thrust(tmp_path):
    file_path = tmp_path / "example.csv"
    file_path.write_text("timestamp_s,chamber_pressure_psi,thrust_lbf\n" \
        "0,14.7,0\n" \
        "0.1,150.0,100\n" \
        "0.2,200,200\n" \
        "0.3,225.0,ERROR")
    
    with pytest.raises(ValueError, match="Invalid thrust_lbf"):
        load_csv(file_path)

def test_load_csv_invalid_timestamp(tmp_path):
    file_path = tmp_path / "example.csv"
    file_path.write_text("timestamp_s,chamber_pressure_psi,thrust_lbf\n"
        "0,14.7,0\n"
        "0.1,150.0,100\n"
        "ERROR,200,200\n"
        "0.3,225.0,300")
    
    with pytest.raises(ValueError, match="Invalid timestamp_s value"):
        load_csv(file_path)

def test_load_csv_negative_timestamp(tmp_path):
    file_path = tmp_path / "example.csv"
    file_path.write_text("timestamp_s,chamber_pressure_psi,thrust_lbf\n"
        "0,14.7,0\n"
        "-0.1,150.0,100\n"
        "0.2,200,200\n"
        "0.3,225.0,300")
    
    with pytest.raises(ValueError, match="Timestamp is negative"):
        load_csv(file_path)

def test_load_csv_zero_timestamp(tmp_path):
    file_path = tmp_path / "example.csv"
    file_path.write_text("timestamp_s,chamber_pressure_psi,thrust_lbf\n"
        "0,14.7,0\n"
        "0.1,150.0,100\n"
        "0.2,200,200\n"
        "0.3,225.0,300")
    
    test_samples = load_csv(file_path)
    assert test_samples[0]["timestamp_s"] == 0.0

def test_load_csv_duplicate_timestamps(tmp_path):
    file_path = tmp_path / "example.csv"
    file_path.write_text("timestamp_s,chamber_pressure_psi,thrust_lbf\n"
        "0,14.7,0\n"
        "0.1,150.0,100\n"
        "0.1,200,200\n"
        "0.3,225.0,300")
    
    with pytest.raises(ValueError, match="Timestamps must be strictly increasing."):
        load_csv(file_path)

def test_load_csv_decreasing_timestamps(tmp_path):
    file_path = tmp_path / "example.csv"
    file_path.write_text("timestamp_s,chamber_pressure_psi,thrust_lbf\n"
        "0,14.7,0\n"
        "0.2,150.0,100\n"
        "0.1,200,200\n"
        "0.3,225.0,300")

    with pytest.raises(ValueError, match="Timestamps must be strictly increasing."):
            load_csv(file_path)
