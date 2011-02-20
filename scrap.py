#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Scott Brenner on 2011-02-18.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import random
import string
import time

##  create all subsets of 'windows'

word = 'windows'
list_of_submultisets = []

for i in word:
    print
    print i,
    #list_of_submultisets += [i]
    for j in word[1:]:
        print j
    #     for k in word[2:]:
    #         list_of_submultisets += [i+j+k]
    #         for l in word[3:]:
    #             list_of_submultisets += [i+j+k+l]
    #             for m in word[4:]:
    #                 list_of_submultisets += [i+j+k+l+m]
    #                 for n in word[5:]:
    #                     list_of_submultisets += [i+j+k+l+m+n]
    #                     for o in word[6:]:
    #                         list_of_submultisets += [i+j+k+l+m+n+o]
#print list_of_submultisets 