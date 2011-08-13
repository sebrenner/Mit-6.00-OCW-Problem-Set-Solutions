#!/usr/local/bin/python

##	Problem 1.  Write a program that computes and prints the 1000th prime number.
## This problem took just over one hour to program.

#	start with the first candiate
candidates = [1,3]

#	start with the know primes
primes = [2]

def next_odd_number(x):
	if x%2 == 0:
		print "Error: next_odd_number was pass an non-odd number."
		return None
	else:
		return x+2
		
def isPrime(x):
	counter = 1
	while counter <= x/2:
		#print counter
		#print x/2
		counter = counter + 1
		#print counter
		if x%counter == 0:
			return 0
	return 1

test9 = 9
test11 = 11
test15 = 15

# print test9, isPrime(test9)
# print test11, isPrime(test11)
# print test15, isPrime(test15)


while len(primes) <= 1000:
	if isPrime(candidates[-1]):
		#print candidates[-1], 'is prime'
		primes.append(candidates[-1])
		#print primes
	#else:
		#print candidates[-1], 'is not prime'
	next_candidate = next_odd_number(candidates[-1])
	candidates.append(next_candidate)
print primes[999]
print 'end of Problem 1.'
print
print

##	Problem 2.  Write a program that computes the sum of the logarithms of all the primes from 2 to some number n, and print out the sum of the logs of the primes, the number n, and the ratio of these two quantities. Test this for different values of n.
## You should be able to make only some small changes to your solution to Problem 1 to solve this problem as well.
## Hints:  While you should see the ratio of the sum of the logs of the primes to the value n slowly get closer to 1, it does not approach this limit monotonically.

## This problem took less than one hour to solve.  2011-01-20

print 'Begining of Problem 2.'

import math
from math import *

prime_sum = 0
for n in range(0,999):
	#prime_log = math.log(primes[n])
	prime_sum = prime_sum + math.log(primes[n])
print prime_sum


# product = 1
# for n in range(0,1000):
#      product = product * primes[n]
# 
# print product
