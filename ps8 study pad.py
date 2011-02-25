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
    
    subjects = {}
    
    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    for line in inputFile:
        line = line.strip('\n')
        splitted = line.split(',')
        subjects[splitted[0]] = (int(splitted[1]), int(splitted[2]))
        
    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).
    
    return

    
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
    
    def sort(l, comparator) :
        """
        Sorts the list of subjects' names in descendig order
        acording to the comparator.
        """
        
        for i in range(1, len(l)) :
            value = l[i]
            j = i - 1
            done = False
            while not done :
                if comparator(subjects[value], subjects[l[j]]) :
                    l[j+1] = l[j]
                    j -= 1
                    if j < 0 :
                        done = True
                else :
                    done = True
            l[j+1] = value
    
    advise = {}
    advisedNames = []
    subjectNameList = subjects.keys()
    sort(subjectNameList, comparator)
    for sub in subjectNameList :
        currentWorkload = subjects[sub][1]
        maxWork -= currentWorkload
        if maxWork >= 0 :
            advisedNames.append(sub)
        else :
            break
    
    advisedNames.sort()#why sort? I mean what for? Should this make a difference?
    for sub in advisedNames :
        advise[sub] = subjects[sub]
    return advise


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
    
    subjects = loadSubjects('subjects.txt')
    maxWork = 1
    cont = True
    while cont :
        print "Deciding for a maximum workload of", maxWork
        startTime = time.time()
        selected = bruteForceAdvisor(subjects, maxWork)
        endTime = time.time()
        printSubjects(selected)
        print "it took", endTime - startTime, "seconds for the brute force advisor to select the subjects."
        ans = raw_input("press enter to continue or any key to exit: ")
        if not ans == '' :
            break
        maxWork += 1

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance
# for a subjects list as bigger as the provided one and a workload of 12 it
# takes almost 7 minutes to compute the solution

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
        without_i, selectedIndexes =\
                   dpAdvisorHelper(valueWorkList, i-1, aWork, memo) ##left branch, do not take
        if ith_workload > aWork :
            memo[(i, aWork)] = without_i, selectedIndexes
            return without_i, selectedIndexes ##commited not to take the element
        else : ##compute value with the i-th element
            with_i, I =\
                    dpAdvisorHelper(valueWorkList, i-1, aWork-ith_workload, memo)
            ##ma sti cazzi!!! three days lost because of this fuckin' I.
            ##the erred one was with_i, selectedIndexes =...
            ##by the way if anyone could kindly explain me why this old version
            ##didn't work i'd be very thankful.
            ##The other version had an if we can take it, take it branch.  But the don't
            ##take branch wasn't under and else: statement.  So it ran everytime even
            ##after the IF recursion.  I'm not sure at all why this is right and the other way
            ##was wrong, but it's hard to argue with success.
            ## I think if you use with_i, selectedIndexes = ... on the left side, then
            ## you have to have some tuple additions on the right side. For example, you want
            ## with_i = ith_value + the first part of dpAdvisorHelper and you want
            ## selectedIndexes = [i] + the second part of dpAdvisorHelper.
            ## Something like this:
            ##    with_i, selectedIndexes =\
            ##        ith_value, [i] + dpAdvisorHelper(valueWorkList, i-1, aWork-ith_workload, memo)
            ## But this doesn't work because you can't add tuples together like this.
            ## So I agree, 'ma sti cazzi!', working with tuples is so much more complex than
            ## working with integers!
            ##
            ## Wait a minute! Writing out this comment, I thought of another way to do this.
            ## You can add the parts of the tuples by separating them out, like this:
            ##
            ## with_i, selectedIndexes =\
            ##     ith_value + dpAdvisorHelper(valueWorkList, i-1, aWork-ith_workload, memo)[0],\
            ##     [i] + dpAdvisorHelper(valueWorkList, i-1, aWork-ith_workload, memo)[1]
            ##
            ## Remember to comment out the with_i += ith_value below along with the
            ## selectedIndexes = [i] + I in the if block below.
            ## These additions are done in the above statement.
            ##
            ## It does work, but the time, dpTime(), is about 10x longer than what is here.
            with_i += ith_value
        ##compare the values with and without i-th element
        if with_i >= without_i :
            ##take the i-th element
            #for keeping track of the indexes, why does only the last of these work properly?
            #selectedIndexes = I
            ##selectedIndexes.append(i)
            ##selectedIndexes.extend([i])
            ##selectedIndexes += [i]
            ###selectedIndexes = selectedIndexes + [i]
            ##Now I'm not 100% here, but I think that by concatenating the lists you're creating
            ##a new one, rather than a reference to one.  Like you need to use dict.copy() if you
            ##want a seperate instance of a data structure and not just a pointer.
            ## http://diveintopython.org/getting_to_know_python/lists.html
            ## 1) Lists can also be concatenated with the + operator. list = list + otherlist has the same
            ## result as list.extend(otherlist). But the + operator returns a new (concatenated) list as a
            ## value, whereas extend only alters an existing list. This means that extend is faster,
            ## especially for large lists.
            ## 2) Python supports the += operator. li += ['two'] is equivalent to li.extend(['two']).
            selectedIndexes = [i] + I
            maxValue = with_i
        else : ##do not take the i-th element
            maxValue = without_i
        memo[(i, aWork)] = maxValue, selectedIndexes
        return maxValue, selectedIndexes
