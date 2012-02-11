# Problem Set 4
# Name: 
# Collaborators: 
# Time: 

#
# Problem 1
# Start time: 2011-02-06 5:10 PM
# End time: 2011-02-06 5:31 PM
# Total time: 21 minutes.

# Write a function, called nestEggFixed, which takes four arguments: a salary, a percentage of your salary to save in an investment account, an annual growth percentage for the investment account, and a number of years to work. This function should return a list, whose values are the size of your retirement account at the end of each year, with the most recent year's value at the end of the list.

##  Complete the implementation of:
def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    # End of year 1 -->   F[0] = salary * save * 0.01
    # End of year 2 -->   F[1] = F[0] * (1 + 0.01 * growthRate) + salary * save * 0.01
    # End of year 3 --> F[2] = F[1] * (1 + 0.01 * growthRate) + salary * save * 0.01
    
    # TODO: Your code here.
    answer = [0]
    for each in range(0,years):
        #print each
        temp = answer[-1] * (1 + 0.01 * growthRate) + salary * save * 0.01
        answer.append(temp)
        #print answer
    del answer[0]
    return answer

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.
    salary     = 40000
    save       = 12
    growthRate = 7
    years      = 20
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord

    salary     = 80000
    save       = 12
    growthRate = 7
    years      = 20
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord

#   testNestEggFixed()  #Just for testing 

#
# Problem 2
#
# Start time: 2011-02-06 5:32 PM
# End time: 2011-02-06  5:41 PM
# Total time: 9 minutes.

# Write a function, called nestEggVariable, which takes three arguments: a salary (salary), a percentage of your salary to save (save), and a list of annual growth percentages on investments (growthRates). The length of the last argument defines the number of years you plan to work; growthRates[0] is the growth rate of the first year, growthRates[1] is the growth rate of the second year, etc. (Note that because the retirement fund's initial value is 0, growthRates[0] is, in fact, irrelevant.) This function should return a list, whose values are the size of your retirement account at the end of each year.


def nestEggVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    # TODO: Your code here.
    answer = [0]
    for each in range(len(growthRates)):
        #print each
        temp = answer[-1] * (1 + 0.01 * growthRates[each]) + salary * save * 0.01
        answer.append(temp)
        #print answer
    del answer[0]
    return answer
    
