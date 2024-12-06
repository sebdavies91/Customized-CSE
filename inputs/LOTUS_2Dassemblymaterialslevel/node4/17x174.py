import numpy as np
import pylotus as lotus
from pylotus import logger
from pylotus import plotter

plot = True
logger.setLevel("WARNING")
spat_modes = [1,1,1,1]
spat_modes_2 = [1,1,1]


materials = lotus.load_from_hdf5(filename="materials4.h5", directory=".")

for mat in materials:
    print(mat)

rad_fuel = lotus.Circle(x0=0., y0=0., r=0.4095)
rad_gap = lotus.Circle(x0=0., y0=0., r=0.4180)
rad_clad = lotus.Circle(x0=0., y0=0., r=0.4750)

rad_guide1 = lotus.Circle(x0=0., y0=0., r=0.5715)
rad_guide2 = lotus.Circle(x0=0., y0=0., r=0.6120)


Ce1 = lotus.SquareCell(pitch=1.26, name="Cell 1")
Ce1.circles = [rad_fuel, rad_gap, rad_clad]
Ce1.materials = [materials['UO2_1'], materials['Gap_1'], materials['Clad_1'], materials['Water_1']]
Ce1.spatial_modes = spat_modes
Ce1.d_u = 0.05
Ce1.n_phi_u = 50


Ce2 = lotus.SquareCell(pitch=1.26, name="Cell 2")
Ce2.circles = [rad_fuel, rad_gap, rad_clad]
Ce2.materials = [materials['UO2_2'], materials['Gap_2'], materials['Clad_2'], materials['Water_2']]
Ce2.spatial_modes = spat_modes
Ce2.d_u = 0.05
Ce2.n_phi_u = 50


Ce3 = lotus.SquareCell(pitch=1.26, name="Cell 3")
Ce3.circles = [rad_fuel, rad_gap, rad_clad]
Ce3.materials = [materials['UO2_3'], materials['Gap_3'], materials['Clad_3'], materials['Water_3']]
Ce3.spatial_modes = spat_modes
Ce3.d_u = 0.05
Ce3.n_phi_u = 50


Ce4 = lotus.SquareCell(pitch=1.26, name="Cell 4")
Ce4.circles = [rad_fuel, rad_gap, rad_clad]
Ce4.materials = [materials['UO2_4'], materials['Gap_4'], materials['Clad_4'], materials['Water_4']]
Ce4.spatial_modes = spat_modes
Ce4.d_u = 0.05
Ce4.n_phi_u = 50


Ce5 = lotus.SquareCell(pitch=1.26, name="Cell 5")
Ce5.circles = [rad_fuel, rad_gap, rad_clad]
Ce5.materials = [materials['UO2_5'], materials['Gap_5'], materials['Clad_5'], materials['Water_5']]
Ce5.spatial_modes = spat_modes
Ce5.d_u = 0.05
Ce5.n_phi_u = 50


Ce6 = lotus.SquareCell(pitch=1.26, name="Cell 6")
Ce6.circles = [rad_fuel, rad_gap, rad_clad]
Ce6.materials = [materials['UO2_6'], materials['Gap_6'], materials['Clad_6'], materials['Water_6']]
Ce6.spatial_modes = spat_modes
Ce6.d_u = 0.05
Ce6.n_phi_u = 50


Ce7 = lotus.SquareCell(pitch=1.26, name="Cell 7")
Ce7.circles = [rad_fuel, rad_gap, rad_clad]
Ce7.materials = [materials['UO2_7'], materials['Gap_7'], materials['Clad_7'], materials['Water_7']]
Ce7.spatial_modes = spat_modes
Ce7.d_u = 0.05
Ce7.n_phi_u = 50


Ce8 = lotus.SquareCell(pitch=1.26, name="Cell 8")
Ce8.circles = [rad_fuel, rad_gap, rad_clad]
Ce8.materials = [materials['UO2_8'], materials['Gap_8'], materials['Clad_8'], materials['Water_8']]
Ce8.spatial_modes = spat_modes
Ce8.d_u = 0.05
Ce8.n_phi_u = 50


Ce9 = lotus.SquareCell(pitch=1.26, name="Cell 9")
Ce9.circles = [rad_fuel, rad_gap, rad_clad]
Ce9.materials = [materials['UO2_9'], materials['Gap_9'], materials['Clad_9'], materials['Water_9']]
Ce9.spatial_modes = spat_modes
Ce9.d_u = 0.05
Ce9.n_phi_u = 50


Ce10 = lotus.SquareCell(pitch=1.26, name="Cell 10")
Ce10.circles = [rad_fuel, rad_gap, rad_clad]
Ce10.materials = [materials['UO2_10'], materials['Gap_10'], materials['Clad_10'], materials['Water_10']]
Ce10.spatial_modes = spat_modes
Ce10.d_u = 0.05
Ce10.n_phi_u = 50


Ce11 = lotus.SquareCell(pitch=1.26, name="Cell 11")
Ce11.circles = [rad_fuel, rad_gap, rad_clad]
Ce11.materials = [materials['UO2_11'], materials['Gap_11'], materials['Clad_11'], materials['Water_11']]
Ce11.spatial_modes = spat_modes
Ce11.d_u = 0.05
Ce11.n_phi_u = 50


Ce12 = lotus.SquareCell(pitch=1.26, name="Cell 12")
Ce12.circles = [rad_fuel, rad_gap, rad_clad]
Ce12.materials = [materials['UO2_12'], materials['Gap_12'], materials['Clad_12'], materials['Water_12']]
Ce12.spatial_modes = spat_modes
Ce12.d_u = 0.05
Ce12.n_phi_u = 50


Ce13 = lotus.SquareCell(pitch=1.26, name="Cell 13")
Ce13.circles = [rad_fuel, rad_gap, rad_clad]
Ce13.materials = [materials['UO2_13'], materials['Gap_13'], materials['Clad_13'], materials['Water_13']]
Ce13.spatial_modes = spat_modes
Ce13.d_u = 0.05
Ce13.n_phi_u = 50


Ce14 = lotus.SquareCell(pitch=1.26, name="Cell 14")
Ce14.circles = [rad_fuel, rad_gap, rad_clad]
Ce14.materials = [materials['UO2_14'], materials['Gap_14'], materials['Clad_14'], materials['Water_14']]
Ce14.spatial_modes = spat_modes
Ce14.d_u = 0.05
Ce14.n_phi_u = 50


Ce15 = lotus.SquareCell(pitch=1.26, name="Cell 15")
Ce15.circles = [rad_fuel, rad_gap, rad_clad]
Ce15.materials = [materials['UO2_15'], materials['Gap_15'], materials['Clad_15'], materials['Water_15']]
Ce15.spatial_modes = spat_modes
Ce15.d_u = 0.05
Ce15.n_phi_u = 50


Ce16 = lotus.SquareCell(pitch=1.26, name="Cell 16")
Ce16.circles = [rad_fuel, rad_gap, rad_clad]
Ce16.materials = [materials['UO2_16'], materials['Gap_16'], materials['Clad_16'], materials['Water_16']]
Ce16.spatial_modes = spat_modes
Ce16.d_u = 0.05
Ce16.n_phi_u = 50


Ce17 = lotus.SquareCell(pitch=1.26, name="Cell 17")
Ce17.circles = [rad_fuel, rad_gap, rad_clad]
Ce17.materials = [materials['UO2_17'], materials['Gap_17'], materials['Clad_17'], materials['Water_17']]
Ce17.spatial_modes = spat_modes
Ce17.d_u = 0.05
Ce17.n_phi_u = 50


Ce18 = lotus.SquareCell(pitch=1.26, name="Cell 18")
Ce18.circles = [rad_fuel, rad_gap, rad_clad]
Ce18.materials = [materials['UO2_18'], materials['Gap_18'], materials['Clad_18'], materials['Water_18']]
Ce18.spatial_modes = spat_modes
Ce18.d_u = 0.05
Ce18.n_phi_u = 50


Ce19 = lotus.SquareCell(pitch=1.26, name="Cell 19")
Ce19.circles = [rad_fuel, rad_gap, rad_clad]
Ce19.materials = [materials['UO2_19'], materials['Gap_19'], materials['Clad_19'], materials['Water_19']]
Ce19.spatial_modes = spat_modes
Ce19.d_u = 0.05
Ce19.n_phi_u = 50


Ce20 = lotus.SquareCell(pitch=1.26, name="Cell 20")
Ce20.circles = [rad_fuel, rad_gap, rad_clad]
Ce20.materials = [materials['UO2_20'], materials['Gap_20'], materials['Clad_20'], materials['Water_20']]
Ce20.spatial_modes = spat_modes
Ce20.d_u = 0.05
Ce20.n_phi_u = 50


Ce21 = lotus.SquareCell(pitch=1.26, name="Cell 21")
Ce21.circles = [rad_fuel, rad_gap, rad_clad]
Ce21.materials = [materials['UO2_21'], materials['Gap_21'], materials['Clad_21'], materials['Water_21']]
Ce21.spatial_modes = spat_modes
Ce21.d_u = 0.05
Ce21.n_phi_u = 50


Ce22 = lotus.SquareCell(pitch=1.26, name="Cell 22")
Ce22.circles = [rad_fuel, rad_gap, rad_clad]
Ce22.materials = [materials['UO2_22'], materials['Gap_22'], materials['Clad_22'], materials['Water_22']]
Ce22.spatial_modes = spat_modes
Ce22.d_u = 0.05
Ce22.n_phi_u = 50


Ce23 = lotus.SquareCell(pitch=1.26, name="Cell 23")
Ce23.circles = [rad_fuel, rad_gap, rad_clad]
Ce23.materials = [materials['UO2_23'], materials['Gap_23'], materials['Clad_23'], materials['Water_23']]
Ce23.spatial_modes = spat_modes
Ce23.d_u = 0.05
Ce23.n_phi_u = 50


Ce24 = lotus.SquareCell(pitch=1.26, name="Cell 24")
Ce24.circles = [rad_fuel, rad_gap, rad_clad]
Ce24.materials = [materials['UO2_24'], materials['Gap_24'], materials['Clad_24'], materials['Water_24']]
Ce24.spatial_modes = spat_modes
Ce24.d_u = 0.05
Ce24.n_phi_u = 50


Ce25 = lotus.SquareCell(pitch=1.26, name="Cell 25")
Ce25.circles = [rad_fuel, rad_gap, rad_clad]
Ce25.materials = [materials['UO2_25'], materials['Gap_25'], materials['Clad_25'], materials['Water_25']]
Ce25.spatial_modes = spat_modes
Ce25.d_u = 0.05
Ce25.n_phi_u = 50


Ce26 = lotus.SquareCell(pitch=1.26, name="Cell 26")
Ce26.circles = [rad_fuel, rad_gap, rad_clad]
Ce26.materials = [materials['UO2_26'], materials['Gap_26'], materials['Clad_26'], materials['Water_26']]
Ce26.spatial_modes = spat_modes
Ce26.d_u = 0.05
Ce26.n_phi_u = 50


Ce27 = lotus.SquareCell(pitch=1.26, name="Cell 27")
Ce27.circles = [rad_fuel, rad_gap, rad_clad]
Ce27.materials = [materials['UO2_27'], materials['Gap_27'], materials['Clad_27'], materials['Water_27']]
Ce27.spatial_modes = spat_modes
Ce27.d_u = 0.05
Ce27.n_phi_u = 50


Ce28 = lotus.SquareCell(pitch=1.26, name="Cell 28")
Ce28.circles = [rad_fuel, rad_gap, rad_clad]
Ce28.materials = [materials['UO2_28'], materials['Gap_28'], materials['Clad_28'], materials['Water_28']]
Ce28.spatial_modes = spat_modes
Ce28.d_u = 0.05
Ce28.n_phi_u = 50


Ce29 = lotus.SquareCell(pitch=1.26, name="Cell 29")
Ce29.circles = [rad_fuel, rad_gap, rad_clad]
Ce29.materials = [materials['UO2_29'], materials['Gap_29'], materials['Clad_29'], materials['Water_29']]
Ce29.spatial_modes = spat_modes
Ce29.d_u = 0.05
Ce29.n_phi_u = 50


Ce30 = lotus.SquareCell(pitch=1.26, name="Cell 30")
Ce30.circles = [rad_fuel, rad_gap, rad_clad]
Ce30.materials = [materials['UO2_30'], materials['Gap_30'], materials['Clad_30'], materials['Water_30']]
Ce30.spatial_modes = spat_modes
Ce30.d_u = 0.05
Ce30.n_phi_u = 50


Ce31 = lotus.SquareCell(pitch=1.26, name="Cell 31")
Ce31.circles = [rad_fuel, rad_gap, rad_clad]
Ce31.materials = [materials['UO2_31'], materials['Gap_31'], materials['Clad_31'], materials['Water_31']]
Ce31.spatial_modes = spat_modes
Ce31.d_u = 0.05
Ce31.n_phi_u = 50


Ce32 = lotus.SquareCell(pitch=1.26, name="Cell 32")
Ce32.circles = [rad_fuel, rad_gap, rad_clad]
Ce32.materials = [materials['UO2_32'], materials['Gap_32'], materials['Clad_32'], materials['Water_32']]
Ce32.spatial_modes = spat_modes
Ce32.d_u = 0.05
Ce32.n_phi_u = 50


Ce33 = lotus.SquareCell(pitch=1.26, name="Cell 33")
Ce33.circles = [rad_fuel, rad_gap, rad_clad]
Ce33.materials = [materials['UO2_33'], materials['Gap_33'], materials['Clad_33'], materials['Water_33']]
Ce33.spatial_modes = spat_modes
Ce33.d_u = 0.05
Ce33.n_phi_u = 50


Ce34 = lotus.SquareCell(pitch=1.26, name="Cell 34")
Ce34.circles = [rad_fuel, rad_gap, rad_clad]
Ce34.materials = [materials['UO2_34'], materials['Gap_34'], materials['Clad_34'], materials['Water_34']]
Ce34.spatial_modes = spat_modes
Ce34.d_u = 0.05
Ce34.n_phi_u = 50


Ce35 = lotus.SquareCell(pitch=1.26, name="Cell 35")
Ce35.circles = [rad_fuel, rad_gap, rad_clad]
Ce35.materials = [materials['UO2_35'], materials['Gap_35'], materials['Clad_35'], materials['Water_35']]
Ce35.spatial_modes = spat_modes
Ce35.d_u = 0.05
Ce35.n_phi_u = 50


Ce36 = lotus.SquareCell(pitch=1.26, name="Cell 36")
Ce36.circles = [rad_fuel, rad_gap, rad_clad]
Ce36.materials = [materials['UO2_36'], materials['Gap_36'], materials['Clad_36'], materials['Water_36']]
Ce36.spatial_modes = spat_modes
Ce36.d_u = 0.05
Ce36.n_phi_u = 50


