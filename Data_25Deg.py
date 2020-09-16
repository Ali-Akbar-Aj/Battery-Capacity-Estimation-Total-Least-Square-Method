import numpy as np
import os
from Loadmat import loadmat

#def moving_average(x, w):
#    return np.convolve(x, np.ones(w), 'valid') / w

def Data_25Deg(Data_Dir) :

    Total_Ah = 2.9 ##Insert Battery Nominal Ah rating

    dataDir = Data_Dir ##Data file location
    Filenames = os.listdir( dataDir ) ##Get file names from the data file

    ##Load data for Cycle_1 (charge and discharge cycle)
    Cycle_1 = loadmat(Filenames[1]) ##Data retrieved for one type of charge/dicharge cycle
    Cycle_1_meas = Cycle_1['meas'] ##Load the data present in the sub-directory
    ## Load Voltage, Current , Capacity and temperature data
    Voltage_Cycle_1 = Cycle_1_meas['Voltage']
    Current_Cycle_1 = Cycle_1_meas['Current']
    Ah_Cycle_1 = Cycle_1_meas['Ah']
    Temp_Cycle_1 = Cycle_1_meas['Battery_Temp_degC']

    ##Load data for Cycle_2 (charge and discharge cycle)
    Cycle_2 = loadmat(Filenames[2])
    Cycle_2_meas = Cycle_2['meas']
    Voltage_Cycle_2 = Cycle_2_meas['Voltage']
    Current_Cycle_2 = Cycle_2_meas['Current']
    Ah_Cycle_2 = Cycle_2_meas['Ah']
    Temp_Cycle_2 = Cycle_2_meas['Battery_Temp_degC']

    ##Merge Cycle_1 and Cycle_2 data into single vectors, more data from different cycle can also be concatenated
    Voltage_25Deg = np.concatenate((Voltage_Cycle_1,Voltage_Cycle_2),axis=0)
    Current_25Deg = np.concatenate((Current_Cycle_1,Current_Cycle_2),axis=0)
    Ah_25Deg = np.concatenate((Ah_Cycle_1,Ah_Cycle_2),axis=0)
    Temp_25Deg = np.concatenate((Temp_Cycle_1,Temp_Cycle_2),axis=0)

    ##Reshape the data for uniformity
    Voltage_25Deg = Voltage_25Deg.reshape(-1,1)
    Current_25Deg = Current_25Deg.reshape(-1,1)
    Ah_25Deg = Ah_25Deg.reshape(-1,1)
    SOC_25Deg = (1+((Ah_25Deg)/Total_Ah)).reshape(-1,1) ##Calculate SOC value using Capacity data
    Ah_25Deg = Total_Ah+Ah_25Deg.reshape(-1, 1)
    Temp_25Deg = Temp_25Deg.reshape(-1,1)

    return Voltage_25Deg, Current_25Deg,Ah_25Deg, SOC_25Deg, Temp_25Deg
