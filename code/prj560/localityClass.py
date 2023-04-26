# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 02:36:10 2023

@author: BRK

File containing the locality class and all the associated stuff with it
"""

# import some useful libraries
from numpy.random import randint, rand
import matplotlib.pyplot as plt
import numpy as np

class locality(): # this is the class for location. its job is to exist
    def __init__(self,locID,posX,posY,neighborList): # this is a constructor call
        self.ID = locID # name/ID of the locality 
        self.pos = [posX,posY] # x, y position - default position is entered as a placeholder
        self.disaster = False # is there a disaster at this node?
        self.agents = [] # empty list - going to be populated by agents. When an agent is in 
        # (or at the vicinity ?) of the locality, it will be added here and vice versa
        self.neighbors = neighborList # empty list - populated by thename of neighbors
        self.type = 'normal' # type of the locality. other possible types could
        # be 'evac' - evacuation zone, 'med' - medical zone, 'fob' -fwd operating
        # base, where rescuers would start. other suggestion welcome 
        
    # normally classes generally have an update method which is called at every 
    # turn but i do not think we will be needing for the locality class
