#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Scott Brenner on 2011-02-25.
Copyright (c) 2011 Scott Brenner. All rights reserved.
"""

import sys
import os
numCalls = 0
num2Calls = 0

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
def maxVal(w, v, i, aW):
    """
    Returns the value of the optimal combination of items that doesn't exceed aW
    But what about the combination itself?  How do we get that?
    
    With this implementation this function is doing the same work over and over again.  For example it call maxVal with the same i, aW value many times.  Note that w and v are constant.
    
     """
    print 'maxVal called with:', i, aW
    global numCalls
    numCalls += 1
    
    # base case: check to see if we are at the end (starting at tail)
    if i == 0:                          # at end (starting at tail) of the vector
        if w[i] <= aW:                  # if there is room for it add it 
            return v[i]                 # return its value
        else: return 0                  # otherwise return 0, i.e., too big to take
    
    """
    do this if we are not at the end, starting at tail.
    don't select the current item move down the vector and 
    set without_i to the result of maxval of this next item
    this is the statement that recurses the function until it reaches the vase case case and begins returning back up the recursed functions.
    """
    without_i = maxVal(w, v, i-1, aW)
    
    
    """
    If the weight of i exceeds the availble work, then return the value of the previously evaluated item (the item closer to the 0th item).  Basically, if there isn't room for this item then the
    """
    if w[i] > aW:
        return without_i
    else:
        with_i = v[i] + maxVal(w, v, i-1, aW - w[i])
    return max(with_i, without_i)

def tryMaxVal():
    w = [1,5,3,2,4]
    v = [15,10,9,5,5]
    
    # w = [1,2,3,4,1,2,3,4]
    # v = [15,10,9,5,15,10,9,5]
    # w = [7,4,3,4,5,6,7,8,8,9,9,5,1,1,9,15,15,10,12,5,9,5,19,15,9,1,5,3,4,1,5,3,4,9,5,9,5,9,5,15,10,15,10,15,10,5,15,10]
    #     v = [9,1,5,3,4,1,5,3,4,9,5,9,5,9,5,15,10,15,10,15,10,5,15,10,7,4,3,4,5,6,7,8,8,9,9,5,1,1,9,15,15,10,12,5,9,5,19,15]
    
    res = maxVal(w,v,len(v)-1,7)
    print 'max val =', res, 'number of calls = ',numCalls


def maxVal0(w, v, i, aW):
    """
    Returns a schedule optimized by value that is equal to less that the maxload (aW).  It takes two vectors describing a course schedule--one describes the work load, the other describes the value of each course.   i is the length of the course catalog/vectors.
    
    SCOTT: CONSIDER ADDING a procedure that reduces the length catalog by elmiinating class with workloads that exceed max work.  Also consider simplifying this function to just take the catalog and aW. That way the prep work can be 'hidden' from the user.
    """
    print "in maxVal0"
    m = {}
    return fastMaxVal(w, v, i, aW, m)

def fastMaxVal(w, v, i, aW, m):
    """
    Returns a schedule optimized by value that is equal to less that the maxload (aW).  It takes two vectors describing a course schedule--one describes the work load, the other describes the value of each course.   i is the index of the currect class being evaluated.
    The functions uses a decision tree to evaluate build every option and then the optimal option is chosen.
    
    w: a list of workloads for each available class.
    v: a list of values for each available class
    i: index; length of vectors
    
    *** This function returns the highes value but how do you find the i's that were choosen.  SUGGESTION:  as each itme is taken along the take branch add the i (index) to a dictionary called best choice. 
    
    """
    global num2Calls
    num2Calls += 1
    
    #   Check if this index, remaining workload pair has been evaluated.
    #   If it has, return the previously calculated result(~vi).
    try: return m[(i, aW)]      #   use the try: except scheme because attempting to access a key that doesn't exist returns an error
    except KeyError:
        
        ################ Base case.  
        if i == 0:
            if w[i] <= aW:          # If there is a enough aW for the w[0] then
                m[(i, aW)] = v[i]   # create dictionary entry for 0th, aw with value of 0th itme
                return v[i]         # return value of 0th itme
            else:
                m[(i, aW)] = 0      # not enough room in aW for 0th item, return 0
                return 0
                
        ################ Recurse with the next item closer to 0th.
        ################ This is basically builing the results for all the don't-take branches.
        without_i = fastMaxVal(w, v, i-1, aW, m)    #   Set without_i to the value returned by fastMaxVal for the next i.
        
        if w[i] > aW:               # If there isnt a enough w[i] then
            m[(i, aW)] = without_i  # This is a dead end with this aW.  Make a dictionary entry.
            return without_i        # Return value of of path to this point.
            
        else:               # There is room in aW for w[i].
            #   Recursibely build the do-take branches
            #   Set with_i value to value of just selected item and add the value of the downstream branch/decisions.
            with_i = v[i] + fastMaxVal(w, v, i-1, aW - w[i], m)
        res = max(with_i, without_i)    # Decide whether choosing the item produces a higher value than not choosing the item.
        m[(i, aW)] = res                # Add a dictionary key for the better decision.
        return res                      # Return the higher value.



def tryMaxVals(n):
    w = [1,5,3,2,4]
    v = [15,10,9,5,5]
    w = [2,1,2,3,4,1,2,3,4]
    v = [8,15,10,9,5,15,10,9,5]
    # w = [7,4,3,4,5,6,7,8,8,9,9,5,1,1,9,15,15,10,12,5,9,5,19,15,9,1,5,3,4,1,5,3,4,9,5,9,5,9,5,15,10,15,10,15,10,5,15,10]
    # v = [9,1,5,3,4,1,5,3,4,9,5,9,5,9,5,15,10,15,10,15,10,5,15,10,7,4,3,4,5,6,7,8,8,9,9,5,1,1,9,15,15,10,12,5,9,5,19,15]
    
    # res = maxVal(w,v,len(v)-1,n)
    # print 'max val =', res, 'number of calls = ',numCalls
    
    res = maxVal0(w,v,len(v)-1,n)
    print 'max val =', res, 'number of calls = ',num2Calls

tryMaxVals(7)