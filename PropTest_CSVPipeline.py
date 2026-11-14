import csv

def load_csv(file_path):
    test_samples = []

    with open(file_path,"r") as file: # opens .csv file and reads file
        reader = csv.DictReader(file)

        required_columns = ["timestamp_s", "chamber_pressure_psi", "thrust_lbf"]

        for col in required_columns:
            if col not in reader.fieldnames:
                raise ValueError(f"Missing required column: {col}")
            
        for row in reader: # reads each row using header names
            converted_row = {}
            for col in required_columns:
                try:
                    converted_row[col] = float(row[col])
                except ValueError:
                    raise ValueError(f"Invalid {col} value in row: {row}")

            if converted_row["timestamp_s"] < 0: # checks for invalid negative time
                raise ValueError("Timestamp is negative.")

            if len(test_samples) >= 1 and converted_row["timestamp_s"] <= test_samples[-1]["timestamp_s"]:
                            raise ValueError("Timestamps must be strictly increasing.")
            
            test_samples.append(converted_row)

        if len(test_samples) == 0: # checks for no data 
            raise ValueError("No test samples.")

    return test_samples


if __name__ == "__main__":
    test_samples = load_csv("fake_test_data.csv")
    print(f"Loaded {len(test_samples)} samples.") # confirms number of samples loaded
    print("First sample:", test_samples[0])
