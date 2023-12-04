# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:19:50 2023

@author: friso
"""

def find_tool(line, finders, key):
    pos = [line.find(f) for f in finders]
    pos =  [1000 if p==-1 else p for p in pos]
    p = pos.index(min(pos))
    nr = key[p]
    return nr

# set this boolean
part2 = False 

file = open("inputs/01input.txt")
data = file.readlines()

values = []
finders = list('0123456789')
if part2:
    finders += ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
key = '0123456789123456789'
rfinders = [val[::-1] for val in finders]

for line in data:
    nr1 = find_tool(line, finders, key)
    nr2 = find_tool(line[::-1], rfinders, key)   
    values.append(int(nr1+nr2))
    
print(sum(values))   

    