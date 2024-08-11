# *********************************************************************
# FUNCTION TO GENERATE PARAMETERS
# *********************************************************************


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import pandas as pd


##We are going to import vars from the previous step

Accept_Reject=np.loadtxt('Accept_Reject.txt')

if Accept_Reject == 1:


	var1=np.loadtxt('var1.txt') # np.random.uniform((1),(1737-350)) #Depth in km of 0 variation
	var2=np.loadtxt('var2.txt') #Degree-0 variation (%)
	var3=np.loadtxt('var3.txt') #Degree-1 order 1 variation (%)
	var4=np.loadtxt('var4.txt') #Degree-1 order 0 variation (%)
	var5=np.loadtxt('var5.txt') #Degree-1 order 1 variation (%)
	var6=np.loadtxt('var6.txt') #Degree-1 order 0 variation (%)
	var7=np.loadtxt('var7.txt') #Degree-1 order 1 variation (%)
	var8=np.loadtxt('var8.txt') #Degree-1 order 0 variation (%)
	var9=np.loadtxt('var9.txt') #Degree-1 order 1 variation (%)
	var10=np.loadtxt('var10.txt') #Degree-1 order 0 variation (%)
	var11=np.loadtxt('var11.txt') #Degree-1 order 1 variation (%)
	var12=np.loadtxt('var12.txt') #Degree-1 order 0 variation (%)
	var13=np.loadtxt('var13.txt') #Degree-1 order 1 variation (%)
	var14=np.loadtxt('var14.txt') #Degree-1 order 0 variation (%)
	var15=np.loadtxt('var15.txt') #Degree-1 order 1 variation (%)
	var16=np.loadtxt('var16.txt') #Degree-1 order 0 variation (%)
	var17=np.loadtxt('var17.txt') #Degree-1 order 1 variation (%)
	var18=np.loadtxt('var18.txt') #Degree-1 order 0 variation (%)
	var19=np.loadtxt('var19.txt') #Degree-1 order 1 variation (%)
	var20=np.loadtxt('var20.txt') #Degree-1 order 0 variation (%)
	var21=np.loadtxt('var21.txt') #Degree-1 order 1 variation (%)





	np.savetxt('var1prev.txt',[var1]) # np.random.uniform((1),(1737-350)) #Depth in km of 0 variation
	np.savetxt('var2prev.txt',[var2]) #Degree-0 variation (%)
	np.savetxt('var3prev.txt',[var3]) #Degree-1 order 1 variation (%)
	np.savetxt('var4prev.txt',[var4]) #Depth in km of 1 1 and 1 0 variation
	np.savetxt('var5prev.txt',[var5]) #Degree-1 order 0 variation (%)
	np.savetxt('var6prev.txt',[var6]) #Degree-0 variation (%)
	np.savetxt('var7prev.txt',[var7]) #Degree-1 order 1 variation (%)
	np.savetxt('var8prev.txt',[var8]) #Depth in km of 1 1 and 1 0 variation
	np.savetxt('var9prev.txt',[var9]) #Degree-1 order 0 variation (%)
	np.savetxt('var10prev.txt',[var10]) #Degree-0 variation (%)
	np.savetxt('var11prev.txt',[var11]) #Degree-1 order 1 variation (%)
	np.savetxt('var12prev.txt',[var12]) #Depth in km of 1 1 and 1 0 variation
	np.savetxt('var13prev.txt',[var13]) #Degree-1 order 0 variation (%)
	np.savetxt('var14prev.txt',[var14]) #Degree-0 variation (%)
	np.savetxt('var15prev.txt',[var15]) #Degree-1 order 1 variation (%)
	np.savetxt('var16prev.txt',[var16]) #Depth in km of 1 1 and 1 0 variation
	np.savetxt('var17prev.txt',[var17]) #Degree-1 order 0 variation (%)
	np.savetxt('var18prev.txt',[var18]) #Depth in km of 1 1 and 1 0 variation
	np.savetxt('var19prev.txt',[var19]) #Degree-1 order 0 variation (%)
	np.savetxt('var20prev.txt',[var20]) #Depth in km of 1 1 and 1 0 variation
	np.savetxt('var21prev.txt',[var21]) #Degree-1 order 0 variation (%)