# Thank you for posting your solution to this, Kamenoko. I struggled with it for quite a while and 
# just wanted to share what I figured out, in case anyone else has the same issues and to see if
# anyone can add any further insight to help me understand the error of my ways.
# My original approach to this was to attempt to add memoization to the brute force solution that
# was provided with the problem set. The brute force algorithm starts by selecting the early items,
# adds items until the max is reached, and recurses to the end of the list before a solution is
# found. I believe that the problem with memoization here is that you end up capturing the first
# answer for a given index/available weight, and it is not necessarily the best answer. On the other
# hand, the solution posted above starts at the end of the list and works it's way back, so that as
# each new index is considered, it can refer to the memoized solutions, which are in fact the
# optimal solutions. Does that sound right?
# If anyone else has any other thoughts or theories on this please chime in. Thanks again for
# posting this. - BriChri
    
# @BriChri... the solution below adds memoization to the brute force solution (just # a note it uses the exact same params as the brute force algorithm). The problem   # was as you noticed that you capture the first answer to a given index / available # weight but not necessarily the best answer. After adding a bunch of print         # statements I noticed that the best answer is computed, just never gets stored
# in the memo. So I added the extra if statement in the try block. This insures that
# the correct value gets stored. However, because of the extra check this ends up
# being slightly slower than the algorithm above, but still faster than the brute
# force method   
    

 availableWork = maxWork - subsetWork
    
    try:
        if (memo[(i, availableWork)][1] > subsetValue):
            return memo[(i, availableWork)]
        else:
            raise KeyError
    except KeyError:
        if i >= len(valueWorkList): # a leaf node... end of the line.
            if bestSubset == None or subsetValue > bestSubsetValue:
                memo [(i, availableWork)] = subset[:], subsetValue
                return subset[:] , subsetValue
            else:
                memo [(i, availableWork)] = bestSubset, bestSubsetValue
                return bestSubset, bestSubsetValue
            
        else:
            s = valueWorkList[i]
            if s[WORK] <= availableWork:
                # Take branch
                subset.append(i)
                bestSubset, bestSubsetValue = dpAdvisorHelper(valueWorkList,
                        maxWork, i+1, bestSubset, bestSubsetValue, subset,
                        subsetValue + s[VALUE], subsetWork + s[WORK], memo)
                subset.pop() # revert (remove the last i)
            
            # Do not take branch
            bestSubset, bestSubsetValue = dpAdvisorHelper(valueWorkList,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue, subsetWork, memo)
        
        memo [(i, availableWork)] = bestSubset, bestSubsetValue
        return bestSubset, bestSubsetValue


#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...
    subjects = loadSubjects('subjects.txt')
    for maxWork in range(0, 1001, 10) :
        print "maximum workload", maxWork, ':',
        startTime = time.time()
        selected = dpAdvisor(subjects, maxWork)
        endTime = time.time()
        print endTime - startTime, "seconds."


# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
# mavaffanculo, va'!

# Here's an alternative solution to the greedy algorithm problem
def greedyAdvisor_alternate(subjects, maxWork, comparator):
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
    
    # Define local variables        
    totalWork = 0
    subDict = {}
    nameList = subjects.keys()
    tupleList = subjects.values()
    
    while totalWork <= maxWork:
        foundStartingPoint = False
        for i in range(len(subjects)):
            if i == 0: # If at the beginning of the list, find a suitable starting point
                for i in range(len(subjects)):
                    if nameList[i] not in subDict and tupleList[i][WORK] + totalWork <= maxWork:
                        foundStartingPoint = True
                        bestSubject = i
                        break
            if foundStartingPoint: # If there is a value to test
                # Find the best subject according to the comparator, allowed work, and presence in the subDict
                if nameList[i] not in subDict and tupleList[i][WORK] + totalWork <= maxWork and comparator(tupleList[i], tupleList[bestSubject]):
                    bestSubject = i
        # Add the best subject to the subject dictionary if there were any found
        if foundStartingPoint:
            subDict[nameList[bestSubject]] = tupleList[bestSubject]
            totalWork += tupleList[bestSubject][WORK]
        # break out of the loop if there are no possible subjects
        else:
            break
    return subDict



# Just because I'm insane, here's yet another way to solve for the greedy algorithm, this solution requires the itemgetter from the operator module
def greedyAdvisor_alternate2(subjects, maxWork, comparator):
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
    def comparatorComparison(x, y):
        """
        Takes two tuples, and compares them, returning 1 if the comparator
        function returns true, -1 if it returns false, and 0 if it returns
        neither. It really shouldn't return 0, but it's there for code
        completeness.
        
        x, y: tuples containing two integers >= 0        
        """
        if comparator(x, y):
            return 1
        elif not comparator(x, y):
            return -1
        else:
            return 0
    
    # Create a list out of the subject dictionary
    subjectList = []
    for key in subjects:
        subjectList.append((key, subjects[key]))
    # Sort the subject list, itemgetter is part of the operator module and is
    # used to get a specific index from a complex object. In this case the
    # work/value pair in subject list. 
    subjectList.sort(cmp=comparatorComparison, key=itemgetter(1), reverse=True)
    # Reconstruct a dictionary, adding the items from the sorted list until
    # totalWork is equal to or greater than maxWork
    totalWork = 0
    syllabus = {}
    for subject in subjectList:
        if totalWork + subject[1][WORK] <= maxWork:
            syllabus[subject[0]] = subject[1]
            totalWork += subject[1][WORK]
    # Return the dictionary
    return syllabus

    