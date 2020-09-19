# Battery-Capacity-Estimation-Total-Least-Square-Method
This project is about estimating the battery capacity using the Approximate Weighted Total Least Square (AWTLS) method. 

# Battery cell Data
The Panasonic 18650 cell data is used for this simulation. The cell is passed through different charge/discharge cycle (Cycle 1 & Cycle 2) at 25 Deg.C. 

Data from the .MAT file is retrieved using the code in file "Data_25Deg". The retrieved data includes voltage, current, capacity and temperature.

# Simulation Scenarios
The code present in "BatteryRunData" file can be edited to run the battery cell at different scenarios and initial conditions

# AWTLS Algorithm
The file "AWTLS_SOH" consist the complete set of algorithm required to estimate the capacity along with error boundaries. 

The code could be easily converted into Fading Memory Approximate Weighted Total Least Square (FMAWTLS) by adding a forgetting factor which would give preference to the recent data entry and hence improve the estimated capacity accuracy.

# RunAWTLS
This file helps in gathering all the data from different file and run the whole project. The final results shows a plot between the estimated caacity with error bounds along with the true capacity for comparison.
It also gives the RMS error  for the capacity estimation.
