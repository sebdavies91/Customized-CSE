import pandas as pd
import numpy as np
import math as mt
np.set_printoptions(threshold=np.inf)
def adf_tables_exp(filename: str,ngroups,nmoddens,nfueltemp,nborconc):
    """
1 burnup state, n groups
    """ 
    """
    adf tables
    """
    tables = open(filename, "r")
    is_tables_part = False
    reading_data = False
    adf_tables= [[] for i in range(ngroups)] 
    i=1
    for line in tables.readlines():
        if "ADF Table" in line:
            is_tables_part = True
            continue
        elif "Fission spectrum" in line:
            is_tables_part = False
            continue
        if is_tables_part:
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
                adf_tables[i-1].append(vals)
    tables.close()
    """
    Convert list of lists into numpy arrays
    """ 
    for i in range(ngroups):
        adf_tables[i]=pd.DataFrame(data=adf_tables[i])
        adf_tables[i]= adf_tables[i].to_numpy(dtype=float)


    adf_tables_arr=np.zeros((ngroups,nmoddens,nfueltemp,nborconc))
    for n in range(ngroups):
        adf_tables_group=adf_tables[n]
        for i in range(0,nmoddens):
            for j in range(0,nfueltemp):
                for k in range(0,nborconc):
                    adf_tables_arr[n,i,j,k]=adf_tables_group[nborconc*j+k,i]
          
    
    return adf_tables_arr

    

