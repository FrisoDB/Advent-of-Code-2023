# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:43:08 2023

@author: friso
"""
#from copy import deepcopy

file = open("inputs/03input.txt")
data = file.readlines()

field = [line.replace('\n','') for line in data]
parts = []
nr = ''
gear = []
found = False

#detect number, get its position
for r in range(len(field)):
    if field[r][0] in '0123456789':
        nr += field[r][0]
   
    for c in range(len(field[0])):
        if ((c+1>=len(field[0])) or (field[r][c+1] not in '0123456789') and nr):
            #line runs out, or no more numbers
            #and thus a complete number available, dus symbol searching
            #up down
            sur = [(x,y) for x in [r-1,r+1] for y in range(c-len(nr), c+2) ]
            #left right
            sur += [(r, c-len(nr)), (r, c+1)]
            
            for x,y in sur:
                if x<0 or y<0:
                    continue
                try:
                    symbol = field[x][y]
                    if symbol == '*':
                        #found specific symbol *
                        gear.append((x,y, int(nr)))
                        found = True
                        break
                        
                    elif (symbol not in '0123456789' and symbol != '.'):
                        #found a symbol
                        found = True
                except:
                    pass
            if found:
                parts.append(int(nr))
                found = False
            nr = ''
            
        elif c+1>=len(field[0]):
                      continue
        elif field[r][c+1] in '0123456789':
            nr += field[r][c+1]

print(sum(parts))

#gear2 = deepcopy(gear)
ratios = []
while gear:
    first = gear.pop()
    for second in gear:
        if first[:2] == second[:2]:
            ratios.append(first[2]*second[2])
            gear.remove(second)

print(sum(ratios))
            
    
    
    

