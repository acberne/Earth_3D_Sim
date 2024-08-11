

# *********************************************************************
# FUNCTION TO GENERATE JOU FILE W/FAULTS FROM TXT FILE
#
# *********************************************************************

import numpy as np
import pandas as pd

pret_c=np.loadtxt('var2.txt')*1e-2 #Crust
pret_um=np.loadtxt('var18.txt')*1e-2 #Upper Mantle
pret_mm=np.loadtxt('var19.txt')*1e-2 #Middle Mantle
pret_lm=np.loadtxt('var20.txt')*1e-2 #Upper Mantle
pret_lvz=np.loadtxt('var21.txt')*1e-2 #Middle Mantle


Example_array=np.loadtxt('ct1_example.dat')

Radius=1737100.0
Spatialdb=open("ct1.dat","w")


#Core
Spatialdb.write("	 "+str(Example_array[0,0])+"          "+str(Example_array[0,1])+"          "+str(Example_array[0,2])+"       "+str(Example_array[0,3])+"	\n")
Spatialdb.write("	 "+str(Example_array[1,0])+"          "+str(Example_array[1,1])+"          "+str(Example_array[1,2])+"       "+str(Example_array[1,3])+"	\n")


#LVZ
Spatialdb.write("	 "+str(Example_array[2,0])+"          "+str(Example_array[2,1])+"          "+str(Example_array[2,2])+"       "+str(Example_array[2,3]*(1+pret_lvz)**(1/2))+"	\n")

#Lower Mantle
Spatialdb.write("	 "+str(Example_array[3,0])+"          "+str(Example_array[3,1])+"          "+str(Example_array[3,2])+"       "+str(Example_array[3,3]*(1+pret_lm)**(1/2))+"	\n")

#Middle Mantle
Spatialdb.write("	 "+str(Example_array[4,0])+"          "+str(Example_array[4,1])+"          "+str(Example_array[4,2])+"       "+str(Example_array[4,3]*(1+pret_mm)**(1/2))+"	\n")
Spatialdb.write("	 "+str(Example_array[5,0])+"          "+str(Example_array[5,1])+"          "+str(Example_array[5,2])+"       "+str(Example_array[5,3]*(1+pret_mm)**(1/2))+"	\n")

#Upper Mantle
Spatialdb.write("	 "+str(Example_array[6,0])+"          "+str(Example_array[6,1])+"          "+str(Example_array[6,2])+"       "+str(Example_array[6,3]*(1+pret_um)**(1/2))+"	\n")
Spatialdb.write("	 "+str(Example_array[7,0])+"          "+str(Example_array[7,1])+"          "+str(Example_array[7,2])+"       "+str(Example_array[7,3]*(1+pret_um)**(1/2))+"	\n")

#Crust
Spatialdb.write("	 "+str(Example_array[8,0])+"          "+str(Example_array[8,1])+"          "+str(Example_array[8,2])+"       "+str(Example_array[8,3]*(1+pret_c)**(1/2))+"	\n")









