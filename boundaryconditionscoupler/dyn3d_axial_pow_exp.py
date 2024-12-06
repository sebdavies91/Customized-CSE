import pandas as pd
import numpy as np
import math as mt
import os
np.set_printoptions(threshold=np.inf)
def dyn3d_axial_pow_exp(filename: str, corerows, corecols, nlayers):
    """
    Reads DYN3D lines and stores the powers
    :param filename: DYN3D file containig data from channels
    :return: numpy array with the read powers
    """
    os.chdir("..")
    path = 'outputs/DYN3D_3Dcoreassemblylevel'
    os.chdir(path)
    filename=filename+str("_lst.dat")
    assemblypowers = open(filename, "r")
    os.chdir("..")
    os.chdir("..")       
    path = 'boundaryconditionscoupler'
    os.chdir(path)
    is_powers_part = False
    reading_data = False
    powers_arr = []
    for line in assemblypowers.readlines():
        if "NORMALIZED POWER DISTRIBUTION" in line:
            is_powers_part = True
            continue
        elif "keff" in line:
            is_powers_part = False
            continue   	
        elif "RADIAL PEAKING FACTOR (MAXIMUM TO AVERAGE OF EACH LAYER)" in line:
            is_powers_part = False
            continue   
        elif "RADIALLLY AVERAGED DISTRIBUTION" in line:
            is_powers_part = False
            continue 		
        if is_powers_part:
            if "ASS. POW." in line:
                reading_data = True
                continue
            if reading_data:
                if len(line.split()) == 0:
                    continue
                elif "K-AXIS" in line:
                    continue
                elif "CAS-NR." in line:
                    reading_data = False
                    continue   			
                else:
                    vals = line.split()
                powers_arr.append(vals)
    powers_arr = pd.DataFrame(data=powers_arr)
    powers_arr = powers_arr.drop(powers_arr.columns[[0]], axis=1)
    powers_arr = powers_arr.to_numpy(dtype=float)
    powers_arr1d=np.zeros(corerows*corecols*nlayers)
    i=0
    j=0
    l=0
    for k in range(corerows*corecols*nlayers):
        if i==(nlayers-1 +l*nlayers) and j==11:
            powers_arr1d[k]=powers_arr[i,j]
            j=0
            l=l+1
            i=l*nlayers
        elif i<(nlayers-1 +l*nlayers) and j==11:
            powers_arr1d[k]=powers_arr[i,j]
            i=i+1 
        elif i==(nlayers-1 +l*nlayers) and j<11:
            powers_arr1d[k]=powers_arr[i,j]
            j=j+1
            i=l*nlayers	
        elif i<(nlayers-1 +l*nlayers) and j<11:
            powers_arr1d[k]=powers_arr[i,j]
            i=i+1
    powers_arr=powers_arr1d.reshape(corerows,corecols,nlayers)
    new_powers_arr=np.zeros((corerows,corecols,nlayers))	
    for k in range(nlayers):
	    new_powers_arr[:,:,k]=powers_arr[:,:,new_powers_arr.shape[2]-1-k]
    powers_arr=new_powers_arr
    powers_arr1d_dyn3d=powers_arr.reshape((corerows*corecols*nlayers,1))
    os.chdir("..")
    path = 'outputs/boundaryconditionscoupler'
    os.chdir(path)                   
    np.savetxt('powersarr1ddyn3d.dat',powers_arr1d_dyn3d,fmt='%1.5e')
    os.chdir("..")
    os.chdir("..")
    path = 'boundaryconditionscoupler'
    os.chdir(path)            
    
    return powers_arr1d_dyn3d



