import math
import queue
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

v = [Vertex(i) for i in range(8)]
upperG = {v[0]:[v[4],v[5]], v[1]:[v[4],v[5],v[6]], v[2]:[v[4],v[5],v[6]], v[4]:[v[0], v[1], v[2], v[5]], v[5]:[v[0],v[1],v[2], v[4]], v[6]:[v[1],v[2]], }
downG = {v[0]:[v[4],v[5]], v[1]:[v[4],v[6]], v[2]:[v[5]], v[3]:[v[7]], v[4]:[v[0], v[1]], v[5]:[v[0],v[2]], v[6]:[v[1]], v[7]:[v[3]],}

print(no_cycles(upperG))
print(no_cycles(downG))