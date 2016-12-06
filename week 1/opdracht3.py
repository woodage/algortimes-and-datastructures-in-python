__author__ = 'robbie'

def getPriem(a):

    pops = 0
    i =0
    checked_index = 0

    while pops > 0 or checked_index == 0:

        pops = 0
        i = 0

        while i < len(a):
            if a[i] % a[checked_index] == 0 and a[i] != a[checked_index]:
                a.remove(a[i])
                pops+=1
            i+=1

        checked_index+=1

    return a


myList = list(range(2, 1001))

print(getPriem(myList))

