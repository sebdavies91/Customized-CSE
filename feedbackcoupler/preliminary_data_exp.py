import pandas as pd
import numpy as np
import math as mt
np.set_printoptions(threshold=np.inf)
def preliminary_data_exp(filename: str):
    xsections = open(filename, "r")
    reading_data = False
    preliminary_arr = []
    for line in xsections.readlines():   
        if "Mod Temp" in line:
            reading_data = True    
            continue  
        elif "*" in line:
              reading_data = False              
        if reading_data:
              vals = line.split()
              preliminary_arr.append(vals)
    preliminary_arr = pd.DataFrame(data=preliminary_arr)
    preliminary_arr = preliminary_arr.to_numpy(dtype=float)
    xsections.close()
    dimensions_arr = preliminary_arr[0,:]
    dimensions_arr = dimensions_arr[~np.isnan(dimensions_arr)]
    """
    This gives us the dimensions of the tables
    """
    nmoddens=int(dimensions_arr[0])
    nborconc=int(dimensions_arr[1])
    nfueltemp=int(dimensions_arr[2])
    """
    This gives us the x variables used in the interpolation
    """ 
    moddensities_arr = preliminary_arr[1,:]
    moddensities_arr = moddensities_arr[~np.isnan(moddensities_arr)]

    boronconcentrations_arr = preliminary_arr[2,:]
    boronconcentrations_arr = boronconcentrations_arr[~np.isnan(boronconcentrations_arr)]

    fueltemperatures_arr = preliminary_arr[3,:]
    fueltemperatures_arr = fueltemperatures_arr[~np.isnan(fueltemperatures_arr)]


    return nmoddens, nborconc, nfueltemp, moddensities_arr, boronconcentrations_arr, fueltemperatures_arr



