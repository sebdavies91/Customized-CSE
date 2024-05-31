import pandas as pd
import numpy as np
import math as mt
import os
np.set_printoptions(threshold=np.inf)
def lotus_2D_mat_alb_imp(filename: str, filename2: str, corerows, corecols, nlayers, nsides, ngroups, assembly_row, assembly_col):
    """
    Reads DYN3D lines and stores the powers
    :param filename: DYN3D file containig data from channels
    :return: numpy array with the read powers
    """
    os.chdir("..")
    path = 'outputs/boundaryconditionscoupler'
    os.chdir(path)     
    albedos_arr1d = np.loadtxt(filename2,float)
  
    albedos_arr=albedos_arr1d.reshape((corerows,corecols,nlayers,ngroups,nsides))
 
    #Temporary fix
    new_albedos_arr=np.zeros((corerows,corecols,nlayers,ngroups,nsides))	
    new_albedos_arr[:,:,:,:,0]=albedos_arr[:,:,:,:,0]
    new_albedos_arr[:,:,:,:,1]=albedos_arr[:,:,:,:,3]
    new_albedos_arr[:,:,:,:,2]=albedos_arr[:,:,:,:,2]
    new_albedos_arr[:,:,:,:,3]=albedos_arr[:,:,:,:,1]
    new_albedos_arr[:,:,:,:,4]=albedos_arr[:,:,:,:,4]
    new_albedos_arr[:,:,:,:,5]=albedos_arr[:,:,:,:,5]
    albedos_arr=new_albedos_arr
    for k in range(nlayers):
        filename3='albedos'
        filename3=filename3+str(k+1)+'.dat'
        output_file= open(filename3,'w')  
        ln0=str("albedo = np.array([")
        for n in range(ngroups):
            ln0=ln0+str("[")
            for s in range(nsides-2):
                ln0=ln0+str(format(albedos_arr[assembly_row,assembly_col,k,n,s],"8.6f"))+", "
            ln0=ln0[:-1]
            ln0=ln0[:-1]
            ln0=ln0+str("], ")
        ln0=ln0[:-1]
        ln0=ln0[:-1]        
        ln0=ln0+str("])")
        output_file.write(ln0)
        output_file.write('\n')  
        output_file.close()   
        
    for k in range(0,nlayers):
        filename3='albedos'
        filename3=filename3+str(k+1)+'.dat'
        with open(filename3,"r") as albedos:
            albedo_string = albedos.read()
            output_file= open(filename,'w')         
        os.chdir("..")
        os.chdir("..")
        path = 'outputs/LOTUS_2Dassemblymaterialslevel_iteration0'
        os.chdir(path)
        path2 = 'node'+str(k+1)
        os.chdir(path2)        
        filename4=filename
        filename4=filename4+str(k+1)+'.py'        
        with open(filename4,"r") as lotus_input:
            input_string = lotus_input.read()
        
        #ALBEDOS    
        leading_input_string=input_string.split('#ALBEDO_COUPLING_START')[0]
        trailing_input_string=input_string.split('#ALBEDO_COUPLING_END')[1]
        input_string=leading_input_string+'#ALBEDO_COUPLING_START \n'+ albedo_string +'#ALBEDO_COUPLING_END'+trailing_input_string
    
        with open(filename4,"w") as lotus_input:
            lotus_input.write(input_string) 
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
        path3 = 'outputs/boundaryconditionscoupler'
        os.chdir(path3)  
    os.chdir("..")
    os.chdir("..")
    path2 = 'boundaryconditionscoupler'
    os.chdir(path2)                  
    return albedos_arr