import pandas as pd
import numpy as np
import math as mt
import shutil
import sys
import os
sys.path.append("..")
from user_input import *
if DYN3D_CTF_2D_cell_level:
    coupling='DYN3D_CTF_2D_cell_level'
    couplingsoftware=[DYN3D_3Dcoreassemblylevel_software, DYN3D_2Dassemblycelllevel_software, CTF_assemblycelllevel_software]
    couplinginputnames=[DYN3D_3Dcoreassemblylevel_inputname, DYN3D_2Dassemblycelllevel_inputname, CTF_assemblycelllevel_inputname]
    couplingoutputnames=[DYN3D_3Dcoreassemblylevel_outputname, DYN3D_2Dassemblycelllevel_outputname, CTF_assemblycelllevel_outputname,CTF_assemblycelllevel_outputname2]
elif DYN3D_CTF_3D_cell_level:
    coupling='DYN3D_CTF_3D_cell_level'
    couplingsoftware=[DYN3D_3Dcoreassemblylevel_software, DYN3D_3Dassemblycelllevel_software, CTF_assemblycelllevel_software]
    couplinginputnames=[DYN3D_3Dcoreassemblylevel_inputname, DYN3D_3Dassemblycelllevel_inputname, CTF_assemblycelllevel_inputname]
    couplingoutputnames=[DYN3D_3Dcoreassemblylevel_outputname, DYN3D_3Dassemblycelllevel_outputname, CTF_assemblycelllevel_outputname,CTF_assemblycelllevel_outputname2]
elif LOTUS_CTF_2D_cell_level:
    coupling='LOTUS_CTF_2D_cell_level'  
    couplingsoftware=[DYN3D_3Dcoreassemblylevel_software, LOTUS_2Dassemblycelllevel_software, CTF_assemblycelllevel_software]
    couplinginputnames=[DYN3D_3Dcoreassemblylevel_inputname, LOTUS_2Dassemblycelllevel_inputname, CTF_assemblycelllevel_inputname]
    couplingoutputnames=[DYN3D_3Dcoreassemblylevel_outputname, LOTUS_2Dassemblycelllevel_outputname, CTF_assemblycelllevel_outputname,CTF_assemblycelllevel_outputname2]
elif LOTUS_CTF_2D_materials_level:
    coupling='LOTUS_CTF_2D_materials_level'
    couplingsoftware=[DYN3D_3Dcoreassemblylevel_software, LOTUS_2Dassemblymaterialslevel_software, CTF_assemblycelllevel_software]
    couplinginputnames=[DYN3D_3Dcoreassemblylevel_inputname, LOTUS_2Dassemblymaterialslevel_inputname, CTF_assemblycelllevel_inputname]
    couplingoutputnames=[DYN3D_3Dcoreassemblylevel_outputname, LOTUS_2Dassemblymaterialslevel_outputname, CTF_assemblycelllevel_outputname,CTF_assemblycelllevel_outputname2]
    
    
if first_iteration_constant_feedback:
    initial='first_iteration_constant_feedback'

elif first_iteration_constant_power:
    initial='first_iteration_constant_power'
    
initialconditions=[fuel_temp0, cool_temp0, cool_dens0, boron_concentration0,pow0]