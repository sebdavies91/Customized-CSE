import pandas as pd
import numpy as np
import math as mt
import os
def ctf_array_to_dyn3d_array(filename: np.ndarray,filename2: str):
    """
    Converts ctf channel array into the dyn3d channels array
    :param filename: numpy array containig data from ctf 
    :return: numpy array with the data converted into the dyn3d channels
    """
    
    os.chdir("..")
    path = 'outputs/boundaryconditionscoupler'
    os.chdir(path)
    conversor = np.loadtxt(filename2, dtype=int)
    conversion_out = []
    for axial_slice in range(filename.shape[2]):
        ctf_1d = filename[:, :, axial_slice].ravel()
        for line in range(conversor.shape[0]):
            s = 0.
            for ctf_chan in range(conversor.shape[1]):
                s += ctf_1d[conversor[line, ctf_chan] - 1]
            conversion_out.append(s / conversor.shape[1])
    conversion_out = np.array(conversion_out).reshape((filename.shape[2], filename.shape[0] - 1, filename.shape[1] - 1))
    conversion_out = np.swapaxes(conversion_out, 0, 2)
    conversion_out = np.swapaxes(conversion_out, 0, 1)
    
    os.chdir("..")
    os.chdir("..")
    path = 'feedbackcoupler'
    os.chdir(path)
    
    return conversion_out
