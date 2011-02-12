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
print "Begin problem 2"
########## Define the functions ##########
def subStringMatchExact(target,key):
	"""Returns a tuple of the starting point for each key in target.  For example, subStringMatchExact("atgacatgcacaagtatgcat","atgc") would return the tuple (5, 15)."""
	answer_tuple = () # initialize the tuple we will return
	start = 0 # use this initial the starting point for find()
	while find(target, key, start) >=0:
		if find(target, key, start) == -1:
			print "in if"
			return answer_tuple
		elif find(target, key, start) >=0:
			print "in elif"
			start = find(target, key, start)
			answer_tuple += (start,)
			start+=1
	return answer_tuple
	
########## Run the code ##########	

print subStringMatchExact(target1,key10)
print subStringMatchExact(target1,key11)
print subStringMatchExact(target1,key12)
print subStringMatchExact(target1,key13)
 	
print subStringMatchExact(target2,key10)
print subStringMatchExact(target2,key11)
print subStringMatchExact(target2,key12)
print subStringMatchExact(target2,key13)
# 
### This problem took awhile to solve.  I am not confident I "got" the lesson being taught.  I think I stumbled, through trial and error, into a working function.  I can walk through the function, but I couldn't really write it from scratch.

### the following procedure you will use in Problem 3

print 'End problem 2'
print
print 'Begin problem 3'
# Problem 3.
# Write a function, called constrainedMatchPair which takes three arguments: a tuple representing starting points for the first substring, a tuple representing starting points for the second substring, and the length of the first substring. The function should return a tuple of all members (call it n) of the first tuple for which there is an element in the second tuple (call it k) such that n+m+1 = k, where m is the length of the first substring. Complete the definition

#	n+m+1 = k  :::::>   firstMatch[0] + length + 1 = secondMatch[0]

def constrainedMatchPair(firstMatch,secondMatch,length):
	answer_tuple = ()  # initialize our answer as an empty tuple

	len_firstMatch = len(firstMatch) # get the length of the two tuples to match
	len_secondMatch = len(secondMatch)

	for j in range(len_firstMatch):
		for k in range(len_secondMatch) :
			if firstMatch[j] + length + 1 ==  secondMatch[k] :
				answer_tuple += (firstMatch[j],)
	return answer_tuple

#print constrainedMatchPair((0,5,14,26),(6,18,20),5)

target = 'atgaatgcatggatgtaaatgcag'
key_full = 'atgc'
key1 = 'at'
key2 = 'c'

starts1 = subStringMatchExact(target,key1) 	# Returns a tuple of the starting points of exact matches
starts2 = subStringMatchExact(target,key2)

length = len(key_full)
print 'target', target
print key_full
print key1
print key2
print 'starts1', starts1
print 'starts2', starts2
print 'length', length
answer = constrainedMatchPair(starts1, starts2, length)
print 'answer:' , answer

for t in range(len(answer)):
	print target[answer[t]:answer[t]+length+1]

# To test this function, we have provided a function called subStringMatchOneSub, which takes two arguments: a target string and a key string. This function will return a tuple of all starting points of matches of the key to the target, such that at most one element of the key is incorrectly matched to the target. This function is provided for you in the file ps3_template.py and invokes the function you are to write.

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
    
    
# 			print 'firstMatch[n]:', firstMatch[n]
# 			print 'secondMatch[m]:',secondMatch[m]
# 			print 'length:', length
