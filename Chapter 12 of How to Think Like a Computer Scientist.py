#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Scott Brenner on 2011-03-01.
Copyright (c) 2011 Scott Brenner. All rights reserved.
"""

import sys
import os


def main():
    class Point:
        pass
    class Rectangle:
        pass
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0
    def findCenter(box):
        p = Point()
        p.x = box.corner.x + box.width / 2.0
        p.y = box.corner.y - box.height / 2.0
        return p
    def growRect(box, dwidth, dheight):
        box.width = box.width + dwidth
        box.height = box.height + dheight
    
    def moveRect(rectangle, dx, dy):
        """
        As an exercise, write a function named moveRect that takes a Rectangle and two parameters named dx and dy. It should change the location of the rectangle by adding dx to the x coordinate of corner and adding dy to the y coordinate of corner.
        """
        rectangle.corner.x = rectangle.corner.x + dx
        rectangle.corner.y = rectangle.corner.y + dy
    
    print box.corner.x,box.corner.y
    print moveRect(box, 5, 11)
    print box.corner.x, box.corner.y
    
    
if __name__ == '__main__':
	main()

