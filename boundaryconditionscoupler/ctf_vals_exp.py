import pandas as pd
import numpy as np
import math as mt
import os
np.set_printoptions(threshold=np.inf)
def ctf_vals_exp(filename: str):
    """
    Reads DYN3D lines and stores the powers
    :param filename: DYN3D file containig data from channels
    :return: numpy array with the read powers
    """
    os.chdir("..")
    path = 'outputs/CTF_assemblycelllevel_iteration0'
    os.chdir(path)
    assemblyvalues = open(filename, "r")
    os.chdir("..")
    os.chdir("..")
    path = 'boundaryconditionscoupler'
    os.chdir(path)
    is_values_part = False
    reading_data = False
    values_arr = []
    for line in assemblyvalues.readlines():
        if "*FIRST_VALUES_COUPLING_END" in line:
            reading_data = False
            continue
        elif "*FIRST_VALUES_COUPLING_START" in line:
            reading_data = True
            continue
        if "*SECOND_VALUES_COUPLING_END" in line:
            reading_data = False
            continue
        elif "*SECOND_VALUES_COUPLING_START" in line:
            reading_data = True
            continue
        if "*THIRD_VALUES_COUPLING_END" in line:
            reading_data = False
            continue
        elif "*THIRD_VALUES_COUPLING_START" in line:
            reading_data = True
            continue
        if "*FOURTH_VALUES_COUPLING_END" in line:
            reading_data = False
            continue
        elif "*FOURTH_VALUES_COUPLING_START" in line:
            reading_data = True
            continue
        if reading_data:
            if len(line.split()) == 0:
                continue
            else:
                vals = line.split()
            values_arr.append(vals)
    assemblyvalues.close()

    os.chdir("..")
    path = 'outputs/CTF_assemblycelllevel_iteration0'
    os.chdir(path)
    assemblyvalues = open(filename, "r")
    os.chdir("..")
    os.chdir("..")
    path = 'boundaryconditionscoupler'
    os.chdir(path)
    is_values_part = False
    reading_data = False
    values_arr_2 = []
    for line in assemblyvalues.readlines():
        if "*FIFTH_VALUES_COUPLING_END" in line:
            reading_data = False
            continue
        elif "*FIFTH_VALUES_COUPLING_START" in line:
            reading_data = True
            continue
        if "*SIXTH_VALUES_COUPLING_END" in line:
            reading_data = False
            continue
        elif "*SIXTH_VALUES_COUPLING_START" in line:
            reading_data = True
            continue
        if reading_data:
            if len(line.split()) == 0:
                continue
            else:
                vals = line.split()
            values_arr_2.append(vals)
    assemblyvalues.close()
    return values_arr,values_arr_2