import pandas as pd
import numpy as np
import math as mt
import os
import vtk
from vtk.util.numpy_support import vtk_to_numpy, numpy_to_vtk                                                   
from ctf_array_to_dyn3d_array import ctf_array_to_dyn3d_array
np.set_printoptions(threshold=np.inf)


def ctf_feed_exp(filename: str,filename2: str,initial,iteration, nrows, ncols, nlayers, boron_concentration):
     """
     Reads CTF files and stores the average fuel temperatures,
     coolant temperature density as well as boron concentration
     Return: numpy arrays with read feedback
     """
     os.chdir("..")
     if (initial == 'first_iteration_constant_feedback'):
        path = 'outputs/CTF_assemblycelllevel_iteration'+str(iteration-1)
     elif (initial == 'first_iteration_constant_power'):
        path = 'outputs/CTF_assemblycelllevel_iteration'+str(iteration)     
     os.chdir(path)     
     for i in range(0,2):
        if i == 0:
            filename3=filename
        elif i == 1:
            filename3=filename2    
        
        filename3=filename3+str(".vtk")            
        # Open file and read unstructured grid.
        reader = vtk.vtkUnstructuredGridReader()
        reader.SetFileName(filename3)
        reader.ReadAllScalarsOn()
        reader.ReadAllVectorsOn()
        reader.ReadAllTensorsOn()
        reader.ReadAllFieldsOn()
        reader.Update()
        grid = reader.GetOutput()
    
        # Read points.
        #vtk_points = grid.GetPoints()
        #xyz3d = vtk_to_numpy( vtk_points.GetData() )
    
        # Read cells.
        #cells = vtk_to_numpy( grid.GetCells().GetData() )
        #cell_locations = vtk_to_numpy( grid.GetCellLocationsArray() )
        #cell_types = vtk_to_numpy( grid.GetCellTypesArray() )   
    
        # Read cells scalar names.    
        # scalar_names = [reader.GetScalarsNameInFile(i) for i in range(0, reader.GetNumberOfScalarsInFile())]
    
        # Read cells scalars. 
     
        if i == 0:
            fuel_centerline_temp_data = vtk_to_numpy(grid.GetCellData().GetArray('Fuel_Centerline_Temp_C')) 
            fuel_surface_temp_data = vtk_to_numpy(grid.GetCellData().GetArray('Max_Fuel_Surface_Temp_C'))
        elif i == 1:
            mixture_temp_data = vtk_to_numpy(grid.GetCellData().GetArray('Mixture_Temperature_C'))
            liquid_density_data = vtk_to_numpy(grid.GetCellData().GetArray('Liquid_Density'))
            vapor_density_data = vtk_to_numpy(grid.GetCellData().GetArray('Vapor_Density'))
            liquid_volume_fraction_data = vtk_to_numpy(grid.GetCellData().GetArray('Liquid_Volume_Fraction'))    
            vapor_volume_fraction_data = vtk_to_numpy(grid.GetCellData().GetArray('Vapor_Volume_Fraction'))  

     os.chdir("..")
     os.chdir("..")
     path = 'feedbackcoupler'
     os.chdir(path)      
     # Fuel Temperatures
     fuel_temp_arr3d = (fuel_centerline_temp_data.reshape((nrows, ncols, nlayers+2))+ fuel_surface_temp_data.reshape((nrows, ncols, nlayers+2)))/2
     fuel_temp_arr3d = np.delete(fuel_temp_arr3d, (0,nlayers+1), axis = 2)

     # Coolant Temperatures
     cool_temp_arr3d = ctf_array_to_dyn3d_array(mixture_temp_data.reshape((nrows+1, ncols+1, nlayers)),"subchanneltochannel.dat")

     # Coolant Densities
     cool_dens_arr3d = ctf_array_to_dyn3d_array(liquid_density_data.reshape((nrows+1, ncols+1, nlayers))*liquid_volume_fraction_data.reshape((nrows+1, ncols+1, nlayers))+vapor_density_data.reshape((nrows+1, ncols+1, nlayers))*vapor_volume_fraction_data.reshape((nrows+1, ncols+1, nlayers)),"subchanneltochannel.dat")

     # Boron Concentration
     bor_conc_arr3d=np.ones((nrows, ncols, nlayers))
     bor_conc_arr3d = boron_concentration*bor_conc_arr3d

     fuel_temp_arr1d= fuel_temp_arr3d.reshape((nrows*ncols*nlayers, 1))
     cool_temp_arr1d= cool_temp_arr3d.reshape((nrows*ncols*nlayers, 1))
     cool_dens_arr1d= cool_dens_arr3d.reshape((nrows*ncols*nlayers, 1))
     bor_conc_arr1d= bor_conc_arr3d.reshape((nrows*ncols*nlayers, 1))
     feedback_arr1d=np.hstack([fuel_temp_arr1d, cool_temp_arr1d, cool_dens_arr1d, bor_conc_arr1d])
     os.chdir("..")
     path = 'outputs/feedbackcoupler_iteration'+str(iteration)
     os.chdir(path) 
     if iteration == 0:
        np.savetxt('feedbackarr1dnewsur.dat',feedback_arr1d, fmt='%1.5e')
     else:
        np.savetxt('feedbackarr1dold.dat',feedback_arr1d, fmt='%1.5e')
     
     os.chdir("..")
     os.chdir("..")

     path = 'feedbackcoupler'
     os.chdir(path) 
     return fuel_temp_arr1d, cool_temp_arr1d, cool_dens_arr1d, bor_conc_arr1d
# ---------------------------Script parameters------------------------------------


