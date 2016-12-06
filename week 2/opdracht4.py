__author__ = 'robbie'

def mybin(dec, res = ''):

    #check
    if dec <= 0:
        return res

    #operation
    new_res = (str)(dec % 2) + res

    #repeat
    return mybin((int)(dec / 2), new_res)


print(mybin(15))