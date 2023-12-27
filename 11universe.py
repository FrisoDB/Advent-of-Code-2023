# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 17:26:08 2023

@author: friso
"""

import numpy as np

def expand_universe(old_galaxies, expansion_size=2):
    #expands universe over ONE axis
    new_galaxies = np.zeros_like(old_galaxies)
    max_old_index = np.max(old_galaxies[:,0])
    new_index = 0
    
    for old_index in range(max_old_index+1):
        pos = old_index == old_galaxies[:,0]
        if np.any(pos):
            new_galaxies[pos,0] = new_index
            new_index += 1
        else:
            #no galaxies on this line, so expansion
            new_index += expansion_size
        
    new_galaxies[:,1] = old_galaxies[:,1]
    return new_galaxies
    

file = open("inputs/11input.txt")
data = file.readlines()
field = [list(line.strip()) for line in data]

old_universe = np.array(field)=='#'
old_galaxies = np.argwhere(old_universe)


expansions = [2, 10, 100, 10**6]
for expans in expansions:
    galaxies = np.fliplr(expand_universe(np.fliplr(expand_universe(old_galaxies,expans)),expans))
    
    distances = 0
    for x,y in galaxies:
        dx = np.abs(galaxies[:,0] -x)
        dy = np.abs(galaxies[:,1] -y)
        distances += np.sum(dx) + np.sum(dy)
    
    print(distances//2)
