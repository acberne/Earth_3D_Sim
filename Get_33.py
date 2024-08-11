

# *********************************************************************
# FUNCTION TO GENERATE JOU FILE W/FAULTS FROM TXT FILE
#
# *********************************************************************

import numpy as np
import pandas as pd

Pots=np.loadtxt('Potentials.txt')

#0 v20
#1 V21
#2 V22
#3 v30
#4 V33
#5 V32
#6 V33


s_20_file=np.loadtxt('resp.MCMC_response_TD20.dat')
s_21_file=np.loadtxt('resp.MCMC_response_TD21.dat')
s_22_file=np.loadtxt('resp.MCMC_response_TD22.dat')

s_33_file=np.loadtxt('resp.MCMC_response_TD30.dat')

#potential ratio, current file on bottom

k33=s_33_file[0,9]+(Pots[0]/Pots[6])*s_20_file[30,9]+(Pots[1]/Pots[6])*s_21_file[37,9]+(Pots[2]/Pots[6])*s_22_file[35,9]


print('k33 Love Number: ')
print(k33)
arr=np.zeros(1)
arr[0]=k33

np.savetxt('k33.txt',arr)













