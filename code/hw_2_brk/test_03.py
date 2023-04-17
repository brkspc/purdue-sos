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

# check if the aircraft could be transferred among the different lists

vertiportA = vertiport('vpA')
vertiportB = vertiport('vpB')
vertiportB.connectedPorts = 'vpA'
vertiportB.flightSchedule = 20
ports = [vertiportA,vertiportB]

# print(vertiportA.idleAircraft, vertiportA.chargingAircraft)
# vertiportA.idleAircraft[0] = 59 # reduce charge of one
# vertiportA.incomingAircraftCharge = [400] 
# vertiportA.incomingAircraftArrival = [30]

totPaxWaiting = [] 
totPaxServed = [] 
totalPax = [] 


timeStep = 5 # min
timeVector = range(0, timeStep*144, timeStep)
# print("vertiport",'\t','Pax Served','\t','pax waiting','\t','total cost','\t','total rev','\t','total profit')
# print("--------",'\t','--------','\t','--------','\t','--------','\t','--------','\t','--------')

# print("vertiport",'\t','Pax Served','\t','pax waiting','\t','available a/c','\t','charging a/c','\t','incoming a/c','\t','time to nxt flight')

for t in timeVector:
    for port in ports:
        port.update(timeStep, ports, False)
        
        # vertiportB.update(timeStep, ports)
        # print("vertiportA",'\t \t',vertiportA.totalPaxServed,'\t \t',vertiportA.paxWaiting,'\t \t',vertiportA.totalCostIncurred,'\t \t', vertiportA.totalRevenueGained,'\t \t \t', vertiportA.totalProfit)   
        # print("vertiportB",'\t \t',vertiportB.totalPaxServed,'\t \t',vertiportB.paxWaiting,'\t \t',vertiportB.totalCostIncurred,'\t \t', vertiportB.totalRevenueGained,'\t \t \t', vertiportB.totalProfit)   
        # totPaxWaitingA.append(vertiportA.paxWaiting)
        # totPaxServedA.append(vertiportA.totalPaxServed)
        # totPaxWaitingB.append(vertiportB.paxWaiting)
    
    totPaxWaiting.append(count_data(ports, 'paxWaiting'))
    totPaxServed.append(count_data(ports, 'totalPaxServed'))
    totalPax.append(count_data(ports, 'totPax'))
    # print("vertiportA",'\t \t',vertiportA.totalPaxServed,'\t \t',vertiportA.paxWaiting,'\t \t',vertiportA.idleAircraft,'\t \t', vertiportA.chargingAircraft,'\t \t \t', vertiportA.incomingAircraftCharge,'\t \t \t', vertiportA.flightSchedule)
    # print("vertiportB",'\t \t',vertiportB.totalPaxServed,'\t \t',vertiportB.paxWaiting,'\t \t',vertiportB.idleAircraft,'\t \t', vertiportB.chargingAircraft,'\t \t \t', vertiportB.incomingAircraftCharge,'\t \t \t', vertiportB.flightSchedule)
    # print("vertiportB",vertiportB.idleAircraft,'\t \t', vertiportB.chargingAircraft,'\t \t', vertiportB.incomingAircraftArrival,'\t \t', vertiportB.incomingAircraftCharge,'\t \t', vertiportB.flightSchedule)
    # print("vertiportA",vertiportA.idleAircraft,'\t \t', vertiportA.chargingAircraft,'\t \t', vertiportA.incomingAircraftArrival,'\t \t', vertiportA.incomingAircraftCharge,'\t \t', vertiportA.flightSchedule)

fig, ax = plt.subplots()
# note that plot returns a list of lines.  The "l1, = plot" usage
# extracts the first element of the list into l1 using tuple
# unpacking.  So l1 is a Line2D instance, not a sequence of lines
l1, = ax.plot(timeVector, totPaxWaiting)
l2, = ax.plot(timeVector, totPaxServed)

ax.legend((l1, l2), ('served', 'waiting'), loc='upper left', shadow=True)
ax.set_xlabel('Time (minutes)')
ax.set_ylabel('Number of Pax')
plt.show()

print('total {} pax in the network',format(totalPax[-1]))
# plt.plot(timeVector,totPaxWaiting)
# plt.plot(timeVector,totPaxServed)
# plt.xlabel("Time (minutes)")
# plt.ylabel("Number of Pax")
# plt.show()