Ce37 = lotus.SquareCell(pitch=1.26, name="Cell 37")
Ce37.circles = [rad_fuel, rad_gap, rad_clad]
Ce37.materials = [materials['UO2_37'], materials['Gap_37'], materials['Clad_37'], materials['Water_37']]
Ce37.spatial_modes = spat_modes
Ce37.d_u = 0.05
Ce37.n_phi_u = 50


Ce38 = lotus.SquareCell(pitch=1.26, name="Cell 38")
Ce38.circles = [rad_fuel, rad_gap, rad_clad]
Ce38.materials = [materials['UO2_38'], materials['Gap_38'], materials['Clad_38'], materials['Water_38']]
Ce38.spatial_modes = spat_modes
Ce38.d_u = 0.05
Ce38.n_phi_u = 50


Ce39 = lotus.SquareCell(pitch=1.26, name="Cell 39")
Ce39.circles = [rad_fuel, rad_gap, rad_clad]
Ce39.materials = [materials['UO2_39'], materials['Gap_39'], materials['Clad_39'], materials['Water_39']]
Ce39.spatial_modes = spat_modes
Ce39.d_u = 0.05
Ce39.n_phi_u = 50


Ce40 = lotus.SquareCell(pitch=1.26, name="Cell 40")
Ce40.circles = [rad_guide1, rad_guide2]
Ce40.materials = [materials['Water_40'], materials['Clad_40'], materials['Water_40']]
Ce40.spatial_modes = spat_modes_2
Ce40.d_u = 0.05
Ce40.n_phi_u = 50


Ce41 = lotus.SquareCell(pitch=1.26, name="Cell 41")
Ce41.circles = [rad_fuel, rad_gap, rad_clad]
Ce41.materials = [materials['UO2_41'], materials['Gap_41'], materials['Clad_41'], materials['Water_41']]
Ce41.spatial_modes = spat_modes
Ce41.d_u = 0.05
Ce41.n_phi_u = 50


Ce42 = lotus.SquareCell(pitch=1.26, name="Cell 42")
Ce42.circles = [rad_fuel, rad_gap, rad_clad]
Ce42.materials = [materials['UO2_42'], materials['Gap_42'], materials['Clad_42'], materials['Water_42']]
Ce42.spatial_modes = spat_modes
Ce42.d_u = 0.05
Ce42.n_phi_u = 50


Ce43 = lotus.SquareCell(pitch=1.26, name="Cell 43")
Ce43.circles = [rad_guide1, rad_guide2]
Ce43.materials = [materials['Water_43'], materials['Clad_43'], materials['Water_43']]
Ce43.spatial_modes = spat_modes_2
Ce43.d_u = 0.05
Ce43.n_phi_u = 50


Ce44 = lotus.SquareCell(pitch=1.26, name="Cell 44")
Ce44.circles = [rad_fuel, rad_gap, rad_clad]
Ce44.materials = [materials['UO2_44'], materials['Gap_44'], materials['Clad_44'], materials['Water_44']]
Ce44.spatial_modes = spat_modes
Ce44.d_u = 0.05
Ce44.n_phi_u = 50


Ce45 = lotus.SquareCell(pitch=1.26, name="Cell 45")
Ce45.circles = [rad_fuel, rad_gap, rad_clad]
Ce45.materials = [materials['UO2_45'], materials['Gap_45'], materials['Clad_45'], materials['Water_45']]
Ce45.spatial_modes = spat_modes
Ce45.d_u = 0.05
Ce45.n_phi_u = 50


Ce46 = lotus.SquareCell(pitch=1.26, name="Cell 46")
Ce46.circles = [rad_guide1, rad_guide2]
Ce46.materials = [materials['Water_46'], materials['Clad_46'], materials['Water_46']]
Ce46.spatial_modes = spat_modes_2
Ce46.d_u = 0.05
Ce46.n_phi_u = 50


Ce47 = lotus.SquareCell(pitch=1.26, name="Cell 47")
Ce47.circles = [rad_fuel, rad_gap, rad_clad]
Ce47.materials = [materials['UO2_47'], materials['Gap_47'], materials['Clad_47'], materials['Water_47']]
Ce47.spatial_modes = spat_modes
Ce47.d_u = 0.05
Ce47.n_phi_u = 50


Ce48 = lotus.SquareCell(pitch=1.26, name="Cell 48")
Ce48.circles = [rad_fuel, rad_gap, rad_clad]
Ce48.materials = [materials['UO2_48'], materials['Gap_48'], materials['Clad_48'], materials['Water_48']]
Ce48.spatial_modes = spat_modes
Ce48.d_u = 0.05
Ce48.n_phi_u = 50


Ce49 = lotus.SquareCell(pitch=1.26, name="Cell 49")
Ce49.circles = [rad_fuel, rad_gap, rad_clad]
Ce49.materials = [materials['UO2_49'], materials['Gap_49'], materials['Clad_49'], materials['Water_49']]
Ce49.spatial_modes = spat_modes
Ce49.d_u = 0.05
Ce49.n_phi_u = 50


Ce50 = lotus.SquareCell(pitch=1.26, name="Cell 50")
Ce50.circles = [rad_fuel, rad_gap, rad_clad]
Ce50.materials = [materials['UO2_50'], materials['Gap_50'], materials['Clad_50'], materials['Water_50']]
Ce50.spatial_modes = spat_modes
Ce50.d_u = 0.05
Ce50.n_phi_u = 50


Ce51 = lotus.SquareCell(pitch=1.26, name="Cell 51")
Ce51.circles = [rad_fuel, rad_gap, rad_clad]
Ce51.materials = [materials['UO2_51'], materials['Gap_51'], materials['Clad_51'], materials['Water_51']]
Ce51.spatial_modes = spat_modes
Ce51.d_u = 0.05
Ce51.n_phi_u = 50


Ce52 = lotus.SquareCell(pitch=1.26, name="Cell 52")
Ce52.circles = [rad_fuel, rad_gap, rad_clad]
Ce52.materials = [materials['UO2_52'], materials['Gap_52'], materials['Clad_52'], materials['Water_52']]
Ce52.spatial_modes = spat_modes
Ce52.d_u = 0.05
Ce52.n_phi_u = 50


Ce53 = lotus.SquareCell(pitch=1.26, name="Cell 53")
Ce53.circles = [rad_fuel, rad_gap, rad_clad]
Ce53.materials = [materials['UO2_53'], materials['Gap_53'], materials['Clad_53'], materials['Water_53']]
Ce53.spatial_modes = spat_modes
Ce53.d_u = 0.05
Ce53.n_phi_u = 50


Ce54 = lotus.SquareCell(pitch=1.26, name="Cell 54")
Ce54.circles = [rad_fuel, rad_gap, rad_clad]
Ce54.materials = [materials['UO2_54'], materials['Gap_54'], materials['Clad_54'], materials['Water_54']]
Ce54.spatial_modes = spat_modes
Ce54.d_u = 0.05
Ce54.n_phi_u = 50


Ce55 = lotus.SquareCell(pitch=1.26, name="Cell 55")
Ce55.circles = [rad_guide1, rad_guide2]
Ce55.materials = [materials['Water_55'], materials['Clad_55'], materials['Water_55']]
Ce55.spatial_modes = spat_modes_2
Ce55.d_u = 0.05
Ce55.n_phi_u = 50


Ce56 = lotus.SquareCell(pitch=1.26, name="Cell 56")
Ce56.circles = [rad_fuel, rad_gap, rad_clad]
Ce56.materials = [materials['UO2_56'], materials['Gap_56'], materials['Clad_56'], materials['Water_56']]
Ce56.spatial_modes = spat_modes
Ce56.d_u = 0.05
Ce56.n_phi_u = 50


Ce57 = lotus.SquareCell(pitch=1.26, name="Cell 57")
Ce57.circles = [rad_fuel, rad_gap, rad_clad]
Ce57.materials = [materials['UO2_57'], materials['Gap_57'], materials['Clad_57'], materials['Water_57']]
Ce57.spatial_modes = spat_modes
Ce57.d_u = 0.05
Ce57.n_phi_u = 50


Ce58 = lotus.SquareCell(pitch=1.26, name="Cell 58")
Ce58.circles = [rad_fuel, rad_gap, rad_clad]
Ce58.materials = [materials['UO2_58'], materials['Gap_58'], materials['Clad_58'], materials['Water_58']]
Ce58.spatial_modes = spat_modes
Ce58.d_u = 0.05
Ce58.n_phi_u = 50


Ce59 = lotus.SquareCell(pitch=1.26, name="Cell 59")
Ce59.circles = [rad_fuel, rad_gap, rad_clad]
Ce59.materials = [materials['UO2_59'], materials['Gap_59'], materials['Clad_59'], materials['Water_59']]
Ce59.spatial_modes = spat_modes
Ce59.d_u = 0.05
Ce59.n_phi_u = 50


Ce60 = lotus.SquareCell(pitch=1.26, name="Cell 60")
Ce60.circles = [rad_fuel, rad_gap, rad_clad]
Ce60.materials = [materials['UO2_60'], materials['Gap_60'], materials['Clad_60'], materials['Water_60']]
Ce60.spatial_modes = spat_modes
Ce60.d_u = 0.05
Ce60.n_phi_u = 50


Ce61 = lotus.SquareCell(pitch=1.26, name="Cell 61")
Ce61.circles = [rad_fuel, rad_gap, rad_clad]
Ce61.materials = [materials['UO2_61'], materials['Gap_61'], materials['Clad_61'], materials['Water_61']]
Ce61.spatial_modes = spat_modes
Ce61.d_u = 0.05
Ce61.n_phi_u = 50


Ce62 = lotus.SquareCell(pitch=1.26, name="Cell 62")
Ce62.circles = [rad_fuel, rad_gap, rad_clad]
Ce62.materials = [materials['UO2_62'], materials['Gap_62'], materials['Clad_62'], materials['Water_62']]
Ce62.spatial_modes = spat_modes
Ce62.d_u = 0.05
Ce62.n_phi_u = 50


Ce63 = lotus.SquareCell(pitch=1.26, name="Cell 63")
Ce63.circles = [rad_fuel, rad_gap, rad_clad]
Ce63.materials = [materials['UO2_63'], materials['Gap_63'], materials['Clad_63'], materials['Water_63']]
Ce63.spatial_modes = spat_modes
Ce63.d_u = 0.05
Ce63.n_phi_u = 50


Ce64 = lotus.SquareCell(pitch=1.26, name="Cell 64")
Ce64.circles = [rad_fuel, rad_gap, rad_clad]
Ce64.materials = [materials['UO2_64'], materials['Gap_64'], materials['Clad_64'], materials['Water_64']]
Ce64.spatial_modes = spat_modes
Ce64.d_u = 0.05
Ce64.n_phi_u = 50


Ce65 = lotus.SquareCell(pitch=1.26, name="Cell 65")
Ce65.circles = [rad_guide1, rad_guide2]
Ce65.materials = [materials['Water_65'], materials['Clad_65'], materials['Water_65']]
Ce65.spatial_modes = spat_modes_2
Ce65.d_u = 0.05
Ce65.n_phi_u = 50


Ce66 = lotus.SquareCell(pitch=1.26, name="Cell 66")
Ce66.circles = [rad_fuel, rad_gap, rad_clad]
Ce66.materials = [materials['UO2_66'], materials['Gap_66'], materials['Clad_66'], materials['Water_66']]
Ce66.spatial_modes = spat_modes
Ce66.d_u = 0.05
Ce66.n_phi_u = 50


Ce67 = lotus.SquareCell(pitch=1.26, name="Cell 67")
Ce67.circles = [rad_fuel, rad_gap, rad_clad]
Ce67.materials = [materials['UO2_67'], materials['Gap_67'], materials['Clad_67'], materials['Water_67']]
Ce67.spatial_modes = spat_modes
Ce67.d_u = 0.05
Ce67.n_phi_u = 50


Ce68 = lotus.SquareCell(pitch=1.26, name="Cell 68")
Ce68.circles = [rad_fuel, rad_gap, rad_clad]
Ce68.materials = [materials['UO2_68'], materials['Gap_68'], materials['Clad_68'], materials['Water_68']]
Ce68.spatial_modes = spat_modes
Ce68.d_u = 0.05
Ce68.n_phi_u = 50


Ce69 = lotus.SquareCell(pitch=1.26, name="Cell 69")
Ce69.circles = [rad_fuel, rad_gap, rad_clad]
Ce69.materials = [materials['UO2_69'], materials['Gap_69'], materials['Clad_69'], materials['Water_69']]
Ce69.spatial_modes = spat_modes
Ce69.d_u = 0.05
Ce69.n_phi_u = 50


Ce70 = lotus.SquareCell(pitch=1.26, name="Cell 70")
Ce70.circles = [rad_fuel, rad_gap, rad_clad]
Ce70.materials = [materials['UO2_70'], materials['Gap_70'], materials['Clad_70'], materials['Water_70']]
Ce70.spatial_modes = spat_modes
Ce70.d_u = 0.05
Ce70.n_phi_u = 50


Ce71 = lotus.SquareCell(pitch=1.26, name="Cell 71")
Ce71.circles = [rad_fuel, rad_gap, rad_clad]
Ce71.materials = [materials['UO2_71'], materials['Gap_71'], materials['Clad_71'], materials['Water_71']]
Ce71.spatial_modes = spat_modes
Ce71.d_u = 0.05
Ce71.n_phi_u = 50


Ce72 = lotus.SquareCell(pitch=1.26, name="Cell 72")
Ce72.circles = [rad_fuel, rad_gap, rad_clad]
Ce72.materials = [materials['UO2_72'], materials['Gap_72'], materials['Clad_72'], materials['Water_72']]
Ce72.spatial_modes = spat_modes
Ce72.d_u = 0.05
Ce72.n_phi_u = 50


Ce73 = lotus.SquareCell(pitch=1.26, name="Cell 73")
Ce73.circles = [rad_fuel, rad_gap, rad_clad]
Ce73.materials = [materials['UO2_73'], materials['Gap_73'], materials['Clad_73'], materials['Water_73']]
Ce73.spatial_modes = spat_modes
Ce73.d_u = 0.05
Ce73.n_phi_u = 50


Ce74 = lotus.SquareCell(pitch=1.26, name="Cell 74")
Ce74.circles = [rad_fuel, rad_gap, rad_clad]
Ce74.materials = [materials['UO2_74'], materials['Gap_74'], materials['Clad_74'], materials['Water_74']]
Ce74.spatial_modes = spat_modes
Ce74.d_u = 0.05
Ce74.n_phi_u = 50


