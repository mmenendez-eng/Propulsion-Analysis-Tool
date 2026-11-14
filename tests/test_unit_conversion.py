from PropTest_UnitConversion import psi_to_pa, lbf_to_n, convert_sample_to_si

def test_psi_to_pa():
    test_pressure_psi = 100
    calculated_pressure_pa = psi_to_pa(test_pressure_psi)

    assert abs(calculated_pressure_pa - test_pressure_psi * 6894.757293) <= 1e-2

def test_lbf_to_n():
    test_thrust_lbf = 100
    calculated_thrust_n = lbf_to_n(test_thrust_lbf)

    assert (abs(calculated_thrust_n - test_thrust_lbf * 4.448221615) <= 1e-2)

def test_convert_sample_to_si():
    test_sample = {
        "timestamp_s": 0.5,
        "chamber_pressure_psi": 100,
        "thrust_lbf": 100
    }
    calculated_si_conversion = convert_sample_to_si(test_sample)
    assert calculated_si_conversion["timestamp_s"] == 0.5 
    assert abs(calculated_si_conversion["chamber_pressure_pa"] - 689475.7293) <= 1e-2 
    assert abs(calculated_si_conversion["thrust_n"] - 444.8221615) <= 1e-2
