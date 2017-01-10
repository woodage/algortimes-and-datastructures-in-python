__author__ = 'robbie'


def next_las_seq(x):
    #sort array first
    x.sort()
    #unique list of all elements in the array
    u = set(x)
    #final list to return
    f = []
    for i in u:
        f.append(x.count(i))
        f.append(i)
    #return list
    return f

x = [3,3,4,1,1,6,6,6,1]
n = next_las_seq(x)
print(n)