Ce75 = lotus.SquareCell(pitch=1.26, name="Cell 75")
Ce75.circles = [rad_fuel, rad_gap, rad_clad]
Ce75.materials = [materials['UO2_75'], materials['Gap_75'], materials['Clad_75'], materials['Water_75']]
Ce75.spatial_modes = spat_modes
Ce75.d_u = 0.05
Ce75.n_phi_u = 50


Ce76 = lotus.SquareCell(pitch=1.26, name="Cell 76")
Ce76.circles = [rad_fuel, rad_gap, rad_clad]
Ce76.materials = [materials['UO2_76'], materials['Gap_76'], materials['Clad_76'], materials['Water_76']]
Ce76.spatial_modes = spat_modes
Ce76.d_u = 0.05
Ce76.n_phi_u = 50


Ce77 = lotus.SquareCell(pitch=1.26, name="Cell 77")
Ce77.circles = [rad_fuel, rad_gap, rad_clad]
Ce77.materials = [materials['UO2_77'], materials['Gap_77'], materials['Clad_77'], materials['Water_77']]
Ce77.spatial_modes = spat_modes
Ce77.d_u = 0.05
Ce77.n_phi_u = 50


Ce78 = lotus.SquareCell(pitch=1.26, name="Cell 78")
Ce78.circles = [rad_fuel, rad_gap, rad_clad]
Ce78.materials = [materials['UO2_78'], materials['Gap_78'], materials['Clad_78'], materials['Water_78']]
Ce78.spatial_modes = spat_modes
Ce78.d_u = 0.05
Ce78.n_phi_u = 50


Ce79 = lotus.SquareCell(pitch=1.26, name="Cell 79")
Ce79.circles = [rad_fuel, rad_gap, rad_clad]
Ce79.materials = [materials['UO2_79'], materials['Gap_79'], materials['Clad_79'], materials['Water_79']]
Ce79.spatial_modes = spat_modes
Ce79.d_u = 0.05
Ce79.n_phi_u = 50


Ce80 = lotus.SquareCell(pitch=1.26, name="Cell 80")
Ce80.circles = [rad_fuel, rad_gap, rad_clad]
Ce80.materials = [materials['UO2_80'], materials['Gap_80'], materials['Clad_80'], materials['Water_80']]
Ce80.spatial_modes = spat_modes
Ce80.d_u = 0.05
Ce80.n_phi_u = 50


Ce81 = lotus.SquareCell(pitch=1.26, name="Cell 81")
Ce81.circles = [rad_fuel, rad_gap, rad_clad]
Ce81.materials = [materials['UO2_81'], materials['Gap_81'], materials['Clad_81'], materials['Water_81']]
Ce81.spatial_modes = spat_modes
Ce81.d_u = 0.05
Ce81.n_phi_u = 50


Ce82 = lotus.SquareCell(pitch=1.26, name="Cell 82")
Ce82.circles = [rad_fuel, rad_gap, rad_clad]
Ce82.materials = [materials['UO2_82'], materials['Gap_82'], materials['Clad_82'], materials['Water_82']]
Ce82.spatial_modes = spat_modes
Ce82.d_u = 0.05
Ce82.n_phi_u = 50


Ce83 = lotus.SquareCell(pitch=1.26, name="Cell 83")
Ce83.circles = [rad_fuel, rad_gap, rad_clad]
Ce83.materials = [materials['UO2_83'], materials['Gap_83'], materials['Clad_83'], materials['Water_83']]
Ce83.spatial_modes = spat_modes
Ce83.d_u = 0.05
Ce83.n_phi_u = 50


Ce84 = lotus.SquareCell(pitch=1.26, name="Cell 84")
Ce84.circles = [rad_fuel, rad_gap, rad_clad]
Ce84.materials = [materials['UO2_84'], materials['Gap_84'], materials['Clad_84'], materials['Water_84']]
Ce84.spatial_modes = spat_modes
Ce84.d_u = 0.05
Ce84.n_phi_u = 50


Ce85 = lotus.SquareCell(pitch=1.26, name="Cell 85")
Ce85.circles = [rad_fuel, rad_gap, rad_clad]
Ce85.materials = [materials['UO2_85'], materials['Gap_85'], materials['Clad_85'], materials['Water_85']]
Ce85.spatial_modes = spat_modes
Ce85.d_u = 0.05
Ce85.n_phi_u = 50


Ce86 = lotus.SquareCell(pitch=1.26, name="Cell 86")
Ce86.circles = [rad_fuel, rad_gap, rad_clad]
Ce86.materials = [materials['UO2_86'], materials['Gap_86'], materials['Clad_86'], materials['Water_86']]
Ce86.spatial_modes = spat_modes
Ce86.d_u = 0.05
Ce86.n_phi_u = 50


Ce87 = lotus.SquareCell(pitch=1.26, name="Cell 87")
Ce87.circles = [rad_fuel, rad_gap, rad_clad]
Ce87.materials = [materials['UO2_87'], materials['Gap_87'], materials['Clad_87'], materials['Water_87']]
Ce87.spatial_modes = spat_modes
Ce87.d_u = 0.05
Ce87.n_phi_u = 50


Ce88 = lotus.SquareCell(pitch=1.26, name="Cell 88")
Ce88.circles = [rad_guide1, rad_guide2]
Ce88.materials = [materials['Water_88'], materials['Clad_88'], materials['Water_88']]
Ce88.spatial_modes = spat_modes_2
Ce88.d_u = 0.05
Ce88.n_phi_u = 50


Ce89 = lotus.SquareCell(pitch=1.26, name="Cell 89")
Ce89.circles = [rad_fuel, rad_gap, rad_clad]
Ce89.materials = [materials['UO2_89'], materials['Gap_89'], materials['Clad_89'], materials['Water_89']]
Ce89.spatial_modes = spat_modes
Ce89.d_u = 0.05
Ce89.n_phi_u = 50


Ce90 = lotus.SquareCell(pitch=1.26, name="Cell 90")
Ce90.circles = [rad_fuel, rad_gap, rad_clad]
Ce90.materials = [materials['UO2_90'], materials['Gap_90'], materials['Clad_90'], materials['Water_90']]
Ce90.spatial_modes = spat_modes
Ce90.d_u = 0.05
Ce90.n_phi_u = 50


Ce91 = lotus.SquareCell(pitch=1.26, name="Cell 91")
Ce91.circles = [rad_guide1, rad_guide2]
Ce91.materials = [materials['Water_91'], materials['Clad_91'], materials['Water_91']]
Ce91.spatial_modes = spat_modes_2
Ce91.d_u = 0.05
Ce91.n_phi_u = 50


Ce92 = lotus.SquareCell(pitch=1.26, name="Cell 92")
Ce92.circles = [rad_fuel, rad_gap, rad_clad]
Ce92.materials = [materials['UO2_92'], materials['Gap_92'], materials['Clad_92'], materials['Water_92']]
Ce92.spatial_modes = spat_modes
Ce92.d_u = 0.05
Ce92.n_phi_u = 50


Ce93 = lotus.SquareCell(pitch=1.26, name="Cell 93")
Ce93.circles = [rad_fuel, rad_gap, rad_clad]
Ce93.materials = [materials['UO2_93'], materials['Gap_93'], materials['Clad_93'], materials['Water_93']]
Ce93.spatial_modes = spat_modes
Ce93.d_u = 0.05
Ce93.n_phi_u = 50


Ce94 = lotus.SquareCell(pitch=1.26, name="Cell 94")
Ce94.circles = [rad_guide1, rad_guide2]
Ce94.materials = [materials['Water_94'], materials['Clad_94'], materials['Water_94']]
Ce94.spatial_modes = spat_modes_2
Ce94.d_u = 0.05
Ce94.n_phi_u = 50


Ce95 = lotus.SquareCell(pitch=1.26, name="Cell 95")
Ce95.circles = [rad_fuel, rad_gap, rad_clad]
Ce95.materials = [materials['UO2_95'], materials['Gap_95'], materials['Clad_95'], materials['Water_95']]
Ce95.spatial_modes = spat_modes
Ce95.d_u = 0.05
Ce95.n_phi_u = 50


Ce96 = lotus.SquareCell(pitch=1.26, name="Cell 96")
Ce96.circles = [rad_fuel, rad_gap, rad_clad]
Ce96.materials = [materials['UO2_96'], materials['Gap_96'], materials['Clad_96'], materials['Water_96']]
Ce96.spatial_modes = spat_modes
Ce96.d_u = 0.05
Ce96.n_phi_u = 50


Ce97 = lotus.SquareCell(pitch=1.26, name="Cell 97")
Ce97.circles = [rad_guide1, rad_guide2]
Ce97.materials = [materials['Water_97'], materials['Clad_97'], materials['Water_97']]
Ce97.spatial_modes = spat_modes_2
Ce97.d_u = 0.05
Ce97.n_phi_u = 50


Ce98 = lotus.SquareCell(pitch=1.26, name="Cell 98")
Ce98.circles = [rad_fuel, rad_gap, rad_clad]
Ce98.materials = [materials['UO2_98'], materials['Gap_98'], materials['Clad_98'], materials['Water_98']]
Ce98.spatial_modes = spat_modes
Ce98.d_u = 0.05
Ce98.n_phi_u = 50


Ce99 = lotus.SquareCell(pitch=1.26, name="Cell 99")
Ce99.circles = [rad_fuel, rad_gap, rad_clad]
Ce99.materials = [materials['UO2_99'], materials['Gap_99'], materials['Clad_99'], materials['Water_99']]
Ce99.spatial_modes = spat_modes
Ce99.d_u = 0.05
Ce99.n_phi_u = 50


Ce100 = lotus.SquareCell(pitch=1.26, name="Cell 100")
Ce100.circles = [rad_guide1, rad_guide2]
Ce100.materials = [materials['Water_100'], materials['Clad_100'], materials['Water_100']]
Ce100.spatial_modes = spat_modes_2
Ce100.d_u = 0.05
Ce100.n_phi_u = 50


Ce101 = lotus.SquareCell(pitch=1.26, name="Cell 101")
Ce101.circles = [rad_fuel, rad_gap, rad_clad]
Ce101.materials = [materials['UO2_101'], materials['Gap_101'], materials['Clad_101'], materials['Water_101']]
Ce101.spatial_modes = spat_modes
Ce101.d_u = 0.05
Ce101.n_phi_u = 50


Ce102 = lotus.SquareCell(pitch=1.26, name="Cell 102")
Ce102.circles = [rad_fuel, rad_gap, rad_clad]
Ce102.materials = [materials['UO2_102'], materials['Gap_102'], materials['Clad_102'], materials['Water_102']]
Ce102.spatial_modes = spat_modes
Ce102.d_u = 0.05
Ce102.n_phi_u = 50


Ce103 = lotus.SquareCell(pitch=1.26, name="Cell 103")
Ce103.circles = [rad_fuel, rad_gap, rad_clad]
Ce103.materials = [materials['UO2_103'], materials['Gap_103'], materials['Clad_103'], materials['Water_103']]
Ce103.spatial_modes = spat_modes
Ce103.d_u = 0.05
Ce103.n_phi_u = 50


Ce104 = lotus.SquareCell(pitch=1.26, name="Cell 104")
Ce104.circles = [rad_fuel, rad_gap, rad_clad]
Ce104.materials = [materials['UO2_104'], materials['Gap_104'], materials['Clad_104'], materials['Water_104']]
Ce104.spatial_modes = spat_modes
Ce104.d_u = 0.05
Ce104.n_phi_u = 50


Ce105 = lotus.SquareCell(pitch=1.26, name="Cell 105")
Ce105.circles = [rad_fuel, rad_gap, rad_clad]
Ce105.materials = [materials['UO2_105'], materials['Gap_105'], materials['Clad_105'], materials['Water_105']]
Ce105.spatial_modes = spat_modes
Ce105.d_u = 0.05
Ce105.n_phi_u = 50


Ce106 = lotus.SquareCell(pitch=1.26, name="Cell 106")
Ce106.circles = [rad_fuel, rad_gap, rad_clad]
Ce106.materials = [materials['UO2_106'], materials['Gap_106'], materials['Clad_106'], materials['Water_106']]
Ce106.spatial_modes = spat_modes
Ce106.d_u = 0.05
Ce106.n_phi_u = 50


Ce107 = lotus.SquareCell(pitch=1.26, name="Cell 107")
Ce107.circles = [rad_fuel, rad_gap, rad_clad]
Ce107.materials = [materials['UO2_107'], materials['Gap_107'], materials['Clad_107'], materials['Water_107']]
Ce107.spatial_modes = spat_modes
Ce107.d_u = 0.05
Ce107.n_phi_u = 50


Ce108 = lotus.SquareCell(pitch=1.26, name="Cell 108")
Ce108.circles = [rad_fuel, rad_gap, rad_clad]
Ce108.materials = [materials['UO2_108'], materials['Gap_108'], materials['Clad_108'], materials['Water_108']]
Ce108.spatial_modes = spat_modes
Ce108.d_u = 0.05
Ce108.n_phi_u = 50


Ce109 = lotus.SquareCell(pitch=1.26, name="Cell 109")
Ce109.circles = [rad_fuel, rad_gap, rad_clad]
Ce109.materials = [materials['UO2_109'], materials['Gap_109'], materials['Clad_109'], materials['Water_109']]
Ce109.spatial_modes = spat_modes
Ce109.d_u = 0.05
Ce109.n_phi_u = 50


Ce110 = lotus.SquareCell(pitch=1.26, name="Cell 110")
Ce110.circles = [rad_fuel, rad_gap, rad_clad]
Ce110.materials = [materials['UO2_110'], materials['Gap_110'], materials['Clad_110'], materials['Water_110']]
Ce110.spatial_modes = spat_modes
Ce110.d_u = 0.05
Ce110.n_phi_u = 50


Ce111 = lotus.SquareCell(pitch=1.26, name="Cell 111")
Ce111.circles = [rad_fuel, rad_gap, rad_clad]
Ce111.materials = [materials['UO2_111'], materials['Gap_111'], materials['Clad_111'], materials['Water_111']]
Ce111.spatial_modes = spat_modes
Ce111.d_u = 0.05
Ce111.n_phi_u = 50


Ce112 = lotus.SquareCell(pitch=1.26, name="Cell 112")
Ce112.circles = [rad_fuel, rad_gap, rad_clad]
Ce112.materials = [materials['UO2_112'], materials['Gap_112'], materials['Clad_112'], materials['Water_112']]
Ce112.spatial_modes = spat_modes
Ce112.d_u = 0.05
Ce112.n_phi_u = 50


