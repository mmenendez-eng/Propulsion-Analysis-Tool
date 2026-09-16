import csv

def load_csv(file_path):
    test_samples = []

    with open(file_path,"r") as file: # opens .csv file and reads file
        reader = csv.DictReader(file)

        for row in reader: # reads each row using header names
            # converts CSV text to numbers
            timestamp_s = float(row["timestamp_s"])
            chamber_pressure_psi = float(row["chamber_pressure_psi"])
            thrust_lbf = float(row["thrust_lbf"])

            if timestamp_s < 0: # checks for invalid negative time
                raise ValueError("Timestamp is negative.")

            # stores each row as a sample dictionary in test_samples
            sample = {
                "timestamp_s": timestamp_s,
                "chamber_pressure_psi": chamber_pressure_psi,
                "thrust_lbf": thrust_lbf
            }

            test_samples.append(sample)

        if len(test_samples) == 0: # checks for no data 
            raise ValueError("No test samples.")

    return test_samples


if __name__ == "__main__":
    test_samples = load_csv("fake_test_data.csv")
    print(f"Loaded {len(test_samples)} samples.") # confirms number of samples loaded
    print("First sample:", test_samples[0])

    '''
    The one remaining validation gap is if a cells says hello instead of 220.5.
    float(...) will stop the program, but the error won't highlight which row or measurement caused it.
    Next improvement is using try/except to give additional useful errors.
    '''