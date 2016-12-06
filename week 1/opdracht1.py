__author__ = 'robbie'

def mymax(x):
    max_item = 0

    for j in range(0, len(x)):
        assert isinstance(x[j], int) == 0 and isinstance(x[j], double) == 0, "type in array is not int or double" + str(x[j])

    if len(x) != 0:

        for i in range(0, len(x)):
            if x[i] > max_item:
                max_item = x[i]


    return max_item


print(mymax([3,2,2,2,6,-3,2,1,9]))