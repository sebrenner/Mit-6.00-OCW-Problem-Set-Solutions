from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

########## Define the string/constants ##########
#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'


# Problem 2.
# Write the function subStringMatchExact. This function takes two arguments: a target string, and a key string. It should return a tuple of the starting points of matches of the key string in the target string, when indexing starts at 0. Complete the definition for:

########## Define the functions ##########
def subStringMatchExact(target,key):
	"""Returns a tuple of the starting point for each key in target.  For example, subStringMatchExact("atgacatgcacaagtatgcat","atgc") would return the tuple (5, 15)."""
	answer_tuple = () # initialize the tuple we will return
	start = 0 # use this initial the starting point for find()
	while find(target, key, start) >=0:
		if find(target, key, start) == -1:
			return answer_tuple
		elif find(target, key, start) >=0:
			start = find(target, key, start)
			answer_tuple += (start,)
			start+=1
	return answer_tuple
	


# failed attempt at recursive solution
# def subStringMatchExact(target,key):
# 	"""Returns a tuple of the starting point for each key in target.  For example, subStringMatchExact("atgacatgcacaagtatgcat","atgc") would return the tuple (5, 15)."""
# 	answer_tuple = ()
# 	matching_point = find(target, key)
# 	# print matching_point
# 	if matching_point == -1 :
# 		return answer_tuple
# 	elif matching_point >= 0 :
# 		answer_tuple += (matching_point,)
# 		newstring = target[matching_point:]
# 		#		new_tuple = subStringMatchExact(newstring,key)
# 	return	answer_tuple += (65,)
	
########## Run the code ##########	

# print 'target1:',target1
# print 'target1[4]:',target1[4:]
# 
# test_tuple = ()  # an empty tuple
# test_tuple2 = (15,67,64)  # create a new test_tuple with 7 append to the end.
# print 'an empty test_tuple', test_tuple
# test_tuple += (7,)  # create a new test_tuple with 7 append to the end.
# print 'an test_tuple with appendages', test_tuple
# test_tuple += test_tuple2  # create a new test_tuple with  append to the end.
# print 'an test_tuple with appendages', test_tuple

#answer_tuple += (next_starting_point,)	
print subStringMatchExact(target1,key10)
print subStringMatchExact(target1,key11)
print subStringMatchExact(target1,key12)
print subStringMatchExact(target1,key13)
 	
print subStringMatchExact(target2,key10)
print subStringMatchExact(target2,key11)
print subStringMatchExact(target2,key12)
print subStringMatchExact(target2,key13)

### This problem took awhile to solve.  I am not confident I "got" the lesson being taught.  I think I stumbled, through trial and error, into a working function.  I can walk through the function, but I couldn't really write it from scratch.

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