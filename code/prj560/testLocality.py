# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 03:25:33 2023

@author: BRK

# simple test file to play around with localities, i.e definging and plotting them
"""

import numpy as np
from localityClass import locality
import matplotlib.pyplot as plt
from plotFunctions import * # this is how we call to 

# define a generic example for locality placement
townA = locality('townA',0,0,'townB')
townB = locality('townB',10,0,['townC','townD'])
townC = locality('townC',10,10,'townB')
townD = locality('townD',10,-10,'townB')
towns = [townA,townB,townC,townD]

# call the specific function to plot the towns
plot_towns(towns)

    
plt.show()