import pandas as pd
import numpy as np
import math as mt
import shutil
import os
def output_gen(coupling, initial, iteration):

   os.chdir("..")
   
   if iteration == -1:
    #Delete everything in outputs  
    folder = 'outputs'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
        
    #Create DYN3D output
    src_dir = "inputs/DYN3D_3Dcoreassemblylevel"   
    dest_dir = "outputs/DYN3D_3Dcoreassemblylevel"
    files = os.listdir(src_dir)
    shutil.copytree(src_dir, dest_dir)

    #Create DYN3D output   
    if coupling == 'DYN3D_CTF_2D_cell_level':
        src_dir = "inputs/DYN3D_2Dassemblycelllevel"   
        dest_dir = "outputs/DYN3D_2Dassemblycelllevel_iteration0"
        files = os.listdir(src_dir)
        shutil.copytree(src_dir, dest_dir)

   #Create DYN3D output    
    elif coupling == 'DYN3D_CTF_3D_cell_level':
        src_dir = "inputs/DYN3D_3Dassemblycelllevel"   
        dest_dir = "outputs/DYN3D_3Dassemblycelllevel_iteration0"
        files = os.listdir(src_dir)
        shutil.copytree(src_dir, dest_dir)

    #Create LOTUS output   
    elif coupling == 'LOTUS_CTF_2D_cell_level':
        src_dir = "inputs/LOTUS_2Dassemblycelllevel"   
        dest_dir = "outputs/LOTUS_2Dassemblycelllevel_iteration0"
        files = os.listdir(src_dir)
        shutil.copytree(src_dir, dest_dir)

   #Create LOTUS output   
    elif coupling == 'LOTUS_CTF_2D_materials_level':
        src_dir = "inputs/LOTUS_2Dassemblymaterialslevel"   
        dest_dir = "outputs/LOTUS_2Dassemblymaterialslevel_iteration0"
        files = os.listdir(src_dir)
        shutil.copytree(src_dir, dest_dir)
    
    #Create CTF output   
    src_dir = "inputs/CTF_assemblycelllevel"   
    dest_dir = "outputs/CTF_assemblycelllevel_iteration0"
    files = os.listdir(src_dir)
    shutil.copytree(src_dir, dest_dir) 
    
   else:
    if iteration == 0:
        dest_dir = "outputs/feedbackcoupler_iteration"+str(iteration)
        os.mkdir(dest_dir)
    else:
        src_dir = "outputs/feedbackcoupler_iteration"+str(iteration-1)   
        dest_dir = "outputs/feedbackcoupler_iteration"+str(iteration)
        files = os.listdir(src_dir)
        shutil.copytree(src_dir, dest_dir)
        
    if coupling == 'DYN3D_CTF_2D_cell_level':
        if iteration != 0:
          src_dir = "outputs/DYN3D_2Dassemblycelllevel_iteration"+str(iteration-1)   
          dest_dir = "outputs/DYN3D_2Dassemblycelllevel_iteration"+str(iteration)
          files = os.listdir(src_dir)
          shutil.copytree(src_dir, dest_dir)
    elif coupling == 'DYN3D_CTF_3D_cell_level':
        if iteration != 0:
          src_dir = "outputs/DYN3D_3Dassemblycelllevel_iteration"+str(iteration-1)   
          dest_dir = "outputs/DYN3D_3Dassemblycelllevel_iteration"+str(iteration)
          files = os.listdir(src_dir)
          shutil.copytree(src_dir, dest_dir)   
    elif coupling == 'LOTUS_CTF_2D_cell_level':
        if iteration != 0:
          src_dir = "outputs/LOTUS_2Dassemblycelllevel_iteration"+str(iteration-1)   
          dest_dir = "outputs/LOTUS_2Dassemblycelllevel_iteration"+str(iteration)
          files = os.listdir(src_dir)
          shutil.copytree(src_dir, dest_dir)
    elif coupling == 'LOTUS_CTF_2D_materials_level':
        if iteration != 0:
          src_dir = "outputs/LOTUS_2Dassemblymaterialslevel_iteration"+str(iteration-1)   
          dest_dir = "outputs/LOTUS_2Dassemblymaterialslevel_iteration"+str(iteration)
          files = os.listdir(src_dir)
          shutil.copytree(src_dir, dest_dir)

    if iteration == 0:
      dest_dir = "outputs/powerscoupler_iteration"+str(iteration)
      os.mkdir(dest_dir)
    else:
      src_dir = "outputs/powerscoupler_iteration"+str(iteration-1)   
      dest_dir = "outputs/powerscoupler_iteration"+str(iteration)
      files = os.listdir(src_dir)
      shutil.copytree(src_dir, dest_dir)         

    if iteration != 0:
      src_dir = "outputs/CTF_assemblycelllevel_iteration"+str(iteration-1)   
      dest_dir = "outputs/CTF_assemblycelllevel_iteration"+str(iteration)
      files = os.listdir(src_dir)
      shutil.copytree(src_dir, dest_dir)  
   path = 'other'
   os.chdir(path)     
   return 