else: 


	var1=np.loadtxt('var1prev.txt') # np.random.uniform((1),(1737-350)) #Depth in km of 0 variation
	var2=np.loadtxt('var2prev.txt') #Degree-0 variation (%)
	var3=np.loadtxt('var3prev.txt') #Degree-1 order 1 variation (%)
	var4=np.loadtxt('var4prev.txt') #Depth in km of 1 1 and 1 0 variation
	var5=np.loadtxt('var5prev.txt') #Degree-1 order 0 variation (%)
	var6=np.loadtxt('var6prev.txt') #Degree-0 variation (%)
	var7=np.loadtxt('var7prev.txt') #Degree-1 order 1 variation (%)
	var8=np.loadtxt('var8prev.txt') #Depth in km of 1 1 and 1 0 variation
	var9=np.loadtxt('var9prev.txt') #Degree-1 order 0 variation (%)
	var10=np.loadtxt('var10prev.txt') #Degree-0 variation (%)
	var11=np.loadtxt('var11prev.txt') #Degree-1 order 1 variation (%)
	var12=np.loadtxt('var12prev.txt') #Depth in km of 1 1 and 1 0 variation
	var13=np.loadtxt('var13prev.txt') #Degree-1 order 0 variation (%)
	var14=np.loadtxt('var14prev.txt') #Degree-1 order 1 variation (%)
	var15=np.loadtxt('var15prev.txt') #Depth in km of 1 1 and 1 0 variation
	var16=np.loadtxt('var16prev.txt') #Degree-1 order 0 variation (%)
	var17=np.loadtxt('var17prev.txt') #Degree-1 order 0 variation (%)
	var18=np.loadtxt('var18prev.txt') #Degree-1 order 0 variation (%)
	var19=np.loadtxt('var19prev.txt') #Degree-1 order 0 variation (%)
	var20=np.loadtxt('var20prev.txt') #Degree-1 order 0 variation (%)
	var21=np.loadtxt('var21prev.txt') #Degree-1 order 0 variation (%)










#Select a standard deviation for each

std1=2#%
std2=0.1 #% ##Very stong tidal coupling
std3=2 #%
std4=2 #%
std5=2 #%
std6=2 #%
std7=2 #%
std8=2 #%
std9=2 #%
std10=2 #%
std11=2 #%
std12=2 #%##Very stong tidal coupling
std13=2 #%
std14=2#%##Very stong tidal coupling
std15=2 #%
std16=2 #%##Very stong tidal coupling
std17=2 #%

std18=0.1#%##Very stong tidal coupling
std19=0.1 #%

std20=0.1 #%##Very stong tidal coupling
std21=0.2 #%


def bound(varcan):
	if varcan > 100: 
		varcan = 99.9
	if varcan < -100: 
		varcan = -99.9
	return varcan


var1can=10**(np.random.normal(np.log10(var1),std1))


if var1can < 1: 
	var1can = 1
if var1can > 1737-400: 
	var1can = 1737-400


var2can=np.random.normal(var2,std2)
var2can=bound(var2can)


var3can=np.random.normal(var3,std3)
var3can=bound(var3can)

var4can=np.random.normal(var4,std4)
var4can=bound(var4can)

var5can=np.random.normal(var5,std5)
var5can=bound(var5can)

var6can=np.random.normal(var6,std6)
var6can=bound(var6can)

var7can=np.random.normal(var7,std7)
var7can=bound(var7can)

var8can=np.random.normal(var8,std8)
var8can=bound(var8can)

var9can=np.random.normal(var9,std9)
var9can=bound(var9can)

var10can=np.random.normal(var10,std10)
var10can=bound(var10can)

var11can=np.random.normal(var11,std11)
var11can=bound(var11can)

var12can=np.random.normal(var12,std12)
var12can=bound(var12can)

var13can=np.random.normal(var13,std13)
var13can=bound(var13can)

var14can=np.random.normal(var14,std14)
var14can=bound(var14can)

var15can=np.random.normal(var15,std15)
var15can=bound(var15can)

var16can=np.random.normal(var16,std16)
var16can=bound(var16can)

var17can=np.random.normal(var17,std17)
var17can=bound(var17can)



var18can=np.random.normal(var18,std18)
var18can=bound(var18can)


var19can=np.random.normal(var19,std19)
var19can=bound(var19can)


var20can=np.random.normal(var20,std20)
var20can=bound(var20can)


var21can=np.random.normal(var21,std21)
var21can=bound(var21can)




