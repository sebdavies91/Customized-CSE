import pandas as pd
import numpy as np
import math as mt
import os
np.set_printoptions(threshold=np.inf)

def cons_feed_gen(fuel_temp, cool_temp, cool_dens, boron_conc, nrows, ncols, nlayers):
     """
     Creates constant feedback for the first NK iteration
     """
     #Calculations
   
     
     # Fuel Temperatures
     fuel_temp_arr3d0 =np.ones((nrows, ncols, nlayers))
     fuel_temp_arr3d0 =fuel_temp*fuel_temp_arr3d0
     # Coolant Temperatures
     cool_temp_arr3d0 =np.ones((nrows, ncols, nlayers))
     cool_temp_arr3d0 =cool_temp*cool_temp_arr3d0
     # Coolant Densities
     cool_dens_arr3d0 =np.ones((nrows, ncols, nlayers))
     cool_dens_arr3d0 =cool_dens*cool_dens_arr3d0
     # Boron Concentration
     bor_conc_arr3d0=np.ones((nrows, ncols, nlayers))
     bor_conc_arr3d0= boron_conc*bor_conc_arr3d0

     fuel_temp_arr1d0= fuel_temp_arr3d0.reshape((nrows*ncols*nlayers, 1))
     cool_temp_arr1d0= cool_temp_arr3d0.reshape((nrows*ncols*nlayers, 1))
     cool_dens_arr1d0= cool_dens_arr3d0.reshape((nrows*ncols*nlayers, 1))
     bor_conc_arr1d0= bor_conc_arr3d0.reshape((nrows*ncols*nlayers, 1))
     arr1d0=np.hstack([fuel_temp_arr1d0, cool_temp_arr1d0, cool_dens_arr1d0, bor_conc_arr1d0])
     os.chdir("..")
     path = 'outputs/feedbackcoupler_iteration0'
     os.chdir(path) 
     np.savetxt('feedbackarr1dnewsur.dat',arr1d0, fmt='%1.5e')
     os.chdir("..")
     os.chdir("..")
     path = 'feedbackcoupler'
     os.chdir(path)      
     
     return fuel_temp_arr1d0, cool_temp_arr1d0, cool_dens_arr1d0, bor_conc_arr1d0
# ---------------------------Script parameters------------------------------------


