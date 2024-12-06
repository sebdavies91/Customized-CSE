import pandas as pd
import numpy as np
import math as mt
import os
from scipy import interpolate
np.set_printoptions(threshold=np.inf)
def ctf_pow_imp(filename: str,filename2: str, iteration,nrows,ncols,nlayers,height):
    """
    Puts new sur powers iteration into CTF format
    """
    os.chdir("..")
    path = 'outputs/powerscoupler_iteration'+str(iteration)
    os.chdir(path) 
    powers_arr1d = np.loadtxt(filename2,float)
    os.chdir("..")
    os.chdir("..")
    path = 'powerscoupler'
    os.chdir(path) 
    powers_arr3d=powers_arr1d.reshape((nrows,ncols,nlayers))
    """
    #Interpolate from the centres of the cells to the faces
    x=np.linspace(height/(2*nlayers),height-height/(2*nlayers),nlayers,endpoint=True)
    xnew=np.linspace(0.0,height,nlayers,endpoint=True)
    y=np.zeros(nlayers)
    ynew=np.zeros(nlayers)
    for i in range(nrows):
        for j in range(ncols):
            for k in range(nlayers):
                y[k]=powers_arr3d[i,j,k]
            yread=interpolate.splrep(x,y,s=0)
            ynew=interpolate.splev(xnew,yread,der=0)
            for k in range(nlayers):
                powers_arr3d[i,j,k]=ynew[k]
	  """
    #RADIAL POWER
    #CTF radial power distributions
    power_arr_radial = np.average(powers_arr3d, axis=2)
    #CTF radial power Normalisation
    power_arr_radial=power_arr_radial/np.nanmean(power_arr_radial,axis=(0, 1))
    #CTF radial power Format
    os.chdir("..")
    path = 'outputs/powerscoupler_iteration'+str(iteration)
    os.chdir(path) 
    
    power_arr_radial=power_arr_radial.reshape((nrows*ncols))
    k=0
    output_file= open('radial_powers.dat','w')
    for i in range(nrows*ncols):
        if i>(7*(k+1)+k):
            k=k+1
            x=str(format(power_arr_radial[i],"8.6f"))
            output_file.write(x+'  ')
        elif i<(7*(k+1)+k):
            x=str(format(power_arr_radial[i],"8.6f"))
            output_file.write(x+'  ')
        elif i==(7*(k+1)+k):
            x=str(format(power_arr_radial[i],"8.6f"))
            output_file.write(x)
            output_file.write('\n')
    output_file.close()
	

    #AXIAL POWER
    #CTF axial power distributions
    power_arr_axial=powers_arr3d
    #CTF axial power Normalisation (yes or no, currently yes)
    for i in range(nrows):
        for j in range(ncols):
            if any(power_arr_axial[i,j,:])==0.0:
                continue
            elif all(power_arr_axial[i,j,:])!=0.0:
                power_arr_axial[i,j,:]=power_arr_axial[i,j,:]/np.nanmean(power_arr_axial[i,j])
                continue
    #CTF Format (height column to each power distribution)
    power_arr_axial=power_arr_axial.reshape((nrows*ncols*nlayers,1))
    x=np.linspace(height/(2*nlayers),height-height/(2*nlayers),nlayers,endpoint=True)
    power_arr2d=np.zeros((nrows*ncols*nlayers, 2))
    #CTF Format (Both arrays together)
    k=0
    j=0
    for i in range(nrows*ncols*nlayers):
        if i> nlayers*(k+1)-1:
            k=k+1
            power_arr2d[i,0]=x[j]
            power_arr2d[i,1]=power_arr_axial[i]
            j=j+1
        elif i==nlayers*(k+1)-1:
            power_arr2d[i,0]=x[j]
            power_arr2d[i,1]=power_arr_axial[i]
            j=0
        elif i< nlayers*(k+1)-1:
            power_arr2d[i,0]=x[j]
            power_arr2d[i,1]=power_arr_axial[i]
            j=j+1
    power_arr_axial=power_arr2d
    #CTF Format (Insert number of rod and node layers as first row per distribution)
    k=0
    j=1
    output_file= open('axial_powers.dat','w')
    for i in range(nrows*ncols*nlayers):
        if i==0:
            x=str(j)
            y=str(nlayers+2)
            output_file.write(x+ '  ')
            output_file.write(y)
            output_file.write('\n')
            x=str(0.0)
            y=str(0.0)
            output_file.write(x+ '  ')
            output_file.write(y)
            output_file.write('\n')
            x=str(format(power_arr_axial[i,0],"8.6f"))
            y=str(format(power_arr_axial[i,1],"8.6f")) 
            output_file.write(x+ '  ')
            output_file.write(y)
            output_file.write('\n')
            j=j+1
        elif i> nlayers*(k+1)-1: 
            x=str(j)
            y=str(nlayers+2)
            output_file.write(x+ '  ')
            output_file.write(y)
            output_file.write('\n')
            k=k+1
            x=str(0.0)
            y=str(0.0)
            output_file.write(x+ '  ')
            output_file.write(y)
            output_file.write('\n')
            x=str(format(power_arr_axial[i,0],"8.6f"))
            y=str(format(power_arr_axial[i,1],"8.6f")) 
            output_file.write(x+ '  ')
            output_file.write(y)
            output_file.write('\n')
            j=j+1
        elif i<nlayers*(k+1)-1:
            x=str(format(power_arr_axial[i,0],"8.6f"))
            y=str(format(power_arr_axial[i,1],"8.6f")) 
            output_file.write(x+ '  ')
            output_file.write(y)
            output_file.write('\n')
        elif i==nlayers*(k+1)-1:
            x=str(format(power_arr_axial[i,0],"8.6f"))
            y=str(format(power_arr_axial[i,1],"8.6f")) 
            output_file.write(x+ '  ')
            output_file.write(y)
            output_file.write('\n')
            x=str(height)
            y=str(0.0)
            output_file.write(x+ '  ')
            output_file.write(y)
            output_file.write('\n')
    output_file.close()

    
    with open('axial_powers.dat',"r") as axial_powers:
        axial_string = axial_powers.read()
    with open('radial_powers.dat',"r") as transversal_powers:
        transversal_string = transversal_powers.read()
    os.chdir("..")
    os.chdir("..")
    path = 'outputs/CTF_assemblycelllevel_iteration'+str(iteration)
    os.chdir(path)
    
    filename=filename+str(".inp")
    with open(filename,"r") as ctf_input:
        input_string = ctf_input.read()
        
    #AXIAL POWERS    
    leading_input_string=input_string.split('*AXIAL_POWER_COUPLING_START')[0]
    trailing_input_string=input_string.split('*AXIAL_POWER_COUPLING_END')[1]
    input_string=leading_input_string+'*AXIAL_POWER_COUPLING_START \n'+ axial_string +'*AXIAL_POWER_COUPLING_END'+trailing_input_string
    
    #TRANSVERSAL POWERS
    leading_input_string=input_string.split('*TRANSVERSAL_POWER_COUPLING_START')[0]
    trailing_input_string=input_string.split('*TRANSVERSAL_POWER_COUPLING_END')[1]
    input_string=leading_input_string+'*TRANSVERSAL_POWER_COUPLING_START \n'+ transversal_string +'*TRANSVERSAL_POWER_COUPLING_END'+trailing_input_string    
    
    with open(filename,"w") as ctf_input:
        ctf_input.write(input_string)    
    os.chdir("..")
    os.chdir("..")
    path2 = 'powerscoupler'
    os.chdir(path2)
    return power_arr_radial, power_arr_axial






