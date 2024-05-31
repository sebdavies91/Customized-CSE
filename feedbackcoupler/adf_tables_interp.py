import pandas as pd
import numpy as np
import math as mt
from scipy.interpolate import interpn
from preliminary_data_exp import preliminary_data_exp
from adf_tables_exp import adf_tables_exp
np.set_printoptions(threshold=np.inf)
def adf_tables_interp(filename2: str, moddensities_arr, fueltemperatures_arr,  boronconcentrations_arr, cool_dens_arr3d, fuel_temp_arr3d, bor_conc_arr3d, adf_tables_arr, ngroups,nrows,ncols,nlayers):
    """
1 burnup state, n groups
    """
    """
interpolating adf tables
    """   
    adf_tables_interp=np.zeros((ngroups,nrows,ncols,nlayers))
    for n in range(0,ngroups):
        for k in range(0,nlayers):
            for j in range (0,ncols):
                for i in range (0,nrows):
                    adf_tables_interp[n,i,j,k]=interpn((moddensities_arr,fueltemperatures_arr,boronconcentrations_arr),adf_tables_arr[n],(cool_dens_arr3d[i,j,k],fuel_temp_arr3d[i,j,k],bor_conc_arr3d[i,j,k]),bounds_error=False,fill_value=None)
    """
we store in h5 file
    """   

    return adf_tables_interp

    

