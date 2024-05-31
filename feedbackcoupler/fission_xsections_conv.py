import pandas as pd
import numpy as np
import math as mt
np.set_printoptions(threshold=np.inf)
def fission_xsections_conv(nu_fission_xsections_interp_material,nmaterials,ngroups,nrows,ncols,nlayers):
    """
    1 burnup state, n groups
    """
    """
    converting from nu_fission xsections to fission cross sections
    """
    fission_xsections_interp_material =np.zeros((nmaterials,ngroups,nrows,ncols,nlayers))
    for n in range(0,ngroups):
        if n==0:
            nu=2.53
        elif n==1:
            nu=2.43
        fission_xsections_interp_material[:,n,:,:,:]=nu_fission_xsections_interp_material[:,n,:,:,:]/nu
    return fission_xsections_interp_material
