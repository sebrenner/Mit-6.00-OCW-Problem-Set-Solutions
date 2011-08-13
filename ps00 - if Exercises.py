#!/usr/local/bin/python

guess_count=0
password = 'taco'

print ("This program requires a password.  You can only guess three times.")

while guess_count < 3:
	entry = raw_input("Password: ")
	if entry != password:
		guess_count = guess_count + 1
		if guess_count == 3:
			print ("You have been denied access.")
		else:
			print 'Wrong.'
	else:
		print ("You have successfully logged in.")
		guess_count = 3