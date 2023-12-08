# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 06:04:38 2023

@author: friso
"""
import numpy as np
from itertools import compress

def sieve_eratosthenes(limit):
    if limit <= 1:
        return []

    primes = [True] * limit
    for base in range(2, int(limit**0.5 + 1)):
        if primes[base]:
            primes[base * base::base] = [False] * ((limit - 1) // base - base + 1)

    primes[0] = primes[1] = False
    return list(compress(range(limit), primes))


file = open("inputs/08input.txt")
data = file.readlines()

instructions = data[0].strip()

network = dict()
for line in data[2:]:
    start, left, right = line.replace('=','').replace('(','').replace(',','').replace(')','').split()
    network[start] = (left,right)

i = 0
nodes = [node for node in network if node[-1]=='A']
count_all = []
found_all = []

for node in nodes:
    i = 0
    found = []
    counts = []
    while True:
        direction = instructions[i%len(instructions)]=='R'
        node = network[node][direction]
        i+=1
        
        if node in found:
            found.append(node)
            counts.append(i)
            break
        elif node[-1]=='Z':
            found.append(node)
            counts.append(i)
            
    count_all.append(counts)
    found_all.append(found)

lines = np.array(count_all,dtype=np.int64)
lines[:,1] -= lines[:,0]
#opmerking: beide kolommen van lines blijken gelijk

primes_list =  np.array(sieve_eratosthenes(np.max(lines)+1),dtype=np.int64)
prime_factors = np.zeros_like(primes_list,shape=(len(lines),len(primes_list)))
for i in range(len(lines)):
    line = lines[i,0]
    while True:
        more_factors = (line%primes_list==0)
        if not np.any(more_factors):
            break
        prime_factors[i,:] += more_factors
        line = line/primes_list
        
total_primefactors = np.max(prime_factors, axis=0)

answer = np.prod(primes_list**total_primefactors)
print(answer)   

