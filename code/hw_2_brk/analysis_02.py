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

for idx in range(1):
    vertiportA = vertiport('vpA')
    vertiportB = vertiport('vpB')
    vertiportB.connectedPorts = 'vpA'
    vertiportB.flightSchedule = 20
    ports = [vertiportA,vertiportB]
    totPaxWaiting = []
    for t in timeVector:
        for port in ports:
            port.update(timeStep, ports, False)
        
        totPaxWaiting.append(count_data(ports, 'paxWaiting'))
        
    plt.plot(timeVector,totPaxWaiting)
plt.xlabel("Time (minutes)")
plt.ylabel("Passenger number")
plt.title("Total passenger waiting - schedule shift & no rideshare")
# plt.title("Total passenger waiting - with rideshare & schedule shift")
plt.show()

