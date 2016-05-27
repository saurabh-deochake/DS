#!/bin/python

""" 
Copyright 2016 Saurabh Deochake

2. Selection Sort

Select smallest element and swap with element at min_index
Time: O(n^2)
Space: O(1)

"""

def selection_sort(A):
	for i in range(len(A)):
		min_index = i
		for j in range((i+1), len(A)):
			if A[j] < A[min_index]:
				min_index = j

		A[i], A[min_index] = A[min_index], A[i]
	return A


if __name__ == "__main__":
	my_list = [54,26,93,17,77,31,44,55,20]
	print "Original List:", my_list
	print "Sorted List:", selection_sort(my_list)