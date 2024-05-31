import pandas as pd
import numpy as np
import math as mt
import os
from dyn3d_transversal_pow_exp import dyn3d_transversal_pow_exp
np.set_printoptions(threshold=np.inf)
def dyn3d_3D_pow_exp(filename: str, initial,iteration, corerows, corecols,nrows, ncols, nlayers,assembly_row, assembly_col):
    """
    Reads lst files and stores the powers
    :param filename: Lotus fission rates in the layers containig data from channels
    :return: numpy array with the read powers
    """
    os.chdir("..")
    if (initial == 'first_iteration_constant_feedback'):
       path = 'outputs/DYN3D_3Dassemblycelllevel_iteration'+str(iteration)
    elif (initial == 'first_iteration_constant_power'):
       path = 'outputs/DYN3D_3Dassemblycelllevel_iteration'+str(iteration-1)
    os.chdir(path)
    
    powersarr3d=np.zeros((nrows,ncols,nlayers))
    filename=filename+str("_lst.dat")
    powers_arr1d = dyn3d_transversal_pow_exp(filename,nrows, ncols,nlayers)

    os.chdir("..")
    os.chdir("..")     
    path2 = 'powerscoupler'
    os.chdir(path2)
    
    os.chdir("..")
    path = 'outputs/powerscoupler_iteration'+str(iteration)
    os.chdir(path)                             
    if iteration == 0:
        np.savetxt('powersarr1dnewsur.dat',powers_arr1d,fmt='%1.5e')
    else:
        np.savetxt('powersarr1dold.dat',powers_arr1d,fmt='%1.5e')
    os.chdir("..")
    os.chdir("..")
    path = 'powerscoupler'
    os.chdir(path)        
    return powers_arr1d



