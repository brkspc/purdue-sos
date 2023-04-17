# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:52:08 2023

@author: BRK
"""

# function for adding stuff
def count_data(pop, stuffToCount):
    return sum(getattr(p, stuffToCount) for p in pop)