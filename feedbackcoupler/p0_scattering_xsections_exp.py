import pandas as pd
import numpy as np
import math as mt
np.set_printoptions(threshold=np.inf)
def p0_scattering_xsections_exp(filename: str,ngroups,nmoddens,nfueltemp,nborconc):
    """
1 burnup state, n groups
    """ 
    """
    p0_scattering xsections
    """
    xsections = open(filename, "r")
    is_xsections_part = False
    reading_data = False
    p0_scattering_xsections= [[] for i in range(ngroups*ngroups)] 
    i=1
    j=1
    for line in xsections.readlines():
        if "P0 Scattering" in line:
            is_xsections_part = True
            continue
        elif "ADF Table" in line:
            is_xsections_part = False
            continue
        if is_xsections_part:
            if "GROUP       "+str(i)+" ->           "+str(j) in line:
                reading_data = True
                continue
            elif "GROUP       "+str(i)+" ->          "+str(j) in line:
                reading_data = True
                continue
            elif "GROUP      "+str(i)+" ->           "+str(j) in line:
                reading_data = True
                continue
            elif "GROUP      "+str(i)+" ->          "+str(j) in line:
                reading_data = True
                continue
            if reading_data:
                if len(line.split()) == 0:
                    continue                            
                elif "GROUP       "+str(i)+" ->           "+str(j+1) in line:
                    j=j+1
                    continue
                elif "GROUP       "+str(i)+" ->          "+str(j+1) in line:
                    j=j+1
                    continue
                elif "GROUP      "+str(i)+" ->           "+str(j+1) in line:
                    j=j+1
                    continue
                elif "GROUP      "+str(i)+" ->          "+str(j+1) in line:
                    j=j+1
                    continue                    
                    
     
                elif "GROUP       "+str(i+1)+" ->           "+str(1) in line:
                    j=1
                    i=i+1
                    continue 
                elif "GROUP      "+str(i+1)+" ->           "+str(1) in line:
                    j=1
                    i=i+1
                    continue 
                elif "*" in line:
                    reading_data = False            
                else:
                    vals = line.split()
                p0_scattering_xsections[ngroups*(i-1)+j-1].append(vals)
    xsections.close()
    """
    Convert list of lists into numpy arrays
    """ 
    for i in range(ngroups*ngroups):
        p0_scattering_xsections[i]=pd.DataFrame(data=p0_scattering_xsections[i])
        p0_scattering_xsections[i]= p0_scattering_xsections[i].to_numpy(dtype=float)


    p0_scattering_xsections_arr=np.zeros((ngroups*ngroups,nmoddens,nfueltemp,nborconc))
    for n in range(ngroups*ngroups):
        p0_scattering_xsections_group=p0_scattering_xsections[n]
        for i in range(0,nmoddens):
            for j in range(0,nfueltemp):
                for k in range(0,nborconc):
                    p0_scattering_xsections_arr[n,i,j,k]=p0_scattering_xsections_group[nborconc*j+k,i]
        
    
    return p0_scattering_xsections_arr

    

