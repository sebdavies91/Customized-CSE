import pandas as pd
import numpy as np
import math as mt
import os
def ctf_map_exp(filename: str,nrows,ncols):
    """
    Converts ctf channel array into the dyn3d channels array
    :param filename: numpy array containig data from ctf 
    :return: numpy array with the data converted into the dyn3d channels
    """
    os.chdir("..")
    path = 'outputs/CTF_assemblycelllevel_iteration0'
    os.chdir(path)
    assemblyvalues = open(filename, "r")
    os.chdir("..")
    os.chdir("..")
    path = 'boundaryconditionscoupler'
    os.chdir(path)
    is_values_part = False
    reading_data = False
    values_arr = []
    for line in assemblyvalues.readlines():
        if "*SUBCHANNEL_TO_CELL_COUPLING_END" in line:
            reading_data = False
            continue
        elif "*SUBCHANNEL_TO_CELL_COUPLING_START" in line:
            reading_data = True
            continue
        if reading_data:
            if len(line.split()) == 0:
                continue
            else:
                vals = line.split()
            values_arr.append(vals)    
    values_arr = pd.DataFrame(data=values_arr)
    values_arr = values_arr.to_numpy(dtype=float)
    conversor =np.zeros((nrows*ncols,4))
    n=0
    for i in range(nrows*ncols):
        conversor[i,0]=values_arr[2*n+1,0]
        conversor[i,1]=values_arr[2*n+1,2]
        conversor[i,2]=values_arr[2*n+1,4]
        conversor[i,3]=values_arr[2*n+1,6]
        n=n+1

        
    return conversor