Ce113 = lotus.SquareCell(pitch=1.26, name="Cell 113")
Ce113.circles = [rad_fuel, rad_gap, rad_clad]
Ce113.materials = [materials['UO2_113'], materials['Gap_113'], materials['Clad_113'], materials['Water_113']]
Ce113.spatial_modes = spat_modes
Ce113.d_u = 0.05
Ce113.n_phi_u = 50


Ce114 = lotus.SquareCell(pitch=1.26, name="Cell 114")
Ce114.circles = [rad_fuel, rad_gap, rad_clad]
Ce114.materials = [materials['UO2_114'], materials['Gap_114'], materials['Clad_114'], materials['Water_114']]
Ce114.spatial_modes = spat_modes
Ce114.d_u = 0.05
Ce114.n_phi_u = 50


Ce115 = lotus.SquareCell(pitch=1.26, name="Cell 115")
Ce115.circles = [rad_fuel, rad_gap, rad_clad]
Ce115.materials = [materials['UO2_115'], materials['Gap_115'], materials['Clad_115'], materials['Water_115']]
Ce115.spatial_modes = spat_modes
Ce115.d_u = 0.05
Ce115.n_phi_u = 50


Ce116 = lotus.SquareCell(pitch=1.26, name="Cell 116")
Ce116.circles = [rad_fuel, rad_gap, rad_clad]
Ce116.materials = [materials['UO2_116'], materials['Gap_116'], materials['Clad_116'], materials['Water_116']]
Ce116.spatial_modes = spat_modes
Ce116.d_u = 0.05
Ce116.n_phi_u = 50


Ce117 = lotus.SquareCell(pitch=1.26, name="Cell 117")
Ce117.circles = [rad_fuel, rad_gap, rad_clad]
Ce117.materials = [materials['UO2_117'], materials['Gap_117'], materials['Clad_117'], materials['Water_117']]
Ce117.spatial_modes = spat_modes
Ce117.d_u = 0.05
Ce117.n_phi_u = 50


Ce118 = lotus.SquareCell(pitch=1.26, name="Cell 118")
Ce118.circles = [rad_fuel, rad_gap, rad_clad]
Ce118.materials = [materials['UO2_118'], materials['Gap_118'], materials['Clad_118'], materials['Water_118']]
Ce118.spatial_modes = spat_modes
Ce118.d_u = 0.05
Ce118.n_phi_u = 50


Ce119 = lotus.SquareCell(pitch=1.26, name="Cell 119")
Ce119.circles = [rad_fuel, rad_gap, rad_clad]
Ce119.materials = [materials['UO2_119'], materials['Gap_119'], materials['Clad_119'], materials['Water_119']]
Ce119.spatial_modes = spat_modes
Ce119.d_u = 0.05
Ce119.n_phi_u = 50


Ce120 = lotus.SquareCell(pitch=1.26, name="Cell 120")
Ce120.circles = [rad_fuel, rad_gap, rad_clad]
Ce120.materials = [materials['UO2_120'], materials['Gap_120'], materials['Clad_120'], materials['Water_120']]
Ce120.spatial_modes = spat_modes
Ce120.d_u = 0.05
Ce120.n_phi_u = 50


Ce121 = lotus.SquareCell(pitch=1.26, name="Cell 121")
Ce121.circles = [rad_fuel, rad_gap, rad_clad]
Ce121.materials = [materials['UO2_121'], materials['Gap_121'], materials['Clad_121'], materials['Water_121']]
Ce121.spatial_modes = spat_modes
Ce121.d_u = 0.05
Ce121.n_phi_u = 50


Ce122 = lotus.SquareCell(pitch=1.26, name="Cell 122")
Ce122.circles = [rad_fuel, rad_gap, rad_clad]
Ce122.materials = [materials['UO2_122'], materials['Gap_122'], materials['Clad_122'], materials['Water_122']]
Ce122.spatial_modes = spat_modes
Ce122.d_u = 0.05
Ce122.n_phi_u = 50


Ce123 = lotus.SquareCell(pitch=1.26, name="Cell 123")
Ce123.circles = [rad_fuel, rad_gap, rad_clad]
Ce123.materials = [materials['UO2_123'], materials['Gap_123'], materials['Clad_123'], materials['Water_123']]
Ce123.spatial_modes = spat_modes
Ce123.d_u = 0.05
Ce123.n_phi_u = 50


Ce124 = lotus.SquareCell(pitch=1.26, name="Cell 124")
Ce124.circles = [rad_fuel, rad_gap, rad_clad]
Ce124.materials = [materials['UO2_124'], materials['Gap_124'], materials['Clad_124'], materials['Water_124']]
Ce124.spatial_modes = spat_modes
Ce124.d_u = 0.05
Ce124.n_phi_u = 50


Ce125 = lotus.SquareCell(pitch=1.26, name="Cell 125")
Ce125.circles = [rad_fuel, rad_gap, rad_clad]
Ce125.materials = [materials['UO2_125'], materials['Gap_125'], materials['Clad_125'], materials['Water_125']]
Ce125.spatial_modes = spat_modes
Ce125.d_u = 0.05
Ce125.n_phi_u = 50


Ce126 = lotus.SquareCell(pitch=1.26, name="Cell 126")
Ce126.circles = [rad_fuel, rad_gap, rad_clad]
Ce126.materials = [materials['UO2_126'], materials['Gap_126'], materials['Clad_126'], materials['Water_126']]
Ce126.spatial_modes = spat_modes
Ce126.d_u = 0.05
Ce126.n_phi_u = 50


Ce127 = lotus.SquareCell(pitch=1.26, name="Cell 127")
Ce127.circles = [rad_fuel, rad_gap, rad_clad]
Ce127.materials = [materials['UO2_127'], materials['Gap_127'], materials['Clad_127'], materials['Water_127']]
Ce127.spatial_modes = spat_modes
Ce127.d_u = 0.05
Ce127.n_phi_u = 50


Ce128 = lotus.SquareCell(pitch=1.26, name="Cell 128")
Ce128.circles = [rad_fuel, rad_gap, rad_clad]
Ce128.materials = [materials['UO2_128'], materials['Gap_128'], materials['Clad_128'], materials['Water_128']]
Ce128.spatial_modes = spat_modes
Ce128.d_u = 0.05
Ce128.n_phi_u = 50


Ce129 = lotus.SquareCell(pitch=1.26, name="Cell 129")
Ce129.circles = [rad_fuel, rad_gap, rad_clad]
Ce129.materials = [materials['UO2_129'], materials['Gap_129'], materials['Clad_129'], materials['Water_129']]
Ce129.spatial_modes = spat_modes
Ce129.d_u = 0.05
Ce129.n_phi_u = 50


Ce130 = lotus.SquareCell(pitch=1.26, name="Cell 130")
Ce130.circles = [rad_fuel, rad_gap, rad_clad]
Ce130.materials = [materials['UO2_130'], materials['Gap_130'], materials['Clad_130'], materials['Water_130']]
Ce130.spatial_modes = spat_modes
Ce130.d_u = 0.05
Ce130.n_phi_u = 50


Ce131 = lotus.SquareCell(pitch=1.26, name="Cell 131")
Ce131.circles = [rad_fuel, rad_gap, rad_clad]
Ce131.materials = [materials['UO2_131'], materials['Gap_131'], materials['Clad_131'], materials['Water_131']]
Ce131.spatial_modes = spat_modes
Ce131.d_u = 0.05
Ce131.n_phi_u = 50


Ce132 = lotus.SquareCell(pitch=1.26, name="Cell 132")
Ce132.circles = [rad_fuel, rad_gap, rad_clad]
Ce132.materials = [materials['UO2_132'], materials['Gap_132'], materials['Clad_132'], materials['Water_132']]
Ce132.spatial_modes = spat_modes
Ce132.d_u = 0.05
Ce132.n_phi_u = 50


Ce133 = lotus.SquareCell(pitch=1.26, name="Cell 133")
Ce133.circles = [rad_fuel, rad_gap, rad_clad]
Ce133.materials = [materials['UO2_133'], materials['Gap_133'], materials['Clad_133'], materials['Water_133']]
Ce133.spatial_modes = spat_modes
Ce133.d_u = 0.05
Ce133.n_phi_u = 50


Ce134 = lotus.SquareCell(pitch=1.26, name="Cell 134")
Ce134.circles = [rad_fuel, rad_gap, rad_clad]
Ce134.materials = [materials['UO2_134'], materials['Gap_134'], materials['Clad_134'], materials['Water_134']]
Ce134.spatial_modes = spat_modes
Ce134.d_u = 0.05
Ce134.n_phi_u = 50


Ce135 = lotus.SquareCell(pitch=1.26, name="Cell 135")
Ce135.circles = [rad_fuel, rad_gap, rad_clad]
Ce135.materials = [materials['UO2_135'], materials['Gap_135'], materials['Clad_135'], materials['Water_135']]
Ce135.spatial_modes = spat_modes
Ce135.d_u = 0.05
Ce135.n_phi_u = 50


Ce136 = lotus.SquareCell(pitch=1.26, name="Cell 136")
Ce136.circles = [rad_fuel, rad_gap, rad_clad]
Ce136.materials = [materials['UO2_136'], materials['Gap_136'], materials['Clad_136'], materials['Water_136']]
Ce136.spatial_modes = spat_modes
Ce136.d_u = 0.05
Ce136.n_phi_u = 50


Ce137 = lotus.SquareCell(pitch=1.26, name="Cell 137")
Ce137.circles = [rad_fuel, rad_gap, rad_clad]
Ce137.materials = [materials['UO2_137'], materials['Gap_137'], materials['Clad_137'], materials['Water_137']]
Ce137.spatial_modes = spat_modes
Ce137.d_u = 0.05
Ce137.n_phi_u = 50


Ce138 = lotus.SquareCell(pitch=1.26, name="Cell 138")
Ce138.circles = [rad_fuel, rad_gap, rad_clad]
Ce138.materials = [materials['UO2_138'], materials['Gap_138'], materials['Clad_138'], materials['Water_138']]
Ce138.spatial_modes = spat_modes
Ce138.d_u = 0.05
Ce138.n_phi_u = 50


Ce139 = lotus.SquareCell(pitch=1.26, name="Cell 139")
Ce139.circles = [rad_guide1, rad_guide2]
Ce139.materials = [materials['Water_139'], materials['Clad_139'], materials['Water_139']]
Ce139.spatial_modes = spat_modes_2
Ce139.d_u = 0.05
Ce139.n_phi_u = 50


Ce140 = lotus.SquareCell(pitch=1.26, name="Cell 140")
Ce140.circles = [rad_fuel, rad_gap, rad_clad]
Ce140.materials = [materials['UO2_140'], materials['Gap_140'], materials['Clad_140'], materials['Water_140']]
Ce140.spatial_modes = spat_modes
Ce140.d_u = 0.05
Ce140.n_phi_u = 50


Ce141 = lotus.SquareCell(pitch=1.26, name="Cell 141")
Ce141.circles = [rad_fuel, rad_gap, rad_clad]
Ce141.materials = [materials['UO2_141'], materials['Gap_141'], materials['Clad_141'], materials['Water_141']]
Ce141.spatial_modes = spat_modes
Ce141.d_u = 0.05
Ce141.n_phi_u = 50


Ce142 = lotus.SquareCell(pitch=1.26, name="Cell 142")
Ce142.circles = [rad_guide1, rad_guide2]
Ce142.materials = [materials['Water_142'], materials['Clad_142'], materials['Water_142']]
Ce142.spatial_modes = spat_modes_2
Ce142.d_u = 0.05
Ce142.n_phi_u = 50


Ce143 = lotus.SquareCell(pitch=1.26, name="Cell 143")
Ce143.circles = [rad_fuel, rad_gap, rad_clad]
Ce143.materials = [materials['UO2_143'], materials['Gap_143'], materials['Clad_143'], materials['Water_143']]
Ce143.spatial_modes = spat_modes
Ce143.d_u = 0.05
Ce143.n_phi_u = 50


Ce144 = lotus.SquareCell(pitch=1.26, name="Cell 144")
Ce144.circles = [rad_fuel, rad_gap, rad_clad]
Ce144.materials = [materials['UO2_144'], materials['Gap_144'], materials['Clad_144'], materials['Water_144']]
Ce144.spatial_modes = spat_modes
Ce144.d_u = 0.05
Ce144.n_phi_u = 50


Ce145 = lotus.SquareCell(pitch=1.26, name="Cell 145")
Ce145.circles = [rad_guide1, rad_guide2]
Ce145.materials = [materials['Water_145'], materials['Clad_145'], materials['Water_145']]
Ce145.spatial_modes = spat_modes_2
Ce145.d_u = 0.05
Ce145.n_phi_u = 50


Ce146 = lotus.SquareCell(pitch=1.26, name="Cell 146")
Ce146.circles = [rad_fuel, rad_gap, rad_clad]
Ce146.materials = [materials['UO2_146'], materials['Gap_146'], materials['Clad_146'], materials['Water_146']]
Ce146.spatial_modes = spat_modes
Ce146.d_u = 0.05
Ce146.n_phi_u = 50


Ce147 = lotus.SquareCell(pitch=1.26, name="Cell 147")
Ce147.circles = [rad_fuel, rad_gap, rad_clad]
Ce147.materials = [materials['UO2_147'], materials['Gap_147'], materials['Clad_147'], materials['Water_147']]
Ce147.spatial_modes = spat_modes
Ce147.d_u = 0.05
Ce147.n_phi_u = 50


Ce148 = lotus.SquareCell(pitch=1.26, name="Cell 148")
Ce148.circles = [rad_guide1, rad_guide2]
Ce148.materials = [materials['Water_148'], materials['Clad_148'], materials['Water_148']]
Ce148.spatial_modes = spat_modes_2
Ce148.d_u = 0.05
Ce148.n_phi_u = 50


Ce149 = lotus.SquareCell(pitch=1.26, name="Cell 149")
Ce149.circles = [rad_fuel, rad_gap, rad_clad]
Ce149.materials = [materials['UO2_149'], materials['Gap_149'], materials['Clad_149'], materials['Water_149']]
Ce149.spatial_modes = spat_modes
Ce149.d_u = 0.05
Ce149.n_phi_u = 50


Ce150 = lotus.SquareCell(pitch=1.26, name="Cell 150")
Ce150.circles = [rad_fuel, rad_gap, rad_clad]
Ce150.materials = [materials['UO2_150'], materials['Gap_150'], materials['Clad_150'], materials['Water_150']]
Ce150.spatial_modes = spat_modes
Ce150.d_u = 0.05
Ce150.n_phi_u = 50


Ce151 = lotus.SquareCell(pitch=1.26, name="Cell 151")
Ce151.circles = [rad_guide1, rad_guide2]
Ce151.materials = [materials['Water_151'], materials['Clad_151'], materials['Water_151']]
Ce151.spatial_modes = spat_modes_2
Ce151.d_u = 0.05
Ce151.n_phi_u = 50


