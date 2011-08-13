#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Scott Brenner on 2011-04-10.
Copyright (c) 2011 Scott Brenner. All rights reserved.
"""

import sys
import os

def findMedian(L):
	"""
	Finds median of L.
	L: a non-empty list of floats
	Returns: If L has an odd number of elements, returns the median element of L.  For example, if L is the list [15.0, 5.3, 18.2], returns 15.0.
	If L has an even number of elements, returns the average of the two median elements. For example, if L is the list [1.0, 2.0, 3.0, 4.0], returns 2.5.
	If the list is empty, raises a ValueError exception.
	Side effects: none.
	"""
	L_middle = len(L) / 2
	L_sorted = sorted(L)
	if len(L) % 2 == 0:		#	even case
	    median = (L_sorted[L_middle] + L_sorted[L_middle+1]) / 2
	else:
	    median = L_sorted[L_middle]
	return median




def main():
    l1 = [5,7,2,43,457,657,768,45,3425.56, 34.234,234.243,324.324,234]
    l2 = [5.453,7.435,342.435,443.433,457,657,768,45,3425.56, 34.234,234.243,324.324,234]
    l3 = [15.0, 5.3, 18.2]
    l4 = [1.0, 2.0, 3.0, 4.0]
    # print findMedian(l1)
    # print findMedian(l2)
    # print findMedian(l3)
    # print findMedian(l4)

    class Shape(object):
        def __cmp__(s1, s2):
            return cmp(s1.area(), s2.area())
    class Square(Shape):
        def __init__(self, h):
            self.side = float(h)
        def area(self):
            return self.side**2
        def __str__(self):
            return 'Square with side ' + str(self.side)
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
        def area(self):
            return 3.14159*(self.radius**2)
        def __str__(self):
            return 'Circle with radius ' + str(self.radius)
    def f(L):
        if len(L) == 0: return None
        x = L[0]
        for s in L:
            if s >= x:
                x = s
        return x

    s = Square(4)                     # Create a square, s, with height 4
    print s.area()                        # Print area of s = 16
    L = []                                # Create list L
    shapes = {0:Circle, 1: Square}        # Create dictionary with two keys.
    for i in range(10):               # loop ten times
        print i, i%2
        L.append(shapes[i%2](i))      # add objects from shapes dictionary L list
        print 
        print L
        print
    print L[4]
    print f(L)





if __name__ == '__main__':
	main()

