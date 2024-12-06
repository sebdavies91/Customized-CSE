import pandas as pd
import numpy as np
import math as mt
np.set_printoptions(threshold=np.inf)
def absorption_xsections_exp(filename: str,ngroups,nmoddens,nfueltemp,nborconc):
    """
1 burnup state, n groups
    """ 
    """
    Absorption xsections
    """
    xsections = open(filename, "r")
    is_xsections_part = False
    reading_data = False
    absorption_xsections= [[] for i in range(ngroups)] 
    i=1
    for line in xsections.readlines():
        if "Absorption" in line:
            is_xsections_part = True
            continue
        elif "Nu-Fission" in line:
            is_xsections_part = False
            continue
        if is_xsections_part:
            if "GROUP       "+str(i) in line:
                reading_data = True
                continue
            elif "GROUP      "+str(i) in line:
                reading_data = True
                continue
            if reading_data:
                if len(line.split()) == 0:
                    continue         
                elif "GROUP       "+str(i+1) in line:
                    i=i+1
                    continue
                elif "GROUP      "+str(i+1) in line:
                    i=i+1
                    continue  
                elif "*" in line:
                    reading_data = False            
                else:
                    vals = line.split()
                absorption_xsections[i-1].append(vals)
    xsections.close()
    """
    Convert list of lists into numpy arrays
    """ 
    for i in range(ngroups):
        absorption_xsections[i]=pd.DataFrame(data=absorption_xsections[i])
        absorption_xsections[i]= absorption_xsections[i].to_numpy(dtype=float)


    absorption_xsections_arr=np.zeros((ngroups,nmoddens,nfueltemp,nborconc))
    for n in range(ngroups):
        absorption_xsections_group=absorption_xsections[n]
        for i in range(0,nmoddens):
            for j in range(0,nfueltemp):
                for k in range(0,nborconc):
                    absorption_xsections_arr[n,i,j,k]=absorption_xsections_group[nborconc*j+k,i]
        
    
    return absorption_xsections_arr

    

