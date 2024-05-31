import pandas as pd
import numpy as np
import math as mt
from cons_feed_gen import cons_feed_gen
from ctf_feed_exp import ctf_feed_exp
from under_rel_feed import under_rel_feed
from dyn3d_2D_feed_imp import dyn3d_2D_feed_imp
from dyn3d_3D_feed_imp import dyn3d_3D_feed_imp
from lotus_2D_cell_feed_imp import lotus_2D_cell_feed_imp
from lotus_2D_mat_feed_imp import lotus_2D_mat_feed_imp
np.set_printoptions(threshold=np.inf)

def main_feedback(coupling,couplinginputnames, couplingoutputnames, initial,initialconditions, iteration,corerows,corecols,nrows,ncols,nlayers, ngroups, assembly_row,assembly_col,feedback_relaxation, nmaterials, materials_libraries,materials_list, burnable_absorbers):

    #Calculations
    if coupling == 'DYN3D_CTF_2D_cell_level':
        if iteration == 0:
            if initial == 'first_iteration_constant_feedback':
                cons_feed_gen(initialconditions[0], initialconditions[1], initialconditions[2], initialconditions[3], nrows, ncols, nlayers)
                dyn3d_2D_feed_imp('feedbackarr1dnewsur.dat',iteration,nrows,ncols,nlayers)
            elif initial == 'first_iteration_constant_power':
                ctf_feed_exp( couplingoutputnames[2], couplingoutputnames[3],initial,iteration, nrows, ncols, nlayers, initialconditions[3])
                dyn3d_2D_feed_imp('feedbackarr1dnewsur.dat',iteration,nrows,ncols,nlayers)
        else:
            ctf_feed_exp( couplingoutputnames[2], couplingoutputnames[3],initial,iteration, nrows, ncols, nlayers, initialconditions[3])
            under_rel_feed('feedbackarr1dold.dat','feedbackarr1doldsur.dat', iteration, nrows, ncols, nlayers, feedback_relaxation)
            dyn3d_2D_feed_imp('feedbackarr1dnewsur.dat',iteration,nrows,ncols,nlayers)
            
    elif coupling == 'DYN3D_CTF_3D_cell_level':
        if iteration == 0:
            if initial == 'first_iteration_constant_feedback':
                cons_feed_gen(initialconditions[0], initialconditions[1], initialconditions[2], initialconditions[3], nrows, ncols, nlayers)
                dyn3d_3D_feed_imp('feedbackarr1dnewsur.dat',iteration,nrows,ncols,nlayers)
            elif initial == 'first_iteration_constant_power':
                ctf_feed_exp( couplingoutputnames[2], couplingoutputnames[3],initial,iteration, nrows, ncols, nlayers, initialconditions[3])
                dyn3d_3D_feed_imp('feedbackarr1dnewsur.dat',iteration,nrows,ncols,nlayers)
        else:
            ctf_feed_exp( couplingoutputnames[2], couplingoutputnames[3],initial,iteration, nrows, ncols, nlayers, initialconditions[3])
            under_rel_feed('feedbackarr1dold.dat','feedbackarr1doldsur.dat', iteration, nrows, ncols, nlayers, feedback_relaxation)
            dyn3d_3D_feed_imp('feedbackarr1dnewsur.dat',iteration,nrows,ncols,nlayers)
            
    elif coupling == 'LOTUS_CTF_2D_cell_level':
        if iteration == 0:
            if initial == 'first_iteration_constant_feedback':
                cons_feed_gen(initialconditions[0], initialconditions[1], initialconditions[2], initialconditions[3], nrows, ncols, nlayers)
                lotus_2D_cell_feed_imp('feedbackarr1dnewsur.dat',iteration,nrows,ncols,nlayers,ngroups,nmaterials,materials_libraries,materials_list, burnable_absorbers)
            elif initial == 'first_iteration_constant_power':
                ctf_feed_exp( couplingoutputnames[2], couplingoutputnames[3],initial,iteration, nrows, ncols, nlayers, initialconditions[3])
                lotus_2D_cell_feed_imp('feedbackarr1dnewsur.dat',iteration,nrows,ncols,nlayers,ngroups,nmaterials,materials_libraries,materials_list, burnable_absorbers)
        else:
            ctf_feed_exp( couplingoutputnames[2], couplingoutputnames[3],initial,iteration, nrows, ncols, nlayers, initialconditions[3])
            under_rel_feed('feedbackarr1dold.dat','feedbackarr1doldsur.dat', iteration, nrows, ncols, nlayers, feedback_relaxation)
            lotus_2D_cell_feed_imp('feedbackarr1dnewsur.dat',iteration,nrows,ncols,nlayers,ngroups,nmaterials,materials_libraries,materials_list, burnable_absorbers)
    
    elif coupling == 'LOTUS_CTF_2D_materials_level':
        if iteration == 0:
            if initial == 'first_iteration_constant_feedback':
                cons_feed_gen(initialconditions[0], initialconditions[1], initialconditions[2], initialconditions[3], nrows, ncols, nlayers)
                lotus_2D_mat_feed_imp('feedbackarr1dnewsur.dat',iteration,nrows,ncols,nlayers,ngroups,nmaterials,materials_libraries,materials_list, burnable_absorbers)
            elif initial == 'first_iteration_constant_power':
                ctf_feed_exp( couplingoutputnames[2], couplingoutputnames[3],initial,iteration, nrows, ncols, nlayers, initialconditions[3])
                lotus_2D_mat_feed_imp('feedbackarr1dnewsur.dat',iteration,nrows,ncols,nlayers,ngroups,nmaterials,materials_libraries,materials_list, burnable_absorbers)
        else:
            ctf_feed_exp( couplingoutputnames[2], couplingoutputnames[3],initial,iteration, nrows, ncols, nlayers, initialconditions[3])
            under_rel_feed('feedbackarr1dold.dat','feedbackarr1doldsur.dat', iteration, nrows, ncols, nlayers, feedback_relaxation)
            lotus_2D_mat_feed_imp('feedbackarr1dnewsur.dat',iteration,nrows,ncols,nlayers,ngroups,nmaterials,materials_libraries,materials_list, burnable_absorbers)
                
    return "Feedback Coupler Iteration "+str(iteration)
