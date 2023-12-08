# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 03:13:30 2023

@author: friso
"""

part2 = True

file = open("inputs/07input.txt")
data = file.readlines()

handbids = [line.split() for line in data]

ordering = '23456789TJQKA'
if part2:
    ordering = 'J23456789TQKA'
key = dict()
for value,card in enumerate(ordering, 2):
    key[card] = value
    
hands = []

for hand,bid in handbids:
    counts = [hand.count(card) for card in ordering]
    if 5 in counts:
        handtype = 10
    elif 4 in counts:
        handtype = 8
    elif (3 in counts) and (2 in counts):
        #full house
        handtype = 4
    elif 3 in counts:
        handtype = 3
    elif counts.count(2)==2:
        #two pair
        handtype = 2
    elif 2 in counts:
        handtype = 1
    else: handtype = 0 #highcard
    
    #jokermath
    if (jokers:=counts[0]) and part2:
        if handtype >= 4:
            handtype = 10
        elif handtype == 3:
            handtype = 8
        elif (handtype == 2) and (jokers == 2):
            handtype = 8
        elif handtype == 0:
            handtype = 1
        else:
            handtype += 2
        
    handvalue = 0
    for pos,card in enumerate(reversed(hand)):
        handvalue += key[card]*100**pos
    
    pos +=1
    handvalue += handtype*100**pos
    
    hands.append((handvalue, int(bid), hand, handtype))
    
ranking = sorted(hands)

winnings = 0
for rank, hand in enumerate(ranking):
    winnings += (rank+1)*hand[1]
    
print(winnings)
