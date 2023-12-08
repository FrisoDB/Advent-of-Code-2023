# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 02:39:09 2023

@author: friso
"""

import numpy as np

file = open("inputs/06input.txt")
data = file.readlines()

time = [int(x) for x in data[0].split()[1:]]
record = [int(x) for x in data[1].split()[1:]]

wins = np.zeros(len(time), dtype=int)
for i in range(len(time)):
    t = time[i]    
    
    speed = np.arange(1, t, dtype=int)
    racetime = t - speed
    distance = speed* racetime
    wins[i] = np.count_nonzero(distance>record[i])

print(np.prod(wins))

time2 = int(data[0].split(':')[1].replace(' ',''))
record2 = int(data[1].split(':')[1].replace(' ',''))

speed = np.arange(1, time2, dtype=np.int64)
racetime = time2 - speed
distance = speed* racetime
wins2 = np.count_nonzero(distance>record2)

print(wins2)