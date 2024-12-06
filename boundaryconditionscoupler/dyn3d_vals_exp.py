import pandas as pd
import numpy as np
import math as mt
import os
np.set_printoptions(threshold=np.inf)
def dyn3d_vals_exp(filename: str, corerows, corecols):
    """
    Reads DYN3D lines and stores the powers
    :param filename: DYN3D file containig data from channels
    :return: numpy array with the read powers
    """
    os.chdir("..")
    path = 'outputs/DYN3D_3Dcoreassemblylevel'
    os.chdir(path)
    filename=filename+str("_lst.dat")
    assemblyvalues = open(filename, "r")
    os.chdir("..")
    os.chdir("..")    
    path = 'boundaryconditionscoupler'
    os.chdir(path)
    is_values_part = False
    reading_data = False
    values_arr = []
    for line in assemblyvalues.readlines():
        if "GLOBAL THERMOHYDRAULICS" in line:
            is_values_part = True
            continue
        elif "AVERAGE" in line:
            is_values_part = False
            continue   		
        if is_values_part:
            if "NUCLEAR" in line:
                reading_data = False
                continue
            elif "NUM  ROD POWER" in line:
                reading_data = True
                continue
            if reading_data:
                if len(line.split()) == 0:
                    continue
                else:
                    vals = line.split()
                    vals = [x for x in vals if "." in x]
                values_arr.append(vals)
    assemblyvalues.close()
    values_arr = pd.DataFrame(data=values_arr)
    total_powers=values_arr[0]
    total_mass_fluxes=values_arr[2]
    total_boron_concentrations=values_arr[11]
    total_powers = total_powers.to_numpy(dtype=float)
    total_powers = total_powers.reshape(corerows,corecols)
    total_mass_fluxes = total_mass_fluxes.to_numpy(dtype=float)
    total_mass_fluxes = total_mass_fluxes.reshape(corerows,corecols)
    total_boron_concentrations = total_boron_concentrations.to_numpy(dtype=float)
    total_boron_concentrations = total_boron_concentrations.reshape(corerows,corecols)

    os.chdir("..")
    path = 'outputs/DYN3D_3Dcoreassemblylevel'
    os.chdir(path)
    assemblyvalues = open(filename, "r")
    os.chdir("..")
    os.chdir("..")    
    path = 'boundaryconditionscoupler'
    os.chdir(path)
    is_values_part = False
    reading_data = False
    values_arr = []
    for line in assemblyvalues.readlines():
        if "GLOBAL THERMOHYDRAULICS" in line:
            is_values_part = True
            continue
        elif "NUM  ROD POWER" in line:
            is_values_part = False
            continue
        elif "PROPERTIES OF COOLANT" in line:
            is_values_part = False
            continue             
        if is_values_part:
            if "NUCLEAR" in line:
                reading_data = True
                continue
            if reading_data:
                if len(line.split()) == 0:
                    continue
                else:
                    vals = line.split()
                    vals = [x for x in vals if "." in x]
                values_arr.append(vals)
    assemblyvalues.close()
    values_arr = pd.DataFrame(data=values_arr)
    values_arr.drop(values_arr.tail(1).index,inplace=True)
    total_core_power=values_arr[0]
    total_core_mass_flux=values_arr[2]
    inlet_core_temperature=values_arr[3]
    outlet_core_pressure=values_arr[5]
    
    global_boundary_conditions =[total_core_power,total_core_mass_flux,inlet_core_temperature,outlet_core_pressure]
    global_boundary_conditions =  np.array(global_boundary_conditions, dtype='float32')



    os.chdir("..")
    path = 'outputs/boundaryconditionscoupler'
    os.chdir(path)     
    total_powers_arr1d=total_powers.reshape((corerows*corecols,1))
    np.savetxt('totalpowersarr1d.dat',total_powers_arr1d,fmt='%1.5e')  
    total_mass_fluxes_arr1d=total_mass_fluxes.reshape((corerows*corecols,1))
    np.savetxt('totalmassfluxesarr1d.dat',total_mass_fluxes_arr1d,fmt='%1.5e') 
    total_boron_concentrations_arr1d=total_boron_concentrations.reshape((corerows*corecols,1)) 
    np.savetxt('totalboronconcentrationsarr1d.dat',total_boron_concentrations_arr1d,fmt='%1.5e') 
    np.savetxt('globalboundaryconditions.dat',global_boundary_conditions,fmt='%1.5e')  
    os.chdir("..")
    os.chdir("..")
    path = 'boundaryconditionscoupler'
    os.chdir(path)
    
    return total_powers_arr1d, total_mass_fluxes_arr1d, total_boron_concentrations_arr1d, global_boundary_conditions