Ce152 = lotus.SquareCell(pitch=1.26, name="Cell 152")
Ce152.circles = [rad_fuel, rad_gap, rad_clad]
Ce152.materials = [materials['UO2_152'], materials['Gap_152'], materials['Clad_152'], materials['Water_152']]
Ce152.spatial_modes = spat_modes
Ce152.d_u = 0.05
Ce152.n_phi_u = 50


Ce153 = lotus.SquareCell(pitch=1.26, name="Cell 153")
Ce153.circles = [rad_fuel, rad_gap, rad_clad]
Ce153.materials = [materials['UO2_153'], materials['Gap_153'], materials['Clad_153'], materials['Water_153']]
Ce153.spatial_modes = spat_modes
Ce153.d_u = 0.05
Ce153.n_phi_u = 50


Ce154 = lotus.SquareCell(pitch=1.26, name="Cell 154")
Ce154.circles = [rad_fuel, rad_gap, rad_clad]
Ce154.materials = [materials['UO2_154'], materials['Gap_154'], materials['Clad_154'], materials['Water_154']]
Ce154.spatial_modes = spat_modes
Ce154.d_u = 0.05
Ce154.n_phi_u = 50


Ce155 = lotus.SquareCell(pitch=1.26, name="Cell 155")
Ce155.circles = [rad_fuel, rad_gap, rad_clad]
Ce155.materials = [materials['UO2_155'], materials['Gap_155'], materials['Clad_155'], materials['Water_155']]
Ce155.spatial_modes = spat_modes
Ce155.d_u = 0.05
Ce155.n_phi_u = 50


Ce156 = lotus.SquareCell(pitch=1.26, name="Cell 156")
Ce156.circles = [rad_fuel, rad_gap, rad_clad]
Ce156.materials = [materials['UO2_156'], materials['Gap_156'], materials['Clad_156'], materials['Water_156']]
Ce156.spatial_modes = spat_modes
Ce156.d_u = 0.05
Ce156.n_phi_u = 50


Ce157 = lotus.SquareCell(pitch=1.26, name="Cell 157")
Ce157.circles = [rad_fuel, rad_gap, rad_clad]
Ce157.materials = [materials['UO2_157'], materials['Gap_157'], materials['Clad_157'], materials['Water_157']]
Ce157.spatial_modes = spat_modes
Ce157.d_u = 0.05
Ce157.n_phi_u = 50


Ce158 = lotus.SquareCell(pitch=1.26, name="Cell 158")
Ce158.circles = [rad_fuel, rad_gap, rad_clad]
Ce158.materials = [materials['UO2_158'], materials['Gap_158'], materials['Clad_158'], materials['Water_158']]
Ce158.spatial_modes = spat_modes
Ce158.d_u = 0.05
Ce158.n_phi_u = 50


Ce159 = lotus.SquareCell(pitch=1.26, name="Cell 159")
Ce159.circles = [rad_fuel, rad_gap, rad_clad]
Ce159.materials = [materials['UO2_159'], materials['Gap_159'], materials['Clad_159'], materials['Water_159']]
Ce159.spatial_modes = spat_modes
Ce159.d_u = 0.05
Ce159.n_phi_u = 50


Ce160 = lotus.SquareCell(pitch=1.26, name="Cell 160")
Ce160.circles = [rad_fuel, rad_gap, rad_clad]
Ce160.materials = [materials['UO2_160'], materials['Gap_160'], materials['Clad_160'], materials['Water_160']]
Ce160.spatial_modes = spat_modes
Ce160.d_u = 0.05
Ce160.n_phi_u = 50


Ce161 = lotus.SquareCell(pitch=1.26, name="Cell 161")
Ce161.circles = [rad_fuel, rad_gap, rad_clad]
Ce161.materials = [materials['UO2_161'], materials['Gap_161'], materials['Clad_161'], materials['Water_161']]
Ce161.spatial_modes = spat_modes
Ce161.d_u = 0.05
Ce161.n_phi_u = 50


Ce162 = lotus.SquareCell(pitch=1.26, name="Cell 162")
Ce162.circles = [rad_fuel, rad_gap, rad_clad]
Ce162.materials = [materials['UO2_162'], materials['Gap_162'], materials['Clad_162'], materials['Water_162']]
Ce162.spatial_modes = spat_modes
Ce162.d_u = 0.05
Ce162.n_phi_u = 50


Ce163 = lotus.SquareCell(pitch=1.26, name="Cell 163")
Ce163.circles = [rad_fuel, rad_gap, rad_clad]
Ce163.materials = [materials['UO2_163'], materials['Gap_163'], materials['Clad_163'], materials['Water_163']]
Ce163.spatial_modes = spat_modes
Ce163.d_u = 0.05
Ce163.n_phi_u = 50


Ce164 = lotus.SquareCell(pitch=1.26, name="Cell 164")
Ce164.circles = [rad_fuel, rad_gap, rad_clad]
Ce164.materials = [materials['UO2_164'], materials['Gap_164'], materials['Clad_164'], materials['Water_164']]
Ce164.spatial_modes = spat_modes
Ce164.d_u = 0.05
Ce164.n_phi_u = 50


Ce165 = lotus.SquareCell(pitch=1.26, name="Cell 165")
Ce165.circles = [rad_fuel, rad_gap, rad_clad]
Ce165.materials = [materials['UO2_165'], materials['Gap_165'], materials['Clad_165'], materials['Water_165']]
Ce165.spatial_modes = spat_modes
Ce165.d_u = 0.05
Ce165.n_phi_u = 50


Ce166 = lotus.SquareCell(pitch=1.26, name="Cell 166")
Ce166.circles = [rad_fuel, rad_gap, rad_clad]
Ce166.materials = [materials['UO2_166'], materials['Gap_166'], materials['Clad_166'], materials['Water_166']]
Ce166.spatial_modes = spat_modes
Ce166.d_u = 0.05
Ce166.n_phi_u = 50


Ce167 = lotus.SquareCell(pitch=1.26, name="Cell 167")
Ce167.circles = [rad_fuel, rad_gap, rad_clad]
Ce167.materials = [materials['UO2_167'], materials['Gap_167'], materials['Clad_167'], materials['Water_167']]
Ce167.spatial_modes = spat_modes
Ce167.d_u = 0.05
Ce167.n_phi_u = 50


Ce168 = lotus.SquareCell(pitch=1.26, name="Cell 168")
Ce168.circles = [rad_fuel, rad_gap, rad_clad]
Ce168.materials = [materials['UO2_168'], materials['Gap_168'], materials['Clad_168'], materials['Water_168']]
Ce168.spatial_modes = spat_modes
Ce168.d_u = 0.05
Ce168.n_phi_u = 50


Ce169 = lotus.SquareCell(pitch=1.26, name="Cell 169")
Ce169.circles = [rad_fuel, rad_gap, rad_clad]
Ce169.materials = [materials['UO2_169'], materials['Gap_169'], materials['Clad_169'], materials['Water_169']]
Ce169.spatial_modes = spat_modes
Ce169.d_u = 0.05
Ce169.n_phi_u = 50


Ce170 = lotus.SquareCell(pitch=1.26, name="Cell 170")
Ce170.circles = [rad_fuel, rad_gap, rad_clad]
Ce170.materials = [materials['UO2_170'], materials['Gap_170'], materials['Clad_170'], materials['Water_170']]
Ce170.spatial_modes = spat_modes
Ce170.d_u = 0.05
Ce170.n_phi_u = 50


Ce171 = lotus.SquareCell(pitch=1.26, name="Cell 171")
Ce171.circles = [rad_fuel, rad_gap, rad_clad]
Ce171.materials = [materials['UO2_171'], materials['Gap_171'], materials['Clad_171'], materials['Water_171']]
Ce171.spatial_modes = spat_modes
Ce171.d_u = 0.05
Ce171.n_phi_u = 50


Ce172 = lotus.SquareCell(pitch=1.26, name="Cell 172")
Ce172.circles = [rad_fuel, rad_gap, rad_clad]
Ce172.materials = [materials['UO2_172'], materials['Gap_172'], materials['Clad_172'], materials['Water_172']]
Ce172.spatial_modes = spat_modes
Ce172.d_u = 0.05
Ce172.n_phi_u = 50


Ce173 = lotus.SquareCell(pitch=1.26, name="Cell 173")
Ce173.circles = [rad_fuel, rad_gap, rad_clad]
Ce173.materials = [materials['UO2_173'], materials['Gap_173'], materials['Clad_173'], materials['Water_173']]
Ce173.spatial_modes = spat_modes
Ce173.d_u = 0.05
Ce173.n_phi_u = 50


Ce174 = lotus.SquareCell(pitch=1.26, name="Cell 174")
Ce174.circles = [rad_fuel, rad_gap, rad_clad]
Ce174.materials = [materials['UO2_174'], materials['Gap_174'], materials['Clad_174'], materials['Water_174']]
Ce174.spatial_modes = spat_modes
Ce174.d_u = 0.05
Ce174.n_phi_u = 50


Ce175 = lotus.SquareCell(pitch=1.26, name="Cell 175")
Ce175.circles = [rad_fuel, rad_gap, rad_clad]
Ce175.materials = [materials['UO2_175'], materials['Gap_175'], materials['Clad_175'], materials['Water_175']]
Ce175.spatial_modes = spat_modes
Ce175.d_u = 0.05
Ce175.n_phi_u = 50


Ce176 = lotus.SquareCell(pitch=1.26, name="Cell 176")
Ce176.circles = [rad_fuel, rad_gap, rad_clad]
Ce176.materials = [materials['UO2_176'], materials['Gap_176'], materials['Clad_176'], materials['Water_176']]
Ce176.spatial_modes = spat_modes
Ce176.d_u = 0.05
Ce176.n_phi_u = 50


Ce177 = lotus.SquareCell(pitch=1.26, name="Cell 177")
Ce177.circles = [rad_fuel, rad_gap, rad_clad]
Ce177.materials = [materials['UO2_177'], materials['Gap_177'], materials['Clad_177'], materials['Water_177']]
Ce177.spatial_modes = spat_modes
Ce177.d_u = 0.05
Ce177.n_phi_u = 50


Ce178 = lotus.SquareCell(pitch=1.26, name="Cell 178")
Ce178.circles = [rad_fuel, rad_gap, rad_clad]
Ce178.materials = [materials['UO2_178'], materials['Gap_178'], materials['Clad_178'], materials['Water_178']]
Ce178.spatial_modes = spat_modes
Ce178.d_u = 0.05
Ce178.n_phi_u = 50


Ce179 = lotus.SquareCell(pitch=1.26, name="Cell 179")
Ce179.circles = [rad_fuel, rad_gap, rad_clad]
Ce179.materials = [materials['UO2_179'], materials['Gap_179'], materials['Clad_179'], materials['Water_179']]
Ce179.spatial_modes = spat_modes
Ce179.d_u = 0.05
Ce179.n_phi_u = 50


Ce180 = lotus.SquareCell(pitch=1.26, name="Cell 180")
Ce180.circles = [rad_fuel, rad_gap, rad_clad]
Ce180.materials = [materials['UO2_180'], materials['Gap_180'], materials['Clad_180'], materials['Water_180']]
Ce180.spatial_modes = spat_modes
Ce180.d_u = 0.05
Ce180.n_phi_u = 50


Ce181 = lotus.SquareCell(pitch=1.26, name="Cell 181")
Ce181.circles = [rad_fuel, rad_gap, rad_clad]
Ce181.materials = [materials['UO2_181'], materials['Gap_181'], materials['Clad_181'], materials['Water_181']]
Ce181.spatial_modes = spat_modes
Ce181.d_u = 0.05
Ce181.n_phi_u = 50


Ce182 = lotus.SquareCell(pitch=1.26, name="Cell 182")
Ce182.circles = [rad_fuel, rad_gap, rad_clad]
Ce182.materials = [materials['UO2_182'], materials['Gap_182'], materials['Clad_182'], materials['Water_182']]
Ce182.spatial_modes = spat_modes
Ce182.d_u = 0.05
Ce182.n_phi_u = 50


Ce183 = lotus.SquareCell(pitch=1.26, name="Cell 183")
Ce183.circles = [rad_fuel, rad_gap, rad_clad]
Ce183.materials = [materials['UO2_183'], materials['Gap_183'], materials['Clad_183'], materials['Water_183']]
Ce183.spatial_modes = spat_modes
Ce183.d_u = 0.05
Ce183.n_phi_u = 50


Ce184 = lotus.SquareCell(pitch=1.26, name="Cell 184")
Ce184.circles = [rad_fuel, rad_gap, rad_clad]
Ce184.materials = [materials['UO2_184'], materials['Gap_184'], materials['Clad_184'], materials['Water_184']]
Ce184.spatial_modes = spat_modes
Ce184.d_u = 0.05
Ce184.n_phi_u = 50


Ce185 = lotus.SquareCell(pitch=1.26, name="Cell 185")
Ce185.circles = [rad_fuel, rad_gap, rad_clad]
Ce185.materials = [materials['UO2_185'], materials['Gap_185'], materials['Clad_185'], materials['Water_185']]
Ce185.spatial_modes = spat_modes
Ce185.d_u = 0.05
Ce185.n_phi_u = 50


Ce186 = lotus.SquareCell(pitch=1.26, name="Cell 186")
Ce186.circles = [rad_fuel, rad_gap, rad_clad]
Ce186.materials = [materials['UO2_186'], materials['Gap_186'], materials['Clad_186'], materials['Water_186']]
Ce186.spatial_modes = spat_modes
Ce186.d_u = 0.05
Ce186.n_phi_u = 50


Ce187 = lotus.SquareCell(pitch=1.26, name="Cell 187")
Ce187.circles = [rad_fuel, rad_gap, rad_clad]
Ce187.materials = [materials['UO2_187'], materials['Gap_187'], materials['Clad_187'], materials['Water_187']]
Ce187.spatial_modes = spat_modes
Ce187.d_u = 0.05
Ce187.n_phi_u = 50


Ce188 = lotus.SquareCell(pitch=1.26, name="Cell 188")
Ce188.circles = [rad_fuel, rad_gap, rad_clad]
Ce188.materials = [materials['UO2_188'], materials['Gap_188'], materials['Clad_188'], materials['Water_188']]
Ce188.spatial_modes = spat_modes
Ce188.d_u = 0.05
Ce188.n_phi_u = 50


Ce189 = lotus.SquareCell(pitch=1.26, name="Cell 189")
Ce189.circles = [rad_fuel, rad_gap, rad_clad]
Ce189.materials = [materials['UO2_189'], materials['Gap_189'], materials['Clad_189'], materials['Water_189']]
Ce189.spatial_modes = spat_modes
Ce189.d_u = 0.05
Ce189.n_phi_u = 50


