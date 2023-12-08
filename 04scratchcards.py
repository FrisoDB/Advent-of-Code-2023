# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:18:42 2023

@author: friso
"""

import numpy as np

file = open("inputs/04input.txt")
data = file.readlines()

cards =  [line.replace('\n','').replace('|',':').split(':') for line in data]
points = []
overlaps = []

for card in cards:
    winnrs = {int(x) for x in card[1].split()}
    havenrs = {int(x) for x in card[2].split()}
    overlap = len(winnrs.intersection(havenrs))
    points.append( int( 2**(overlap-1)) )
    overlaps.append(overlap)
    
print(sum(points))

pile = np.ones(len(cards), dtype=int)
for cardnr,copies in enumerate(overlaps):
    pile[cardnr+1:cardnr+copies+1] += pile[cardnr]  
    
print(sum(pile)) 

