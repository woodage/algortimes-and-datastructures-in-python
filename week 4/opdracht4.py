__author__ = 'robbie'

def f(n):
    assert type(n) == int
    assert n <= 1000
    solutions = [1] + ([0] * n)
    moneys = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    for money in moneys:
        for i in range(money, n + 1):
            solutions[i] += solutions[i - money]
    return solutions[n]

print(f(100))