import pandas as pd
import numpy as np
import math as mt
import h5py
import os
np.set_printoptions(threshold=np.inf)
def hdf5_mat_converter(iteration, materials_list,fission_spectrum_material, fission_xsections_interp_material, nu_fission_xsections_interp_material, corrected_scattering_xsections_interp_material, transport_xsections_interp_material, nmaterials, ngroups, nrows, ncols, nlayers):
    """
    1 burnup state, n groups
    """
    """
saving in h5 format
    """
    os.chdir("..")
    path = 'outputs/LOTUS_2Dassemblymaterialslevel_iteration'+str(iteration)
    os.chdir(path)    
    for k in range(0,nlayers):
        path = 'node'+str(k+1)
        if not os.path.exists(path):
            os.makedirs(path)
        materials= h5py.File('node'+str(k+1)+'/materials'+str(k+1)+'.h5','w')
        materials.attrs['# groups']=ngroups
        for m in range(0,nmaterials):
            material=materials_list[m]           
            for j in range (0,ncols):
                for i in range (0, nrows):
                    g=materials.create_group('material/'+str(material)+str(nrows*j+i+1))
                    g.create_dataset('chi',data=fission_spectrum_material[m,:])
                    g.create_dataset('fission',data=fission_xsections_interp_material[m,:,i,j,k])
                    g.create_dataset('nu-fission',data=nu_fission_xsections_interp_material[m,:,i,j,k])            
                    g.create_dataset('scatter matrix',data=corrected_scattering_xsections_interp_material[m,:,i,j,k])
                    g.create_dataset('total',data=transport_xsections_interp_material[m,:,i,j,k])
        materials.close()
    os.chdir("..")
    os.chdir("..")
    path2 = 'feedbackcoupler'
    os.chdir(path2) 
    return 
