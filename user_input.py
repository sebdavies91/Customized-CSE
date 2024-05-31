#Customised Coupling Software Environment Input


#Core size
corerows=3
corecols=3
nassemblies=4
nreflectors=5

#Assembly size
nrows=17
ncols=17
nlayers=9
nsides=6
nrodsperassembly=289
height=3.6576
ngroups=2


#Option for desired fuel assembly in the corresponding coupling.
assembly_row=0
assembly_col=1


#Number of iterations
niterations=5


#Options for the fuel assembly coupling relaxation
power_relaxation=0.5
feedback_relaxation=0.5


#Options for the fuel assembly coupling solution, 2D/3D means without or with axial streaming
#DYN3D_2D_assembly_level=False
#DYN3D_3D_assembly_level=False
DYN3D_CTF_2D_cell_level=False
DYN3D_CTF_3D_cell_level=True
LOTUS_CTF_2D_cell_level=False
LOTUS_CTF_2D_materials_level=False


#Options for the fuel assembly coupling first iteration

#first iteration neutronics
first_iteration_constant_feedback=True
fuel_temp0=287.0
cool_temp0=287.0
cool_dens0=752.0
boron_concentration0=900

#first iteration thermal hydraulics
first_iteration_constant_power=False
pow0=1.000000


#Inputs/Outputs adresses for the core and fuel assembly 
DYN3D_3Dcoreassemblylevel_inputname="bdcore" 
DYN3D_3Dcoreassemblylevel_outputname="bdcore" 

DYN3D_2Dassemblycelllevel_inputname="bd"
DYN3D_2Dassemblycelllevel_outputname="bd"

DYN3D_3Dassemblycelllevel_inputname="bd"
DYN3D_3Dassemblycelllevel_outputname="bd"

LOTUS_2Dassemblycelllevel_inputname="17x17"
LOTUS_2Dassemblycelllevel_outputname="fissionrates"

LOTUS_2Dassemblymaterialslevel_inputname="17x17"
LOTUS_2Dassemblymaterialslevel_inputname="fissionrates"

CTF_assemblycelllevel_inputname="deck"
CTF_assemblycelllevel_outputname="rods"
CTF_assemblycelllevel_outputname2="vis_results"

#Software adresses 
DYN3D_3Dcoreassemblylevel_software="/mnt/data2/users/nuclear/DYN3D/DYN3D_sebda"
DYN3D_2Dassemblycelllevel_software="/mnt/data2/users/nuclear/DYN3D/DYN3D_sebda"
DYN3D_3Dassemblycelllevel_software="/mnt/data2/users/nuclear/DYN3D/DYN3D_sebda"
LOTUS_2Dassemblycelllevel_software="python"
LOTUS_2Dassemblymaterialslevel_software="python"
CTF_assemblycelllevel_software="/mnt/data2/users/nuclear/CTF/mpi/cobratf"


#Options for the fuel assembly LOTUS cell or materials level coupling iterpolation
nmaterials=2
#Cell level
materials_libraries=["2G_uo2_cr.dat","2G_tube_cr.dat"]
materials_list=["Rod_","Guide_"]
#Materials level
#materials_libraries=["2G_u_cr.dat","2G_gap_cr.dat","2G_clad_cr.dat","2G_water_cr.dat"]
#materials_list=["UO2_","Gap_","Clad_","Water_"]
burnable_absorbers=False








    
    
