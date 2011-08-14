# Problem Set 11: Simulating robots
# Name:  Scott Brenner
# Collaborators:  None
# Time: 

import math
import random
# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        
        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.
        
        Does NOT test whether the returned position fits inside the room.
        
        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed
        
        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)



# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.
    
    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.
        
        width: an integer > 0
        height: an integer > 0
        """
        # TODO: Your code goes here
        self.roomWidth = width
        self.roomHeight = height
        self.cleanTiles = {}         # a dictionary of Position objects
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.
        
        pos: a Position
        """
        # TODO: Your code goes here
        # Convert postion to integer, add the position to the dictionary of clean positions; increment if necessary
        intPosition = (int(pos.getX()), int(pos.getY()))
        self.cleanTiles[intPosition] = self.cleanTiles.get(intPosition,0) + 1
    
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.
        
        Assumes that (m, n) represents a valid tile inside the room.
        
        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # TODO: Your code goes here
        questionedPosition = Position(m,n)
        if questionedPosition in self.cleanTiles:
            return True
        return False
        
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.
        
        returns: an integer
        """
        # TODO: Your code goes here
        return self.roomWidth * self.roomHeight
    
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        # Counts dictionary entries.  Assumes that dictionary value cannot be 0, i.e., no tile can become unclean after being cleaned.
        return len(self.cleanTiles)
    
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        # TODO: Your code goes here
        # generate random numbers between 0 and width or height inclusive
        randomWidth = random.randint(0, self.roomWidth-1)
        randomHeight = random.randint(0, self.roomHeight-1)
        return Position(randomWidth, randomHeight)
        
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        # TODO: Your code goes here
        # if Pos X or Y are greater than or eqaul to width of room they are outside the room.
        # What if X or Y are negative?
        if pos.getX() < 0: return False
        if pos.getY() < 0: return False
        
        if pos.getX() >= self.roomWidth: return False
        if pos.getY() >= self.roomHeight: return False
        return True


class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.
    
    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.
    
    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.
        
        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.
        
        p is a Position object giving the robot's position.
        
        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # TODO: Your code goes here
        self.robotSpeed = speed
        self.robotDirection = random.randint(0, 360)
        self.robotPosition = room.getRandomPosition()
        # print self.robotPosition.getX(), self.robotPosition.getY()
        self.robotRoom = room
    
    def getRobotPosition(self):
        """
        Return the position of the robot.
        
        returns: a Position object giving the robot's position.
        """
        # TODO: Your code goes here
        # print "self.robotPosition is %s" %self.robotPosition
        return self.robotPosition
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # TODO: Your code goes here
        return self.robotDirection
    
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        # TODO: Your code goes here
        self.robotPosition = position
    
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        # TODO: Your code goes here
        self.robotDirection = direction 

class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # TODO: Your code goes here
        
        notAtWall = True
            
        while notAtWall:
            currentPosition = self.getRobotPosition()
            # print "\ncurrent robot position: %s" % currentPosition
            # print "current robot position: %s" % self.getRobotPosition()
            nextPosition = currentPosition.getNewPosition(self.getRobotDirection(), self.robotSpeed)
            if self.robotRoom.isPositionInRoom(nextPosition):
                self.robotPosition = nextPosition
                # tell room this tile is clean
                self.robotRoom.cleanTileAtPosition(self.robotPosition)
                notAtWall = False
            else:   # pick a new direction at random
                self.robotDirection = random.randint(0, 360)

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.
    
    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.
    
    Visualization is turned on when boolean VISUALIZE is set to True.
    
    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    
    test case:
    avg = runSimulation(10, 1.0, 15, 20, 0.8, 30, Robot, False)
    
    """
    # TODO: Your code goes here
    
    trialsCollection = []                       # list to hold lists of date from each trial
    for m in range(num_trials-1):               # for each trial
        # create the room
        testRoom = RectangularRoom(width, height)
        
        # create robots and put them in a list
        robotList = []
        for i in range(num_robots):
            robotList.append(robot_type(testRoom, speed))
        # print "%i robots created" %len(robotList)
        
        
        # initialize for this trial
        percentClean = 0.0000000
        progressList = []
        # print
        while percentClean < min_coverage:     # clean until percent clean >= min coverage
            # print "percentClean, min_coverage", percentClean, min_coverage
            for eachRobot in robotList:             # for each time-step make each robot clean
                eachRobot.updatePositionAndClean()
                # print eachRobot.getRobotPosition().getX(), eachRobot.getRobotPosition().getY()
            # print "number cleaned, number of tiles: %i, %i" % (testRoom.getNumCleanedTiles(),testRoom.getNumTiles())
            percentClean = float(testRoom.getNumCleanedTiles()) / float(testRoom.getNumTiles())
            # print "time-steps: %i, Percent complete %f." % (len(progressList), percentClean)
            progressList.append(percentClean)
        trialsCollection.append(progressList)
    sumTimeSteps = 0    
    for each in trialsCollection:
        # print "the %i robot(s) took %i clock ticks to %f clean a %i x %i room." %(num_robots, len(each), min_coverage, width, height)
        sumTimeSteps += len(each)
    avgTimeSteps = sumTimeSteps / num_trials
    print "avgTimeSteps:", avgTimeSteps
            
            
        

# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.
    
    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means


# === Problem 4
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    # TODO: Your code goes here

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # TODO: Your code goes here

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # TODO: Your code goes here

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # TODO: Your code goes here


# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    # TODO: Your code goes here


# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    # TODO: Your code goes here


# === Run code
# def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,robot_type, visualize):
# print "simulation 1"
# avg = runSimulation(10, 1.0, 15, 20, 0.8, 30, Robot, False)
print "simulation 2"
avg = runSimulation(01, 1.0, 05, 05, 1.0, 3000, Robot, False)
print "simulation 3"
avg = runSimulation(01, 1.0, 10, 10, 0.75, 3000, Robot, False)
print "simulation 4"
avg = runSimulation(01, 1.0, 10, 10, 0.9, 3000, Robot, False)
print "simulation 5"
avg = runSimulation(01, 1.0, 20, 20, 1.0, 3000, Robot, False)
