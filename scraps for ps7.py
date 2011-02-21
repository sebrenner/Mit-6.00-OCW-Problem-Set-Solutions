#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Scott Brenner on 2011-02-18.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import time

def fact0(i):
	"""
	Takes and int and returns the factorial of that int.
	Recursive.
	"""
	
	assert type(i) == int and i >= 0
	if i == 0 or i == 1:
		return 1
	return i * fact0(i-1)

test_range = range(2,200)

start_time = time.time()
for i in test_range:
    fact0(i)
end_time = time.time()
print "Total time to complete fact0(i):", end_time - start_time

def fact1(i):
	"""
	Takes and int and returns the factorial of that int.
	Use a while loop.
	"""
	
	assert type(i) == int and i >= 0
	res = 1
	while i > 1:
		res = res * i
		i -= 1
	return res

start_time = time.time()
for i in test_range:
    fact1(i)
end_time = time.time()
print "Total time to complete fact1(i):", end_time - start_time

def makeSet(s):
    """
    Takes a string and returns a set of the string.  I.e., it removes any duplicates.
    """
    assert type(s) == str
    res = ''
    for c in s:
        if not c in res:
            res = res + c
    return res

i = 'aklf sfea'

start_time = time.time()
makeSet(i)
end_time = time.time()
print "Total time to complete makeSet(i):", end_time - start_time

def intersect(s1, s2):
	"""
	Takes two strings and returns a strings of all the characters that appear in both strings.
	"""
	assert type(s1) == str and type(s2) == str
	s1 = makeSet(s1)
	s2 = makeSet(s2)
	res = ''
	for e in s1:
		if e in s2:
			res = res + e
	return res
s2 = "missy"
s1 = "mississipi"
start_time = time.time()
print intersect(s1, s2)
end_time = time.time()
print "Total time to complete intersect(s1, s2):", end_time - start_time


def swap0(s1, s2):
    assert type(s1) == list and type(s2) == list
    print 'In swap0. s1, s2:', s1, s2
    tmp = s1[:]
    print 'In swap0. s1, s2, tmp:', s1, s2, tmp
    s1 = s2[:]
    print 'In swap0. s1, s2, tmp:', s1, s2, tmp
    s2 = tmp
    print 'In swap0. s1, s2, tmp:', s1, s2, tmp
    return

s1 = [1]
s2 = [2]
print 's1, s2:', s1, s2
swap0(s1, s2)
print s1, s2

def rev(s):
	assert type(s) == list
	for i in range(len(s)/2):
		tmp = s[i]
		s[i] = s[-(i+1)]
		s[-(i+1)] = tmp
s =	[1,2,3]
rev(s)
print s



