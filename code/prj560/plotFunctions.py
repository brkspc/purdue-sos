# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 04:28:38 2023

@author: BRK

This script includes the functions designed for plotting stuff such as 
plot_towns
plot_agents (to be added later)
..and whatnot

"""
import matplotlib.pyplot as plt


# define the function for plotting towns
def plot_towns(towns):
    for eachTown in towns:
        # first plot their positions
        plt.scatter(eachTown.pos[0],eachTown.pos[1]) 
        txtOffset = 0.15  
        # now add labels
        plt.text(eachTown.pos[0]+txtOffset,eachTown.pos[1]+txtOffset,eachTown.ID)
        # now go over their neighbors and plot the links between them
        for idx,stuffz in enumerate([eachTown.neighbors]):
            if isinstance(stuffz, str): # if there is one neighbor
                for x in towns:
                    if x.ID == stuffz:
                        plt.plot([eachTown.pos[0], x.pos[0]],[eachTown.pos[1], x.pos[1]], color = 'b')
            else: #if there is more than one neighbor
                for stuff in stuffz:
                    for x in towns:
                        if x.ID == stuff:
                            plt.plot([eachTown.pos[0], x.pos[0]],[eachTown.pos[1], x.pos[1]], color = 'b')