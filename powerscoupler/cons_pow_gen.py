import pandas as pd
import numpy as np
import math as mt
import os
np.set_printoptions(threshold=np.inf)

def cons_pow_gen(pow, nrows, ncols, nlayers):
     """
     Creates constant feedback for the first NK iteration
     """
     #Calculations
   
     
     # Power Factor (always 1)
     pow_arr3d0 =np.ones((nrows, ncols, nlayers))
     pow_arr3d0 =pow*pow_arr3d0
    

     pow_arr1d0= pow_arr3d0.reshape((nrows*ncols*nlayers, 1))
     os.chdir("..")
     path = 'outputs/powerscoupler_iteration0'
     os.chdir(path)                                                                         
     np.savetxt('powersarr1dnewsur.dat',pow_arr1d0, fmt='%1.5e')
     os.chdir("..")
     os.chdir("..")
     path = 'powerscoupler'
     os.chdir(path)  
     
     return pow_arr1d0
# ---------------------------Script parameters------------------------------------


