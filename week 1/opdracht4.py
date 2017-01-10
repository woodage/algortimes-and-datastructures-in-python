from random import randint

__author__ = 'robbie'


def calculateSameBirth(students, ntests):
    sameBirth = 0
    for r in range(0, ntests):
        #create a list for all birthdays
        births = []
        #loop each student
        for s in range(0,students):
            #append a birth (number between 1 and 365) to list that represent as student birthday
            births.append(randint(1,366))
        if len(set(births)) != students:
            sameBirth+=1
    return sameBirth

print(calculateSameBirth(23, 100))