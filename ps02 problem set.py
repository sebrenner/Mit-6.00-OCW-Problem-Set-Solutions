#!/usr/local/bin/python

##	Problem 1.
	##	Show that it is possible to buy exactly 50, 51, 52, 53, 54, and 55 McNuggets, by finding solutions to the Diophantine equation. You can solve this in your head, using paper and pencil, or writing a program. However you chose to solve this problem, list the combinations of 6, 9 and 20 packs of McNuggets you need to buy in order to get each of the exact amounts.  Given that it is possible to buy sets of 50, 51, 52, 53, 54 or 55 McNuggets by combinations of 6, 9 and 20 packs, show that it is possible to buy 56, 57,..., 65 McNuggets. In other words, show how, given solutions for 50-55, one can derive solutions for 56-65.  If it is possible to buy x,x+1,...,x+5 sets of McNuggets,for some x,then it is possible to buy any number of McNuggets >= x, given that McNuggets come in 6, 9 and 20 packs.

	##	6a + 9b + 20c = n
	##	6a = n - 9b -20c 
	##	a = n/6 - 3/2b - 10/3c
	
	# 49 = (2*20) + (0*6) + (1*9)  # just curious
	# 50 = (1*20) + (2*6) + (2*9)
	# 51 = (0*20) + (4*6) + (3*9)
	# 52 = (2*20) + (2*6) + (0*9)
	# 53 = (1*20) + (1*6) + (3*9)
	# 54 = (0*20) + (0*6) + (6*9)
	# 55 = (2*20) + (1*6) + (1*9)
##------
	# 56 = (1*20) + (3*6) + (2*9)
	# 57 = (0*20) + (4*6) + (3*9)
	# 58 = (2*20) + (3*6) + (0*9)
	# 59 = (1*20) + (2*6) + (3*9)
	# 60 = (0*20) + (1*6) + (6*9)
	# 61 = (2*20) + (2*6) + (1*9)
	# 62 = (1*20) + (4*6) + (2*9)
	# 63 = (0*20) + (6*6) + (3*9)
	# 64 = (2*20) + (4*6) + (0*9)
	# 65 = (1*20) + (3*6) + (3*9)
	
#	Problem 2: Explain, in English, why this theorem is true.
## For this type of problem, if you can find a string of sequential numbers that is as long as the smallest counting unit then you can count to any subsequent number by adding this smallest counting unit a member of this base sequential series. Wow. 


# Problem 3
#
	#	Write an iterative program that finds the largest number of McNuggets that cannot be bought in exact quantity. Your program should print the answer in the following format (where the correct number is provided in place of <n>):

#	largest number of McNuggets that cannot be bought in exact quantity:
	#	Hint: your program should follow the outline above.
	#	Hint: think about what information you need to keep track of as you loop through possible ways of buying exactly n McNuggets. This will guide you in deciding what state variables you will need to utilize.
	#	Save your code for Problem 3 in ps2a.py.



#	Using this theorem, we can write an exhaustive search to find the largest number of McNuggets that cannot be bought in exact quantity. The format of the search should probably follow this outline:
#	Hypothesize possible instances of numbers of McNuggets that cannot be purchased exactly, starting with 1
#For each possible instance, called n,
	#Test if there exists non-negative integers a, b, and c, such that 6a+9b+20c = n. (This can be done by looking at all feasible combinations of a, b, and c) 
	#If not, n cannot be bought in exact quantity, save n
#	When you have found six consecutive values of n that in fact pass the test of having an exact solution, the last answer that was saved (not the last value of n that had a solution) is the correct answer, since you know by the theorem that any amount larger can also be bought in exact quantity

print 'Problem 3'
print

def is_n_solveable(n):
	a = 0
	b = 0
	c = 0
	for a in range(10):
		#print 'in a for loop. a:', a,'b:',b,'c:',c,'n:',n
		if 6*a + 9*b + 20*c == n:
			return 1
			#ns_passed_test.append(n)
			#print n, "passed"	
		for b in range(10):
			#print 'in b for loop. a:', a,'b:',b,'c:',c,'n:',n
			if 6*a + 9*b + 20*c == n:
				return 1
				#ns_passed_test.append(n)
				#print n, "passed"
			for c in range(10):
				#print 'in c for loop. a:', a,'b:',b,'c:',c,'n:',n
				if 6*a + 9*b + 20*c == n:
					return 1
					#ns_passed_test.append(n)
					#print n, "passed"
	return 0

counter = 0
highest_number_to_test = 43

for n in range(highest_number_to_test+7):
	if is_n_solveable(n):
		counter = counter + 1
	else:
		counter = 0

	if counter == 6:
		print n-6, "is highest number of nuggets that can not be ordered in a 6,9,20 combo."
	elif n == highest_number_to_test+7:
		print 'The highest number of noggest that cannot be ordereed in a in 6,9,20 combo is greater than', highest_number_to_test

