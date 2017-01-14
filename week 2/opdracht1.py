__author__ = 'robbie'

def machtv3(a, n):
    assert n > 0
    x = 0
    m = 1
    while n > 0:
        if n % 2 == 0:
            a *= a
            x += 1
            n /= 2
        else:
            m *= a
            n -= 1
            x += 1
    return x

print(machtv3(2, 10000))