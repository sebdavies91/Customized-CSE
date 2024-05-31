import pandas as pd
import numpy as np
import math as mt
from dyn3d_axial_pow_exp import dyn3d_axial_pow_exp
from dyn3d_alb_exp import dyn3d_alb_exp
from dyn3d_2D_alb_imp import dyn3d_2D_alb_imp
from dyn3d_3D_alb_imp import dyn3d_3D_alb_imp
from lotus_2D_cell_alb_imp import lotus_2D_cell_alb_imp
from lotus_2D_mat_alb_imp import lotus_2D_mat_alb_imp
from dyn3d_vals_exp import dyn3d_vals_exp
from ctf_vals_imp import ctf_vals_imp
np.set_printoptions(threshold=np.inf)

def main_boundary_conditions(coupling, couplinginputnames, couplingoutputnames,corerows,corecols,nassemblies,nreflectors,nrows,ncols,nlayers,nsides,nrodsperassembly,height,ngroups,assembly_row,assembly_col):

    
    #Calculations
    
    if coupling == 'DYN3D_CTF_2D_cell_level':
        dyn3d_axial_pow_exp(couplingoutputnames[0], corerows, corecols, nlayers)
        dyn3d_alb_exp(couplingoutputnames[0], corerows, corecols, nlayers, nsides, ngroups)
        dyn3d_2D_alb_imp( couplinginputnames[1], 'albedosarr1d.dat',corerows, corecols, nlayers, nsides, ngroups, assembly_row, assembly_col)
        dyn3d_vals_exp(couplingoutputnames[0], corerows, corecols)
        ctf_vals_imp(couplinginputnames[2],'totalpowersarr1d.dat', 'totalmassfluxesarr1d.dat', 'totalboronconcentrationsarr1d.dat', 'globalboundaryconditions.dat',corerows, corecols, nassemblies,nreflectors, nrows,ncols,nrodsperassembly, height,assembly_row, assembly_col)
        
    elif coupling == 'DYN3D_CTF_3D_cell_level':
        dyn3d_alb_exp(couplingoutputnames[0], corerows, corecols, nlayers, nsides, ngroups)
        dyn3d_3D_alb_imp( couplinginputnames[1], 'albedosarr1d.dat',corerows, corecols, nlayers, nsides, ngroups, assembly_row, assembly_col)
        dyn3d_vals_exp(couplingoutputnames[0], corerows, corecols)
        ctf_vals_imp(couplinginputnames[2],'totalpowersarr1d.dat', 'totalmassfluxesarr1d.dat', 'totalboronconcentrationsarr1d.dat', 'globalboundaryconditions.dat',corerows, corecols, nassemblies,nreflectors, nrows,ncols,nrodsperassembly, height,assembly_row, assembly_col)
        
    elif  coupling == 'LOTUS_CTF_2D_cell_level':
        dyn3d_axial_pow_exp(couplingoutputnames[0], corerows, corecols, nlayers)
        dyn3d_alb_exp(couplingoutputnames[0], corerows, corecols, nlayers, nsides, ngroups)
        lotus_2D_cell_alb_imp(couplinginputnames[1],'albedosarr1d.dat',  corerows, corecols, nlayers, nsides, ngroups, assembly_row, assembly_col)   
        dyn3d_vals_exp(couplingoutputnames[0], corerows, corecols)
        ctf_vals_imp(couplinginputnames[2],'totalpowersarr1d.dat', 'totalmassfluxesarr1d.dat', 'totalboronconcentrationsarr1d.dat', 'globalboundaryconditions.dat',corerows, corecols, nassemblies,nreflectors, nrows,ncols,nrodsperassembly, height,assembly_row, assembly_col)
        
    elif  coupling == 'LOTUS_CTF_2D_materials_level':
        dyn3d_axial_pow_exp(couplingoutputnames[0], corerows, corecols, nlayers)
        dyn3d_alb_exp(couplingoutputnames[0], corerows, corecols, nlayers, nsides, ngroups)
        lotus_2D_mat_alb_imp(couplinginputnames[1],'albedosarr1d.dat',  corerows, corecols, nlayers, nsides, ngroups, assembly_row, assembly_col)   
        dyn3d_vals_exp(couplingoutputnames[0], corerows, corecols)
        ctf_vals_imp(couplinginputnames[2],'totalpowersarr1d.dat', 'totalmassfluxesarr1d.dat', 'totalboronconcentrationsarr1d.dat', 'globalboundaryconditions.dat',corerows, corecols, nassemblies,nreflectors, nrows,ncols,nrodsperassembly, height,assembly_row, assembly_col)

    
    return "Boundary Conditions Coupler"
