def peak_chamber_pressure(data):
    pressures = []

    for sample in data:
        pressures.append(sample["chamber_pressure_pa"])

    return max(pressures)

def peak_thrust(data):
    thrust = []

    for sample in data:
        thrust.append(sample["thrust_n"])

    return max(thrust)

def average_thrust(data):
    thrust = []

    for sample in data:
        thrust.append(sample["thrust_n"])

    return sum(thrust) / len(thrust)

def total_impulse(data):
    total = 0.0

    for i in range(len(data) - 1):
        t1 = data[i]["timestamp_s"]
        t2 = data[i + 1]["timestamp_s"]

        dt = t2 - t1

        f1 = data[i]["thrust_n"]
        f2 = data[i + 1]["thrust_n"]

        interval_impulse = (f1 + f2) * dt / 2
        total += interval_impulse

    return total

def burn_duration(data, threshold):
    burn_samples = []

    for sample in data:
        if sample["thrust_n"] > threshold:
            burn_samples.append(sample)

    if len(burn_samples) == 0: 
        return 0.0
    
    start_time = burn_samples[0]["timestamp_s"]
    end_time = burn_samples[-1]["timestamp_s"]

    return end_time - start_time