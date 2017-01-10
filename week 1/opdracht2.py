__author__ = 'robbie'

def getNumbers(a):
    # list to return with digits that are found
    returnList = []
    #temp string to keep all digits together
    tempString = ""
    for i in range(0, len(a)):
        if a[i].isdigit():
            tempString += str(a[i])
        else:
            if tempString != "":
                returnList.append(int(tempString))
                tempString = ""
    if tempString != "":
        returnList.append(int(tempString))
        tempString = ""
    return returnList

someText = "a have163caps fo3r my 18 4 birhtd55"

print(getNumbers(someText))