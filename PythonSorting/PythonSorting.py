#This syntax is killing me

import random
from timeit import default_timer as timer

def printElements(array):
    for index in array:
        print(index , end =" ")

def scrambleArray(array, ran):
    for index in range(0, len(array)):
        array[index] = random.randrange(1, ran)

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
    print("\nComparisons: " + str(comparisons) + "\nSwaps: " + str(swaps))

size = int(input("Size of array: "))
numList = [None] * size
rang = int(input("Range of numbers: "))

scrambleArray(numList, rang)
printElements(numList)

print("\nSorting array...\n")
start = timer()
insertionSort(numList)
end = timer()
print("Elapsed Time: " + str(end-start))