fac=0.01
count=0
while (var3can)-(var8can)+(var10can) +(var17can)> 100 or (var3can)-(var8can)+(var10can) +(var17can)<-100 or (var3can)+(var8can)-(var10can) +(var17can)> 100 or (var3can)+(var8can)-(var10can) +(var17can)<-100 or (var4can)-(var8can)+(var14can) > 100 or (var4can)-(var8can)+(var14can) <-100 or (var4can)+(var8can)+(var14can) >100 or (var4can)+(var8can)+(var14can) < - 100 or (var5can)+(var10can)-(var11can) > 100 or (var5can)+(var10can)-(var11can) < -100 or (var5can)-(var10can)-(var11can) > 100 or (var5can)-(var10can)-(var11can) < -100:

	var3can=np.random.normal(var3,std3+fac)
	var3can=bound(var3can)

	var4can=np.random.normal(var4,std4+fac)
	var4can=bound(var4can)

	var5can=np.random.normal(var5,std5+fac)
	var5can=bound(var5can)

	var8can=np.random.normal(var8,std8+fac)
	var8can=bound(var8can)

	var10can=np.random.normal(var10,std10+fac)
	var10can=bound(var10can)

	var11can=np.random.normal(var11,std11+fac)
	var11can=bound(var11can)

	var17can=np.random.normal(var17,std17+fac)
	var17can=bound(var17can)

	fac=fac+0.01
	count=count+1


print(count)







varp=np.zeros(1)
varp[0]=var1can
np.savetxt('var1.txt',varp)

varp=np.zeros(1)
varp[0]=var2can
np.savetxt('var2.txt',varp)


varp=np.zeros(1)
varp[0]=var3can
np.savetxt('var3.txt',varp)

varp=np.zeros(1)
varp[0]=var4can
np.savetxt('var4.txt',varp)

varp=np.zeros(1)
varp[0]=var5can
np.savetxt('var5.txt',varp)

#


varp=np.zeros(1)
varp[0]=var6can
np.savetxt('var6.txt',varp)


varp=np.zeros(1)
varp[0]=var7can
np.savetxt('var7.txt',varp)


varp=np.zeros(1)
varp[0]=var8can
np.savetxt('var8.txt',varp)


varp=np.zeros(1)
varp[0]=var9can
np.savetxt('var9.txt',varp)


varp=np.zeros(1)
varp[0]=var10can
np.savetxt('var10.txt',varp)


varp=np.zeros(1)
varp[0]=var11can
np.savetxt('var11.txt',varp)


varp=np.zeros(1)
varp[0]=var12can
np.savetxt('var12.txt',varp)


varp=np.zeros(1)
varp[0]=var13can
np.savetxt('var13.txt',varp)


varp=np.zeros(1)
varp[0]=var14can
np.savetxt('var14.txt',varp)


varp=np.zeros(1)
varp[0]=var15can
np.savetxt('var15.txt',varp)


varp=np.zeros(1)
varp[0]=var16can
np.savetxt('var16.txt',varp)


varp=np.zeros(1)
varp[0]=var17can
np.savetxt('var17.txt',varp)


varp=np.zeros(1)
varp[0]=var18can
np.savetxt('var18.txt',varp)

varp=np.zeros(1)
varp[0]=var19can
np.savetxt('var19.txt',varp)

varp=np.zeros(1)
varp[0]=var20can
np.savetxt('var20.txt',varp)

varp=np.zeros(1)
varp[0]=var21can
np.savetxt('var21.txt',varp)




var=np.zeros(21)
var[0]=var1can
var[1]=var2can
var[2]=var3can
var[3]=var4can
var[4]=var5can
var[5]=var6can
var[6]=var7can
var[7]=var8can
var[8]=var9can
var[9]=var10can
var[10]=var11can
var[11]=var12can
var[12]=var13can
var[13]=var14can
var[14]=var15can
var[15]=var16can
var[16]=var17can
var[17]=var18can
var[18]=var19can
var[19]=var20can
var[20]=var21can


#var=str(var)

var_sec=np.loadtxt('input.txt')
var_third=np.zeros((len(var_sec[:,0])+1,len(var_sec[0,:])))
var_third[0:len(var_third[:,0])-1,:]=var_sec
var_third[len(var_third[:,0])-1,0:21]=var


var_UM=np.loadtxt('var_UM.txt')
var_MM=np.loadtxt('var_MM.txt')
var_LM=np.loadtxt('var_LM.txt')
var_LVZ=np.loadtxt('var_LVZ.txt')


var_third[len(var_third[:,0])-1,21:36]=var_UM
var_third[len(var_third[:,0])-1,36:51]=var_MM
var_third[len(var_third[:,0])-1,51:66]=var_LM
var_third[len(var_third[:,0])-1,66:81]=var_LVZ

np.savetxt('input.txt',var_third)




