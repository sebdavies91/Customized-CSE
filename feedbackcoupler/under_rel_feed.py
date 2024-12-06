import pandas as pd
import numpy as np
import math as mt
import os
np.set_printoptions(threshold=np.inf)
def under_rel_feed(filename: str,filename2: str, iteration, nrows, ncols, nlayers, relaxation):
    """
    Creates new sur powers iteration from both 
	the old powers iteration and the old sur 
	powers iteration
    """
    os.chdir("..")
    path = 'outputs/feedbackcoupler_iteration'+str(iteration)
    os.chdir(path) 
    feedback_arr1d_old = np.loadtxt(filename,float)
    if iteration >1:
        os.remove('feedbackarr1doldsur.dat')
    os.rename('feedbackarr1dnewsur.dat', 'feedbackarr1doldsur.dat')
    feedback_arr1d_old_sur = np.loadtxt(filename2,float)
    feedback_arr1d_new_sur=np.zeros([nrows*ncols*nlayers,1])
    feedback_arr1d_new_sur=relaxation*feedback_arr1d_old+(1-relaxation)*feedback_arr1d_old_sur 
    np.savetxt('feedbackarr1dnewsur.dat',feedback_arr1d_new_sur,fmt='%1.5e')
    os.chdir("..")
    os.chdir("..")
    path = 'feedbackcoupler'
    os.chdir(path) 
    return feedback_arr1d_new_sur

