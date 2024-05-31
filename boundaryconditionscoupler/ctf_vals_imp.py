import pandas as pd
import numpy as np
import math as mt
import os
from ctf_vals_exp import ctf_vals_exp
from ctf_map_exp import ctf_map_exp
np.set_printoptions(threshold=np.inf)
def ctf_vals_imp(filename: str, filename2: str, filename3:str, filename4:str, filename5:str,corerows, corecols, nassemblies,nreflectors, nrows,ncols,nrodsperassembly, height,assembly_row, assembly_col):  
    """
    Reads DYN3D lines and stores the powers
    :param filename2: DYN3D file containig data from channels
    :return: numpy array with the read powers
    """
    os.chdir("..")
    path = 'outputs/boundaryconditionscoupler'
    os.chdir(path)     
    
    total_powers_arr1d = np.loadtxt(filename2,float)
    total_powers_arr=total_powers_arr1d.reshape((corerows,corecols))
    
    total_mass_fluxes_arr1d = np.loadtxt(filename3,float)
    total_mass_fluxes_arr=total_mass_fluxes_arr1d.reshape((corerows,corecols))

    total_boron_concentrations_arr1d = np.loadtxt(filename4,float)
    total_boron_concentrations_arr=total_boron_concentrations_arr1d.reshape((corerows,corecols))
     
    global_boundary_conditions = np.loadtxt(filename5,float)
 
    total_core_power=global_boundary_conditions[0]
    total_core_mass_flux=global_boundary_conditions[1]
    inlet_core_temperature=global_boundary_conditions[2]
    outlet_core_pressure=global_boundary_conditions[3]
    
    
    
    #calculations
    total_powers=total_powers_arr/np.nanmean(total_powers_arr[total_powers_arr!=0])
    total_powers=total_core_power*total_powers/nassemblies
    total_powers=total_powers/(nrodsperassembly*height) 
    total_mass_fluxes=total_mass_fluxes_arr*total_core_mass_flux/np.sum(total_mass_fluxes_arr)
    outlet_core_pressure=outlet_core_pressure*10
    
    total_power=str(total_powers[assembly_row,assembly_col])
    total_mass_flux=str(total_mass_fluxes[assembly_row,assembly_col])
    inlet_temperature=str(inlet_core_temperature)
    outlet_pressure=str(outlet_core_pressure)
    total_boron_concentration=str(total_boron_concentrations_arr[assembly_row,assembly_col])
    
    output_file= open('total_power.dat','w')
    output_file.write(total_power)
    output_file.close()
    output_file= open('total_mass_flux.dat','w')
    output_file.write(total_mass_flux)
    output_file.close()
    output_file= open('inlet_temperature.dat','w')
    output_file.write(inlet_temperature)
    output_file.close()
    output_file= open('outlet_pressure.dat','w')
    output_file.write(outlet_pressure)
    output_file.close()
    output_file= open('total_boron_concentration.dat','w')
    output_file.write(total_boron_concentration)
    output_file.close()

    filename6='total_power.dat'
    with open(filename6,"r") as total_power:
        total_power_string = total_power.read()
    filename6='total_mass_flux.dat'
    with open(filename6,"r") as total_mass_flux:
        total_mass_flux_string = total_mass_flux.read()
    filename6='inlet_temperature.dat'
    with open(filename6,"r") as inlet_temperature:
        inlet_temperature_string = inlet_temperature.read()
    filename6='outlet_pressure.dat'
    with open(filename6,"r") as outlet_pressure:
        outlet_pressure_string = outlet_pressure.read()
    filename6='total_boron_concentration.dat'
    with open(filename6,"r") as total_boron_concentration:
        total_boron_concentration_string = total_boron_concentration.read()
        
        
        
    os.chdir("..")            
    os.chdir("..")
    path = 'outputs/CTF_assemblycelllevel_iteration0'
    os.chdir(path)  
 
    filename=filename+str(".inp")
    with open(filename,"r") as ctf_input:
        input_string = ctf_input.read()

    os.chdir("..")
    os.chdir("..")
    path = 'boundaryconditionscoupler'
    os.chdir(path)  


    #VALUES    

    values_string_1 =  ctf_vals_exp(filename)[0][0]
    values_string_2 =  ctf_vals_exp(filename)[0][1]
    values_string_3 =  ctf_vals_exp(filename)[0][2]
    values_string_4 =  ctf_vals_exp(filename)[0][3]
    values_string_5 =  ctf_vals_exp(filename)[0][4]  
    
    values_string_1[5]=total_mass_flux_string
    values_string_2[0]=total_mass_flux_string
    values_string_2[1]=total_power_string
    values_string_3[0]=outlet_pressure_string
    values_string_3[1]=str("-")+inlet_temperature_string
    values_string_3[5]=total_boron_concentration_string
      
    values_string_4[0]=0.00000E+00
    values_string_4[1]=inlet_temperature_string
    values_string_5[0]=height
    values_string_5[1]=inlet_temperature_string   
    
    values_string_1=" ".join(str(x) for x in values_string_1)
    values_string_2=" ".join(str(x) for x in values_string_2)
    values_string_3=" ".join(str(x) for x in values_string_3)
    values_string_4=" ".join(str(x) for x in values_string_4)
    values_string_5=" ".join(str(x) for x in values_string_5)
    leading_input_string=input_string.split('*FIRST_VALUES_COUPLING_START')[0]
    trailing_input_string=input_string.split('*FIRST_VALUES_COUPLING_END')[1]
    input_string=leading_input_string+'*FIRST_VALUES_COUPLING_START\n'+ values_string_1 +'\n*FIRST_VALUES_COUPLING_END'+trailing_input_string
    leading_input_string=input_string.split('*SECOND_VALUES_COUPLING_START')[0]
    trailing_input_string=input_string.split('*SECOND_VALUES_COUPLING_END')[1]
    input_string=leading_input_string+'*SECOND_VALUES_COUPLING_START\n'+ values_string_2 +'\n*SECOND_VALUES_COUPLING_END'+trailing_input_string
    leading_input_string=input_string.split('*THIRD_VALUES_COUPLING_START')[0]
    trailing_input_string=input_string.split('*THIRD_VALUES_COUPLING_END')[1]
    input_string=leading_input_string+'*THIRD_VALUES_COUPLING_START\n'+ values_string_3 +'\n*THIRD_VALUES_COUPLING_END'+trailing_input_string
    leading_input_string=input_string.split('*FOURTH_VALUES_COUPLING_START')[0]
    trailing_input_string=input_string.split('*FOURTH_VALUES_COUPLING_END')[1]
    input_string=leading_input_string+'*FOURTH_VALUES_COUPLING_START\n'+ values_string_4+'\n'+ values_string_5+'\n*FOURTH_VALUES_COUPLING_END'+trailing_input_string    

    #VALUES2  
    values2_string_1 = ctf_vals_exp(filename)[1][0:((nrows+1)*(ncols+1))]
    values2_string_2 = ctf_vals_exp(filename)[1][(nrows+1)*(ncols+1):(2*((nrows+1)*(ncols+1)))]  
    values2_string_1 = pd.DataFrame(data=values2_string_1)
    values2_string_2 = pd.DataFrame(data=values2_string_2)
 
    
    values2_string_1[7] = str("-")+inlet_temperature_string
    values2_string_1[10] = total_boron_concentration_string
    values2_string_2[8] = outlet_pressure_string
    
    values2_string_1=values2_string_1.to_string(header=False,index=False)
    values2_string_2=values2_string_2.to_string(header=False,index=False)
        
    leading_input_string=input_string.split('*FIFTH_VALUES_COUPLING_START')[0]
    trailing_input_string=input_string.split('*FIFTH_VALUES_COUPLING_END')[1]
    input_string=leading_input_string+'*FIFTH_VALUES_COUPLING_START\n'+ values2_string_1 +'\n*FIFTH_VALUES_COUPLING_END'+trailing_input_string

    leading_input_string=input_string.split('*SIXTH_VALUES_COUPLING_START')[0]
    trailing_input_string=input_string.split('*SIXTH_VALUES_COUPLING_END')[1]
    input_string=leading_input_string+'*SIXTH_VALUES_COUPLING_START\n'+ values2_string_2 +'\n*SIXTH_VALUES_COUPLING_END'+trailing_input_string 

    
    os.chdir("..")
    path = 'outputs/CTF_assemblycelllevel_iteration0'
    os.chdir(path)
    with open(filename,"w") as ctf_input:
        ctf_input.write(input_string) 
        
    os.chdir("..")
    os.chdir("..")
    path3 = 'boundaryconditionscoupler'
    os.chdir(path3)   
    
    #MAPPING     
    
    mapping =  ctf_map_exp(filename,nrows,ncols)
    os.chdir("..")
    path = 'outputs/boundaryconditionscoupler'
    os.chdir(path)
    np.savetxt('subchanneltochannel.dat',mapping.astype(int), fmt='%i', delimiter=" ") 
    
    os.chdir("..")
    os.chdir("..")
    path3 = 'boundaryconditionscoupler'
    os.chdir(path3)   
    
    return total_powers, total_mass_fluxes, mapping
