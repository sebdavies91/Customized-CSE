import pandas as pd
import numpy as np
import math as mt
import os

np.set_printoptions(threshold=np.inf)
def dyn3d_2D_feed_imp(filename: str,iteration,nrows,ncols,nlayers):
    """
    Puts new sur powers iteration into CTF format
    """
    os.chdir("..")
    path = 'outputs/feedbackcoupler_iteration'+str(iteration)
    os.chdir(path)     
    feedback_arr1d = np.loadtxt(filename,float)
    os.chdir("..")
    os.chdir("..")
    path = 'feedbackcoupler'
    os.chdir(path)     
    fuel_temp_arr1d= feedback_arr1d[:,0]
    cool_temp_arr1d= feedback_arr1d[:,1]
    cool_dens_arr1d= feedback_arr1d[:,2]
    bor_conc_arr1d= feedback_arr1d[:,3]

    fuel_temp_arr3d=fuel_temp_arr1d.reshape((nrows,ncols,nlayers))	
    cool_temp_arr3d=cool_temp_arr1d.reshape((nrows,ncols,nlayers))
    cool_dens_arr3d=cool_dens_arr1d.reshape((nrows,ncols,nlayers))
    bor_conc_arr3d=bor_conc_arr1d.reshape((nrows,ncols,nlayers))	
    #The arrays are for different coordinates/sizes in CTF, we refer them to the node edges in DYN3D


 
    
    #Fuel temperature
    fuel_temp_arr2d_new=np.zeros((nrows*ncols,nlayers))
    for k in range(nlayers):
        fuel_temp_arr2d_new[:,k]=fuel_temp_arr3d[:,:,k].reshape((nrows*ncols))
    fuel_temp_arr1d_new=np.zeros((nrows*ncols*nlayers,1))
    i=0
    j=0
    for k in range(nlayers*nrows*ncols):
        if i<nrows*ncols-1:
            fuel_temp_arr1d_new[k]=fuel_temp_arr2d_new[i,j]
            i=i+1
        elif i==nrows*ncols-1:
            fuel_temp_arr1d_new[k]=fuel_temp_arr2d_new[i,j]
            i=0
            j=j+1
    #Coolant temperature
    cool_temp_arr2d_new=np.zeros((nrows*ncols,nlayers))
    for k in range(nlayers):
        cool_temp_arr2d_new[:,k]=cool_temp_arr3d[:,:,k].reshape((nrows*ncols))
    cool_temp_arr1d_new=np.zeros((nrows*ncols*nlayers,1))
    i=0
    j=0
    for k in range(nlayers*nrows*ncols):
        if i<nrows*ncols-1:
            cool_temp_arr1d_new[k]=cool_temp_arr2d_new[i,j]
            i=i+1
        elif i==nrows*ncols-1:
            cool_temp_arr1d_new[k]=cool_temp_arr2d_new[i,j]
            i=0
            j=j+1
    #Coolant density
    cool_dens_arr2d_new=np.zeros((nrows*ncols,nlayers))
    for k in range(nlayers):
        cool_dens_arr2d_new[:,k]=cool_dens_arr3d[:,:,k].reshape((nrows*ncols))
    cool_dens_arr1d_new=np.zeros((nrows*ncols*nlayers,1))
    i=0
    j=0
    for k in range(nlayers*nrows*ncols):
        if i<nrows*ncols-1:
            cool_dens_arr1d_new[k]=cool_dens_arr2d_new[i,j]
            i=i+1
        elif i==nrows*ncols-1:
            cool_dens_arr1d_new[k]=cool_dens_arr2d_new[i,j]
            i=0
            j=j+1
    #Boron Concentration
    bor_conc_arr2d_new=np.zeros((nrows*ncols,nlayers))
    for k in range(nlayers):
        bor_conc_arr2d_new[:,k]=bor_conc_arr3d[:,:,k].reshape((nrows*ncols))
    bor_conc_arr1d_new=np.zeros((nrows*ncols*nlayers,1))
    i=0
    j=0
    for k in range(nlayers*nrows*ncols):
        if i<nrows*ncols-1:
            bor_conc_arr1d_new[k]=bor_conc_arr2d_new[i,j]
            i=i+1
        elif i==nrows*ncols-1:
            bor_conc_arr1d_new[k]=bor_conc_arr2d_new[i,j]
            i=0
            j=j+1
    x=np.hstack([fuel_temp_arr1d_new, cool_temp_arr1d_new, cool_dens_arr1d_new, bor_conc_arr1d_new])
    os.chdir("..")
    path = 'outputs/DYN3D_2Dassemblycelllevel_iteration'+str(iteration)
    os.chdir(path)
    for k in range(nlayers):    
        path2 = 'node'+str(k+1)
        if not os.path.exists(path2):
            os.makedirs(path2)          
        output_file_feedback= open('node'+str(k+1)+'/ctf_feedback.dat','w')
        xlayer=np.zeros((nrows*ncols,4))
        for i in range(0, nrows*ncols):
            xlayer[i,:]=x[k*nrows*ncols+i,:]
        xlayer=np.array2string(xlayer, 250, 3, ' ').replace("[", "")
        xlayer=xlayer.replace("]", "")
        output_file_feedback.write(xlayer)
        output_file_feedback.close()
    os.chdir("..")
    os.chdir("..")
    path2 = 'feedbackcoupler'
    os.chdir(path2)  
    return x
