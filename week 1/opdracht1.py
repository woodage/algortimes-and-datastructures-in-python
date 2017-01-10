__author__ = 'robbie'


def mymax(x):
    assert len(x) > 0
    max_item = x[0]
    for j in range(0, len(x)):
        assert type(x[j]) in [int, float]
    for i in range(0, len(x)):
        if x[i] > max_item:
            max_item = x[i]
    return max_item

print(mymax([-2, -9]))