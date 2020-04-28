#This syntax is killing me

import random
from timeit import default_timer as timer

def printElements(array):
    for index in array:
        print(index , end =" ")
    print()

def populateArray(array):
    for index in range(0, len(array)):
        array[index] = index+1

def scrambleArray(array):
    for index in range(0, len(array)):
        swapElements(array, index, random.randrange(1, len(array)))

def swapElements(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

def bogoSort(array):
    comparisons = 0
    swaps = 0
    isArraySorted = True
    for index in range(1, len(array)):
        comparisons += 1
        if (array[index-1] > array[index]):
            isArraySorted = False
    while isArraySorted == False:
        isArraySorted = True
        for index in range(0, len(array)):
            swapElements(array, index, random.randrange(1, len(array)))
            swaps += 1
        for index in range(1, len(array)):
            comparisons += 1
            if (array[index-1] > array[index]):
                isArraySorted = False

    printElements(array)
    print("\nComparisons: " + str(comparisons) + "\nSwaps: " + str(swaps) + "\n")

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
    printElements(array)
    print("\nComparisons: " + str(comparisons) + "\nSwaps: " + str(swaps) + "\n")

def insertionSort(array):
    comparisons = 0
    swaps = 0
    for i in range(1, len(array)):
        j = i
        comparisons += 1
        while (j > 0) and (array[j-1] > array[j]):
            comparisons += 1
            swapElements(array, j-1, j)
            swaps += 1
            j -= 1
    printElements(array)
    print("Comparisons: " + str(comparisons) + "\nSwaps: " + str(swaps))

def mergeSort(array):
    comparisons = 0
    swaps = 0
    
def merge(array1, array2):
    return

size = int(input("Size of array: "))
numList = [None] * size

populateArray(numList)
scrambleArray(numList)
printElements(numList)
print("Sorting array...\n")
start = timer()
bogoSort(numList)
end = timer()
print("Elapsed Time: " + str(end-start))