Ce190 = lotus.SquareCell(pitch=1.26, name="Cell 190")
Ce190.circles = [rad_guide1, rad_guide2]
Ce190.materials = [materials['Water_190'], materials['Clad_190'], materials['Water_190']]
Ce190.spatial_modes = spat_modes_2
Ce190.d_u = 0.05
Ce190.n_phi_u = 50


Ce191 = lotus.SquareCell(pitch=1.26, name="Cell 191")
Ce191.circles = [rad_fuel, rad_gap, rad_clad]
Ce191.materials = [materials['UO2_191'], materials['Gap_191'], materials['Clad_191'], materials['Water_191']]
Ce191.spatial_modes = spat_modes
Ce191.d_u = 0.05
Ce191.n_phi_u = 50


Ce192 = lotus.SquareCell(pitch=1.26, name="Cell 192")
Ce192.circles = [rad_fuel, rad_gap, rad_clad]
Ce192.materials = [materials['UO2_192'], materials['Gap_192'], materials['Clad_192'], materials['Water_192']]
Ce192.spatial_modes = spat_modes
Ce192.d_u = 0.05
Ce192.n_phi_u = 50


Ce193 = lotus.SquareCell(pitch=1.26, name="Cell 193")
Ce193.circles = [rad_guide1, rad_guide2]
Ce193.materials = [materials['Water_193'], materials['Clad_193'], materials['Water_193']]
Ce193.spatial_modes = spat_modes_2
Ce193.d_u = 0.05
Ce193.n_phi_u = 50


Ce194 = lotus.SquareCell(pitch=1.26, name="Cell 194")
Ce194.circles = [rad_fuel, rad_gap, rad_clad]
Ce194.materials = [materials['UO2_194'], materials['Gap_194'], materials['Clad_194'], materials['Water_194']]
Ce194.spatial_modes = spat_modes
Ce194.d_u = 0.05
Ce194.n_phi_u = 50


Ce195 = lotus.SquareCell(pitch=1.26, name="Cell 195")
Ce195.circles = [rad_fuel, rad_gap, rad_clad]
Ce195.materials = [materials['UO2_195'], materials['Gap_195'], materials['Clad_195'], materials['Water_195']]
Ce195.spatial_modes = spat_modes
Ce195.d_u = 0.05
Ce195.n_phi_u = 50


Ce196 = lotus.SquareCell(pitch=1.26, name="Cell 196")
Ce196.circles = [rad_guide1, rad_guide2]
Ce196.materials = [materials['Water_196'], materials['Clad_196'], materials['Water_196']]
Ce196.spatial_modes = spat_modes_2
Ce196.d_u = 0.05
Ce196.n_phi_u = 50


Ce197 = lotus.SquareCell(pitch=1.26, name="Cell 197")
Ce197.circles = [rad_fuel, rad_gap, rad_clad]
Ce197.materials = [materials['UO2_197'], materials['Gap_197'], materials['Clad_197'], materials['Water_197']]
Ce197.spatial_modes = spat_modes
Ce197.d_u = 0.05
Ce197.n_phi_u = 50


Ce198 = lotus.SquareCell(pitch=1.26, name="Cell 198")
Ce198.circles = [rad_fuel, rad_gap, rad_clad]
Ce198.materials = [materials['UO2_198'], materials['Gap_198'], materials['Clad_198'], materials['Water_198']]
Ce198.spatial_modes = spat_modes
Ce198.d_u = 0.05
Ce198.n_phi_u = 50


Ce199 = lotus.SquareCell(pitch=1.26, name="Cell 199")
Ce199.circles = [rad_guide1, rad_guide2]
Ce199.materials = [materials['Water_199'], materials['Clad_199'], materials['Water_199']]
Ce199.spatial_modes = spat_modes_2
Ce199.d_u = 0.05
Ce199.n_phi_u = 50


Ce200 = lotus.SquareCell(pitch=1.26, name="Cell 200")
Ce200.circles = [rad_fuel, rad_gap, rad_clad]
Ce200.materials = [materials['UO2_200'], materials['Gap_200'], materials['Clad_200'], materials['Water_200']]
Ce200.spatial_modes = spat_modes
Ce200.d_u = 0.05
Ce200.n_phi_u = 50


Ce201 = lotus.SquareCell(pitch=1.26, name="Cell 201")
Ce201.circles = [rad_fuel, rad_gap, rad_clad]
Ce201.materials = [materials['UO2_201'], materials['Gap_201'], materials['Clad_201'], materials['Water_201']]
Ce201.spatial_modes = spat_modes
Ce201.d_u = 0.05
Ce201.n_phi_u = 50


Ce202 = lotus.SquareCell(pitch=1.26, name="Cell 202")
Ce202.circles = [rad_guide1, rad_guide2]
Ce202.materials = [materials['Water_202'], materials['Clad_202'], materials['Water_202']]
Ce202.spatial_modes = spat_modes_2
Ce202.d_u = 0.05
Ce202.n_phi_u = 50


Ce203 = lotus.SquareCell(pitch=1.26, name="Cell 203")
Ce203.circles = [rad_fuel, rad_gap, rad_clad]
Ce203.materials = [materials['UO2_203'], materials['Gap_203'], materials['Clad_203'], materials['Water_203']]
Ce203.spatial_modes = spat_modes
Ce203.d_u = 0.05
Ce203.n_phi_u = 50


Ce204 = lotus.SquareCell(pitch=1.26, name="Cell 204")
Ce204.circles = [rad_fuel, rad_gap, rad_clad]
Ce204.materials = [materials['UO2_204'], materials['Gap_204'], materials['Clad_204'], materials['Water_204']]
Ce204.spatial_modes = spat_modes
Ce204.d_u = 0.05
Ce204.n_phi_u = 50


Ce205 = lotus.SquareCell(pitch=1.26, name="Cell 205")
Ce205.circles = [rad_fuel, rad_gap, rad_clad]
Ce205.materials = [materials['UO2_205'], materials['Gap_205'], materials['Clad_205'], materials['Water_205']]
Ce205.spatial_modes = spat_modes
Ce205.d_u = 0.05
Ce205.n_phi_u = 50


Ce206 = lotus.SquareCell(pitch=1.26, name="Cell 206")
Ce206.circles = [rad_fuel, rad_gap, rad_clad]
Ce206.materials = [materials['UO2_206'], materials['Gap_206'], materials['Clad_206'], materials['Water_206']]
Ce206.spatial_modes = spat_modes
Ce206.d_u = 0.05
Ce206.n_phi_u = 50


Ce207 = lotus.SquareCell(pitch=1.26, name="Cell 207")
Ce207.circles = [rad_fuel, rad_gap, rad_clad]
Ce207.materials = [materials['UO2_207'], materials['Gap_207'], materials['Clad_207'], materials['Water_207']]
Ce207.spatial_modes = spat_modes
Ce207.d_u = 0.05
Ce207.n_phi_u = 50


Ce208 = lotus.SquareCell(pitch=1.26, name="Cell 208")
Ce208.circles = [rad_fuel, rad_gap, rad_clad]
Ce208.materials = [materials['UO2_208'], materials['Gap_208'], materials['Clad_208'], materials['Water_208']]
Ce208.spatial_modes = spat_modes
Ce208.d_u = 0.05
Ce208.n_phi_u = 50


Ce209 = lotus.SquareCell(pitch=1.26, name="Cell 209")
Ce209.circles = [rad_fuel, rad_gap, rad_clad]
Ce209.materials = [materials['UO2_209'], materials['Gap_209'], materials['Clad_209'], materials['Water_209']]
Ce209.spatial_modes = spat_modes
Ce209.d_u = 0.05
Ce209.n_phi_u = 50


Ce210 = lotus.SquareCell(pitch=1.26, name="Cell 210")
Ce210.circles = [rad_fuel, rad_gap, rad_clad]
Ce210.materials = [materials['UO2_210'], materials['Gap_210'], materials['Clad_210'], materials['Water_210']]
Ce210.spatial_modes = spat_modes
Ce210.d_u = 0.05
Ce210.n_phi_u = 50


Ce211 = lotus.SquareCell(pitch=1.26, name="Cell 211")
Ce211.circles = [rad_fuel, rad_gap, rad_clad]
Ce211.materials = [materials['UO2_211'], materials['Gap_211'], materials['Clad_211'], materials['Water_211']]
Ce211.spatial_modes = spat_modes
Ce211.d_u = 0.05
Ce211.n_phi_u = 50


Ce212 = lotus.SquareCell(pitch=1.26, name="Cell 212")
Ce212.circles = [rad_fuel, rad_gap, rad_clad]
Ce212.materials = [materials['UO2_212'], materials['Gap_212'], materials['Clad_212'], materials['Water_212']]
Ce212.spatial_modes = spat_modes
Ce212.d_u = 0.05
Ce212.n_phi_u = 50


Ce213 = lotus.SquareCell(pitch=1.26, name="Cell 213")
Ce213.circles = [rad_fuel, rad_gap, rad_clad]
Ce213.materials = [materials['UO2_213'], materials['Gap_213'], materials['Clad_213'], materials['Water_213']]
Ce213.spatial_modes = spat_modes
Ce213.d_u = 0.05
Ce213.n_phi_u = 50


Ce214 = lotus.SquareCell(pitch=1.26, name="Cell 214")
Ce214.circles = [rad_fuel, rad_gap, rad_clad]
Ce214.materials = [materials['UO2_214'], materials['Gap_214'], materials['Clad_214'], materials['Water_214']]
Ce214.spatial_modes = spat_modes
Ce214.d_u = 0.05
Ce214.n_phi_u = 50


Ce215 = lotus.SquareCell(pitch=1.26, name="Cell 215")
Ce215.circles = [rad_fuel, rad_gap, rad_clad]
Ce215.materials = [materials['UO2_215'], materials['Gap_215'], materials['Clad_215'], materials['Water_215']]
Ce215.spatial_modes = spat_modes
Ce215.d_u = 0.05
Ce215.n_phi_u = 50


Ce216 = lotus.SquareCell(pitch=1.26, name="Cell 216")
Ce216.circles = [rad_fuel, rad_gap, rad_clad]
Ce216.materials = [materials['UO2_216'], materials['Gap_216'], materials['Clad_216'], materials['Water_216']]
Ce216.spatial_modes = spat_modes
Ce216.d_u = 0.05
Ce216.n_phi_u = 50


Ce217 = lotus.SquareCell(pitch=1.26, name="Cell 217")
Ce217.circles = [rad_fuel, rad_gap, rad_clad]
Ce217.materials = [materials['UO2_217'], materials['Gap_217'], materials['Clad_217'], materials['Water_217']]
Ce217.spatial_modes = spat_modes
Ce217.d_u = 0.05
Ce217.n_phi_u = 50


Ce218 = lotus.SquareCell(pitch=1.26, name="Cell 218")
Ce218.circles = [rad_fuel, rad_gap, rad_clad]
Ce218.materials = [materials['UO2_218'], materials['Gap_218'], materials['Clad_218'], materials['Water_218']]
Ce218.spatial_modes = spat_modes
Ce218.d_u = 0.05
Ce218.n_phi_u = 50


Ce219 = lotus.SquareCell(pitch=1.26, name="Cell 219")
Ce219.circles = [rad_fuel, rad_gap, rad_clad]
Ce219.materials = [materials['UO2_219'], materials['Gap_219'], materials['Clad_219'], materials['Water_219']]
Ce219.spatial_modes = spat_modes
Ce219.d_u = 0.05
Ce219.n_phi_u = 50


Ce220 = lotus.SquareCell(pitch=1.26, name="Cell 220")
Ce220.circles = [rad_fuel, rad_gap, rad_clad]
Ce220.materials = [materials['UO2_220'], materials['Gap_220'], materials['Clad_220'], materials['Water_220']]
Ce220.spatial_modes = spat_modes
Ce220.d_u = 0.05
Ce220.n_phi_u = 50


Ce221 = lotus.SquareCell(pitch=1.26, name="Cell 221")
Ce221.circles = [rad_fuel, rad_gap, rad_clad]
Ce221.materials = [materials['UO2_221'], materials['Gap_221'], materials['Clad_221'], materials['Water_221']]
Ce221.spatial_modes = spat_modes
Ce221.d_u = 0.05
Ce221.n_phi_u = 50


Ce222 = lotus.SquareCell(pitch=1.26, name="Cell 222")
Ce222.circles = [rad_fuel, rad_gap, rad_clad]
Ce222.materials = [materials['UO2_222'], materials['Gap_222'], materials['Clad_222'], materials['Water_222']]
Ce222.spatial_modes = spat_modes
Ce222.d_u = 0.05
Ce222.n_phi_u = 50


Ce223 = lotus.SquareCell(pitch=1.26, name="Cell 223")
Ce223.circles = [rad_fuel, rad_gap, rad_clad]
Ce223.materials = [materials['UO2_223'], materials['Gap_223'], materials['Clad_223'], materials['Water_223']]
Ce223.spatial_modes = spat_modes
Ce223.d_u = 0.05
Ce223.n_phi_u = 50


Ce224 = lotus.SquareCell(pitch=1.26, name="Cell 224")
Ce224.circles = [rad_fuel, rad_gap, rad_clad]
Ce224.materials = [materials['UO2_224'], materials['Gap_224'], materials['Clad_224'], materials['Water_224']]
Ce224.spatial_modes = spat_modes
Ce224.d_u = 0.05
Ce224.n_phi_u = 50


Ce225 = lotus.SquareCell(pitch=1.26, name="Cell 225")
Ce225.circles = [rad_guide1, rad_guide2]
Ce225.materials = [materials['Water_225'], materials['Clad_225'], materials['Water_225']]
Ce225.spatial_modes = spat_modes_2
Ce225.d_u = 0.05
Ce225.n_phi_u = 50


Ce226 = lotus.SquareCell(pitch=1.26, name="Cell 226")
Ce226.circles = [rad_fuel, rad_gap, rad_clad]
Ce226.materials = [materials['UO2_226'], materials['Gap_226'], materials['Clad_226'], materials['Water_226']]
Ce226.spatial_modes = spat_modes
Ce226.d_u = 0.05
Ce226.n_phi_u = 50


Ce227 = lotus.SquareCell(pitch=1.26, name="Cell 227")
Ce227.circles = [rad_fuel, rad_gap, rad_clad]
Ce227.materials = [materials['UO2_227'], materials['Gap_227'], materials['Clad_227'], materials['Water_227']]
Ce227.spatial_modes = spat_modes
Ce227.d_u = 0.05
Ce227.n_phi_u = 50


