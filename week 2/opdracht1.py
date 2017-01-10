__author__ = 'robbie'


def machtv3(a,n):
    assert n > 0
    m = 1
    square = a * a
    while n > 0:
        if n%2 == 0:
            n = n // 2
        else:
            n = n - 1
        m += square * square
    return m
print(machtv3(2, 1))
#AFMAKEN!!!