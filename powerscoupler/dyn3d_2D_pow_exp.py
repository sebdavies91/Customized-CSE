import pandas as pd
import numpy as np
import math as mt
import os
from dyn3d_transversal_pow_exp import dyn3d_transversal_pow_exp
np.set_printoptions(threshold=np.inf)
def dyn3d_2D_pow_exp(filename: str, filename2: str, initial,iteration, corerows, corecols,nrows, ncols, nlayers,assembly_row, assembly_col):
    """
    Reads lst files and stores the powers
    :param filename: Lotus fission rates in the layers containig data from channels
    :return: numpy array with the read powers
    """
    os.chdir("..")
    if (initial == 'first_iteration_constant_feedback'):
       path = 'outputs/DYN3D_2Dassemblycelllevel_iteration'+str(iteration)
    elif (initial == 'first_iteration_constant_power'):
       path = 'outputs/DYN3D_2Dassemblycelllevel_iteration'+str(iteration-1)
    os.chdir(path)
    powersarr3d=np.zeros((nrows,ncols,nlayers))
    for i in range(nlayers):
        path3 = 'node'+str(i+1)
        os.chdir(path3)
        filename3=filename+str(i+1)
        filename3=filename3+str("_lst.dat")
        powers_arr1d = dyn3d_transversal_pow_exp(filename3,nrows, ncols,1)
        powersarr3d[:,:,i]=powers_arr1d.reshape(nrows,ncols)
        os.chdir("..")
    os.chdir("..")
    os.chdir("..")                  
    path2 = 'powerscoupler'
    os.chdir(path2)
    for i in range(nlayers):
        powersarr3d[:,:,i]=powersarr3d[:,:,i]/np.nanmean(powersarr3d[:,:,i])
    os.chdir("..")    
    path3 = 'outputs/boundaryconditionscoupler'
    os.chdir(path3)      
    powers_arr1d_dyn3d = np.loadtxt(filename2,float)
    powers_arr3d_dyn3d=powers_arr1d_dyn3d.reshape((corerows,corecols,nlayers))
    os.chdir("..")
    os.chdir("..")
    path2 = 'powerscoupler'
    os.chdir(path2)        
    for i in range(corerows):
        for j in range(corerows):
            if powers_arr3d_dyn3d[i,j,:].all() != 0:
                powers_arr3d_dyn3d[i,j,:]=powers_arr3d_dyn3d[i,j,:]/np.nanmean(powers_arr3d_dyn3d[i,j,:])

    for i in range(nlayers):
        powersarr3d[:,:,i]=powersarr3d[:,:,i]*powers_arr3d_dyn3d[assembly_row, assembly_col, i]
    powers_arr1d=powersarr3d.reshape((nrows*ncols*nlayers,1))
    os.chdir("..")
    path = 'outputs/powerscoupler_iteration'+str(iteration)
    os.chdir(path) 
    if iteration == 0:
        np.savetxt('powersarr1dnewsur.dat',powers_arr1d,fmt='%1.5e')
    else:
        np.savetxt('powersarr1dold.dat',powers_arr1d,fmt='%1.5e')
    os.chdir("..")
    os.chdir("..")
    path = 'powerscoupler'
    os.chdir(path) 
    return powers_arr1d



