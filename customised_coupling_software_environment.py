import pandas as pd
import numpy as np
import math as mt
import sys
import os
import subprocess
import functools
import multiprocessing
sys.path.append("boundaryconditionscoupler")
from main_boundary_conditions import main_boundary_conditions
sys.path.append("feedbackcoupler")
from main_feedback import main_feedback
sys.path.append("powerscoupler")
from main_powers import main_powers
sys.path.append("other")
from output_gen import output_gen
np.set_printoptions(threshold=np.inf)
def customised_coupling_software_environment(coupling,couplingsoftware,couplinginputnames, couplingoutputnames,  initial, initialconditions,niterations, corerows,corecols,nassemblies,nreflectors,nrows,ncols,nlayers,nsides,nrodsperassembly,height,ngroups, assembly_row,assembly_col, feedback_relaxation, power_relaxation, nmaterials, materials_libraries,materials_list, burnable_absorbers):

   print("Coupling between "+str(coupling)+" Start")

   path = 'other'
   os.chdir(path)   
   output_gen(coupling, initial, -1)
   os.chdir("..")
  
   #DYN3D assembly level Execution  
   print("DYN3D Fuel Assembly Level Start") 
   path = 'outputs/DYN3D_3Dcoreassemblylevel'
   os.chdir(path)
   DYN3D_execution = subprocess.run([str(couplingsoftware[0])+" "+str(couplinginputnames[0])+" echo"], shell=True) 
   os.chdir("..")
   os.chdir("..")
   print("DYN3D Fuel Assembly Level End")  
   
   #DYN3D Boundary Conditions Export   
   print("Boundary Conditions Coupler Start")  
   path2= 'outputs/boundaryconditionscoupler'
   os.mkdir(path2)
   path = 'boundaryconditionscoupler'
   os.chdir(path)
   main_boundary_conditions(coupling, couplinginputnames, couplingoutputnames,corerows,corecols,nassemblies,nreflectors,nrows,ncols,nlayers,nsides,nrodsperassembly,height,ngroups,assembly_row,assembly_col)
   os.chdir("..")   
   print("Boundary Conditions Coupler End")  
   
   #Main Coupling
   for iteration in range(niterations):
      
      path = 'other'
      os.chdir(path)   
      output_gen(coupling, initial, iteration) 
      os.chdir("..")
      
      if initial == 'first_iteration_constant_feedback':       
        #Feedback Generation or Export from CTF and import into DYN3D or LOTUS
        print("Feedback Coupler Start Iteration"+str(iteration))
        path = 'feedbackcoupler'
        os.chdir(path)
        main_feedback(coupling,couplinginputnames, couplingoutputnames, initial,initialconditions, iteration,corerows,corecols,nrows,ncols,nlayers, ngroups, assembly_row,assembly_col,feedback_relaxation, nmaterials, materials_libraries,materials_list, burnable_absorbers)
        os.chdir("..")
        print("Feedback Coupler End Iteration"+str(iteration))
      
        #DYN3D pin level or LOTUS pin or materials level Execution        
        if coupling == 'DYN3D_CTF_2D_cell_level':
            print("DYN3D Fuel Pin Level Start Iteration"+str(iteration))
            path = 'outputs/DYN3D_2Dassemblycelllevel_iteration'+str(iteration)
            os.chdir(path)
            shell = functools.partial(subprocess.run, shell=True)
            DYN3D_execution =[]
            for k in range(nlayers):
                DYN3D_execution.append("cd node"+str(k+1)+" && "+str(couplingsoftware[1])+" "+str(couplinginputnames[1])+str(k+1)+" echo && cd ..")
            pool = multiprocessing.Pool(processes=nlayers)
            pool.map(shell,DYN3D_execution)
            pool.close()
            pool.join()
            os.chdir("..")
            os.chdir("..")
            print("DYN3D Fuel Pin Level End Iteration"+str(iteration))   
          
        elif coupling == 'DYN3D_CTF_3D_cell_level':
            print("DYN3D Fuel Pin Level Start Iteration"+str(iteration))
            path = 'outputs/DYN3D_3Dassemblycelllevel_iteration'+str(iteration)
            os.chdir(path)
            DYN3D_execution = subprocess.run([str(couplingsoftware[1])+" "+str(couplinginputnames[1])+" echo"], shell=True)
            os.chdir("..")
            os.chdir("..")
            print("DYN3D Fuel Pin Level End Iteration"+str(iteration))  
           
        elif coupling == 'LOTUS_CTF_2D_cell_level':
            print("LOTUS Fuel Pin Level Start Iteration"+str(iteration))
            path = 'outputs/LOTUS_2Dassemblycelllevel_iteration'+str(iteration)
            os.chdir(path)
            shell = functools.partial(subprocess.run, shell=True)
            LOTUS_execution =[]
            for k in range(nlayers):
              LOTUS_execution.append("cd node"+str(k+1)+" && "+str(couplingsoftware[1])+" "+str(couplinginputnames[1])+str(k+1)+".py && cd ..")
            pool = multiprocessing.Pool(processes=nlayers)
            pool.map(shell,LOTUS_execution)
            pool.close()
            pool.join()
            os.chdir("..")
            os.chdir("..")
            print("LOTUS Fuel Pin Level End Iteration"+str(iteration))  
          
        elif coupling == 'LOTUS_CTF_2D_materials_level':
            print("LOTUS Fuel Pin Level Start Iteration"+str(iteration))
            path = 'outputs/LOTUS_2Dassemblymaterialslevel_iteration'+str(iteration)
            os.chdir(path)
            shell = functools.partial(subprocess.run, shell=True)
            LOTUS_execution =[]
            for k in range(nlayers):
              LOTUS_execution.append("cd node"+str(k+1)+" && "+str(couplingsoftware[1])+" "+str(couplinginputnames[1])+str(k+1)+".py && cd ..")
            pool = multiprocessing.Pool(processes=nlayers)
            pool.map(shell,LOTUS_execution)
            pool.close()
            pool.join()
            os.chdir("..")
            os.chdir("..")
            print("LOTUS Materials Level End Iteration"+str(iteration))  
          
        #Power Generation or Export from DYN3D or LOTUS and import into CTF
        print("Powers Coupler Start Iteration"+str(iteration))
        path = 'powerscoupler' 
        os.chdir(path)
        main_powers(coupling,couplinginputnames, couplingoutputnames, initial,initialconditions, iteration,corerows,corecols,nrows,ncols,nlayers,height,assembly_row,assembly_col,power_relaxation)
        os.chdir("..")
        print("Powers Coupler End Iteration"+str(iteration))
      
        #CTF pin level Execution
        print("CTF Fuel Pin Level Start Iteration"+str(iteration))
        path = 'outputs/CTF_assemblycelllevel_iteration'+str(iteration)
        os.chdir(path)
        CTF_execution = subprocess.run([str(couplingsoftware[2])+" "+str(couplinginputnames[2])+".inp"], shell=True)
        os.chdir("..")
        os.chdir("..")
        print("CTF Fuel Pin Level End Iteration"+str(iteration))
        
      elif initial == 'first_iteration_constant_power':         
        #Power Generation or Export from DYN3D or LOTUS and import into CTF
        print("Powers Coupler Start Iteration"+str(iteration))
        path = 'powerscoupler' 
        os.chdir(path)
        main_powers(coupling,couplinginputnames, couplingoutputnames, initial,initialconditions, iteration,corerows,corecols,nrows,ncols,nlayers,height,assembly_row,assembly_col,power_relaxation)
        os.chdir("..")
        print("Powers Coupler End Iteration"+str(iteration))
      
        #CTF pin level Execution
        print("CTF Fuel Pin Level Start Iteration"+str(iteration))
        path = 'outputs/CTF_assemblycelllevel_iteration'+str(iteration)
        os.chdir(path)
        CTF_execution = subprocess.run([str(couplingsoftware[2])+" "+str(couplinginputnames[2])+".inp"], shell=True)
        os.chdir("..")
        os.chdir("..")
        print("CTF Fuel Pin Level End Iteration"+str(iteration))

        #Feedback Generation or Export from CTF and import into DYN3D or LOTUS
        print("Feedback Coupler Start Iteration"+str(iteration))
        path = 'feedbackcoupler'
        os.chdir(path)
        main_feedback(coupling,couplinginputnames, couplingoutputnames, initial,initialconditions, iteration,corerows,corecols,nrows,ncols,nlayers, ngroups, assembly_row,assembly_col,feedback_relaxation, nmaterials, materials_libraries,materials_list, burnable_absorbers)
        os.chdir("..")
        print("Feedback Coupler End Iteration"+str(iteration))
      
        #DYN3D pin level or LOTUS pin or materials level Execution        
        if coupling == 'DYN3D_CTF_2D_cell_level':
            print("DYN3D Fuel Pin Level Start Iteration"+str(iteration))
            path = 'outputs/DYN3D_2Dassemblycelllevel_iteration'+str(iteration)
            os.chdir(path)
            shell = functools.partial(subprocess.run, shell=True)
            DYN3D_execution =[]
            for k in range(nlayers):
                DYN3D_execution.append("cd node"+str(k+1)+" && "+str(couplingsoftware[1])+" "+str(couplinginputnames[1])+str(k+1)+" echo && cd ..")
            pool = multiprocessing.Pool(processes=nlayers)
            pool.map(shell,DYN3D_execution)
            pool.close()
            pool.join()
            os.chdir("..")
            os.chdir("..")
            print("DYN3D Fuel Pin Level End Iteration"+str(iteration))   
          
        elif coupling == 'DYN3D_CTF_3D_cell_level':
            print("DYN3D Fuel Pin Level Start Iteration"+str(iteration))
            path = 'outputs/DYN3D_3Dassemblycelllevel_iteration'+str(iteration)
            os.chdir(path)
            DYN3D_execution = subprocess.run([str(couplingsoftware[1])+" "+str(couplinginputnames[1])+" echo"], shell=True)
            os.chdir("..")
            os.chdir("..")
            print("DYN3D Fuel Pin Level End Iteration"+str(iteration))  
           
        elif coupling == 'LOTUS_CTF_2D_cell_level':
            print("LOTUS Fuel Pin Level Start Iteration"+str(iteration))
            path = 'outputs/LOTUS_2Dassemblycelllevel_iteration'+str(iteration)
            os.chdir(path)
            shell = functools.partial(subprocess.run, shell=True)
            LOTUS_execution =[]
            for k in range(nlayers):
              LOTUS_execution.append("cd node"+str(k+1)+" && "+str(couplingsoftware[1])+" "+str(couplinginputnames[1])+str(k+1)+".py && cd ..")
            pool = multiprocessing.Pool(processes=nlayers)
            pool.map(shell,LOTUS_execution)
            pool.close()
            pool.join()
            os.chdir("..")
            os.chdir("..")
            print("LOTUS Fuel Pin Level End Iteration"+str(iteration))  
          
        elif coupling == 'LOTUS_CTF_2D_materials_level':
            print("LOTUS Fuel Pin Level Start Iteration"+str(iteration))
            path = 'outputs/LOTUS_2Dassemblymaterialslevel_iteration'+str(iteration)
            os.chdir(path)
            shell = functools.partial(subprocess.run, shell=True)
            LOTUS_execution =[]
            for k in range(nlayers):
              LOTUS_execution.append("cd node"+str(k+1)+" && "+str(couplingsoftware[1])+" "+str(couplinginputnames[1])+str(k+1)+".py && cd ..")
            pool = multiprocessing.Pool(processes=nlayers)
            pool.map(shell,LOTUS_execution)
            pool.close()
            pool.join()
            os.chdir("..")
            os.chdir("..")
            print("LOTUS Materials Level End Iteration"+str(iteration))  
            
   return "Coupling between "+str(coupling)+" End"

