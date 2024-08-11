

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
#potential ratio, current file on bottom


k22=s_22_file[0,9]+s_22_file[29,9]+(Pots[0]/Pots[2])*s_20_file[25,9]+(Pots[1]/Pots[2])*s_21_file[30,9]

print('k22 Love Number: ')
print(k22)
arr=np.zeros(1)
arr[0]=k22

np.savetxt('k22.txt',arr)













