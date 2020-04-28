#This syntax is killing me

import random

def printElements(array):
    for index in array:
        print(index , end =" ")

def scrambleArray(array):
    for index in range(0, len(array)):
        array[index] = random.randrange(1, 100)

def swapElements(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

def bubbleSort(array):
    comparisons = 0
    swaps = 0
    isArraySorted = False
    while isArraySorted == False:
        isArraySorted = True
        for index in range(1, len(array)):
            comparisons += 1
            if (array[index-1] > array[index]):
                swaps += 1
                isArraySorted = False
                swapElements(array, index-1, index)

    print("\nComparisons: " + str(comparisons) + "\nSwaps: " + str(swaps) + "\n")


numList = [None] * 100

scrambleArray(numList)
printElements(numList)

print("\nSorting array...")

bubbleSort(numList)
printElements(numList)