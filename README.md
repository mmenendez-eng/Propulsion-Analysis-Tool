# Propulsion-Analysis-Tool
Given time-series rocket-engine test data, the analysis tool will identify a firing interval, calculate a basic steady-state performance metrics, generate standardized engineering plots, and export a concise test report.

## Requirements
1. PropTest shall represent engine-configuration separately from measured time-series data.
2. PropTest shall use SI units internally.
3. PropTest shall calculate total propellant mass flow and mixture ratio.
4. PropTest shall calculate c*, CF, and Isp when the necessary measurements exist.
5. PropTest shall allow calculations over a user-selected time interval.
6. PropTest shall gracefully handle optional/missing sensor channels instead of requiring every measurement.
7. PropTest shall preserve the original test data so derived quantities do not overwirte measurements.


## Data Model
What information would I need to completely describe this test to the program?

### Test Information
- Test ID:
- Date:
- Description:

### Engine Information
- Engine Name:
- Throat Diameter:
- Exit Diameter:

### Propellants
- Fuel:
- Oxidizer:

### Measured Data
- Time:
- Chamber Pressure:
- Thrust:
- Fuel Mass Flow:
- Oxidizer Mass Flow:
