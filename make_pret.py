
# *********************************************************************
# FUNCTION TO GENERATE JOU FILE W/FAULTS FROM TXT FILE
#
# *********************************************************************

import numpy as np
import pandas as pd


depth_1_1=np.loadtxt('var1.txt')*1e3 #Depth of preturbation in m
pret_1_1_C=np.loadtxt('var3.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_1_0_C=np.loadtxt('var4.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_1_m1_C=np.loadtxt('var5.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_m2_C=np.loadtxt('var6.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_m1_C=np.loadtxt('var7.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_0_C=np.loadtxt('var8.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_1_C=np.loadtxt('var9.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_2_C=np.loadtxt('var10.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m3_C=np.loadtxt('var11.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m2_C=np.loadtxt('var12.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m1_C=np.loadtxt('var13.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_0_C=np.loadtxt('var14.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_1_C=np.loadtxt('var15.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_2_C=np.loadtxt('var16.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_3_C=np.loadtxt('var17.txt')*1e-2 #Amount of preturbation 1 1 #C


pret_1_1_UM=np.loadtxt('var1_UM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_1_0_UM=np.loadtxt('var2_UM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_1_m1_UM=np.loadtxt('var3_UM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_m2_UM=np.loadtxt('var4_UM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_m1_UM=np.loadtxt('var5_UM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_0_UM=np.loadtxt('var6_UM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_1_UM=np.loadtxt('var7_UM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_2_UM=np.loadtxt('var8_UM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m3_UM=np.loadtxt('var9_UM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m2_UM=np.loadtxt('var10_UM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m1_UM=np.loadtxt('var11_UM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_0_UM=np.loadtxt('var12_UM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_1_UM=np.loadtxt('var13_UM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_2_UM=np.loadtxt('var14_UM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_3_UM=np.loadtxt('var15_UM.txt')*1e-2 #Amount of preturbation 1 1 #C


pret_1_1_MM=np.loadtxt('var1_MM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_1_0_MM=np.loadtxt('var2_MM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_1_m1_MM=np.loadtxt('var3_MM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_m2_MM=np.loadtxt('var4_MM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_m1_MM=np.loadtxt('var5_MM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_0_MM=np.loadtxt('var6_MM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_1_MM=np.loadtxt('var7_MM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_2_MM=np.loadtxt('var8_MM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m3_MM=np.loadtxt('var9_MM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m2_MM=np.loadtxt('var10_MM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m1_MM=np.loadtxt('var11_MM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_0_MM=np.loadtxt('var12_MM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_1_MM=np.loadtxt('var13_MM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_2_MM=np.loadtxt('var14_MM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_3_MM=np.loadtxt('var15_MM.txt')*1e-2 #Amount of preturbation 1 1 #C

pret_1_1_LM=np.loadtxt('var1_LM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_1_0_LM=np.loadtxt('var2_LM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_1_m1_LM=np.loadtxt('var3_LM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_m2_LM=np.loadtxt('var4_LM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_m1_LM=np.loadtxt('var5_LM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_0_LM=np.loadtxt('var6_LM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_1_LM=np.loadtxt('var7_LM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_2_LM=np.loadtxt('var8_LM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m3_LM=np.loadtxt('var9_LM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m2_LM=np.loadtxt('var10_LM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m1_LM=np.loadtxt('var11_LM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_0_LM=np.loadtxt('var12_LM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_1_LM=np.loadtxt('var13_LM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_2_LM=np.loadtxt('var14_LM.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_3_LM=np.loadtxt('var15_LM.txt')*1e-2 #Amount of preturbation 1 1 #C

pret_1_1_LVZ=np.loadtxt('var1_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_1_0_LVZ=np.loadtxt('var2_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_1_m1_LVZ=np.loadtxt('var3_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_m2_LVZ=np.loadtxt('var4_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_m1_LVZ=np.loadtxt('var5_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_0_LVZ=np.loadtxt('var6_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_1_LVZ=np.loadtxt('var7_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_2_2_LVZ=np.loadtxt('var8_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m3_LVZ=np.loadtxt('var9_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m2_LVZ=np.loadtxt('var10_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_m1_LVZ=np.loadtxt('var11_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_0_LVZ=np.loadtxt('var12_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_1_LVZ=np.loadtxt('var13_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_2_LVZ=np.loadtxt('var14_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C
pret_3_3_LVZ=np.loadtxt('var15_LVZ.txt')*1e-2 #Amount of preturbation 1 1 #C




Radius=1737100.0
Spatialdb=open("ct1_spectrum_enh.dat","w")

Spatialdb.write("5	15	\n")

#LVZ

Spatialdb.write(str(330000.0)+"   "+str(330100.0)+"		\n")
Spatialdb.write("1	1	1	"+str(pret_1_1_MM)+"	0	0	\n")
Spatialdb.write("2	1	0	"+str(pret_1_0_MM)+"	0	0	\n")
Spatialdb.write("3	1	-1	"+str(pret_1_m1_MM)+"	0	0	\n")
Spatialdb.write("4	2	-2	"+str(pret_2_m2_MM)+"	0	0	\n")
Spatialdb.write("5	2	-1	"+str(pret_2_m1_MM)+"	0	0	\n")
Spatialdb.write("6	2	0	"+str(pret_2_0_MM)+"	0	0	\n")
Spatialdb.write("7	2	1	"+str(pret_2_1_MM)+"	0	0	\n")
Spatialdb.write("8	2	2	"+str(pret_2_2_MM)+"	0	0	\n")
Spatialdb.write("9	3	-3	"+str(pret_3_m3_MM)+"	0	0	\n")
Spatialdb.write("10	3	-2	"+str(pret_3_m2_MM)+"	0	0	\n")
Spatialdb.write("11	3	-1	"+str(pret_3_m1_MM)+"	0	0	\n")
Spatialdb.write("12	3	0	"+str(pret_3_0_MM)+"	0	0	\n")
Spatialdb.write("13	3	1	"+str(pret_3_1_MM)+"	0	0	\n")
Spatialdb.write("14	3	2	"+str(pret_3_2_MM)+"	0	0	\n")
Spatialdb.write("15	3	3	"+str(pret_3_3_MM)+"	0	0	\n")



#LM

Spatialdb.write(str(330100.0)+"   "+str(1003100.0)+"		\n")
Spatialdb.write("1	1	1	"+str(pret_1_1_MM)+"	0	0	\n")
Spatialdb.write("2	1	0	"+str(pret_1_0_MM)+"	0	0	\n")
Spatialdb.write("3	1	-1	"+str(pret_1_m1_MM)+"	0	0	\n")
Spatialdb.write("4	2	-2	"+str(pret_2_m2_MM)+"	0	0	\n")
Spatialdb.write("5	2	-1	"+str(pret_2_m1_MM)+"	0	0	\n")
Spatialdb.write("6	2	0	"+str(pret_2_0_MM)+"	0	0	\n")
Spatialdb.write("7	2	1	"+str(pret_2_1_MM)+"	0	0	\n")
Spatialdb.write("8	2	2	"+str(pret_2_2_MM)+"	0	0	\n")
Spatialdb.write("9	3	-3	"+str(pret_3_m3_MM)+"	0	0	\n")
Spatialdb.write("10	3	-2	"+str(pret_3_m2_MM)+"	0	0	\n")
Spatialdb.write("11	3	-1	"+str(pret_3_m1_MM)+"	0	0	\n")
Spatialdb.write("12	3	0	"+str(pret_3_0_MM)+"	0	0	\n")
Spatialdb.write("13	3	1	"+str(pret_3_1_MM)+"	0	0	\n")
Spatialdb.write("14	3	2	"+str(pret_3_2_MM)+"	0	0	\n")
Spatialdb.write("15	3	3	"+str(pret_3_3_MM)+"	0	0	\n")

##MM


Spatialdb.write(str(1003100.0)+"   "+str(1675100.0)+"		\n")
Spatialdb.write("1	1	1	"+str(pret_1_1_MM)+"	0	0	\n")
Spatialdb.write("2	1	0	"+str(pret_1_0_MM)+"	0	0	\n")
Spatialdb.write("3	1	-1	"+str(pret_1_m1_MM)+"	0	0	\n")
Spatialdb.write("4	2	-2	"+str(pret_2_m2_MM)+"	0	0	\n")
Spatialdb.write("5	2	-1	"+str(pret_2_m1_MM)+"	0	0	\n")
Spatialdb.write("6	2	0	"+str(pret_2_0_MM)+"	0	0	\n")
Spatialdb.write("7	2	1	"+str(pret_2_1_MM)+"	0	0	\n")
Spatialdb.write("8	2	2	"+str(pret_2_2_MM)+"	0	0	\n")
Spatialdb.write("9	3	-3	"+str(pret_3_m3_MM)+"	0	0	\n")
Spatialdb.write("10	3	-2	"+str(pret_3_m2_MM)+"	0	0	\n")
Spatialdb.write("11	3	-1	"+str(pret_3_m1_MM)+"	0	0	\n")
Spatialdb.write("12	3	0	"+str(pret_3_0_MM)+"	0	0	\n")
Spatialdb.write("13	3	1	"+str(pret_3_1_MM)+"	0	0	\n")
Spatialdb.write("14	3	2	"+str(pret_3_2_MM)+"	0	0	\n")
Spatialdb.write("15	3	3	"+str(pret_3_3_MM)+"	0	0	\n")


#UM
pret_1_1_MM=pret_1_1_MM-0.1684741
pret_1_0_MM=pret_1_0_MM+0.01592423
pret_1_m1_MM=pret_1_m1_MM-0.09077046
pret_2_m2_MM=pret_2_m2_MM-0.09454566
pret_2_m1_MM=pret_2_m1_MM-0.00794353
pret_2_0_MM=pret_2_0_MM+0.08672127
pret_2_1_MM=pret_2_1_MM+0.06992722
pret_2_2_MM=pret_2_2_MM-0.03165318
pret_3_m3_MM=pret_3_m3_MM-0.03032151
pret_3_m2_MM=pret_3_m2_MM+0.02854378
pret_3_m1_MM=pret_3_m1_MM-0.00058969
pret_3_0_MM=pret_3_0_MM-0.00843395
pret_3_1_MM=pret_3_1_MM+0.0434972
pret_3_2_MM=pret_3_2_MM+0.06828972
pret_3_3_MM=pret_3_3_MM+0.0532422


Spatialdb.write(str(1675100.0)+"   "+str(1703100.0 )+"		\n")
Spatialdb.write("1	1	1	"+str(pret_1_1_MM)+"	-0.18310258	-0.04068946	\n")
Spatialdb.write("2	1	0	"+str(pret_1_0_MM)+"	0.01730692	0.00384598	\n")
Spatialdb.write("3	1	-1	"+str(pret_1_m1_MM)+"	-0.09865199	-0.02192267	\n")
Spatialdb.write("4	2	-2	"+str(pret_2_m2_MM)+"	-0.102755	-0.02283444	\n")
Spatialdb.write("5	2	-1	"+str(pret_2_m1_MM)+"	-0.00863326	-0.0019185	\n")
Spatialdb.write("6	2	0	"+str(pret_2_0_MM)+"	0.09425121	0.02094471	\n")
Spatialdb.write("7	2	1	"+str(pret_2_1_MM)+"	0.07599895	0.01688866	\n")
Spatialdb.write("8	2	2	"+str(pret_2_2_MM)+"	-0.03440161	-0.0076448	\n")
Spatialdb.write("9	3	-3	"+str(pret_3_m3_MM)+"	-0.03295431	-0.00732318	\n")
Spatialdb.write("10	3	-2	"+str(pret_3_m2_MM)+"	0.03102222	0.00689383	\n")
Spatialdb.write("11	3	-1	"+str(pret_3_m1_MM)+"	-0.00064089	-0.00014242	\n")
Spatialdb.write("12	3	0	"+str(pret_3_0_MM)+"	-0.00916627	-0.00203695	\n")
Spatialdb.write("13	3	1	"+str(pret_3_1_MM)+"	0.04727403	0.01050534	\n")
Spatialdb.write("14	3	2	"+str(pret_3_2_MM)+"	0.07421927	0.01649317	\n")
Spatialdb.write("15	3	3	"+str(pret_3_3_MM)+"	0.05786518	0.01285893	\n")

#Crust
pret_1_1_C=pret_1_1_C-0.04194814 #Amount of preturbation 1 1 #C
pret_1_0_C=pret_1_0_C+0.01623984 #Amount of preturbation 1 1 #C
pret_1_m1_C=pret_1_m1_C+0.03328657 #Amount of preturbation 1 1 #C
pret_2_m2_C=pret_2_m2_C+0.02474275 #Amount of preturbation 1 1 #C
pret_2_m1_C=pret_2_m1_C+0.02017667 #Amount of preturbation 1 1 #C
pret_2_0_C=pret_2_0_C-0.03494383 #Amount of preturbation 1 1 #C
pret_2_1_C=pret_2_1_C+0.13703188 #Amount of preturbation 1 1 #C
pret_2_2_C=pret_2_2_C+0.07746865 #Amount of preturbation 1 1 #C
pret_3_m3_C=pret_3_m3_C+0.0410576 #Amount of preturbation 1 1 #C
pret_3_m2_C=pret_3_m2_C+0.01631885 #Amount of preturbation 1 1 #C
pret_3_m1_C=pret_3_m1_C-0.00159178 #Amount of preturbation 1 1 #C
pret_3_0_C=pret_3_0_C+0.05033976 #Amount of preturbation 1 1 #C
pret_3_1_C=pret_3_1_C+0.0528225 #Amount of preturbation 1 1 #C
pret_3_2_C=pret_3_2_C-0.00524213 #Amount of preturbation 1 1 #C
pret_3_3_C=pret_3_3_C+0.02997059 #Amount of preturbation 1 1 #C



Spatialdb.write(str(1703100.0 )+"   "+str(1737100.0 )+"		\n")
Spatialdb.write("1	1	1	"+str(pret_1_1_C)+"	-0.07323822	0.0878832	\n")
Spatialdb.write("2	1	0	"+str(pret_1_0_C)+"	0.02267531	-0.01046268	\n")
Spatialdb.write("3	1	-1	"+str(pret_1_m1_C)+"	0.03103993	0.04260849	\n")
Spatialdb.write("4	2	-2	"+str(pret_2_m2_C)+"	0.02154863	0.03799606	\n")
Spatialdb.write("5	2	-1	"+str(pret_2_m1_C)+"	0.02479172	0.00102756	\n")
Spatialdb.write("6	2	0	"+str(pret_2_0_C)+"	-0.02764125	-0.06524428	\n")
Spatialdb.write("7	2	1	"+str(pret_2_1_C)+"	0.18268942	-0.05241405	\n")
Spatialdb.write("8	2	2	"+str(pret_2_2_C)+"	0.09135358	0.01985622	\n")
Spatialdb.write("9	3	-3	"+str(pret_3_m3_C)+"	0.04955442	0.00580191	\n")
Spatialdb.write("10	3	-2	"+str(pret_3_m2_C)+"	0.02388243	-0.01506459	\n")
Spatialdb.write("11	3	-1	"+str(pret_3_m1_C)+"	-7.33e-006	-0.00816609	\n")
Spatialdb.write("12	3	0	"+str(pret_3_0_C)+"	0.06230645	0.00068658	\n")
Spatialdb.write("13	3	1	"+str(pret_3_1_C)+"	0.07605002	-0.04355499	\n")
Spatialdb.write("14	3	2	"+str(pret_3_2_C)+"	0.00325882	-0.0405149	\n")
Spatialdb.write("15	3	3	"+str(pret_3_3_C)+"	0.04516213	-0.03306339	\n")











