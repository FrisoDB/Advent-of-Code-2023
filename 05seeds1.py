# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 00:09:13 2023

@author: friso
"""

file = open("inputs/05input.txt")
data = file.readlines()

seeds = [int(x) for x in data[0].split()[1:]]
transforms = []
trans = []

for line in data[1:]:
    if 'map' in line:
        if trans:
            transforms.append(trans)
        trans = []
        continue
    elif line == '\n':
        continue
    dest, source, ran = [int(x) for x in line.split()]
    #reformatting: Sbegin, Send, Tbegin
    trans.append((source, source+ran-1, dest))
transforms.append(trans)

seedpaths = []
locations = []
for seed in seeds:
    seedpath = (seed,)
    source = seed
    for trans in transforms:
        for Sbegin, Send, Tbegin in trans:
            if (Sbegin <= source <= Send):
                target = Tbegin + source - Sbegin
                seedpath += (target,)
                source = target
                break
        else:
            #no mapping
            target = source
            seedpath += (target,)
    seedpaths.append(seedpath)
    locations.append(target)
    
print(min(locations))
        
        
