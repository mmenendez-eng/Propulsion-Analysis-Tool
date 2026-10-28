from PropTest_Analysis import total_impulse

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

print(f'Total Impulse: {calculated_impulse:.2f} N.s')

assert calculated_impulse == 200