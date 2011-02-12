# Problem Set 3 (Part I)
# Name: Scott Brenner
# Collaborators: None
# Date: 2011-01-29
# Time: 2:45 PM
#

#!/usr/local/bin/python

from string import *		#	used for find()


# Problem 1.
# Write two functions, called countSubStringMatch and countSubStringMatchRecursive that take two arguments, a key string and a target string. These functions iteratively and recursively count the number of instances of the key in the target string. You should complete definitions for
print 'Begin problem 1'
#	Targets and keys
target = "atgacatgcacaagtatgcat"
key = "atgc"


def countSubStringMatch(target,key):
	"""This function returns the number of times a key string appears in target string.  This function iterates through the taret string."""
	count = 0
	start = 0
	while find(target, key, start) != -1:
		count += 1
		start = find(target, key, start) + 1
	return count


def countSubStringMatchRecursive (target, key):
	"""This function returns the number of times a key string appears in target string.  This function uses recursion."""
	answer = 0
	next_match = find(target,key)
	if next_match == -1:
		return answer
	else:
		answer = 1 + countSubStringMatchRecursive(target[next_match+1:], key)
		return answer

print countSubStringMatch(target,key)
print countSubStringMatchRecursive(target,key)
print 'End problem 1'
print









# def countSubStringMatch(target,key):
# 	"""This function returns a tuple of the starting position(s) of a key string within a target string"""
# 	count = 0
# 	answer = ()
# 	next_match = find(target,key)
# 
# 	
# 	
# 	while next_match != -1:
# 		##	This while loop will loop until find() returns a -1.  So as find returns a value other than -1 the next_match will be appended to the answer tuple.  Note that find() within the while loop takes a third argument.  This is the starting point for the next find().  Without it the function would return the starting point count from the last match, not from the start of the target string.
# 		
# 		answer += (next_match,)	
# 		next_match = find(target,key,next_match+1)
# 	return answer
# 
# 
# 
# def countSubStringMatchRecursive (target, key):
# 	"""This function returns a tuple of the starting position(s) of a key string within a target string"""
# 	answer = ()		#	the tuple that will be returned
# 	next_match = find(target,key)
# 	if next_match == -1:
# 		return ()
# 	else:
# 		if answer == ():
# 			holder = next_match
# 		else:
# 			holder = answer[-1] + next_match
# 			print 'in else'
# 		answer += (holder,)
# 		answer += countSubStringMatchRecursive(target[next_match+1:], key)
# 		return answer

