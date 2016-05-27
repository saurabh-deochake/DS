#!/bin/python

"""
Copyright 2016 Saurabh Deochake

1. Bubble Sort

O(n^2)
"""

def sort_bubblesort(my_list):

    for pos_upper in xrange(len(my_list)-1,0,-1):
        for i in xrange(pos_upper):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                print "pos_upper: " + str(pos_upper) + " i: " + str(i) + " my_list: " + str(my_list)
    return my_list

if __name__ == "__main__":

    my_list = [54,26,93,17,77,31,44,55,20]
    print my_list
    print sort_bubblesort(my_list)