import pandas as pd
import numpy as np
import math as mt
from cons_pow_gen import cons_pow_gen
from dyn3d_2D_pow_exp import dyn3d_2D_pow_exp
from dyn3d_3D_pow_exp import dyn3d_3D_pow_exp
from lotus_2D_cell_pow_exp import lotus_2D_cell_pow_exp
from lotus_2D_mat_pow_exp import lotus_2D_mat_pow_exp
from under_rel_pow import under_rel_pow
from ctf_pow_imp import ctf_pow_imp
np.set_printoptions(threshold=np.inf)

def main_powers(coupling,couplinginputnames, couplingoutputnames, initial,initialconditions, iteration,corerows,corecols,nrows,ncols,nlayers,height,assembly_row,assembly_col,power_relaxation):

    #Calculations
    if coupling == 'DYN3D_CTF_2D_cell_level':
        if iteration == 0:
            if initial == 'first_iteration_constant_feedback':
                dyn3d_2D_pow_exp(couplingoutputnames[1], 'powersarr1ddyn3d.dat', initial,iteration, corerows, corecols,nrows, ncols, nlayers,assembly_row, assembly_col)
                ctf_pow_imp(couplinginputnames[2],'powersarr1dnewsur.dat', iteration,nrows,ncols,nlayers,height)  
            elif initial == 'first_iteration_constant_power':
                cons_pow_gen(initialconditions[4], nrows, ncols, nlayers)
                ctf_pow_imp(couplinginputnames[2],'powersarr1dnewsur.dat', iteration,nrows,ncols,nlayers,height)  
        else:
            dyn3d_2D_pow_exp(couplingoutputnames[1], 'powersarr1ddyn3d.dat', initial,iteration, corerows, corecols,nrows, ncols, nlayers,assembly_row, assembly_col)
            under_rel_pow('powersarr1dold.dat','powersarr1doldsur.dat', iteration, nrows, ncols, nlayers,power_relaxation)
            ctf_pow_imp(couplinginputnames[2],'powersarr1dnewsur.dat', iteration,nrows,ncols,nlayers,height) 
            
    elif coupling == 'DYN3D_CTF_3D_cell_level':
        if iteration == 0:
            if initial == 'first_iteration_constant_feedback':
                dyn3d_3D_pow_exp(couplingoutputnames[1], initial,iteration, corerows, corecols,nrows, ncols, nlayers,assembly_row, assembly_col)
                ctf_pow_imp(couplinginputnames[2],'powersarr1dnewsur.dat', iteration,nrows,ncols,nlayers,height)   
            elif initial == 'first_iteration_constant_power':
                cons_pow_gen(initialconditions[4], nrows, ncols, nlayers)
                ctf_pow_imp(couplinginputnames[2],'powersarr1dnewsur.dat', iteration,nrows,ncols,nlayers,height)   
        else:
            dyn3d_3D_pow_exp(couplingoutputnames[1], initial,iteration, corerows, corecols,nrows, ncols, nlayers,assembly_row, assembly_col)
            under_rel_pow('powersarr1dold.dat','powersarr1doldsur.dat', iteration, nrows, ncols, nlayers,power_relaxation)
            ctf_pow_imp(couplinginputnames[2],'powersarr1dnewsur.dat', iteration,nrows,ncols,nlayers,height)  
            
    elif coupling == 'LOTUS_CTF_2D_cell_level':
        if iteration == 0:
            if initial == 'first_iteration_constant_feedback':
                lotus_2D_cell_pow_exp( couplingoutputnames[1], 'powersarr1ddyn3d.dat', initial,iteration, corerows, corecols,nrows, ncols, nlayers,assembly_row, assembly_col)
                ctf_pow_imp(couplinginputnames[2],'powersarr1dnewsur.dat', iteration,nrows,ncols,nlayers,height) 
            elif initial == 'first_iteration_constant_power':
                cons_pow_gen(initialconditions[4], nrows, ncols, nlayers)
                ctf_pow_imp(couplinginputnames[2],'powersarr1dnewsur.dat', iteration,nrows,ncols,nlayers,height)  
        else:
            lotus_2D_cell_pow_exp( couplingoutputnames[1], 'powersarr1ddyn3d.dat', initial,iteration, corerows, corecols,nrows, ncols, nlayers,assembly_row, assembly_col)
            under_rel_pow('powersarr1dold.dat','powersarr1doldsur.dat', iteration, nrows, ncols, nlayers,power_relaxation)
            ctf_pow_imp(couplinginputnames[2],'powersarr1dnewsur.dat', iteration,nrows,ncols,nlayers,height) 
            
    elif coupling == 'LOTUS_CTF_2D_materials_level':
        if iteration == 0:
            if initial == 'first_iteration_constant_feedback':
                lotus_2D_mat_pow_exp( couplingoutputnames[1], 'powersarr1ddyn3d.dat', initial,iteration, corerows, corecols,nrows, ncols, nlayers,assembly_row, assembly_col)
                ctf_pow_imp(couplinginputnames[2],'powersarr1dnewsur.dat', iteration,nrows,ncols,nlayers,height)   
            elif initial == 'first_iteration_constant_power':
                cons_pow_gen(initialconditions[4], nrows, ncols, nlayers)
                ctf_pow_imp(couplinginputnames[2],'powersarr1dnewsur.dat', iteration,nrows,ncols,nlayers,height) 
        else:
            lotus_2D_mat_pow_exp( couplingoutputnames[1], 'powersarr1ddyn3d.dat', initial,iteration, corerows, corecols,nrows, ncols, nlayers,assembly_row, assembly_col)
            under_rel_pow('powersarr1dold.dat','powersarr1doldsur.dat', iteration, nrows, ncols, nlayers,power_relaxation)
            ctf_pow_imp(couplinginputnames[2],'powersarr1dnewsur.dat', iteration,nrows,ncols,nlayers,height)       
        
  
    return "Powers Coupler Iteration "+str(iteration)
