#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Scott Brenner on 2011-02-25.
Copyright (c) 2011 Scott Brenner. All rights reserved.
"""

import sys
import os
import time
import string
from operator import itemgetter, attrgetter

#SUBJECT_FILENAME = "my_subjects.txt"
SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1
maxLoad = 15

def main():
    """
    Just some codes scraps to test an possible improvement to the sort() function.
    """
    def loadSubjects(filename):
        """
        Returns a dictionary mapping subject name to (value, work), where the name
        is a string and the value and work are integers. The subject information is
        read from the file named by the string filename. Each line of the file
        contains a string of the form "name,value,work".
        
        returns: dictionary mapping subject name to (value, work)
        """
        result = {}
        inputFile = open(filename)

        for line in inputFile:
            line = line.strip()
            line_as_list = line.split(',')
            result[line_as_list[0]] = (int(line_as_list[-2]),int(line_as_list[-1])) 
        return result

        # TODO: Instead of printing each line, modify the above to parse the name,
        # value, and work of each subject and create a dictionary mapping the name
        # to the (value, work).
    

    def printSubjects(subjects):
        """
        Prints a string containing name, value, and work of each subject in
        the dictionary of subjects and total value and work of all subjects
        """
        totalVal, totalWork = 0,0
        if len(subjects) == 0:
            return 'Empty SubjectList'
        res = 'Course\tValue\tWork\n======\t====\t=====\n'
        subNames = subjects.keys()
        subNames.sort()
        for s in subNames:
            val = subjects[s][VALUE]
            work = subjects[s][WORK]
            res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
            totalVal += val
            totalWork += work
        res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
        res = res + 'Total Work:\t' + str(totalWork) + '\n'
        print res


    def sort(subjects,sort_key,hi_low):
        """
        Takes a dictionary converts it to a list;
        swaps the key for the value;
        sorts by the value (high to low);
        then swaps value and key again.
        
        Returns a list of tuples that represent each dictionary entry sorted by value.
        
        subjects: dictionary mapping subject name to (value, work)
        sort_key: an int that represents the index of the tuple by which the list should be sorted, e.g., if sort_key = 1, then list will be sorted by work.
        hi_low: a boolean.  If true the list will be sorted high to low, otherwise it will be sorted low to high
        returns: list of subjects sorted by sort_key, ordered by hi_low
        
        """
        result = []
        items = subjects.items()
        items = sorted(items, key=lambda items: items[1][sort_key], reverse=hi_low)
        for i in items:
            result.append(i[0])
        return result
    
    def pare_subjects():
    	"""
    	Creates a list of courses to be considered.  It excludes the courses with workloads that exced the maxLoad.
    	"""
    	result =[]
    	for each in subjects:
    		if subjects[each][WORK] <= maxLoad:
    			result.append(each)
    	return result
    
    subjects = loadSubjects(SUBJECT_FILENAME)
    # printSubjects(subjects)
    work_list = sort(subjects,WORK,False)
    value_list = sort(subjects,VALUE,True)
    pared_list = pare_subjects()
    
    counter = 0
    for each in pared_list:
        counter += 1
        print counter,":", each, "\t", subjects[each][0], "\t", subjects[each][1]
    
    
    pass


if __name__ == '__main__':
    main()

