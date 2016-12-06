__author__ = 'robbie'

import sys

def check(a, i):  # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or  # niet in dezelfde kolom
                i + n in [a[j] + j for j in range(n)] or  # niet op dezelfde diagonaal
                i - n in [a[j] - j for j in range(n)])  # niet op dezelfde diagonaal

def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("x", end=" ")
            else:
                print("*", end=" ")


def rsearch(N):
    global a, aCollection
    for i in range(N):
        if check(a, i):
            a.append(i)
            if len(a) == N and a not in aCollection:
                aCollection.append(a)
                a = []
                return True  # geschikte a gevonden
            else:
                if rsearch(N):
                    return True
            del a[-1]  # verwijder laatste element
    return False

def search_all_things(N):
    if rsearch(N):
        search_all_things(N)

aCollection = []
a = []  # a geeft voor iedere rij de kolompositie aan
t = 0

sys.setrecursionlimit(10000)

search_all_things(8)

for queen in aCollection:
    print(queen)

print("variations: " + str(len(aCollection)))
printQueens(a)