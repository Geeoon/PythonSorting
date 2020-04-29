#This syntax is killing me

import random
import math

from timeit import default_timer as timer
comparisons = 0
swaps = 0

def getSize():
	size = int(input("Size of list: "))
	while (size <= 1):
		print("The list must have a size greater than 1")
		size = int(input("Size of list: "))
	return size

def printElements(list):
	for index in list:
		print(index , end =" ")
	print()

def populatelist(list):
	for index in range(0, len(list)):
		list[index] = index+1

def scramblelist(list):
	for index in range(0, len(list)):
		swapElements(list, index, random.randrange(0, len(list)))

def swapElements(list, index1, index2):
	list[index1], list[index2] = list[index2], list[index1]

def bogoSort(list):
	islistSorted = True
	for index in range(1, len(list)):
		comparisons += 1
		if (list[index-1] > list[index]):
			islistSorted = False
			return
	while islistSorted == False:
		islistSorted = True
		for index in range(0, len(list)):
			swapElements(list, index, random.randrange(0, len(list)))
			swaps += 1
		for index in range(1, len(list)):
			comparisons += 1
			if (list[index-1] > list[index]):
				islistSorted = False

	printElements(list)
	print("\nComparisons: " + str(comparisons) + "\nSwaps: " + str(swaps) + "\n")

def bubbleSort(list):
	islistSorted = False
	while islistSorted == False:
		islistSorted = True
		for index in range(1, len(list)):
			comparisons += 1
			if (list[index-1] > list[index]):
				swaps += 1
				islistSorted = False
				swapElements(list, index-1, index)
	printElements(list)
	print("\nComparisons: " + str(comparisons) + "\nSwaps: " + str(swaps) + "\n")

def insertionSort(list):
	for i in range(1, len(list)):
		j = i
		comparisons += 1
		while (j > 0) and (list[j-1] > list[j]):
			comparisons += 1
			swapElements(list, j-1, j)
			swaps += 1
			j -= 1
	printElements(list)
	print("Comparisons: " + str(comparisons) + "\nSwaps: " + str(swaps))

def mergeSort(list):
	printElements(mergeDivide(list))

def mergeDivide(list):
	end = math.ceil(len(list) / 2)
	list1 = list[0:end]
	list2 = list[end:len(list)]
	if (len(list1) > 1 or len(list2) > 1):
		return mergeConquer(mergeDivide(list1), mergeDivide(list2))
	else:
		return mergeConquer(list1, list2)


def mergeConquer(list1, list2):
	size = len(list1) + len(list2)
	listF = [None] * size
	pos1 = 0
	pos2 = 0
	i = 0
	while (i < size):
		if (pos1 >= len(list1)):
			for i in range(i, size):
				listF[i] = list2[pos2]
				pos2 += 1
		elif (pos2 >= len(list2)):
			for i in range(i, size):
				listF[i] = list1[pos1]
				pos1 += 1
		elif (list1[pos1] > list2[pos2]): 
			listF[i] = list2[pos2]
			pos2 += 1
		elif (list1[pos1] < list2[pos2]):
			listF[i] = list1[pos1]
			pos1 += 1
		else:
			listF[i] = list1[pos1]
			i += 1
			listF[i] = list2[pos2]
			pos1 += 1
			pos2 += 1
		i += 1
	return listF


size = getSize()
numList = [None] * size
populatelist(numList)
scramblelist(numList)
printElements(numList)
print("Sorting list...\n")
list1 = [1]
list2 = [2]
start = timer()
mergeSort(numList)
end = timer()
print("Elapsed Time: " + str(end-start) + " seconds")