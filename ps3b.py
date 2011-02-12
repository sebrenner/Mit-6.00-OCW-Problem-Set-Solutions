# Problem Set 3 (Problem 2)
# Name: Scott Brenner
# Collaborators: None
# Date: 2011-02-01
# Start Time: 11:29 AM
# End Time: 12:04 PM
# I reused code I had drafted earlier.

#!/usr/local/bin/python

from string import *		#	used for find()


# Problem 2.
# Write the function subStringMatchExact. This function takes two arguments: a target string, and a key string. It should return a tuple of the starting points of matches of the key string in the target string, when indexing starts at 0. Complete the definition for

#	def subStringMatchExact(target,key):

#	For example, would return the tuple (5, 15). The file ps3_template.py includes some test strings that you can use to test your function. In particular, we provide two target strings and four key strings.  Test your function on each combination of key and target string, as well as other examples that you create. Place your answer in a file named ps3b.py

#	Targets and keys
target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'


def subStringMatchExact (target, key):
	"""This function returns a tuple of the starting position(s) of a key string within a target string"""
	answer_tuple = () # initialize the tuple we will return
	start = 0 # use this initial the starting point for find()
	while find(target, key, start) >=0:
		start = find(target, key, start)
		answer_tuple += (start,)
		start+=1
	return answer_tuple
	
####	Run Program with a variety of strings and keys	####
print "atgacatgcacaagtatgcat", "atgc"
print subStringMatchExact("atgacatgcacaagtatgcat", "atgc")
print target1, key10
print subStringMatchExact(target1, key10)
print target1, key11
print subStringMatchExact(target1, key11)
print target1, key12
print subStringMatchExact(target1, key12)
print target1, key13
print subStringMatchExact(target1, key13)
print target2, key10
print subStringMatchExact(target2, key10)
print target2, key11
print subStringMatchExact(target2, key11)
print target2, key12
print subStringMatchExact(target2, key12)
print target2, key13
print subStringMatchExact(target2,key13)
