# 6.00 Problem Set 12
#
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab
import csvExporter
import os, sys, csv

def write_lists_csv(block_list,file_name, headers):
    """
    Takes a list or list of lists, a files location//name, and a list of headers
    Writes the itemsof the lists as rows in a CSV file.  Each item of the list is a comma-separated value.
    Returns the location of the CSV file.
    """
    fileWriter = csv.writer(open(file_name, 'wb'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    fileWriter.writerow(headers)
    for each in block_list:
        fileWriter.writerow(each)

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """    

#
# PROBLEM 1
#
class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        # TODO
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
    
    def doesClear(self):
        """
        Stochastically determines whether this virus is cleared from the
        patient's body at a time step. 

        returns: Using a random number generator (random.random()), this method
        returns True with probability self.clearProb and otherwise returns
        False.
        """
        # TODO
        randomPossibility = random.random()
        # print "randomPossibility, self.clearProb", randomPossibility, self.clearProb,
        if randomPossibility <= self.clearProb:
            # print "virus clears"
            return True
        else:
            # print "virus does not clear"
            return False
    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent). 
        
        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population. 
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.       
        """
        # TODO
            
        randomPossibility = random.random()
        # print "randomPossibility: %2.3f, self.maxBirthProb * (1 - popDensity):%2.3f" %( randomPossibility, self.maxBirthProb * (1 - popDensity)),
        
        if randomPossibility <= (self.maxBirthProb * (1 - popDensity)):
            # print "virus reproduces"
            return SimpleVirus( self.maxBirthProb, self.clearProb)
        else:
            # print "virus does not reproduce"
            raise NoChildException('In reproduce()')
    

class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.
        
        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        self.virusesList = viruses
        self.maxPop = maxPop
    
    def getTotalPop(self):
        """
        Gets the current total virus population. 

        returns: The total virus population (an integer)
        """
        # TODO
        return len(self.virusesList)
    
    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
          of virus particles accordingly.
  
        - The current population density is calculated. This population density
          value is used until the next call to update().  popDensity is defined
          as the ratio of the current virus population to the maximum virus
          population for a patient
  
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.            
  
        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
        
        # Determine whether each virus particle survives
        listNonSurvivingViruses = []
        print "Updating.  Patient has %i viruses." % len(self.virusesList),
        for index, virus in enumerate(self.virusesList):
            if virus.doesClear():
                listNonSurvivingViruses.append(index)
        # print "%i viruses cleared." % len(listNonSurvivingViruses),
        
        # remove the non-surviving in reverse order to preserve the original indexes
        listNonSurvivingViruses.reverse()
        for index in listNonSurvivingViruses:
            self.virusesList.pop(index)
        print "%i viruses did not survive." % len(listNonSurvivingViruses)
        
        # Calculate current population density. This population density value is used
        # until the next call to update()
        popDensity = float(len(self.virusesList)) / self.maxPop
        
        # Determine whether each virus particle should reproduce
        # if it reproduces adjust the population density
        # add new virus to list of viruses.
        newVirusCount = 0
        for virus in self.virusesList:
            try:
                newVirus = virus.reproduce(popDensity)
                newVirusCount += 1
                # This line of code would make the model more accurate by preventing the
                # virus population from excedeing the max population.  But that wouldn't match the instructions.
                # popDensity = (len(self.virusesList)  + newVirusCount) / self.maxPop
            except NoChildException:
                continue
            self.virusesList.append(newVirus)
        print "%i new viruses produced." % newVirusCount
    

#
# PROBLEM 2
#

def problem2():
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.
    
    The patient virus population stabalizes at ~1000 after 40 time-steps.
    """
    # TODO    
    # Create some viruses; create a patient.
    listOfViruses = [] 
    for each in range(100):
        # (maxBirthProb, clearProb):
        listOfViruses.append(SimpleVirus(0.1, .05))
    patient = SimplePatient(listOfViruses, 1000)
    # print "patient initially has: %i viruses" % patient.getTotalPop()
    
    virusCount = []
    trialCount = 0
    dataSet = []
    for each in range(300):
        print "trial #:", trialCount
        patient.update()
        virusCount.append(patient.getTotalPop())
        dataSet.append((trialCount,patient.getTotalPop()))
        trialCount += 1
        # print "patient has: %i viruses" % patient.getTotalPop()
    write_lists_csv(dataSet,"PS12-problem2-data.csv", "virus population")


# problem2()
#
# PROBLEM 3
#

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """    
    
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        
        clearProb: Maximum clearance probability (a float between 0-1).
        
        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.
        
        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        # TODO
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistance(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.
        
        drug: the drug (a string).
        
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        # TODO
        if self.resistances[drug]:
            return True
        return False 
    
    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.
        
        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).               
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 
        
        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.
        
        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.
        
        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population
        
        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce. 
        """
        # TODO
        #If the virus particle is not resistant to any drug in activeDrugs,then it does not reproduce.
        for drug in activeDrugs:
            if self.getResistance(drug) == False:
                raise NoChildException('In reproduce()')
        
        if random.random() <= (self.maxBirthProb * (1 - popDensity)):
            offspringResistances = {}
            for drug in self.resistances:
                offspringResistances[drug] = self.resistances[drug]
                if random.random() <= self.mutProb:
                    offspringResistances[drug] = not offspringResistances[drug]
            # Returns a resistant virus with the same properties as the parent except for the resistances
            return ResistantVirus(self.maxBirthProb, self.clearProb, offspringResistances, self.mutProb)
        else:
            # print "virus does not reproduce"
            raise NoChildException('In reproduce()')
        
    
class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).       
        
        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        self.virusesList = viruses      # a list
        self.maxPop = maxPop        # an int
        self.listOfDrugs = []
    
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.
        
        newDrug: The name of the drug to administer to the patient (a string).
        
        postcondition: list of drugs being administered to a patient is updated
        """
        # TODO
        if newDrug not in self.listOfDrugs:
            self.listOfDrugs.append(newDrug)
        
    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.
        
        returns: The list of drug names (strings) being administered to this
        patient.
        """
        # TODO
        return self.listOfDrugs

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # TODO
        virusPopulation = 0
        for virus in self.virusesList:
            for drug in drugResist:            
                if virus.getResistance(drug):
                    virusPopulation += 1
                    break       # break ensures that a virus that is resistent to two drugs is only counted once.
        return virusPopulation
    
    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:
        
        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly
        
        - The current population density is calculated. This population density
          value is used until the next call to update().
          
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 
          
        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
        # print "In update:",
        # Determine whether each virus particle survives and update the list 
        # of virus particles accordingly.  Use doesClear from base class.
        listNonSurvivingViruses = []
        # print "Updating.  Patient has %i viruses." % len(self.virusesList),
        for index, virus in enumerate(self.virusesList):
            if virus.doesClear():
                listNonSurvivingViruses.append(index)
        
        # remove the non-surviving in reverse order to preserve the original indexes
        listNonSurvivingViruses.reverse()
        for index in listNonSurvivingViruses:
            self.virusesList.pop(index)
        # print "%i viruses did not survive." % len(listNonSurvivingViruses),
        
        
        
        # Calculate current population density. This population density value is used
        # until the next call to update()
        # print "len(self.virusesList) / self.maxPop", len(self.virusesList), self.maxPop
        popDensity = float(len(self.virusesList)) / self.maxPop
        # print "popDensity:%2.2f" % popDensity,
        # Determine whether each virus particle should reproduce
        # 
        # add new virus to list of viruses.
        newVirusCount = 0
        for virus in self.virusesList:
            try:
                newVirus = virus.reproduce(popDensity, self.listOfDrugs)
                self.virusesList.append(newVirus)
                newVirusCount += 1
                # This line of code would make the model more accurate by preventing the
                # virus population from excedeing the max population.  But that wouldn't match the instructions.
                # popDensity = (len(self.virusesList)  + newVirusCount) / self.maxPop
            except NoChildException:
                continue
            
        # print "%i new viruses produced." % newVirusCount
        

#
# PROBLEM 4
#

def problem4():
    """
    Runs simulations and plots graphs for problem 4.
        
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
        
    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    # TODO
    print "Problem 4: Testing code from problem 3"
    testViruses = []
    for each in range(100):
        testViruses.append(ResistantVirus(.1, .05, {"guttagonol":False}, .005))
    print "%i viruses created." %len(testViruses)
    testPatient = Patient(testViruses, 1000)
    print "Patient created:", testPatient
        
    dataSet = []
    timeStepCount = 0
    print "Preparing to loop 3000 times."
    for timeStep in range(3000):
        
        print "trial #:", timeStepCount, 
        timeStepCount += 1
        testPatient.update()
        if timeStepCount == 150:
            print "Looped 150 times"
            testPatient.addPrescription("guttagonol")
        dataSet.append((timeStepCount,testPatient.getTotalPop()))
    write_lists_csv(dataSet,"PS12-problem-3+4-data.csv", ["Time-Step""virus population"])
    
    
# problem4()
#
# PROBLEM 5
#

def problem5(stepsTillTreatment):
    """
    Runs simulations and make histograms for problem 5.
    
    Takes the number of steps until the drug is administered.
    
    Returns a list of virus puplulations at the end of each step.
    
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    # TODO
    # print "Problem 5:"
    testViruses = []
    for each in range(100):
        testViruses.append(ResistantVirus(.1, .05, {"guttagonol":False}, .005))
    # print "%i viruses created." %len(testViruses)
    testPatient = Patient(testViruses, 1000)
    # print "Patient created:", testPatient
    
    
    totalTimeSteps = stepsTillTreatment + 150
    dataSet = []
    timeStepCount = 0
    
    # print "Preparing to loop %i times; treatment at %i." % (totalTimeSteps, stepsTillTreatment)
    
    for timeStep in range(totalTimeSteps):
        # print "trial #:", timeStepCount, 
        timeStepCount += 1
        testPatient.update()
        if timeStepCount == stepsTillTreatment:
            # print "Looped %i times" % stepsTillTreatment
            testPatient.addPrescription("guttagonol")
        dataSet.append((timeStepCount,testPatient.getTotalPop()))
    return dataSet
    
    # write_lists_csv(dataSet,"PS12-problem-3+4-data.csv", ["virus population"])
    
def runProblem5(numTrials):
    trialVariations = [300, 150, 75, 0]
    
    # histogramData will be a list of lists. 
    # Each list lists the final virus populations for each vaiation
    histogramData = []      
    
    # loop through each trial variation
    for stepsTillTreatment in trialVariations:
        finalVirusPopulations = []    #["trials:" + str(stepsTillTreatment)]
        
        # repeat numTrials trial on this variation
        # add the list of virus pop to list of 
        for each in range(numTrials):
            result = problem5(stepsTillTreatment)
            
            # Add the final virus population to list of all final populations for this variation
            finalVirusPopulations.append(result[-1][-1])
        # Calculate the average virus population at the end of the trials
        total = 0
        
        for value in finalVirusPopulations:
            total += value
        average = float(total) / len(finalVirusPopulations)
        print "Treatment at %i step; Average viruses at end of %i trials: %2.3f" % (stepsTillTreatment, numTrials, average)
        print "histogram:"
        printHistogram(finalVirusPopulations)
        print "\n\n"
        # append  list to list of lists
        histogramData.append(finalVirusPopulations)
        # print histogramData
    # write_lists_csv(histogramData,"PS12-problem-5-" + str(stepsTillTreatment) + "-histo-data.csv", ["trials","Treatment at " + stepsTillTreatment])
    print histogramData
    for theList in histogramData:
        printHistogram(theList)

def printHistogram(theList):
    """
    takes a list and print a rudimentary historgram of the list values
    """
    x_max = max(theList) + 2
    # make dicitionary 
    dictionary ={}
    for value in theList:
       dictionary[value] = dictionary.get(value,0) + 1
    
    sortedKeysList = sorted(dictionary)
    # print sortedKeysList
    for each in sortedKeysList:
        print each, "\t",
        print "*" * (dictionary[each])
    

runProblem5(550)




#
# PROBLEM 6
#

def problem6():
    """
    Runs simulations and make histograms for problem 6.
    
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
    
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    # TODO

#
# PROBLEM 7
#
     
def problem7():
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.

    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.
    """
    # TODO
