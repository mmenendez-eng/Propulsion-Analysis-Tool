from PropTest_CSVPipeline import load_csv

def psi_to_pa(pressure_psi):
    # Converts pressure from pounds per square inch (psi) to pascals (Pa).
    
    return pressure_psi * 6894.757

def lbf_to_n(thrust_lbf):
    # Converts thrust from pounds force (lbf) to newtons (N).
    return thrust_lbf * 4.44822

def convert_sample_to_si(sample):
    # Creates dictionary with SI units converted from English units.
    return {
        "timestamp_s" : sample["timestamp_s"],
        "chamber_pressure_pa" : psi_to_pa(sample["chamber_pressure_psi"]),
        "thrust_n" : lbf_to_n(sample["thrust_lbf"])
    }



def convert_samples_to_si(samples):
    si_samples = []

    for sample in samples:
        si_samples.append(convert_sample_to_si(sample))

    return si_samples

if __name__ == "__main__":
    test_samples = load_csv("fake_test_data.csv")
    si_samples = convert_samples_to_si(test_samples)
    
    print(si_samples)