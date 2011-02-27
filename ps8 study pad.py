# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#
# Studypad Details:http://openstudy.com/studypads/Problem-Set-8-4c6bf092e6153a7f05c12e1e#
# ------------------------------------------------------------------------------------
# dynamic, greedy, and brute force algorithms

import time

SUBJECT_FILENAME = "my_subjects.txt"
SUBJECT_FILENAME = "subjects.txt"

VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
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

def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.
    
    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    valueWorkList = subjects.values()   # creates a list of values
    nameList = subjects.keys()          # creates a list of course names
    
    memo = {}
    
    #   Returns two results: valaue and selectedIndexes.  SelectedIndexes is a list of recommended class load. Value is the totaf value of the class load.
    value, selectedIndexes = dpAdvisorHelper(valueWorkList, len(valueWorkList)-1, maxWork, memo)
    
    advisedSubjects = {}
    for i in selectedIndexes :          # create advised subjects dcitionary from selectedIndexes list.
        subName = nameList[i]
        advisedSubjects[subName] = valueWorkList[i]
    return advisedSubjects

def dpAdvisorHelper(valueWorkList, i, aWork, memo) :
    """
    Finds the indexes of the elements in (value, work) list that lead to the
    maximum value subject to maximum work constraint.
    
    valueWorkList:      list of tuples (value, work)
    i:                  i-th element to consider, initially len(valueWorkList)-1
    aWork:              available workload limit, int >= 0
    memo:               dictionary to store already computed values
                            keys: (i, aWork) tuple
                            values: (maximum value, selectedIndexes) tuple
    selectedIndexes:    list of the indexes of the selected elements in
                        valueWorkList
    """
    # print '\nIn dpAdvisorHelper.'   ,'\nvalueWorkList', valueWorkList
    # print 'i:', i,
    # print 'a:', aWork,
    # print 'v[i]', valueWorkList[i],
    # print '\tmemo:', memo
    
    ##trying to make use of already computed values
    try : return memo[(i, aWork)]
    except KeyError :
        ith_value = valueWorkList[i][VALUE]
        ith_workload = valueWorkList[i][WORK]
        if i == 0 : ##end of recursion, a leaf node in the decision tree,
                    ##first element in the valueWorkList
            if ith_workload <= aWork :
                ##take the first element
                selectedIndexes = [0]
                memo[(i, aWork)] = ith_value, selectedIndexes
                return ith_value, selectedIndexes
            else : ##unable to take the first element
                selectedIndexes = []
                memo[(i, aWork)] = 0, selectedIndexes
                return 0, selectedIndexes        
        ##somewhere in the middle of the decision tree,
        ##computing value without the i-th element
        without_i, selectedIndexes = dpAdvisorHelper(valueWorkList, i-1, aWork, memo) ##left branch, do not take
        
        if ith_workload > aWork :
            memo[(i, aWork)] = without_i, selectedIndexes
            return without_i, selectedIndexes ##commited not to take the element
        else : ##compute value with the i-th element
            with_i, I = dpAdvisorHelper(valueWorkList, i-1, aWork-ith_workload, memo)
            with_i += ith_value
        ##compare the values with and without i-th element
        if with_i >= without_i :
            selectedIndexes = [i] + I
            maxValue = with_i
        else : ##do not take the i-th element
            maxValue = without_i
        memo[(i, aWork)] = maxValue, selectedIndexes
        return maxValue, selectedIndexes

def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...
    subjects = loadSubjects(SUBJECT_FILENAME)
    # print "subjects:", subjects
    test_maxWork = [30]
    for each in test_maxWork:
        print "maximum workload", each, '\n',
        startTime = time.time()
        selected = dpAdvisor(subjects, each)
        endTime = time.time()
        print endTime - startTime, "seconds."
        printSubjects(selected)

dpTime()