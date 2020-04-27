#Where are all the semicolons?

import random

def printElements(array):
    for index in array:
        print(index)

def scrambleArray(array):
    for index in range(0, len(array)):
        array[index] = random.randrange(1, 100)

numList = [None] * 100

scrambleArray(numList)
printElements(numList)

