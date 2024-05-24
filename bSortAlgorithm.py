list = [1, 6, 3, 9, 4, 7,2,9,5]

#This does not fully work, my own experiment with the bubble sort algorithm.
def bubbleSort(mylist):
	n = len(mylist)
	swapped = True
	if(swapped == True):
		for i in range(0, n):
			for j in range(n, 0):
				if(mylist[i] < mylist[j]):
					temp = mylist[i]
					mylist[i] = mylist[j]
					mylist[j] = temp
				else:
					swapped = False
					
	return mylist
					
					
list = bubbleSort(list)
print(list)
