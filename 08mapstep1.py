# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 06:04:38 2023

@author: friso
"""

file = open("inputs/08input.txt")
data = file.readlines()

instructions = data[0].strip()

nodes = dict()
for line in data[2:]:
    start, left, right = line.replace('=','').replace('(','').replace(',','').replace(')','').split()
    nodes[start] = (left,right)

i = 0
node = 'AAA'
while True:
    if instructions[i%len(instructions)]=='L':
        node = nodes[node][0]
    else: 
        node = nodes[node][1]
    
    i+=1
    
    if node == 'ZZZ':
        break
    
print(i)
    
    





