import pandas as pd
import numpy as np
import math as mt
np.set_printoptions(threshold=np.inf)
def fission_spectrum_exp(filename: str,ngroups):
    xsections = open(filename, "r")
    is_xsections_part = False
    reading_data = False
    fission_spectrum = []
    for line in xsections.readlines():
        if "Fission spectrum" in line:
            is_xsections_part = True
            continue
        elif "Inverse velocities" in line:
            is_xsections_part = False
            continue
        if is_xsections_part:
            if "GROUP       1" in line:
                reading_data = True
                continue
            if reading_data:
                if len(line.split()) == 0:
                    continue         
                elif "*" in line:
                    reading_data = False
                    continue
                else:
                    vals = line.split()
                fission_spectrum.append(vals)
    xsections.close()
    fission_spectrum=pd.DataFrame(data=fission_spectrum)
    fission_spectrum_arr= fission_spectrum.to_numpy(dtype=float)


    return fission_spectrum_arr



