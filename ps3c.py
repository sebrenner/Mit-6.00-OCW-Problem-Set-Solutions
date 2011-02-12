# Problem Set 3 (Problem 3)
# Name: Scott Brenner
# Collaborators: None
# Date: 2011-02-01
# Time: 11:29 AM
#

#!/usr/local/bin/python

from string import *		#	used for find()


# Problem 3.
# Write a function, called constrainedMatchPair which takes three arguments: a tuple representing starting points for the first substring, a tuple representing starting points for the second substring, and the length of the first substring. The function should return a tuple of all members (call it n) of the first tuple for which there is an element in the second tuple (call it k) such that n+m+1 = k, where m is the length of the first substring. Complete the definition

# To test this function, we have provided a function called subStringMatchOneSub, which takes two arguments: a target string and a key string. This function will return a tuple of all starting points of matches of the key to the target, such that at most one element of the key is incorrectly matched to the target. This function is provided for you in the file ps3_template.py and invokes the function you are to write. Save your answers in a file named ps3c.py.

# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
#		   01234567890123456789
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg' 	# matches in target1 == (0, 5, 15)	length == 3
key12 = 'atgc'	# matches in target1 == (5, 15)
key13 = 'atgca'


#### This is the method I defined.  ####
def constrainedMatchPair(firstMatch,secondMatch,length):
	"""This function takes three arguments: a tuple representing starting points for the first substring, a tuple representing starting points for the second substring, and the length of the first substring. The function should return a tuple of all members (call it n) of the first tuple for which there is an element in the second tuple (call it k) such that n+m+1 = k, where m is the length of the first substring."""
	answer = ()
	for i in firstMatch:
		for j in secondMatch:
			if i + length + 1 == j:
				answer += (i,)
	return answer

#### This is the method I defined in the earlier problem.  ####
def subStringMatchExact (target, key):
	"""This function returns a tuple of the starting position(s) of a key string within a target string"""
	answer_tuple = () # initialize the tuple we will return
	start = 0 # use this initial the starting point for find()
	while find(target, key, start) >=0:
		start = find(target, key, start)
		answer_tuple += (start,)
		start+=1
	return answer_tuple

### the following procedure you will use in Problem 3


def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers

print subStringMatchOneSub(key11,target1)