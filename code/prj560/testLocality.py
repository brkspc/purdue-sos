# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 03:25:33 2023

@author: BRK

# simple test file to play around with localities, i.e definging and plotting them
"""

import numpy as np
from localityClass import locality
import matplotlib.pyplot as plt

# define a generic example for locality placement
townA = locality('townA',0,0,'townB')
townB = locality('townB',10,0,['townC','townD'])
townC = locality('townC',10,10,'townB')
townD = locality('townD',10,-10,'townB')
towns = [townA,townB,townC,townD]

# maybe we should create a function such as pltTowns from the below stuff
# drawing connected lines between neighbouring towns would also be helpful
for eachTown in towns:
    plt.scatter(eachTown.pos[0],eachTown.pos[1])
    txtOffset = 0.15  
    plt.text(eachTown.pos[0]+txtOffset,eachTown.pos[1]+txtOffset,eachTown.ID)
    
plt.show()