print 
print 'End of problem 3'
print 

##	Problem 4.
##	Assume that the variable packages is bound to a tuple of length 3, the values of which specify the sizes of the packages, ordered from smallest to largest. Write a program that uses exhaustive search to find the largest number (less than 200) of McNuggets that cannot be bought in exact quantity. We limit the number to be less than 200 (although this is an arbitrary choice) because in some cases there is no largest value that cannot be bought in exact quantity, and we don't want to search forever. Please use ps2b_template.py to structure your code.
##	Have your code print out its result in the following format:
##	"Given package sizes <x>, <y>, and <z>, the largest number of McNuggets that cannot be bought in exact quantity is: <n>"

##	Test your program on a variety of choices, by changing the value for packages. Include the case (6,9,20), as well as some other test cases of your own choosing.

##	This problem took 4-5 hours over the course of a couple days.

print 'Problem 4'
print 

packages = (6, 9, 20)

def is_n_solveable(n,packages):
	"""Takes a value n and a 3-member tuple.  The tuple describes the three package size, e.g., 6, 9, 20 McNuggets. The function tests whether any combination of the packages will add up to exactly n."""

	a = 0
	b = 0
	c = 0
	for a in range(10):
		#print 'in a for loop. a:', a,'b:',b,'c:',c,'n:',n
		if packages[0]*a + packages[1]*b + packages[2]*c == n:
			return 1
			#ns_passed_test.append(n)
			#print n, "passed"	
		for b in range(10):
			#print 'in b for loop. a:', a,'b:',b,'c:',c,'n:',n
			if packages[0]*a + packages[1]*b + packages[2]*c == n:
				return 1
				#ns_passed_test.append(n)
				#print n, "passed"
			for c in range(10):
				#print 'in c for loop. a:', a,'b:',b,'c:',c,'n:',n
				if packages[0]*a + packages[1]*b + packages[2]*c == n:
					return 1
					#ns_passed_test.append(n)
					#print n, "passed"
	return 0

counter = 0	

x = 6
y = 9
z = 20

for n in range(100):
	if is_n_solveable(n, packages):
		counter = counter + 1
	else:
		counter = 0
	if counter == packages[0]:
		print 'Given package sizes', packages[0], ',', packages[1], ', and', packages[2], 'the largest number of McNuggets that cannot be bought in exact quantity is:', n-packages[0]
print		
print 'end of Problem 4'
print 

		
print 'Problem 4.1: the prescribed format.'

bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity

packages = (6,9,20)   # variable that contains package sizes
packages_1 = (16,19,20)   # variable that contains package sizes
packages_2 = (7,15,20)   # variable that contains package sizes
packages_3 = (9,12,20)   # variable that contains package sizes
packages_4 = (11,16,20)   # variable that contains package sizes
packages_5 = (4,9,16)   # variable that contains package sizes

six_packages = (packages,packages_1,packages_2,packages_3,packages_4,packages_5)
packages_to_test = len(six_packages)

def is_n_solveable(n,packages):
	"""Takes a value n and a 3-member tuple.  The tuple describes the three package size, e.g., 6, 9, 20 McNuggets. The function tests whether any combination of the packages will add up to exactly n."""
	a = 0	# Initialize the multiples of each package size.
	b = 0
	c = 0
	for a in range(10):
		# print 'in a for loop. a:', a,'b:',b,'c:',c,'n:',n
		# print packages[0]
		
		if packages[0]*a + packages[1]*b + packages[2]*c == n:
			return 1
			#ns_passed_test.append(n)
			#print n, "passed"	
		for b in range(10):
			#print 'in b for loop. a:', a,'b:',b,'c:',c,'n:',n
			if packages[0]*a + packages[1]*b + packages[2]*c == n:
				return 1
				#ns_passed_test.append(n)
				#print n, "passed"
			for c in range(10):
				#print 'in c for loop. a:', a,'b:',b,'c:',c,'n:',n
				if packages[0]*a + packages[1]*b + packages[2]*c == n:
					return 1
					#ns_passed_test.append(n)
					#print n, "passed"
	return 0

	
def test_multiple_pack_combos(packages):
	"""This function takes a tuple of tuples and tests each tuple to see what is the highest number of nuggets that cannot be exactly purchased by the packages sizes described in the tuples."""
	for n in range(1, 150):   # only search for solutions up to size 150
		## complete code here to find largest size that cannot be bought
		## when done, your answer should be bound to bestSoFar
		
		
		if is_n_solveable(n, packages):
			bestSoFar = bestSoFar + 1
		else:
			bestSoFar = 0
		
		if bestSoFar == packages[0]:
			print 'Given package sizes', packages[0], ',', packages[1], ', and', packages[2], 'the largest number of McNuggets that cannot be bought in exact quantity is:', n-packages[0]
			
for each in range(packages_to_test-1):
	#	print six_packages[each]
	test_multiple_pack_combos(six_packages[each])