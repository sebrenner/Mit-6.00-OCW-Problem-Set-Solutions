#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Scott Brenner on 2011-02-25.
Copyright (c) 2011 Scott Brenner. All rights reserved.
"""

import sys
import os

## This code does not produce the correct answer.
def fib(n):
    global numCalls
    numCalls += 1
    print 'fib called with', n
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib1(n):
    memo = {0:1,1:1}
    return fastFib(n,memo)

def fastFib(n, memo):
    global numCalls
    numCalls += 1
    print 'fib1 called with', n
    if not n in memo:
        memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
    return memo[n]

# numCalls = 0
# n = 16
# res = fib(n)
# print 'fib of %i = %i. \tnumbCalls = %i.' %(n, res, numCalls)
# numCalls = 0
# res = fib1(n)
# print 'fib of %i = %i. \tnumbCalls = %i.' %(n, res, numCalls)



# dynamic programming functions from lecture handout

def maxVal0(w, v, i, aW):
    """
    Returns a schedule optimized by value that is equal to less that the maxload (aW).  It takes two vectors describing a course schedule--one describes the work load, the other describes the value of each course.   i is the length of the course catalog/vectors.
    
    SCOTT: CONSIDER ADDING a procedure that reduces the length catalog by elmiinating class with workloads that exceed max work.  Also consider simplifying this function to just take the catalog and aW. That way the prep work can be 'hidden' from the user.
    """
    m = {}
    return fastMaxVal(w, v, i, aW, m)

def fastMaxVal(w, v, i, aW, m):
    """
    Returns a schedule optimized by value that is equal to less that the maxload (aW).  It takes two vectors describing a course schedule--one describes the work load, the other describes the value of each course.   i is the index of the currect class being evaluated.
    The functions uses a decision tree to evaluate build every option and then the optimal option is chosen.
    
    w: a list of workloads for each available class.
    v: a list of values for each available class
    i: index; length of vectors
    """
    global numCalls
    numCalls += 1
    try: return m[(i, aW)]
    except KeyError:
        if i == 0:
            if w[i] <= aW:
                m[(i, aW)] = v[i]
                return v[i]
            else:
                m[(i, aW)] = 0
                return 0
        without_i = fastMaxVal(w, v, i-1, aW, m)
        if w[i] > aW:
            m[(i, aW)] = without_i
            return without_i
        else:
            with_i = v[i] + fastMaxVal(w, v, i-1, aW - w[i], m)
        res = max(with_i, without_i)
        m[(i, aW)] = res
        return res
