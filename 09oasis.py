# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 16:45:29 2023

@author: friso
"""
import numpy as np

file = open("inputs/09input.txt")
data = file.readlines()

next_values = []
prev_values = []
for line in data:
    numbers = np.array(line.split(), dtype=int)
    
    #stack = [numbers]
    next_value = numbers[-1]
    prev_value = numbers[0]
    dif =  np.diff(numbers)
    i = 1 #iteration determines sign prev_addition
    
    while np.any(dif):
        #stack.append(dif)
        next_value += dif[-1]
        prev_value += (-1)**i * dif[0]
        dif = np.diff(dif)
        i +=1
    next_values.append(next_value)
    prev_values.append(prev_value)

print(sum(next_values))
print(sum(prev_values))   
    
    
    
