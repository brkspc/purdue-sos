#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:21:17 2023

@author: burak.akbulut
"""

import numpy as np
from UAMclasses import vertiport
import matplotlib.pyplot as plt

# check if the aircraft could be transferred among the different lists

vertiportA = vertiport('vpA')
vertiportB = vertiport('vpB')
ports = [vertiportA,vertiportB]

# print(vertiportA.idleAircraft, vertiportA.chargingAircraft)
# vertiportA.idleAircraft[0] = 59 # reduce charge of one
vertiportA.incomingAircraftCharge = [400] 
vertiportA.incomingAircraftArrival = [30]

totPaxWaiting = [] 


timeStep = 5 # min
timeVector = range(0, timeStep*144, timeStep)
print("vertiport",'\t','Pax Served','\t','pax waiting','\t','total cost','\t','total rev','\t','total profit')
print("--------",'\t','--------','\t','--------','\t','--------','\t','--------','\t','--------')

# print("vertiport",'\t','Pax Served','\t','pax waiting','\t','available a/c','\t','charging a/c','\t','incoming a/c','\t','time to nxt flight')

for t in timeVector:
    vertiportA.update(timeStep, ports)
    print("vertiportA",'\t \t',vertiportA.totalPaxServed,'\t \t',vertiportA.paxWaiting,'\t \t',vertiportA.totalCostIncurred,'\t \t', vertiportA.totalRevenueGained,'\t \t \t', vertiportA.totalProfit)   
    totPaxWaiting.append(vertiportA.paxWaiting)
    # print("vertiportA",'\t \t',vertiportA.totalPaxServed,'\t \t',vertiportA.paxWaiting,'\t \t',vertiportA.idleAircraft,'\t \t', vertiportA.chargingAircraft,'\t \t \t', vertiportA.incomingAircraftCharge,'\t \t \t', vertiportA.flightSchedule)
    # print("vertiportB",'\t \t',vertiportB.totalPaxServed,'\t \t',vertiportB.paxWaiting,'\t \t',vertiportB.idleAircraft,'\t \t', vertiportB.chargingAircraft,'\t \t \t', vertiportB.incomingAircraftCharge,'\t \t \t', vertiportB.flightSchedule)

plt.plot(timeVector,totPaxWaiting)
plt.show()
# vpA = vertiport('A')
# vpB = vertiport('B')
# ports = [vpA, vpB]
# totPaxWaiting = [] 
# totPax = [] 
# timeStep = 5 # min
# timeVector = range(0, 5*60, timeStep)
# for t in timeVector:
#     for port in ports:
#         port.update(timeStep)
#     totPaxWaiting.append(count_paxWaiting(ports))
#     totPax.append(count_totPax(ports))
