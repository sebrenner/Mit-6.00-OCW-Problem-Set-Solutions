#!/usr/bin/env python
# encoding: utf-8
"""
Lectures 14-16 Readings.py

Created by Scott Brenner on 2011-03-06.
Copyright (c) 2011 Scott Brenner. All rights reserved.
"""

import sys
import os


# ========================================================
# = Chapter 12 of How to Think Like a Computer Scientist =
# ========================================================

def point_id():
    """
    As an exercise, create and print a Point object, and then use id to print the object’s unique identifier. Translate the hexadecimal form into decimal and confirm that they match.
    """
    class Point: pass
    my_point = Point()
    my_point.x = 7
    my_point.y = 21
    print my_point
    print hex(id(my_point))
    
    
def main():
	point_id()


if __name__ == '__main__':
	main()