Ce228 = lotus.SquareCell(pitch=1.26, name="Cell 228")
Ce228.circles = [rad_fuel, rad_gap, rad_clad]
Ce228.materials = [materials['UO2_228'], materials['Gap_228'], materials['Clad_228'], materials['Water_228']]
Ce228.spatial_modes = spat_modes
Ce228.d_u = 0.05
Ce228.n_phi_u = 50


Ce229 = lotus.SquareCell(pitch=1.26, name="Cell 229")
Ce229.circles = [rad_fuel, rad_gap, rad_clad]
Ce229.materials = [materials['UO2_229'], materials['Gap_229'], materials['Clad_229'], materials['Water_229']]
Ce229.spatial_modes = spat_modes
Ce229.d_u = 0.05
Ce229.n_phi_u = 50


Ce230 = lotus.SquareCell(pitch=1.26, name="Cell 230")
Ce230.circles = [rad_fuel, rad_gap, rad_clad]
Ce230.materials = [materials['UO2_230'], materials['Gap_230'], materials['Clad_230'], materials['Water_230']]
Ce230.spatial_modes = spat_modes
Ce230.d_u = 0.05
Ce230.n_phi_u = 50


Ce231 = lotus.SquareCell(pitch=1.26, name="Cell 231")
Ce231.circles = [rad_fuel, rad_gap, rad_clad]
Ce231.materials = [materials['UO2_231'], materials['Gap_231'], materials['Clad_231'], materials['Water_231']]
Ce231.spatial_modes = spat_modes
Ce231.d_u = 0.05
Ce231.n_phi_u = 50


Ce232 = lotus.SquareCell(pitch=1.26, name="Cell 232")
Ce232.circles = [rad_fuel, rad_gap, rad_clad]
Ce232.materials = [materials['UO2_232'], materials['Gap_232'], materials['Clad_232'], materials['Water_232']]
Ce232.spatial_modes = spat_modes
Ce232.d_u = 0.05
Ce232.n_phi_u = 50


Ce233 = lotus.SquareCell(pitch=1.26, name="Cell 233")
Ce233.circles = [rad_fuel, rad_gap, rad_clad]
Ce233.materials = [materials['UO2_233'], materials['Gap_233'], materials['Clad_233'], materials['Water_233']]
Ce233.spatial_modes = spat_modes
Ce233.d_u = 0.05
Ce233.n_phi_u = 50


Ce234 = lotus.SquareCell(pitch=1.26, name="Cell 234")
Ce234.circles = [rad_fuel, rad_gap, rad_clad]
Ce234.materials = [materials['UO2_234'], materials['Gap_234'], materials['Clad_234'], materials['Water_234']]
Ce234.spatial_modes = spat_modes
Ce234.d_u = 0.05
Ce234.n_phi_u = 50


Ce235 = lotus.SquareCell(pitch=1.26, name="Cell 235")
Ce235.circles = [rad_guide1, rad_guide2]
Ce235.materials = [materials['Water_235'], materials['Clad_235'], materials['Water_235']]
Ce235.spatial_modes = spat_modes_2
Ce235.d_u = 0.05
Ce235.n_phi_u = 50


Ce236 = lotus.SquareCell(pitch=1.26, name="Cell 236")
Ce236.circles = [rad_fuel, rad_gap, rad_clad]
Ce236.materials = [materials['UO2_236'], materials['Gap_236'], materials['Clad_236'], materials['Water_236']]
Ce236.spatial_modes = spat_modes
Ce236.d_u = 0.05
Ce236.n_phi_u = 50


Ce237 = lotus.SquareCell(pitch=1.26, name="Cell 237")
Ce237.circles = [rad_fuel, rad_gap, rad_clad]
Ce237.materials = [materials['UO2_237'], materials['Gap_237'], materials['Clad_237'], materials['Water_237']]
Ce237.spatial_modes = spat_modes
Ce237.d_u = 0.05
Ce237.n_phi_u = 50


Ce238 = lotus.SquareCell(pitch=1.26, name="Cell 238")
Ce238.circles = [rad_fuel, rad_gap, rad_clad]
Ce238.materials = [materials['UO2_238'], materials['Gap_238'], materials['Clad_238'], materials['Water_238']]
Ce238.spatial_modes = spat_modes
Ce238.d_u = 0.05
Ce238.n_phi_u = 50


Ce239 = lotus.SquareCell(pitch=1.26, name="Cell 239")
Ce239.circles = [rad_fuel, rad_gap, rad_clad]
Ce239.materials = [materials['UO2_239'], materials['Gap_239'], materials['Clad_239'], materials['Water_239']]
Ce239.spatial_modes = spat_modes
Ce239.d_u = 0.05
Ce239.n_phi_u = 50


Ce240 = lotus.SquareCell(pitch=1.26, name="Cell 240")
Ce240.circles = [rad_fuel, rad_gap, rad_clad]
Ce240.materials = [materials['UO2_240'], materials['Gap_240'], materials['Clad_240'], materials['Water_240']]
Ce240.spatial_modes = spat_modes
Ce240.d_u = 0.05
Ce240.n_phi_u = 50


Ce241 = lotus.SquareCell(pitch=1.26, name="Cell 241")
Ce241.circles = [rad_fuel, rad_gap, rad_clad]
Ce241.materials = [materials['UO2_241'], materials['Gap_241'], materials['Clad_241'], materials['Water_241']]
Ce241.spatial_modes = spat_modes
Ce241.d_u = 0.05
Ce241.n_phi_u = 50


Ce242 = lotus.SquareCell(pitch=1.26, name="Cell 242")
Ce242.circles = [rad_fuel, rad_gap, rad_clad]
Ce242.materials = [materials['UO2_242'], materials['Gap_242'], materials['Clad_242'], materials['Water_242']]
Ce242.spatial_modes = spat_modes
Ce242.d_u = 0.05
Ce242.n_phi_u = 50


Ce243 = lotus.SquareCell(pitch=1.26, name="Cell 243")
Ce243.circles = [rad_fuel, rad_gap, rad_clad]
Ce243.materials = [materials['UO2_243'], materials['Gap_243'], materials['Clad_243'], materials['Water_243']]
Ce243.spatial_modes = spat_modes
Ce243.d_u = 0.05
Ce243.n_phi_u = 50


Ce244 = lotus.SquareCell(pitch=1.26, name="Cell 244")
Ce244.circles = [rad_guide1, rad_guide2]
Ce244.materials = [materials['Water_244'], materials['Clad_244'], materials['Water_244']]
Ce244.spatial_modes = spat_modes_2
Ce244.d_u = 0.05
Ce244.n_phi_u = 50


Ce245 = lotus.SquareCell(pitch=1.26, name="Cell 245")
Ce245.circles = [rad_fuel, rad_gap, rad_clad]
Ce245.materials = [materials['UO2_245'], materials['Gap_245'], materials['Clad_245'], materials['Water_245']]
Ce245.spatial_modes = spat_modes
Ce245.d_u = 0.05
Ce245.n_phi_u = 50


Ce246 = lotus.SquareCell(pitch=1.26, name="Cell 246")
Ce246.circles = [rad_fuel, rad_gap, rad_clad]
Ce246.materials = [materials['UO2_246'], materials['Gap_246'], materials['Clad_246'], materials['Water_246']]
Ce246.spatial_modes = spat_modes
Ce246.d_u = 0.05
Ce246.n_phi_u = 50


Ce247 = lotus.SquareCell(pitch=1.26, name="Cell 247")
Ce247.circles = [rad_guide1, rad_guide2]
Ce247.materials = [materials['Water_247'], materials['Clad_247'], materials['Water_247']]
Ce247.spatial_modes = spat_modes_2
Ce247.d_u = 0.05
Ce247.n_phi_u = 50


Ce248 = lotus.SquareCell(pitch=1.26, name="Cell 248")
Ce248.circles = [rad_fuel, rad_gap, rad_clad]
Ce248.materials = [materials['UO2_248'], materials['Gap_248'], materials['Clad_248'], materials['Water_248']]
Ce248.spatial_modes = spat_modes
Ce248.d_u = 0.05
Ce248.n_phi_u = 50


Ce249 = lotus.SquareCell(pitch=1.26, name="Cell 249")
Ce249.circles = [rad_fuel, rad_gap, rad_clad]
Ce249.materials = [materials['UO2_249'], materials['Gap_249'], materials['Clad_249'], materials['Water_249']]
Ce249.spatial_modes = spat_modes
Ce249.d_u = 0.05
Ce249.n_phi_u = 50


Ce250 = lotus.SquareCell(pitch=1.26, name="Cell 250")
Ce250.circles = [rad_guide1, rad_guide2]
Ce250.materials = [materials['Water_250'], materials['Clad_250'], materials['Water_250']]
Ce250.spatial_modes = spat_modes_2
Ce250.d_u = 0.05
Ce250.n_phi_u = 50


Ce251 = lotus.SquareCell(pitch=1.26, name="Cell 251")
Ce251.circles = [rad_fuel, rad_gap, rad_clad]
Ce251.materials = [materials['UO2_251'], materials['Gap_251'], materials['Clad_251'], materials['Water_251']]
Ce251.spatial_modes = spat_modes
Ce251.d_u = 0.05
Ce251.n_phi_u = 50


Ce252 = lotus.SquareCell(pitch=1.26, name="Cell 252")
Ce252.circles = [rad_fuel, rad_gap, rad_clad]
Ce252.materials = [materials['UO2_252'], materials['Gap_252'], materials['Clad_252'], materials['Water_252']]
Ce252.spatial_modes = spat_modes
Ce252.d_u = 0.05
Ce252.n_phi_u = 50


Ce253 = lotus.SquareCell(pitch=1.26, name="Cell 253")
Ce253.circles = [rad_fuel, rad_gap, rad_clad]
Ce253.materials = [materials['UO2_253'], materials['Gap_253'], materials['Clad_253'], materials['Water_253']]
Ce253.spatial_modes = spat_modes
Ce253.d_u = 0.05
Ce253.n_phi_u = 50


Ce254 = lotus.SquareCell(pitch=1.26, name="Cell 254")
Ce254.circles = [rad_fuel, rad_gap, rad_clad]
Ce254.materials = [materials['UO2_254'], materials['Gap_254'], materials['Clad_254'], materials['Water_254']]
Ce254.spatial_modes = spat_modes
Ce254.d_u = 0.05
Ce254.n_phi_u = 50


Ce255 = lotus.SquareCell(pitch=1.26, name="Cell 255")
Ce255.circles = [rad_fuel, rad_gap, rad_clad]
Ce255.materials = [materials['UO2_255'], materials['Gap_255'], materials['Clad_255'], materials['Water_255']]
Ce255.spatial_modes = spat_modes
Ce255.d_u = 0.05
Ce255.n_phi_u = 50


Ce256 = lotus.SquareCell(pitch=1.26, name="Cell 256")
Ce256.circles = [rad_fuel, rad_gap, rad_clad]
Ce256.materials = [materials['UO2_256'], materials['Gap_256'], materials['Clad_256'], materials['Water_256']]
Ce256.spatial_modes = spat_modes
Ce256.d_u = 0.05
Ce256.n_phi_u = 50


Ce257 = lotus.SquareCell(pitch=1.26, name="Cell 257")
Ce257.circles = [rad_fuel, rad_gap, rad_clad]
Ce257.materials = [materials['UO2_257'], materials['Gap_257'], materials['Clad_257'], materials['Water_257']]
Ce257.spatial_modes = spat_modes
Ce257.d_u = 0.05
Ce257.n_phi_u = 50


Ce258 = lotus.SquareCell(pitch=1.26, name="Cell 258")
Ce258.circles = [rad_fuel, rad_gap, rad_clad]
Ce258.materials = [materials['UO2_258'], materials['Gap_258'], materials['Clad_258'], materials['Water_258']]
Ce258.spatial_modes = spat_modes
Ce258.d_u = 0.05
Ce258.n_phi_u = 50


Ce259 = lotus.SquareCell(pitch=1.26, name="Cell 259")
Ce259.circles = [rad_fuel, rad_gap, rad_clad]
Ce259.materials = [materials['UO2_259'], materials['Gap_259'], materials['Clad_259'], materials['Water_259']]
Ce259.spatial_modes = spat_modes
Ce259.d_u = 0.05
Ce259.n_phi_u = 50


Ce260 = lotus.SquareCell(pitch=1.26, name="Cell 260")
Ce260.circles = [rad_fuel, rad_gap, rad_clad]
Ce260.materials = [materials['UO2_260'], materials['Gap_260'], materials['Clad_260'], materials['Water_260']]
Ce260.spatial_modes = spat_modes
Ce260.d_u = 0.05
Ce260.n_phi_u = 50


Ce261 = lotus.SquareCell(pitch=1.26, name="Cell 261")
Ce261.circles = [rad_fuel, rad_gap, rad_clad]
Ce261.materials = [materials['UO2_261'], materials['Gap_261'], materials['Clad_261'], materials['Water_261']]
Ce261.spatial_modes = spat_modes
Ce261.d_u = 0.05
Ce261.n_phi_u = 50


Ce262 = lotus.SquareCell(pitch=1.26, name="Cell 262")
Ce262.circles = [rad_fuel, rad_gap, rad_clad]
Ce262.materials = [materials['UO2_262'], materials['Gap_262'], materials['Clad_262'], materials['Water_262']]
Ce262.spatial_modes = spat_modes
Ce262.d_u = 0.05
Ce262.n_phi_u = 50


Ce263 = lotus.SquareCell(pitch=1.26, name="Cell 263")
Ce263.circles = [rad_fuel, rad_gap, rad_clad]
Ce263.materials = [materials['UO2_263'], materials['Gap_263'], materials['Clad_263'], materials['Water_263']]
Ce263.spatial_modes = spat_modes
Ce263.d_u = 0.05
Ce263.n_phi_u = 50


Ce264 = lotus.SquareCell(pitch=1.26, name="Cell 264")
Ce264.circles = [rad_fuel, rad_gap, rad_clad]
Ce264.materials = [materials['UO2_264'], materials['Gap_264'], materials['Clad_264'], materials['Water_264']]
Ce264.spatial_modes = spat_modes
Ce264.d_u = 0.05
Ce264.n_phi_u = 50


Ce265 = lotus.SquareCell(pitch=1.26, name="Cell 265")
Ce265.circles = [rad_fuel, rad_gap, rad_clad]
Ce265.materials = [materials['UO2_265'], materials['Gap_265'], materials['Clad_265'], materials['Water_265']]
Ce265.spatial_modes = spat_modes
Ce265.d_u = 0.05
Ce265.n_phi_u = 50


Ce266 = lotus.SquareCell(pitch=1.26, name="Cell 266")
Ce266.circles = [rad_fuel, rad_gap, rad_clad]
Ce266.materials = [materials['UO2_266'], materials['Gap_266'], materials['Clad_266'], materials['Water_266']]
Ce266.spatial_modes = spat_modes
Ce266.d_u = 0.05
Ce266.n_phi_u = 50