def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.
    salary      = 40000
    save        = 10
    growthRates = [3, 7, 8, 10, 3,7, 8, 10, 3,7, 8, 10, 3,7, 8, 10, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord

    salary      = 80000
    save        = 10
    growthRates = [3, 0, 15, 0, 31,7, 8, 10, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord

    salary      = 650000
    save        = 10
    growthRates = [7, 8, 10, 3, 7, 8, 10, 3, 13, 7, 8, 10, 3, 14, 15, 10, 13]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord

#testNestEggVariable() # Just for testing

#
# Problem 3
#
# Start time: 2011-02-06 5:46 PM
# End time: 2011-02-06 5:57 PM
# Total time:  11 minutes.

# Write a function, called postRetirement, which takes three arguments: an initial amount of money in your retirement fund (savings), a list of annual growth percentages on investments while you are retired (growthRates), and your annual expenses (expenses). Assume that the increase in the investment account savings is calculated before subtracting the annual expenditures (as shown in the above table). Your function should return a list of fund sizes after each year of retirement, accounting for annual expenses and the growth of the retirement fund. Like problem 2, the length of the growthRates argument defines the number of years you plan to be retired.

# Note that if the retirement fund balance becomes negative, expenditures should continue to be subtracted, and the growth rate comes to represent the interest rate on the debt(i.e. the formulas in the above table still apply).

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    # TODO: Your code here.
    answer = [savings]
    for each in range(len(growthRates)):
        temp = answer[-1] * (1 + 0.01 * growthRates[each]) - expenses
        answer.append(temp)
#    del answer[0]
    return answer[-1]




def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.
    savings     = 367000
    growthRates = [10, 5, 0, 5, 1,5,6,7,8,9,1,2,3,4,5,6,12,13,14]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord

    savings     = 900000
    growthRates = [10, 5, 0,10, 5, 0, 5, 1]
    expenses    = 60000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord

    savings     = 1500000
    growthRates = [10, 5, 0, 5, 1,10, 5, 0, 5, 1,6,7,8,4,3,1,8,9,0,21, 5, 0, 5, 1,6,7,8,4,3,1,8,9,0,12]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord

    savings     = 1000000
    growthRates = [10, 5, 0, 5, 1,6,7,8,4,3,1,8,9,0,12]
    expenses    = 18000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    
    
# testPostRetirement() #Just for testing    

#
# Problem 4
#
# Start time: 2011-02-06 6:02 PM
# End time: 2011-02-06 6:42 PM
#
# Total time: minutes.


# Write a function, called findMaxExpenses, which takes five arguments: a salary(salary), a percentage of your salary to save (save), a list of annual growth percentages on investments while you are still working (preRetireGrowthRates), a list of annual growth percentages on investments while you are retired (postRetireGrowthRates), and a value for epsilon (epsilon). As with problems 2 and 3, the lengths of preRetireGrowthRates and postRetireGrowthRates determine the number of years you plan to be working and retired, respectively.

# Use the idea of binary search to find a value for the amount of expenses you can withdraw each year from your retirement fund, such that at the end of your retirement,the absolute value of the amount remaining in your retirement fund is less than epsilon(note that you can overdraw by a small amount). 

# Start with a range of possible values for your annual expenses between 0 and your savings at the start of your retirement (HINT #1: this can be determined by utilizing your solution to problem 2). Your function should print out the current estimate for the amount of expenses on each iteration through the binary search (HINT #2: your binary search should make use of your solution to problem 3), and should return the estimate for the amount of expenses to withdraw. (HINT #3: the answer should lie between zero and the initial value of the savings + epsilon.)

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # TODO: Your code here.

    # Start with a range of possible values for your annual expenses between 0 and your savings at the start of your retirement (HINT #1: this can be determined by utilizing your solution to problem 2).
    low = 0
    
    ##  Set the high guess to value of the nest egg at moment of retirement or 1, which ever is higher.
    high = max(nestEggVariable(salary, save, preRetireGrowthRates)[-1],1)
    
    balanceAtRetirement = nestEggVariable(salary, save, preRetireGrowthRates)[-1]

    ##  Bisect the range between high & low and initialize the guess to this value.
    guess = (low + high) / 2
    
    ctr = 1
    
    ##  Set the remaining balance to the balance at the end of retirement (death?).
    remainingBalance = postRetirement(balanceAtRetirement, postRetireGrowthRates, guess)
    
    while abs(remainingBalance) > epsilon and ctr <= 100:
        #print 'low:', low, 'high:', high, 'guess:', guess, 'remainingBalance:',remainingBalance
        #print 'guess - remainingBalance', guess - remainingBalance
        if remainingBalance < 0:
            high = guess
        else:
            low = guess
        ctr += 1
        guess = (low + high)/2
        remainingBalance = postRetirement(balanceAtRetirement, postRetireGrowthRates, guess)
    assert ctr <= 100, 'Iteration count exceeded'
    return guess
    
def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.

    salary                = 80000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3,6,7,8,5,4,7,4,8,9,11,21,11,2,5]
    postRetireGrowthRates = [3, 4, 5, 0, 3,6,7,8,5,4,7,4,8,2,5,10, 5, 0, 5, 1]
    epsilon               = 1000
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    
    salary                = 100000
    save                  = 15
    preRetireGrowthRates  = [3, 4, 5, 0, 3,6,7,8,5,4,7,4,8,9,11,21,11,2,5,3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0,3, 4, 5, 0, 3,6,7,8,5,4,7,4,8,9,11,21,11,2,5, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    
    salary                = 1000
    save                  = 90
    preRetireGrowthRates  = [3, 4, 5, 0, 3,6,7,8,5,4,7,4,8,9,11,21,11,2,53, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1,3, 4, 5, 0, 3,6,7,8,5,4,7,4,8,9,11,21,11,2,5]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses

testFindMaxExpenses() # just to test