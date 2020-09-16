import numpy as np
from runAWTLS import runAWTLS
from Data_25Deg import Data_25Deg

Data_Dir = r'D:\GitHub Upload\Battery Capacity Estimation using Least Square' ##Data file location

##Call data function to retrieve voltage, current, capacity (Ah), state of charge, temperature
Voltage_25Deg, Current_25Deg, Ah_25Deg, SOC_25Deg, Temp_25Deg = Data_25Deg(Data_Dir)

Q0 = 2.9 ##Initial battery capacity
maxI = (1/20)*Q0 ##C/20 capacity
precisionI = np.power(2,10) ##10 bit precision on current sensor
slope = -0.01 ##Rate of change of capacity
Qnom = 0.99*Q0 ##Nominal Battery capacity
xmax = 0.8 ##Max SOC
xmin = -xmax ##Min SOC
SOC_true = SOC_25Deg ##True SOC
Ah_true = Ah_25Deg ##True Capacity
m = 300 ##Number of measurementbetween capcity estimates
theCase = 1 ##fixed update interval
mode = 0.5
sigma = 0.6
socnoise = 0.01 ##Standard Deviation of SOC
gamma = 0.99 ##forgetting factor
plot_title = 'EV Scenario'
ylim = np.arange(0, 4, 0.5) ##Y-axis range
runAWTLS(Q0, maxI, precisionI, slope, Qnom, SOC_true, Ah_true, m, theCase, mode, sigma, socnoise, gamma, plot_title, ylim, xmax, xmin)
