# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name: Scott Brenner
# Collaborators: http://openstudy.com/studypads/Problem-Set-8-4c6bf092e6153a7f05c12e1e
# Time: problem 1: 20 minutes
#

import time
import string
from operator import itemgetter, attrgetter

SUBJECT_FILENAME = "my_subjects.txt"
#SUBJECT_FILENAME = "subjects.txt"
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

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.
    
    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """    
    # TODO...
    #
    # Build function that sorts based on comparator returns list of subject names sorted by comparator criteria.
    #
    def sort(l, comparator) :
        """
        Sorts the list of subjects' names in descendig order
        acording to the comparator.
        """
        # print "l, comparator type:", type(l), type(comparator)
        # print 
        
        for i in range(1, len(l)) :
            value = l[i]
            j = i - 1
            done = False
            # print 'i, value, j', i, value, j
            # print
            while not done:
                # print "subjects[value], subjects[l[j]] type:", type(subjects[value]), type(subjects[l[j]])
                # print
                if comparator(subjects[value], subjects[l[j]]):
                    l[j+1] = l[j]
                    j -= 1
                    if j < 0 :
                        done = True
                else :
                    done = True
            l[j+1] = value
    #
    # Pick classes from top of sorted list until maxWork is reached
    #
    schedule_list = subjects.keys()
    #print 'schedule_list unsorted: ', schedule_list
    #print
    sort(schedule_list, comparator)
    # print 'schedule_list sorted: ', schedule_list
    #     print
    recommended_schedule = {}
    courseLoad = 0
    done = False
    for course in schedule_list:
        if subjects[course][1] <= maxWork - courseLoad:
            recommended_schedule[course] = subjects[course]
            courseLoad += subjects[course][1]
    return recommended_schedule


def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.
        
    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work) 
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects


counter = 0

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue, subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#

def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...
    trial_work = [15]
    total_times = {}
    for each in trial_work:
        start_time = time.time()
        print bruteForceAdvisor(subjects,each)
        end_time = time.time()
        total_times[each] = round(end_time - start_time, 2)
    print total_times

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance
# Th brute force function is very slow for even moderately large course loads.
   # For a maxLoad of  2: 0.01 seconds
                           # 4: 0.22
                           # 6: 1.76
                           # 7: 3.70
                           # 8: 11.42
                           # 9: 27.57
                           # 10: 122.58
                           # 11: 354.55
                           # 12: 778.29
                           # 13: 1714.95
                           # 14: 2907.09
                           # 14: 2850.40
       # Unreasonable depends on a multiple  factors, including the importance of the results and the quality of the results of a faster, less optimal function.  In this case the greedy function probably produces results that nearly as good as the results of the brute force method.
   #  Considering MIT costs ~$200k in tuition and room and board.  Perhaps a few minutes to optimize a semester course load is worth it. 
   


#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.
    
    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    
    rec_dict = {}
    m = {}
        
    #   Build the work and value lists.
    work_list = []
    value_list = []
    for each in subjects:
        work_list.append(subjects[each][1])
        value_list.append(subjects[each][0])
    
    # Build optimal list of courses to take.
    rec_list = dp_decision_tree(work_list,value_list,len(work_list)-1,maxWork,m)
    
    #   Build dictionary from list.
    for each in rec_list:
        rec_dict[each] = subjects[each]
    return rec_dict

def dp_decision_tree(w,v,i,aW,m):
    
    ##  base case decision
    
    
    ## Don't take branch
    
    
    
    ## Take branch
    
    
    ## Which option is better
    
    
    return ["6.01", "15.01"]
    


#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    
    Prints total schedule, recommended schedule, time to complete each trial.
    """
    # TODO...
    trial_work = [15]
    total_times = {}
    for each in trial_work:
        start_time = time.time()
        recommendation = dpAdvisor(subjects, each)
        end_time = time.time()
        total_times[each] = round(end_time - start_time, 2)
        printSubjects(recommendation)
    print total_times
    return
    
    
    
    
    
    
    
    
    
    
    
    
    

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.

subjects = loadSubjects(SUBJECT_FILENAME)
printSubjects(subjects)
dpTime()

#print subjects
#print "Course Catalog"
#printSubjects(loadSubjects(SUBJECT_FILENAME))

# print 'greedy(cmpValue):'
# printSubjects(greedyAdvisor(subjects, 15, cmpValue))
# 
# print '\ngreedy(cmpWork):'
# printSubjects(greedyAdvisor(subjects, 15, cmpWork))
# 
# print '\ngreedy(cmpRatio)'
# printSubjects(greedyAdvisor(subjects, 15, cmpRatio))

# printSubjects(bruteForceAdvisor(subjects,15))
# 
#bruteForceTime()

#print dpAdvisor(subjects, 15)
