__author__ = 'robbie'

import random

hashDict = dict()

while(True):
    r = random.random()
    if r not in hashDict.values():
        rh = hash(r) % ( 2 ** 32)
        if rh in hashDict.keys():
            print(repr(r) + " == "+  repr(rh) +" same hash value : "+ repr(hashDict[rh]))
            break
        hashDict[rh] = r