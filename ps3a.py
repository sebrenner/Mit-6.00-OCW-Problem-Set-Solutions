# Problem Set 3 (Problem 1)
# Name: Scott Brenner
# Collaborators: None
# Date: 2011-01-29
# Time: 2:45 PM
#

#!/usr/local/bin/python

from string import *		#	used for find()


# Problem 1.
# Write two functions, called countSubStringMatch and countSubStringMatchRecursive that take two arguments, a key string and a target string. These functions iteratively and recursively count the number of instances of the key in the target string. You should complete definitions for
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