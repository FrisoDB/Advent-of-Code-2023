# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:14:20 2023

@author: friso
"""

file = open("inputs/02input.txt")
data = file.readlines()

limits = {'red':12, 'green':13, 'blue':14}

possible_games = []
powers = []

for game in data:
    game = game.replace(':', '').replace(',', '').replace(';','').split()
    game_id = int(game[1])
    possible = True
    minima = {'red':0, 'green':0, 'blue':0}
    
    for i in range( (len(game)-2)//2 ):
        count =  int(game[2+2*i])
        colour =  game[3+2*i]
        if count > limits[colour]:
            possible = False
        if count > minima[colour]:
            minima[colour] = count

    if possible:
        possible_games.append(game_id)
    
    power = 1
    for minimum in minima.values():
        power *= minimum
    powers.append(power)
            
print(sum(possible_games))
print(sum(powers))