Ce267 = lotus.SquareCell(pitch=1.26, name="Cell 267")
Ce267.circles = [rad_fuel, rad_gap, rad_clad]
Ce267.materials = [materials['UO2_267'], materials['Gap_267'], materials['Clad_267'], materials['Water_267']]
Ce267.spatial_modes = spat_modes
Ce267.d_u = 0.05
Ce267.n_phi_u = 50


Ce268 = lotus.SquareCell(pitch=1.26, name="Cell 268")
Ce268.circles = [rad_fuel, rad_gap, rad_clad]
Ce268.materials = [materials['UO2_268'], materials['Gap_268'], materials['Clad_268'], materials['Water_268']]
Ce268.spatial_modes = spat_modes
Ce268.d_u = 0.05
Ce268.n_phi_u = 50


Ce269 = lotus.SquareCell(pitch=1.26, name="Cell 269")
Ce269.circles = [rad_fuel, rad_gap, rad_clad]
Ce269.materials = [materials['UO2_269'], materials['Gap_269'], materials['Clad_269'], materials['Water_269']]
Ce269.spatial_modes = spat_modes
Ce269.d_u = 0.05
Ce269.n_phi_u = 50


Ce270 = lotus.SquareCell(pitch=1.26, name="Cell 270")
Ce270.circles = [rad_fuel, rad_gap, rad_clad]
Ce270.materials = [materials['UO2_270'], materials['Gap_270'], materials['Clad_270'], materials['Water_270']]
Ce270.spatial_modes = spat_modes
Ce270.d_u = 0.05
Ce270.n_phi_u = 50


Ce271 = lotus.SquareCell(pitch=1.26, name="Cell 271")
Ce271.circles = [rad_fuel, rad_gap, rad_clad]
Ce271.materials = [materials['UO2_271'], materials['Gap_271'], materials['Clad_271'], materials['Water_271']]
Ce271.spatial_modes = spat_modes
Ce271.d_u = 0.05
Ce271.n_phi_u = 50


Ce272 = lotus.SquareCell(pitch=1.26, name="Cell 272")
Ce272.circles = [rad_fuel, rad_gap, rad_clad]
Ce272.materials = [materials['UO2_272'], materials['Gap_272'], materials['Clad_272'], materials['Water_272']]
Ce272.spatial_modes = spat_modes
Ce272.d_u = 0.05
Ce272.n_phi_u = 50


Ce273 = lotus.SquareCell(pitch=1.26, name="Cell 273")
Ce273.circles = [rad_fuel, rad_gap, rad_clad]
Ce273.materials = [materials['UO2_273'], materials['Gap_273'], materials['Clad_273'], materials['Water_273']]
Ce273.spatial_modes = spat_modes
Ce273.d_u = 0.05
Ce273.n_phi_u = 50


Ce274 = lotus.SquareCell(pitch=1.26, name="Cell 274")
Ce274.circles = [rad_fuel, rad_gap, rad_clad]
Ce274.materials = [materials['UO2_274'], materials['Gap_274'], materials['Clad_274'], materials['Water_274']]
Ce274.spatial_modes = spat_modes
Ce274.d_u = 0.05
Ce274.n_phi_u = 50


Ce275 = lotus.SquareCell(pitch=1.26, name="Cell 275")
Ce275.circles = [rad_fuel, rad_gap, rad_clad]
Ce275.materials = [materials['UO2_275'], materials['Gap_275'], materials['Clad_275'], materials['Water_275']]
Ce275.spatial_modes = spat_modes
Ce275.d_u = 0.05
Ce275.n_phi_u = 50


Ce276 = lotus.SquareCell(pitch=1.26, name="Cell 276")
Ce276.circles = [rad_fuel, rad_gap, rad_clad]
Ce276.materials = [materials['UO2_276'], materials['Gap_276'], materials['Clad_276'], materials['Water_276']]
Ce276.spatial_modes = spat_modes
Ce276.d_u = 0.05
Ce276.n_phi_u = 50


Ce277 = lotus.SquareCell(pitch=1.26, name="Cell 277")
Ce277.circles = [rad_fuel, rad_gap, rad_clad]
Ce277.materials = [materials['UO2_277'], materials['Gap_277'], materials['Clad_277'], materials['Water_277']]
Ce277.spatial_modes = spat_modes
Ce277.d_u = 0.05
Ce277.n_phi_u = 50


Ce278 = lotus.SquareCell(pitch=1.26, name="Cell 278")
Ce278.circles = [rad_fuel, rad_gap, rad_clad]
Ce278.materials = [materials['UO2_278'], materials['Gap_278'], materials['Clad_278'], materials['Water_278']]
Ce278.spatial_modes = spat_modes
Ce278.d_u = 0.05
Ce278.n_phi_u = 50


Ce279 = lotus.SquareCell(pitch=1.26, name="Cell 279")
Ce279.circles = [rad_fuel, rad_gap, rad_clad]
Ce279.materials = [materials['UO2_279'], materials['Gap_279'], materials['Clad_279'], materials['Water_279']]
Ce279.spatial_modes = spat_modes
Ce279.d_u = 0.05
Ce279.n_phi_u = 50


Ce280 = lotus.SquareCell(pitch=1.26, name="Cell 280")
Ce280.circles = [rad_fuel, rad_gap, rad_clad]
Ce280.materials = [materials['UO2_280'], materials['Gap_280'], materials['Clad_280'], materials['Water_280']]
Ce280.spatial_modes = spat_modes
Ce280.d_u = 0.05
Ce280.n_phi_u = 50


Ce281 = lotus.SquareCell(pitch=1.26, name="Cell 281")
Ce281.circles = [rad_fuel, rad_gap, rad_clad]
Ce281.materials = [materials['UO2_281'], materials['Gap_281'], materials['Clad_281'], materials['Water_281']]
Ce281.spatial_modes = spat_modes
Ce281.d_u = 0.05
Ce281.n_phi_u = 50


Ce282 = lotus.SquareCell(pitch=1.26, name="Cell 282")
Ce282.circles = [rad_fuel, rad_gap, rad_clad]
Ce282.materials = [materials['UO2_282'], materials['Gap_282'], materials['Clad_282'], materials['Water_282']]
Ce282.spatial_modes = spat_modes
Ce282.d_u = 0.05
Ce282.n_phi_u = 50


Ce283 = lotus.SquareCell(pitch=1.26, name="Cell 283")
Ce283.circles = [rad_fuel, rad_gap, rad_clad]
Ce283.materials = [materials['UO2_283'], materials['Gap_283'], materials['Clad_283'], materials['Water_283']]
Ce283.spatial_modes = spat_modes
Ce283.d_u = 0.05
Ce283.n_phi_u = 50


Ce284 = lotus.SquareCell(pitch=1.26, name="Cell 284")
Ce284.circles = [rad_fuel, rad_gap, rad_clad]
Ce284.materials = [materials['UO2_284'], materials['Gap_284'], materials['Clad_284'], materials['Water_284']]
Ce284.spatial_modes = spat_modes
Ce284.d_u = 0.05
Ce284.n_phi_u = 50


Ce285 = lotus.SquareCell(pitch=1.26, name="Cell 285")
Ce285.circles = [rad_fuel, rad_gap, rad_clad]
Ce285.materials = [materials['UO2_285'], materials['Gap_285'], materials['Clad_285'], materials['Water_285']]
Ce285.spatial_modes = spat_modes
Ce285.d_u = 0.05
Ce285.n_phi_u = 50


Ce286 = lotus.SquareCell(pitch=1.26, name="Cell 286")
Ce286.circles = [rad_fuel, rad_gap, rad_clad]
Ce286.materials = [materials['UO2_286'], materials['Gap_286'], materials['Clad_286'], materials['Water_286']]
Ce286.spatial_modes = spat_modes
Ce286.d_u = 0.05
Ce286.n_phi_u = 50


Ce287 = lotus.SquareCell(pitch=1.26, name="Cell 287")
Ce287.circles = [rad_fuel, rad_gap, rad_clad]
Ce287.materials = [materials['UO2_287'], materials['Gap_287'], materials['Clad_287'], materials['Water_287']]
Ce287.spatial_modes = spat_modes
Ce287.d_u = 0.05
Ce287.n_phi_u = 50


Ce288 = lotus.SquareCell(pitch=1.26, name="Cell 288")
Ce288.circles = [rad_fuel, rad_gap, rad_clad]
Ce288.materials = [materials['UO2_288'], materials['Gap_288'], materials['Clad_288'], materials['Water_288']]
Ce288.spatial_modes = spat_modes
Ce288.d_u = 0.05
Ce288.n_phi_u = 50


Ce289 = lotus.SquareCell(pitch=1.26, name="Cell 289")
Ce289.circles = [rad_fuel, rad_gap, rad_clad]
Ce289.materials = [materials['UO2_289'], materials['Gap_289'], materials['Clad_289'], materials['Water_289']]
Ce289.spatial_modes = spat_modes
Ce289.d_u = 0.05
Ce289.n_phi_u = 50


assmb_lat = lotus.SquareLattice()
assmb_lat.n_cols = 17
assmb_lat.n_rows = 17
assmb_lat.set_objects(np.array([[Ce1, Ce2, Ce3, Ce4, Ce5, Ce6, Ce7, Ce8, Ce9, Ce10, Ce11, Ce12, Ce13, Ce14, Ce15, Ce16, Ce17],
                                [Ce18, Ce19, Ce20, Ce21, Ce22, Ce23, Ce24, Ce25, Ce26, Ce27, Ce28, Ce29, Ce30, Ce31, Ce32, Ce33, Ce34],
                                [Ce35, Ce36, Ce37, Ce38, Ce39, Ce40, Ce41, Ce42, Ce43, Ce44, Ce45, Ce46, Ce47, Ce48, Ce49, Ce50, Ce51],
                                [Ce52, Ce53, Ce54, Ce55, Ce56, Ce57, Ce58, Ce59, Ce60, Ce61, Ce62, Ce63, Ce64, Ce65, Ce66, Ce67, Ce68],
                                [Ce69, Ce70, Ce71, Ce72, Ce73, Ce74, Ce75, Ce76, Ce77, Ce78, Ce79, Ce80, Ce81, Ce82, Ce83, Ce84, Ce85],
                                [Ce86, Ce87, Ce88, Ce89, Ce90, Ce91, Ce92, Ce93, Ce94, Ce95, Ce96, Ce97, Ce98, Ce99, Ce100, Ce101, Ce102],
                                [Ce103, Ce104, Ce105, Ce106, Ce107, Ce108, Ce109, Ce110, Ce111, Ce112, Ce113, Ce114, Ce115, Ce116, Ce117, Ce118, Ce119],
                                [Ce120, Ce121, Ce122, Ce123, Ce124, Ce125, Ce126, Ce127, Ce128, Ce129, Ce130, Ce131, Ce132, Ce133, Ce134, Ce135, Ce136],
                                [Ce137, Ce138, Ce139, Ce140, Ce141, Ce142, Ce143, Ce144, Ce145, Ce146, Ce147, Ce148, Ce149, Ce150, Ce151, Ce152, Ce153],
                                [Ce154, Ce155, Ce156, Ce157, Ce158, Ce159, Ce160, Ce161, Ce162, Ce163, Ce164, Ce165, Ce166, Ce167, Ce168, Ce169, Ce170],
                                [Ce171, Ce172, Ce173, Ce174, Ce175, Ce176, Ce177, Ce178, Ce179, Ce180, Ce181, Ce182, Ce183, Ce184, Ce185, Ce186, Ce187],
                                [Ce188, Ce189, Ce190, Ce191, Ce192, Ce193, Ce194, Ce195, Ce196, Ce197, Ce198, Ce199, Ce200, Ce201, Ce202, Ce203, Ce204],
                                [Ce205, Ce206, Ce207, Ce208, Ce209, Ce210, Ce211, Ce212, Ce213, Ce214, Ce215, Ce216, Ce217, Ce218, Ce219, Ce220, Ce221],
                                [Ce222, Ce223, Ce224, Ce225, Ce226, Ce227, Ce228, Ce229, Ce230, Ce231, Ce232, Ce233, Ce234, Ce235, Ce236, Ce237, Ce238],
                                [Ce239, Ce240, Ce241, Ce242, Ce243, Ce244, Ce245, Ce246, Ce247, Ce248, Ce249, Ce250, Ce251, Ce252, Ce253, Ce254, Ce255],
                                [Ce256, Ce257, Ce258, Ce259, Ce260, Ce261, Ce262, Ce263, Ce264, Ce265, Ce266, Ce267, Ce268, Ce269, Ce270, Ce271, Ce272],
                                [Ce273, Ce274, Ce275, Ce276, Ce277, Ce278, Ce279, Ce280, Ce281, Ce282, Ce283, Ce284, Ce285, Ce286, Ce287, Ce288, Ce289]]))

assmb = lotus.Assembly(name="Mini assembly")
assmb.set_lattice(assmb_lat)
assmb.pitch = 1.26 * 17

core_lat = lotus.SquareLattice()
core_lat.n_cols = 1
core_lat.n_rows = 1
core_lat.set_objects(np.array([[assmb]]))

core = lotus.Geometry()
core.set_lattice(core_lat)
core.d_seg = 0.9
core.n_phi = 12
core.n_theta = 3
core.symmetry = 360
# Setting up albedos (2 groups, 4 sides)
#ALBEDO_COUPLING_START
albedo = np.array([[3.30754E-01, 1.00000E+00, 1.03177E+00,8.32174E-01],[1.37441E+00, 1.00000E+00, 9.50643E-01, 9.00704E-01]])
#ALBEDO_COUPLING_END
core.set_albedos(albedo=albedo, kind="side")

opt = lotus.Options()
opt.eps_k = 1.0e-6
opt.set_iteration_scheme_helios()
opt.verbosity = 0

model = lotus.Model(core, opt)

if plot:
    # Plot materials
    plotter.plot_materials(model=model, gridsize=1000)
    # Plot cells
    plotter.plot_cells(geometry=model, gridsize=1000)

model.build_model()
model.run_model()

eff_mult_fact= model.get_keff()
output_file= open('keff4.txt','w')
eff_mult_fact=str(eff_mult_fact)
output_file.write(eff_mult_fact)
output_file.close()

fiss_rates_aver = model.get_cell_averaged_fission_rates()
np.savetxt('fissionrates4.dat',fiss_rates_aver, fmt='%1.5e')

if plot:
    # Plot results of simulations
    plotter.plot_spatial_fluxes(model=model, energy_groups=[i + 1 for i in range(core.get_num_energy_groups())])
    plotter.plot_fission_rates(model=model, norm=True)
