from PropTest_Analysis import burn_duration, average_thrust,peak_chamber_pressure, total_impulse, peak_thrust

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