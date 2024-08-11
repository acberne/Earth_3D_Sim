

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
#4 V31
#5 V32
#6 V33



s_20_file=np.loadtxt('resp.MCMC_response_TD20.dat')
s_21_file=np.loadtxt('resp.MCMC_response_TD21.dat')
s_22_file=np.loadtxt('resp.MCMC_response_TD22.dat')

s_32_file=np.loadtxt('resp.MCMC_response_TD30.dat')

#potential ratio, current file on bottom

k32=s_32_file[0,9]+(Pots[1]/Pots[5])*s_21_file[36,9]+(Pots[2]/Pots[5])*s_22_file[34,9]

print('k32 Love Number: ')
print(k32)
arr=np.zeros(1)
arr[0]=k32

np.savetxt('k32.txt',arr)













