import pandas as pd
import numpy as np
import math as mt
import os         
np.set_printoptions(threshold=np.inf)
from preliminary_data_exp import preliminary_data_exp
from transport_xsections_exp import transport_xsections_exp
from transport_xsections_interp import transport_xsections_interp
from absorption_xsections_exp import absorption_xsections_exp
from absorption_xsections_interp import absorption_xsections_interp
from nu_fission_xsections_exp import nu_fission_xsections_exp
from nu_fission_xsections_interp import nu_fission_xsections_interp
from kappa_fission_xsections_exp import kappa_fission_xsections_exp
from kappa_fission_xsections_interp import kappa_fission_xsections_interp
from p0_scattering_xsections_exp import p0_scattering_xsections_exp
from p0_scattering_xsections_interp import p0_scattering_xsections_interp
from adf_tables_exp import adf_tables_exp
from adf_tables_interp import adf_tables_interp
from fission_spectrum_exp import fission_spectrum_exp
from fission_xsections_conv import fission_xsections_conv
from hdf5_mat_converter import hdf5_mat_converter

def lotus_2D_mat_feed_imp(filename2: str,iteration,nrows,ncols,nlayers,ngroups,nmaterials,materials_libraries,materials_list, burnable_absorbers):


    """
    1 burnup state, n groups
    """
    """
    loading feedback
    """
    os.chdir("..")
    path = 'outputs/feedbackcoupler_iteration'+str(iteration)
    os.chdir(path)     
    feedback_arr1d = np.loadtxt(filename2,float)
    os.chdir("..")
    os.chdir("..")
    path = 'feedbackcoupler'
    os.chdir(path)  	
    fuel_temp_arr1d= feedback_arr1d[:,0]
    cool_temp_arr1d= feedback_arr1d[:,1]
    cool_dens_arr1d= feedback_arr1d[:,2]
    bor_conc_arr1d= feedback_arr1d[:,3]

    fuel_temp_arr3d=fuel_temp_arr1d.reshape((nrows,ncols,nlayers))	
    cool_temp_arr3d=cool_temp_arr1d.reshape((nrows,ncols,nlayers))
    cool_dens_arr3d=cool_dens_arr1d.reshape((nrows,ncols,nlayers))
    bor_conc_arr3d=bor_conc_arr1d.reshape((nrows,ncols,nlayers))

    transport_xsections_interp_material =np.zeros((nmaterials,ngroups,nrows,ncols,nlayers))
    absorption_xsections_interp_material =np.zeros((nmaterials,ngroups,nrows,ncols,nlayers))
    nu_fission_xsections_interp_material =np.zeros((nmaterials,ngroups,nrows,ncols,nlayers))
    kappa_fission_xsections_interp_material =np.zeros((nmaterials,ngroups,nrows,ncols,nlayers))
    p0_scattering_xsections_interp_material =np.zeros((nmaterials,ngroups*ngroups,nrows,ncols,nlayers))
    transport_xsections_interp_material =np.zeros((nmaterials,ngroups,nrows,ncols,nlayers))
    adf_tables_interp_material =np.zeros((nmaterials,ngroups,nrows,ncols,nlayers))
    fission_spectrum_material =np.zeros((nmaterials,ngroups))
    fission_xsections_interp_material =np.zeros((nmaterials,ngroups,nrows,ncols,nlayers))
    total_xsections_interp_material =np.zeros((nmaterials,ngroups,nrows,ncols,nlayers))
    for m in range(0,nmaterials):
        
        filename=materials_libraries[m]
        
        """
        loading preliminary data
        """
        os.chdir("..")
        path = 'libraries'
        os.chdir(path) 
        preliminary_data_exp_arr=preliminary_data_exp(filename)
        os.chdir("..")
        path = 'feedbackcoupler'
        os.chdir(path)         
        nmoddens=preliminary_data_exp_arr[0]
        nborconc=preliminary_data_exp_arr[1]
        nfueltemp=preliminary_data_exp_arr[2]
        moddensities_arr=preliminary_data_exp_arr[3]
        boronconcentrations_arr=preliminary_data_exp_arr[4]
        fueltemperatures_arr=preliminary_data_exp_arr[5]
   
        """
        loading transport xsections
        """
        os.chdir("..")
        path = 'libraries'
        os.chdir(path) 
        transport_xsections_arr= transport_xsections_exp(filename,ngroups,nmoddens,nfueltemp,nborconc)
        os.chdir("..")
        path = 'feedbackcoupler'
        os.chdir(path) 
        """
        interpolating transport xsections
        """   
        transport_xsections_interp_material[m] = transport_xsections_interp(filename2, moddensities_arr, fueltemperatures_arr, boronconcentrations_arr, cool_dens_arr3d, fuel_temp_arr3d, bor_conc_arr3d, transport_xsections_arr, ngroups,nrows,ncols,nlayers)

        #print(transport_xsections_interp_material.shape)


        """
        loading absorption xsections
        """
        os.chdir("..")
        path = 'libraries'
        os.chdir(path) 
        absorption_xsections_arr= absorption_xsections_exp(filename,ngroups,nmoddens,nfueltemp,nborconc)
        os.chdir("..")
        path = 'feedbackcoupler'
        os.chdir(path)         
        """
        interpolating absorption xsections
        """ 
        
        absorption_xsections_interp_material[m] = absorption_xsections_interp(filename2, moddensities_arr, fueltemperatures_arr, boronconcentrations_arr, cool_dens_arr3d, fuel_temp_arr3d, bor_conc_arr3d, absorption_xsections_arr, ngroups,nrows,ncols,nlayers)

        #print(absorption_xsections_interp_material.shape)
        
        
        """
        loading nu_fission xsections
        """
        os.chdir("..")
        path = 'libraries'
        os.chdir(path) 
        nu_fission_xsections_arr= nu_fission_xsections_exp(filename,ngroups,nmoddens,nfueltemp,nborconc)
        os.chdir("..")
        path = 'feedbackcoupler'
        os.chdir(path)         
        """
        interpolating nu_fission xsections
        """   
        nu_fission_xsections_interp_material[m] =nu_fission_xsections_interp(filename2, moddensities_arr, fueltemperatures_arr, boronconcentrations_arr, cool_dens_arr3d, fuel_temp_arr3d, bor_conc_arr3d, nu_fission_xsections_arr, ngroups,nrows,ncols,nlayers)

        #print(nu_fission_xsections_interp_material.shape)

       
        """
        loading kappa_fission xsections
        """
        #os.chdir("..")
        #path = 'libraries'
        #os.chdir(path) 
        #kappa_fission_xsections_arr= kappa_fission_xsections_exp(filename,ngroups,nmoddens,nfueltemp,nborconc)
        #os.chdir("..")
        #path = 'feedbackcoupler'
        #os.chdir(path)   
        """
        interpolating kappa_fission xsections
        """
        #kappa_fission_xsections_interp_material[m] = kappa_fission_xsections_interp(filename2, moddensities_arr, fueltemperatures_arr, boronconcentrations_arr, cool_dens_arr3d, fuel_temp_arr3d, bor_conc_arr3d,  kappa_fission_xsections_arr, ngroups,nrows,ncols,nlayers)

        #print(kappa_fission_xsections_interp_material.shape)
        

        """
        loading p0_scattering xsections
        """
        os.chdir("..")
        path = 'libraries'
        os.chdir(path) 
        p0_scattering_xsections_arr= p0_scattering_xsections_exp(filename,ngroups,nmoddens,nfueltemp,nborconc)
        os.chdir("..")
        path = 'feedbackcoupler'
        os.chdir(path)  
        """
        interpolating p0_scattering xsections
        """   
        p0_scattering_xsections_interp_material[m] = p0_scattering_xsections_interp(filename2, moddensities_arr, fueltemperatures_arr, boronconcentrations_arr, cool_dens_arr3d, fuel_temp_arr3d, bor_conc_arr3d, p0_scattering_xsections_arr, ngroups,nrows,ncols,nlayers)

        #print(p0_scattering_xsections_interp_material.shape)


        """
        loading adf_tables xsections
        """
        #os.chdir("..")
        #path = 'libraries'
        #os.chdir(path) 
        #adf_tables_arr= adf_tables_exp(filename,ngroups,nmoddens,nfueltemp,nborconc)
        #os.chdir("..")
        #path = 'feedbackcoupler'
        #os.chdir(path) 
        """
        interpolating adf_tables xsections
        """   
        #adf_tables_interp_material[m] = adf_tables_interp(filename2, moddensities_arr, fueltemperatures_arr, boronconcentrations_arr, cool_dens_arr3d, fuel_temp_arr3d, bor_conc_arr3d, adf_tables_arr, ngroups,nrows,ncols,nlayers)

        #print(adf_tables_interp_material.shape)


        """
        loading fission_spectrum
        """
        os.chdir("..")
        path = 'libraries'
        os.chdir(path)
        fission_spectrum_arr= fission_spectrum_exp(filename,ngroups)
        os.chdir("..")
        path = 'feedbackcoupler'
        os.chdir(path) 
        
        fission_spectrum_material[m]=fission_spectrum_arr

        #print(fission_spectrum_material.shape)

    """
    converting from nu_fission xsections to fission cross sections
    """
    fission_xsections_interp_material = fission_xsections_conv(nu_fission_xsections_interp_material,nmaterials,ngroups,nrows,ncols,nlayers)
 
    #print(fission_xsections_interp_material.shape)
    """
    converting from absorption xsections and scattering xsections to total cross sections
    """  
    sum_scattering_xsections_interp_material =np.zeros((nmaterials,ngroups,nrows,ncols,nlayers))    
    for n in range(0,ngroups):
        for l in range (0,ngroups):
            sum_scattering_xsections_interp_material[:,n,:,:,:]=sum_scattering_xsections_interp_material[:,n,:,:,:]+p0_scattering_xsections_interp_material[:,n*ngroups+l,:,:,:]   
        total_xsections_interp_material[:,n,:,:,:]   =absorption_xsections_interp_material[:,n,:,:,:]+sum_scattering_xsections_interp_material[:,n,:,:,:]
    """
    correcting scattering xsections 
    """     
    correction_scattering_xsections_interp_material =total_xsections_interp_material-transport_xsections_interp_material
    corrected_scattering_xsections_interp_material =np.zeros((nmaterials,ngroups*ngroups,nrows,ncols,nlayers)) 
    for m in range(0,nmaterials):
        if m==1 and burnable_absorbers:
            for n in range(0,ngroups):
                transport_xsections_interp_material[m,n,:,:,:]=total_xsections_interp_material[m,n,:,:,:]
        else:
            for n in range(0,ngroups):
                transport_xsections_interp_material[m,n,:,:,:]=transport_xsections_interp_material[m,n,:,:,:] 
                        
    for m in range(0,nmaterials):
        if m==1 and burnable_absorbers:
            for n in range(0,ngroups):
                for l in range (0,ngroups):
                    corrected_scattering_xsections_interp_material[m,n*ngroups+l,:,:,:]=p0_scattering_xsections_interp_material[m,n*ngroups+l,:,:,:]
        else:
            for n in range(0,ngroups):
                for l in range (0,ngroups):
                    if l==n:
                        corrected_scattering_xsections_interp_material[:,n*ngroups+l,:,:,:]=p0_scattering_xsections_interp_material[:,n*ngroups+l,:,:,:]-correction_scattering_xsections_interp_material[:,n,:,:,:]
                    else:
                        corrected_scattering_xsections_interp_material[:,n*ngroups+l,:,:,:]=p0_scattering_xsections_interp_material[:,n*ngroups+l,:,:,:]
    """
    saving in h5 format
    """  
    hdf5_mat_converter(iteration,materials_list,fission_spectrum_material, fission_xsections_interp_material, nu_fission_xsections_interp_material, corrected_scattering_xsections_interp_material, transport_xsections_interp_material, nmaterials, ngroups, nrows, ncols, nlayers)
            
    return




