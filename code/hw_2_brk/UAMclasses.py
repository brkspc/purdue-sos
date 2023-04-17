#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 2 16:50:17 2023

@author: burak.akbulut
"""

from numpy.random import randint, rand
import matplotlib.pyplot as plt
import numpy as np

class vertiport():
    def __init__(self, vpID):
        self.ID = vpID
        # aircraft info
        self.idleAircraft = [3*60, 3*60] # [8.5*60, 8.5*60] # initiate with 2 aircrafts
        self.chargingAircraft = []
        self.incomingAircraftArrival = []
        self.incomingAircraftCharge = []
        # connected vertiports info
        self.flightSchedule = 40 # minutes
        self.flightScheduleMax = 40 # minutes
        # self.flightScheduleMissed = 0 # of flights
        self.flightDistances = 30 # minutes
        self.connectedPorts = 'vpB'
        self.aircraftPaxCapacity = 6 
        # passenger info
        self.paxWaiting = 0 
        self.totPax = 0 
        self.totalPaxServed = 0 
        # financials
        self.costPerMin = 2.25*2.58
        self.pricePerMin = 4.5*2.58
        self.totalCostIncurred = 0 
        self.totalRevenueGained = 0 
        self.totalProfit = 0

    def update(self, timeStep, ports,rideshare):
        # with every time step
        
        
        # generate passenger demand & update passenger count
        if rideshare:
            incomingPax = np.floor( (1/4)*timeStep/5*randint(5) )
            if self.flightSchedule == 5: # rideshare passengers
                incomingPax = 4 + incomingPax
        else:
            incomingPax = np.round( (1/1.4)*timeStep/5*randint(3) )
        # update pax info
        self.paxWaiting = self.paxWaiting + incomingPax
        self.totPax = self.totPax + incomingPax
        # check for low charge aircraft if low charge them. if charging complete, move to available list
        if self.idleAircraft != []:
            for ac in self.idleAircraft:
                if ac <= 40:
                    self.chargingAircraft.append(ac)
                    self.idleAircraft.remove(ac)
                    print("started charging a/c at ",format(self.ID) )
        if self.chargingAircraft != []:
            for idx, ac in enumerate(self.chargingAircraft):
                self.chargingAircraft[idx] = self.chargingAircraft[idx] + timeStep*3*60/90
                if self.chargingAircraft[idx] >= 3*60:
                    self.chargingAircraft[idx] = 3*60
                    self.idleAircraft.append(self.chargingAircraft[idx])
                    self.chargingAircraft.remove(self.chargingAircraft[idx])
                    print("a/c charged at ",format(self.ID) )
                
        # check for incoming a/c and adjust their status
        if self.incomingAircraftArrival!= []:
            for idx, ac in enumerate(self.incomingAircraftCharge):
                if self.incomingAircraftArrival[idx] <= 0:
                    self.idleAircraft.append(self.incomingAircraftCharge[idx])
                    self.incomingAircraftCharge.remove(self.incomingAircraftCharge[idx])
                    self.incomingAircraftArrival.remove(self.incomingAircraftArrival[idx])
                    print("a/c arrived at vertiport ",format(self.ID) )
                else:
                    self.incomingAircraftCharge[idx] = self.incomingAircraftCharge[idx] - timeStep
                    self.incomingAircraftArrival[idx] = self.incomingAircraftArrival[idx] - timeStep
        
        # check for flight interval; if time arrives dispatch aircraft, restart interval 
        # deduct from your available aircraft list and add to target vport's incoming a/c list
        self.flightSchedule = self.flightSchedule - timeStep
        if self.flightSchedule <= 0:
            if self.idleAircraft != []:
                for idx, port in enumerate(ports):
                    if port.ID == self.connectedPorts:
                        port.incomingAircraftCharge.append(self.idleAircraft[0])
                        port.incomingAircraftArrival.append(self.flightDistances)
                        self.idleAircraft.remove(self.idleAircraft[0])
                        self.flightSchedule = self.flightScheduleMax
                        # do the pax calculations
                        paxChange = min(self.aircraftPaxCapacity,self.paxWaiting)
                        self.paxWaiting = self.paxWaiting - paxChange
                        self.totalPaxServed = self.totalPaxServed + paxChange
                        # do the econ calculations
                        self.totalCostIncurred = self.totalCostIncurred + self.flightDistances*self.costPerMin*self.aircraftPaxCapacity  
                        self.totalRevenueGained = self.totalRevenueGained + self.flightDistances*self.pricePerMin*paxChange
                        self.totalProfit = self.totalProfit + self.totalRevenueGained - self.totalCostIncurred 
                        print("a/c dispatched to vertiport ",format(self.connectedPorts))
            # if no available a/c, dispatch from other vertiports
            
        
#         if self.timeToNextFlight > 0:
#             self.timeToNextFlight = self.timeToNextFlight - timeStep
#         else:
#             self.timeToNextFlight = 0
#         for ac in vpA.aircrafts:
#             ac = ac - timeStep
#             if ac < 60: # charging limit
#                 self.aircrafts.remove(ac)
#                 self.charging.append(ac)
#         for charingAC
