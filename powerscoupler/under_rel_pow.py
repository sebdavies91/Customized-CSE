import pandas as pd
import numpy as np
import math as mt
import os
np.set_printoptions(threshold=np.inf)
def under_rel_pow(filename: str,filename2: str, iteration, nrows, ncols, nlayers,relaxation):
    """
    Creates new sur powers iteration from both 
	the old powers iteration and the old sur 
	powers iteration
    """
    os.chdir("..")
    path = 'outputs/powerscoupler_iteration'+str(iteration)
    os.chdir(path)           
    powers_arr1d_old = np.loadtxt(filename,float)
    if iteration >1:
        os.remove('powersarr1doldsur.dat')
    os.rename('powersarr1dnewsur.dat', 'powersarr1doldsur.dat')                                                                   
    powers_arr1d_old_sur = np.loadtxt(filename2,float)
    powers_arr1d_new_sur=np.zeros([nrows*ncols*nlayers,1])
    powers_arr1d_new_sur=relaxation*powers_arr1d_old+(1-relaxation)*powers_arr1d_old_sur 
    np.savetxt('powersarr1dnewsur.dat',powers_arr1d_new_sur,fmt='%1.5e')
    os.chdir("..")
    os.chdir("..")
    path = 'powerscoupler'
    os.chdir(path)                             
    return powers_arr1d_new_sur

