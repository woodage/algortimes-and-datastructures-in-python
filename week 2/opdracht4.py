__author__ = 'robbie'

def mybin(dec):
    assert dec > 0
    if dec <= 1:
        return str(dec)
    else:
        s1 = mybin(dec // 2)
        s2 = str(dec % 2)
        return s1 + s2

print(mybin(16))