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
		swapElements(list, index, random.randint(0, len(list) - 1))

def swapElements(list, index1, index2):
	list[index1], list[index2] = list[index2], list[index1]

def bogoSort(list):
	global comparisons
	global swaps
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
	global comparisons
	global swaps
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
	global comparisons
	global swaps
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
	listF = list1 + list2
	size = len(listF)
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

def quickSort(list):
	print(quickDivide(list))

def quickDivide(list):
	pvt = quickPivot(list)
	list1 = list[0:pvt-1]
	list2 = list[pvt+1:list[len(list) - 1]]
	if (len(list) > 1):
		quickConquer(quickDivide(list1), quickDivide(list2), pvt)
	else:
		return quickConquer(list1, list2, pvt)

def quickConquer(list1, list2, pvt):
	listF = list1 + [pvt] + list2
	return listF

def quickPivot(list):
	middle = math.floor(len(list) / 2)
	#sorts array without creating a new array
	if (list[0] > list[-1]): 
		swapElements(list, 0, len(list) - 1)
	if (list[0] > list[middle]):
		swapElements(list, 0, middle)
	if (list[middle] > list[-1]):
		swapElements(list, middle, len(list) - 1)

	print(middle)
	printElements(list)
	return middle
size = getSize()
print("Generating list...\n")
numList = [None] * size
populatelist(numList)
scramblelist(numList)
printElements(numList)
print("Sorting list...\n")
list1 = [1]
list2 = [2]
start = timer()
quickSort(numList)
end = timer()
print("Elapsed Time: " + str(end-start) + " seconds (includes time to print)")