#!/usr/local/bin/python

##	Problem 2.  Write a program that computes the sum of the logarithms of all the primes from 2 to some number n, and print out the sum of the logs of the primes, the number n, and the ratio of these two quantities. Test this for different values of n.
## You should be able to make only some small changes to your solution to Problem 1 to solve this problem as well.
## Hints:  While you should see the ratio of the sum of the logs of the primes to the value n slowly get closer to 1, it does not approach this limit monotonically.

## Probably took two hours+ to make this work.


import math
from math import *


def next_odd_number(x):
	"""This function takes an odd number and returns the next odd number."""
	if x%2 == 0:
		print "Error: next_odd_number was pass an non-odd number."
		return None
	else:
		return x+2
		
def isPrime(x):
	"""This function takes an integer and returns a 1 if the number is prime and a 0 if it is not prime."""
	counter = 1
	while counter <= x/2:
		#print counter
		#print x/2
		counter = counter + 1
		#print counter
		if x%counter == 0:
			return 0
	return 1

def find_primes_up_to_n(n):
	"""This function takes a number, n, and returns the largest prime less than or equal to n."""
	#	start with the first candiate
	candidates = [1,3]  # 1,3,5,7,11,13,17,19

	#	start with the lowest known prime
	primes = [2]
	prime_sum = 0.0
	while primes[-1] <= n:
		if isPrime(candidates[-1]):
			primes.append(candidates[-1])
			prime_sum = prime_sum + math.log(primes[-1])
		next_candidate = next_odd_number(candidates[-1])
		candidates.append(next_candidate)

	primes = primes[0:-1]
	
	print 'N', n,'; the largest prime <=', n, 'is', primes[-1], ';Sum of logs:', prime_sum
	return prime_sum

# def compute_prime_sums(n):
# 	"""This function takes a number, n, and returns the sum of the logs of the primes numbers less than or equal to n."""
# 	highestprime
# 	
# 	prime_sum = 0
# 	for n in range(0,999):
# 		prime_sum = prime_sum + math.log(primes[n])
# 	print prime_sum
# 	return prime_sum


trials = [5,7,956,78,98,1454,3412,6789,23124]

for each in trials:
	answer = find_primes_up_to_n(each)
	print 'and the ratio of these two quantities is ', each / answer

