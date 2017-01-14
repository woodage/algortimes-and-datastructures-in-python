__author__ = 'robbie'

import random
import sys

sys.setrecursionlimit(10000000)

temp = 0

def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

def qsort(a,low=0,high=-1):
    global temp

    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low, low + 1)
        m = low
        for j in range(low+1,high+1):
            if a[j] < a[low]:
                temp += 1
                m += 1
                swap(a,m,j)
                swap(a,low,m)
        if m > 0:
            temp += 1
            qsort(a,low,m-1)
        qsort(a,m+1,high)


qsort([random.random()] * 2000)
print(temp)