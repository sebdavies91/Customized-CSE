#Customised Coupling Software Environment Execution
import sys
from customised_coupling_software_environment import customised_coupling_software_environment
sys.path.append("other")
from input_set import *
from user_input import *


customised_coupling_software_environment(coupling,couplingsoftware,couplinginputnames, couplingoutputnames,  initial, initialconditions,niterations, corerows,corecols,nassemblies,nreflectors,nrows,ncols,nlayers,nsides,nrodsperassembly,height,ngroups, assembly_row,assembly_col, feedback_relaxation, power_relaxation, nmaterials, materials_libraries,materials_list, burnable_absorbers)
