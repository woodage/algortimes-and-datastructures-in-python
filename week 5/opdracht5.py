import math
import queue
from random import randint
import sys
import copy
import os
import random

sys.setrecursionlimit(15000)
INFINITY = float("inf")

__author__ = 'robbie'

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Vertex:

    def __init__(self, elem):
        self.data = elem

    def __repr__(self):
        return str(self.data)

    def __lt__(self, other):
        return self.data < other.data


def vertices(G):
    return sorted(G)

def BFS(G, s):
    s.distance = 0
    s.predecessor = None
    V = vertices(G)
    for v in V:
        if v != s:
            v.distance = INFINITY
    q = Queue()
    q.enqueue(s)
    while q.isEmpty() is False:
        u = q.dequeue()
        for n in G[u]:
            if n.distance == INFINITY:
                n.distance = u.distance + 1
                n.predecessor = u
                q.enqueue(n)

def path_BFS(G,u,v):
    BFS(G,u)
    a = []
    if hasattr(v,'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
        a.reverse()
    clear(G)
    return a

def clear(G): # verwijder alle toegevoegde attributen van de nodes
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v,e)


def show_tree_info(G):
    print('tree:')
    for v in vertices(G):
        print('(' + str(v))
        if hasattr(v, 'distance'):
            print(',d:' + str(v.distance))
        if hasattr(v, 'predecessor'):
            print(',p:' + str(v.predecessor))
        print(')')
    print()

def show_sorted_tree_info(G):
    print('sorted tree:')
    V = vertices(G)
    V = [v for v in V if hasattr(v,'distance') and hasattr(v,'predecessor')]
    V.sort(key = lambda x: (x.distance,x.predecessor))
    d = 0
    for v in V:
        if v.distance > d:
            print()
            d += 1
            print('(' + str(v) + ',d:' + str(v.distance) + ',p:'+ str(v.predecessor), end = '')
            print(')')
    print()

def is_connected(G):
    for v in vertices(G):
        if hasattr(v, 'distance'):
            if v.distance == INFINITY:
                return False
        else:
            return False
    return True

def no_cycles(G):
    for k,j in G.items():
        if len(j) >= 2:
            for n in j:
                Gc = G
                Gc[n].remove(k)
                Gc[k].remove(n)
                if len(path_BFS(Gc, k, n)):
                    return True
    return False

def get_bridges(G,v):
    r = []
    for k,j in G.items():
        for n in j:
            Gc = G
            Gc[n].remove(k)
            Gc[k].remove(n)
            BFS(Gc, v)
            if is_connected(Gc) is False:
                if (k,n) not in r:
                    r.append((k,n))
                    r.append((n,k))
            Gc[n].append(k)
            Gc[k].append(n)
    return r

def is_Euler_graph(G):
    weighted = []
    counted = 0
    for k,j in G.items():
        counted = 0
        for e in j:
            if e == k:
                counted += 2
            else:
                counted +=1
        weighted.append(counted)
    return len(weighted) == weighted.count(counted)

def get_Euler_graph(G, s):
    r = []
    r.append(s)
    while len(G.get(s)) > 0:
        bestN = None
        for n in G[s]:
            if (n, s) not in get_bridges(G, s):
                bestN = n
        if bestN is None:
            bestN = G[s][0]
        r.append(bestN)
        G[s].remove(bestN)
        G[bestN].remove(s)
        s = bestN
    for k,j in G.items():
        if len(j) > 0:
            exit('recursive doesnt work proper yet. Please try again.')
    return r

v = [Vertex(i) for i in range(8)]
G = {v[0]: [v[1],v[2]], v[1]: [v[0],v[3]], v[2]: [v[0],v[3]], v[3]: [v[1],v[2],v[4],v[6]], v[4]: [v[3],v[6],v[7],v[5]], v[5]: [v[4], v[6]], v[6]: [v[3],v[4],v[5],v[7]], v[7]: [v[6],v[4]]}

BFS(G, v[0])
print(get_Euler_graph(G, v[0]))

