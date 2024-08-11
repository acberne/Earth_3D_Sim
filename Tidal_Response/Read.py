
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the .npy file
data = np.load("arr_4.npy")
data_indeces = np.load("tidal_input_coor_0724.npy")

# Display the data
density,bulk,shear=data[:,:,:,0],data[:,:,:,1],data[:,:,:,2]
radius,lat,lon=data_indeces[0,:,:,:],data_indeces[1,:,:,:],data_indeces[2,:,:,:]


#############
###Okay, let's build our model. First I am going to define the radial vectors

Radius_vec=np.zeros(len(radius[:,0,0]))
density_vec=np.zeros(len(radius[:,0,0]))
bulk_vec=np.zeros(len(radius[:,0,0]))
shear_vec=np.zeros(len(radius[:,0,0]))


for i in range(len(radius[:,0,0])):

	Radius_vec[i]=(radius[i,0,0])*1e3 #in m
	density_vec[i]=np.average(density[i,:,:]) * 1e3
	bulk_vec[i]=np.average(bulk[i,:,:])* 1e9
	shear_vec[i]=np.average(shear[i,:,:])* 1e9


vs_vec=(shear_vec/density_vec)**(1/2) 
vp_vec=((bulk_vec+(4/3)*shear_vec)/density_vec)**(1/2) 
Spatialdb=open("ct1.dat","w")
Spatialdb.write("	 "+str(240000.0  )+"          "+str(12.9*1e3)+"          "+str(11.1*1e3  )+"       "+str(3.7*1e3)+"	\n")
Spatialdb.write("	 "+str(330000.0 )+"          "+str(12.9*1e3 )+"          "+str(11.1*1e3 )+"       "+str(0.0)+"	\n")
Spatialdb.write("	 "+str(1220000.0)+"          "+str(12.9*1e3)+"          "+str(11.1*1e3)+"       "+str(3.7*1e3)+"	\n")
Spatialdb.write("	 "+str(Radius_vec[len(vs_vec)-1]-100 )+"          "+str(11.1*1e3)+"          "+str(9.0*1e3)+"       "+str(30)+"	\n")


for i in range(len(vs_vec)):

	Spatialdb.write("	 "+str(Radius_vec[len(vs_vec)-i-1])+"          "+str(density_vec[len(vs_vec)-i-1])+"          "+str(vp_vec[len(vs_vec)-i-1])+"       "+str(vs_vec[len(vs_vec)-i-1])+"	\n")


###Now for the lateral heterogeneities

import pyshtools as pysh

#for i in range(len(radius[:,0,0])):
#	density_sh=pysh.XX(density[i,:,:]) #ortho


val=60
Spatialdb=open("ct1_spectrum_enh.dat","w")
Spatialdb.write(str(int(val))+"	"+str(int(15))+"\n")

#Need lame

lambd=bulk-2*shear/3

for i in range(val):
	#density
	shape_grid=pysh.SHGrid.from_array(density[len(vs_vec)-i-1,:,:])
	shape=shape_grid.expand(normalization='ortho')
	clm_den=shape.to_array()/np.average(density[len(vs_vec)-i-1,:,:])+1e-5
	#shear
	shape_grid=pysh.SHGrid.from_array(shear[len(vs_vec)-i-1,:,:])
	shape=shape_grid.expand(normalization='ortho')
	clm_shear=shape.to_array()/np.average(shear[len(vs_vec)-i-1,:,:]) +1e-5
	#lambda
	shape_grid=pysh.SHGrid.from_array(lambd[len(vs_vec)-i-1,:,:])
	shape=shape_grid.expand(normalization='ortho')
	clm_lambd=shape.to_array()/np.average(lambd[len(vs_vec)-i-1,:,:])+1e-5
	Spatialdb.write(str(1e3*radius[len(vs_vec)-i-1,0,0])+"	"+str(1e3*radius[len(vs_vec)-i-2,0,0])+"\n")
	Spatialdb.write("1	1	1	"+str(clm_shear[0,1,1])+"	"+str(clm_lambd[0,1,1])+"	"+str(clm_den[0,1,1])+"\n")	
	Spatialdb.write("2	1	0	"+str(clm_shear[0,1,0])+"	"+str(clm_lambd[0,1,0])+"	"+str(clm_den[0,1,0])+"\n")	
	Spatialdb.write("3	1	-1	"+str(clm_shear[1,1,1])+"	"+str(clm_lambd[1,1,1])+"	"+str(clm_den[1,1,1])+"\n")	
	Spatialdb.write("4	2	-2	"+str(clm_shear[1,2,2])+"	"+str(clm_lambd[1,2,2])+"	"+str(clm_den[1,2,2])+"\n")	
	Spatialdb.write("5	2	-1	"+str(clm_shear[1,2,1])+"	"+str(clm_lambd[1,2,1])+"	"+str(clm_den[1,2,1])+"\n")	
	Spatialdb.write("6	2	0	"+str(clm_shear[0,2,0])+"	"+str(clm_lambd[0,2,0])+"	"+str(clm_den[0,2,0])+"\n")	
	Spatialdb.write("7	2	1	"+str(clm_shear[0,2,1])+"	"+str(clm_lambd[0,2,1])+"	"+str(clm_den[0,2,1])+"\n")	
	Spatialdb.write("8	2	2	"+str(clm_shear[0,2,2])+"	"+str(clm_lambd[0,2,2])+"	"+str(clm_den[0,2,2])+"\n")	
	Spatialdb.write("9	3	-3	"+str(clm_shear[1,3,3])+"	"+str(clm_lambd[1,3,3])+"	"+str(clm_den[1,3,3])+"\n")	
	Spatialdb.write("10	3	-2	"+str(clm_shear[1,3,2])+"	"+str(clm_lambd[1,3,2])+"	"+str(clm_den[1,3,2])+"\n")	
	Spatialdb.write("11	3	-1	"+str(clm_shear[1,3,1])+"	"+str(clm_lambd[1,3,1])+"	"+str(clm_den[1,3,1])+"\n")	
	Spatialdb.write("12	3	0	"+str(clm_shear[0,3,0])+"	"+str(clm_lambd[0,3,0])+"	"+str(clm_den[0,3,0])+"\n")	
	Spatialdb.write("13	3	1	"+str(clm_shear[0,3,1])+"	"+str(clm_lambd[0,3,1])+"	"+str(clm_den[0,3,1])+"\n")	
	Spatialdb.write("14	3	2	"+str(clm_shear[0,3,2])+"	"+str(clm_lambd[0,3,2])+"	"+str(clm_den[0,3,2])+"\n")	
	Spatialdb.write("15	3	3	"+str(clm_shear[0,3,3])+"	"+str(clm_lambd[0,3,3])+"	"+str(clm_den[0,3,3])+"\n")	



	
	


