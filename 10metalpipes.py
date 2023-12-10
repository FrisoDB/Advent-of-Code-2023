# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:59:22 2023

@author: friso
"""

import networkx as nx

file = open("inputs/10input.txt")
data = file.readlines()
grid = ['.'+line.strip()+'.' for line in data]
grid = ['.'*len(grid[0])] + grid + ['.'*len(grid[0])]

pipes = nx.Graph()
for r in range(1,len(grid)-1):
    for c in range(1,len(grid[0])-1):
        if grid[r][c]=='|' and (grid[r-1][c] in '|7FS') and (grid[r+1][c] in '|LJS'):
            pipes.add_edges_from([ ((r,c),(r-1,c)), ((r,c),(r+1,c)) ])
            
        elif grid[r][c]=='-' and (grid[r][c-1] in '-LFS') and (grid[r][c+1] in '-J7S'):
            pipes.add_edges_from([ ((r,c),(r,c-1)), ((r,c),(r,c+1)) ])
            
        elif grid[r][c]=='L' and (grid[r-1][c] in '|7FS') and (grid[r][c+1] in '-J7S'):
            pipes.add_edges_from([ ((r,c),(r-1,c)), ((r,c),(r,c+1)) ])
            
        elif grid[r][c]=='J' and (grid[r][c-1] in '-LFS') and (grid[r-1][c] in '|7FS'):
            pipes.add_edges_from([ ((r,c),(r,c-1)), ((r,c),(r-1,c)) ])
            
        elif grid[r][c]=='7' and (grid[r][c-1] in '-LFS') and (grid[r+1][c] in '|LJS'):
            pipes.add_edges_from([ ((r,c),(r,c-1)), ((r,c),(r+1,c)) ])
            
        elif grid[r][c]=='F' and (grid[r+1][c] in '|LJS') and (grid[r][c+1] in '-J7S'):
            pipes.add_edges_from([ ((r,c),(r+1,c)), ((r,c),(r,c+1)) ])
            
        elif grid[r][c]=='S':
            start = (r,c)
            
cycles = nx.cycle_basis(pipes, root=start)
loop = cycles[0]
print(len(loop)//2)


#S uitzoeken
nbs = dict(pipes[start])
r,c = start
shifts = [(x-r,y-c) for x,y in nbs]
if all(shift in shifts for shift in [(-1,0),(1,0)]):
                                     S = '|'
elif all(shift in shifts for shift in [(0,-1),(0,1)]):
                                     S = '-'
elif all(shift in shifts for shift in [(-1,0),(0,1)]):
                                     S = 'L'
elif all(shift in shifts for shift in [(0,-1),(-1,0)]):
                                     S = 'J'
elif all(shift in shifts for shift in [(1,0),(0,-1)]):
                                     S = '7'
elif all(shift in shifts for shift in [(1,0),(0,1)]):
                                     S = 'F'
print(f'S=={S}')

#enclosed =  []
count = 0
for r in range(0,len(grid)):
    #line =  ''
    inside = 0
    for c in range(0,len(grid[0])):
        if (r,c) not in loop:
            #char = '.'
            if inside%2==1:
                #line += 'I'
                count += 1
            #else:
                #line += 'O'
            continue
        
        char = grid[r][c]
        #line += char

        if char=='S':
            char = S
            
        if char=='|':
            inside += 1
        elif char in 'L7':
            inside += 0.5
        elif char in 'FJ':
            inside -= 0.5
        
    #enclosed.append(line)
        
print(count)
