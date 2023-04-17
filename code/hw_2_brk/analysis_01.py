#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:21:17 2023

@author: burak.akbulut
"""

from UAMfunctions import *
import numpy as np
from UAMclasses import vertiport
import matplotlib.pyplot as plt

timeStep = 5 # min
timeVector = range(0, timeStep*144, timeStep)

for idx in range(9):
    vertiportA = vertiport('vpA')
    vertiportB = vertiport('vpB')
    vertiportB.connectedPorts = 'vpA'
    ports = [vertiportA,vertiportB]
    totPaxServed = []
    for t in timeVector:
        for port in ports:
            port.update(timeStep, ports, True)
        

        # totPaxWaiting.append(count_data(ports, 'paxWaiting'))
        totPaxServed.append(count_data(ports, 'totalPaxServed'))
        # totalPax.append(count_data(ports, 'totPax'))
        
        # plt.plot(timeVector,totPaxWaiting)
    plt.plot(timeVector,totPaxServed)
plt.xlabel("Time (minutes)")
plt.ylabel("Passenger number")
# plt.title("Total passenger served - no rideshare")
plt.title("Total passenger served - with rideshare")
plt.show()

