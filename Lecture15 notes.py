#!/usr/bin/env python
# encoding: utf-8
"""
Lecture 15 notes.py

Created by Scott Brenner on 2011-02-28.
Copyright (c) 2011 Scott Brenner. All rights reserved.
"""

"""
Class notes:
    Shallow (object)equality is tested by 'is.' E.g., p1 is ps returns true if  both p1 and p2 point to the same instant; false if they point at different instants, even if the values are equal.
    Deep (value) equality tests the value. E.g., p1 = p2 returns true if the values are the same, regardless of whether they point to the same instance.
"""


import sys
import os


class cartesianPoint:
    pass

cp1 = cartesianPoint()  # Creates an instance of cartesianPoint = to cp1
cp2 = cartesianPoint()

cp1.x = 1.0
cp1.y = 2.0

cp2.x = 1.0
cp2.y = 3.0