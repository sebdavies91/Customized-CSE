import pandas as pd
import numpy as np
import math as mt
np.set_printoptions(threshold=np.inf)
def transport_xsections_exp(filename: str,ngroups,nmoddens,nfueltemp,nborconc):
    """
1 burnup state, n groups
    """ 
    """
    Transport xsections
    """
    xsections = open(filename, "r")
    is_xsections_part = False
    reading_data = False
    transport_xsections= [[] for i in range(ngroups)] 
    i=1
    for line in xsections.readlines():
        if "Transport" in line:
            is_xsections_part = True
            continue
        elif "Absorption" in line:
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
                transport_xsections[i-1].append(vals)
    xsections.close()
    """
    Convert list of lists into numpy arrays
    """ 
    for i in range(ngroups):
        transport_xsections[i]=pd.DataFrame(data=transport_xsections[i])
        transport_xsections[i]= transport_xsections[i].to_numpy(dtype=float)


    transport_xsections_arr=np.zeros((ngroups,nmoddens,nfueltemp,nborconc))
    for n in range(ngroups):
        transport_xsections_group=transport_xsections[n]
        for i in range(0,nmoddens):
            for j in range(0,nfueltemp):
                for k in range(0,nborconc):
                    transport_xsections_arr[n,i,j,k]=transport_xsections_group[nborconc*j+k,i]
          
    
    return transport_xsections_arr

    

