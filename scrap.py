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


def fib1(n):
    global memo
    global numCalls
    numCalls = 0 
    numCalls += 1
    if not n in memo:
        memo[n] = fib1(n-1) + fib1(n-2)
    return memo[n]
memo = {0:0, 1:1}

print fib1(25)
print memo

def msum(a):
    return max(
        [
            (sum(a[j:i]), (j,i)) for i in range(1,len(a)+1) for j in range(i)
        ]
    )

print
print msum([-9,2,3,4,-5,1,12,-4,6,7,2,3,-34,4,])



def msum2(a):
    bounds, s, t, j = (0,0), -float('infinity'), 0, 0
    print
    print a
    
    for i in range(len(a)):
        print "i: %i, t:%i, a[i]: %i, j:%s, s:%s, bounds:%s." %(i,t,a[i], j, s, bounds)
        t = t + a[i]
        if t > s: bounds, s = (j, i+1), t
        if t < 0: t, j = 0, i+1
    return (s, bounds)

print msum2([-9,2,3,4,-5,1,12,-4,6,7,2,3,-34,4,19])


def A(w, v, i,j):
    if i == 0 or j == 0:
        return 0
    if w[i-1] > j:
        return A(w, v, i-1, j)
    if w[i-1] <= j:
        return max(A(w,v, i-1, j), v[i-1] + A(w,v, i-1, j - w[i-1]))