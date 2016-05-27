#!/bin/python

"""
Copyright 2016 Saurabh Deochake

3. Insertion Sort

Insert and element in already sorted subsequence
Time: O(n^2)
Space: O(1)
"""

def insertion_sort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

    return arr



if __name__ == "__main__":
	my_list = [54,26,93,17,77,31,44,55,20]
	print "Original List:", my_list
	print "Sorted List:", insertion_sort(my_list)