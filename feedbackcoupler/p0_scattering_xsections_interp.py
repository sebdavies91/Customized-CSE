import pandas as pd
import numpy as np
import math as mt
from scipy.interpolate import interpn
np.set_printoptions(threshold=np.inf)
def p0_scattering_xsections_interp(filename2: str, moddensities_arr, fueltemperatures_arr,  boronconcentrations_arr, cool_dens_arr3d, fuel_temp_arr3d, bor_conc_arr3d, p0_scattering_xsections_arr, ngroups,nrows,ncols,nlayers):
    """
1 burnup state, n groups
    """
    """
interpolating p0_scattering xsections
    """   
    p0_scattering_xsections_interp=np.zeros((ngroups*ngroups,nrows,ncols,nlayers))
    for n in range(0,ngroups*ngroups):
        for k in range(0,nlayers):
            for j in range (0,ncols):
                for i in range (0,nrows):
                    p0_scattering_xsections_interp[n,i,j,k]=interpn((moddensities_arr,fueltemperatures_arr,boronconcentrations_arr),p0_scattering_xsections_arr[n],(cool_dens_arr3d[i,j,k],fuel_temp_arr3d[i,j,k],bor_conc_arr3d[i,j,k]),bounds_error=False,fill_value=None)
    """
we store in h5 file
    """   

    return p0_scattering_xsections_interp

    

