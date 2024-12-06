import pandas as pd
import numpy as np
import math as mt
import os
np.set_printoptions(threshold=np.inf)
def dyn3d_alb_exp(filename: str, corerows, corecols, nlayers, nsides, ngroups):
    """
    Reads DYN3D lines and stores the powers
    :param filename: DYN3D file containig data from channels
    :return: numpy array with the read powers
    """
    os.chdir("..")
    path = 'outputs/DYN3D_3Dcoreassemblylevel'
    os.chdir(path)
    filename=filename+str("_lst.dat")
    assemblyalbedos = open(filename, "r")
    os.chdir("..")
    os.chdir("..")
    path = 'boundaryconditionscoupler'
    os.chdir(path)
    is_albedos_part = False
    reading_data = False
    albedos_arr = []
    for line in assemblyalbedos.readlines():
        if "ALBEDOS AT THE NODE SURFACES" in line:
            is_albedos_part = True
            continue
        elif "Partial Currents AT THE NODE SURFACES" in line:
            is_albedos_part = False
            continue   		
        if is_albedos_part:
            if "ASS-NR." in line:
                reading_data = False
                continue
            elif "AXIAL  GR SIDE" in line:
                reading_data = True
                continue
            if reading_data:
                if len(line.split()) == 0:
                    continue
                else:
                    vals = line.split()
                    vals = [x for x in vals if "." in x]
                albedos_arr.append(vals)
    albedos_arr = pd.DataFrame(data=albedos_arr)
    albedos_arr = albedos_arr.to_numpy(dtype=float)

    albedos_arr1d=np.zeros(corerows*corecols*nlayers*ngroups*nsides)
    i=0
    j=0
    l=0
    for k in range(corerows*corecols*nlayers*ngroups*nsides):
        if i==(nlayers*ngroups*nsides-1 +l*nlayers*ngroups*nsides) and j==11:
            albedos_arr1d[k]=albedos_arr[i,j]
            j=0
            l=l+1
            i=l*nlayers*ngroups*nsides
        elif i<(nlayers*ngroups*nsides-1 +l*nlayers*ngroups*nsides) and j==11:
            albedos_arr1d[k]=albedos_arr[i,j]
            i=i+1 
        elif i==(nlayers*ngroups*nsides-1 +l*nlayers*ngroups*nsides) and j<11:
            albedos_arr1d[k]=albedos_arr[i,j]
            j=j+1
            i=l*nlayers*ngroups*nsides	
        elif i<(nlayers*ngroups*nsides-1 +l*nlayers*ngroups*nsides) and j<11:
            albedos_arr1d[k]=albedos_arr[i,j]
            i=i+1
    albedos_arr=albedos_arr1d.reshape(corerows,corecols,nlayers,ngroups,nsides)

    new_albedos_arr=np.zeros((corerows,corecols,nlayers,ngroups,nsides))	
    for k in range(nlayers):
	    new_albedos_arr[:,:,k,:,:]=albedos_arr[:,:,new_albedos_arr.shape[2]-1-k,:,:]
    albedos_arr=new_albedos_arr 
    albedos_arr1d=albedos_arr.reshape((corerows*corecols*nlayers*ngroups*nsides,1))
    os.chdir("..")
    path = 'outputs/boundaryconditionscoupler'
    os.chdir(path)      
    np.savetxt('albedosarr1d.dat',albedos_arr1d,fmt='%1.5e')      
    os.chdir("..")
    os.chdir("..")
    path = 'boundaryconditionscoupler'
    os.chdir(path)
    
    return albedos_arr