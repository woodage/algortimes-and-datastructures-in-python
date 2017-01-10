__author__ = 'robbie'
fDict = dict()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def B(n, k):
    if n not in fDict.keys():
        fDict[n] = factorial(n)
    if k not in fDict.keys():
        fDict[k] = factorial(k)
    if (n - k) not in fDict.keys():
        fDict[(n - k)] = factorial((n - k))
    return fDict[n] // fDict[k] // fDict[n-k]

print(B(100, 50))
print(B(100, 50))
