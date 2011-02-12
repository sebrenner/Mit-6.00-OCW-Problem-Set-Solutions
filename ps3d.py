# Problem Set 3 (Problem 4)
# Name: Scott Brenner
# Collaborators: None
# Date: 2011-02-01
# Time: 11:29 AM
#

#!/usr/local/bin/python

from string import *		#	used for find()


# Problem 4
# Write a function, called subStringMatchExactlyOneSub which takes two arguments: a target string and a key string. This function should return a tuple of all starting points of matches of the key to the target, such that at exactly one element of the key is incorrectly matched to the target. Complete the definition.  Save your answers in a file named ps3d.py.

target1 = 'atgacatgcacaagtatgcat'
#		   01234567890123456789
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg' 	# matches in target1 == (0, 5, 15)	length == 3
key12 = 'atgc'	# matches in target1 == (5, 15)
key13 = 'atgca'



def subStringMatchExactlyOneSub(target,key):
	"""This function takes two arguments: a target string and a key string. It returns a tuple of all starting points of matches of the key to the target, such that at exactly one element of the key is incorrectly matched to the target."""

	possible_answer = subStringMatchOneSub(key,target)
	answer = possible_answer
	perfect_matches = subStringMatchExact(target,key)
	to_remove_from_answer = ()

	#	this for loop identifies the positions in possible_answer that contain perfect matches.
	for i in range(0,len(possible_answer)):
		for j in range(0,len(perfect_matches)):
			if possible_answer[i] == perfect_matches[j]:
#				print "matches:", possible_answer[i]
				to_remove_from_answer += (i,)
#				print to_remove_from_answer
	# this for loop removes the items from the possible_answer tuple begin at the end and working forward. 
	for m in to_remove_from_answer:
		print to_remove_from_answer[-m]
		answer = to_remove_from_answer[-m]
		print answer
	return to_remove_from_answer


def constrainedMatchPair(firstMatch,secondMatch,length, excluded):  
	"""This function takes four arguments: a tuple representing starting points for the first substring, a tuple representing starting points for the second substring, and the length of the first substring; and a tuple representing the starting point of perfect matches.
	
	The function returns a tuple of all members (call it n) of the first tuple for which there is an element in the second tuple (call it k) such that n+m+1 = k, where m is the length of the first substring, the starting points of perfect matches are omitted."""
	
	answer = ()
	matches = False 
	for i in firstMatch:
		for j in secondMatch:
			if i + length + 1 == j:
				for t in excluded:
					if i == t :
						matches = True
				if matches == False:
					answer += (i,)
	return answer

def subStringMatchExact(target, key):
	"""This function returns a tuple of the starting position(s) of a key string within a target string"""
	answer_tuple = () # initialize the tuple we will return
	start = 0 # use this initial the starting point for find()
	while find(target, key, start) >=0:
		start = find(target, key, start)
		answer_tuple += (start,)
		start+=1
	return answer_tuple

def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        #print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        # and we need to remove the starting points of perfect matchs.
        perfect_matches = subStringMatchExact(target, key)
        filtered = constrainedMatchPair(match1,match2,len(key1), perfect_matches)

        allAnswers = allAnswers + filtered
        #print 'match1',match1
        #print 'match2',match2
        #print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers
    
print subStringMatchOneSub(key12, target1)