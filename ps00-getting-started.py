#!/usr/local/bin/python

import math

print "Hello, Python!"

print "Exercise #1"
var_calc=math.pow(23.0,5)
print var_calc


print "Exercise #2"


var_a = 34
var_b = 68
var_c = -510

#print var_a
#print var_b
#print var_c

var_to_sqrt = (var_b**2) - (4 * var_a * var_c)

var_sqrt = math.sqrt(var_to_sqrt)
var_calc1 = (-var_b + var_sqrt) / 2 * var_a
var_calc2 = (-var_b - var_sqrt) / 2 * var_a

if var_calc1 > var_calc2: print var_calc1
else: print var_calc2
