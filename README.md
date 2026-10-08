
# Propulsion-Analysis-Tool

Given time-series rocket-engine test data, PropTest will identify a firing interval, calculate propulsion performance metrics, generate standardized engineering plots, and export a concise test report.

## Version 0.1 — Project Objectives

Version 0.1 is complete when a user can provide a correctly formatted propulsion-test CSV and, with one command, receive a validated summary of the firing, including performance calculations and publication-quality plots, without manually editing the data.

The tool shall support incomplete datasets by calculating available metrics when sufficient measurements exist.

## Requirements

1. PropTest shall represent engine configuration separately from measured time-series data.
2. PropTest shall use SI units internally.
3. PropTest shall calculate total propellant mass flow and mixture ratio when the necessary measurements exist.
4. PropTest shall calculate characteristic velocity (c*), thrust coefficient (CF), and specific impulse (Isp) when the necessary measurements exist.
5. PropTest shall allow calculations over a user-selected time interval.
6. PropTest shall gracefully handle optional or missing sensor channels instead of requiring every measurement.
7. PropTest shall preserve the original test data so derived quantities do not overwrite measurements.

## Inputs

### Time-Series Measurements

PropTest shall accept time-series measurements from a CSV file.

Supported measurements include:

- Time
- Thrust
- Chamber pressure
- Fuel mass flow rate
- Oxidizer mass flow rate
- Fuel feed pressure (optional)
- Oxidizer feed pressure (optional)

Time is required for all analyses. Other measurements are required only when necessary for a particular calculation.

### Engine Configuration

Engine configuration parameters shall be stored separately from time-series measurements.

Potential parameters include:

- Engine identifier
- Fuel type
- Oxidizer type
- Nozzle throat area
- Nozzle exit area
- Design chamber pressure
- Design mixture ratio

Only parameters necessary for a requested calculation need to be provided.

## Calculations

### Fundamental Measurements

**Total Propellant Mass Flow Rate**

Total mass flow rate is the sum of fuel and oxidizer mass flow rates.

**Mixture Ratio (O/F)**

Mixture ratio is the ratio of oxidizer mass flow rate to fuel mass flow rate.

### Propulsion Performance Metrics

**Specific Impulse (Isp)**

Calculate specific impulse using thrust and total propellant mass flow rate.

**Characteristic Velocity (c*)**

Calculate characteristic velocity using chamber pressure, nozzle throat area, and total propellant mass flow rate.

**Thrust Coefficient (CF)**

Calculate thrust coefficient using thrust, chamber pressure, and nozzle throat area.

### Test Summary Metrics

- Peak thrust
- Average thrust
- Peak chamber pressure
- Average chamber pressure
- Total impulse
- Burn duration

Calculations shall use the user-selected analysis interval where applicable.

Metrics requiring unavailable measurements shall be reported as unavailable rather than causing the entire analysis to fail.

## Reports

Version 0.1 shall generate a concise summary of the analyzed rocket-engine firing.

### Numerical Results

The report shall present calculated performance metrics with appropriate SI units.

### Engineering Plots

Planned plots include:

- Thrust vs. time
- Chamber pressure vs. time
- Fuel and oxidizer mass flow rates vs. time (when available)
- Additional calculated performance parameters as supported

Plots shall clearly identify the relevant measurements, units, and analysis interval.

## Data Model

*To be developed.*

The data model shall define how PropTest organizes and relates:

- Test identification and metadata
- Engine configuration
- Original time-series measurements
- Analysis settings
- Derived performance calculations
- Generated results

The original measurements shall remain unchanged throughout the analysis process.
