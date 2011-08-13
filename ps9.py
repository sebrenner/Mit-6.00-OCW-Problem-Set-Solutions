# 6.00 Problem Set 9
#
# Name:  Scott Brenner
# Collaborators: None
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")
    

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    
    def area(self):
        """
        Returns area of the square
        """
        return round(self.side**2)
    
    def __str__(self):
        return 'Square with side ' + str(self.side)
    
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side
    

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    
    def area(self):
        """
        Returns approximate area of the circle
        """
        return round(3.14159*(self.radius**2))
    
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius
    

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

class Triangle(Shape):
    def __init__(self, base, height):
        """
        base: length of base.
        height: height of triangle
        """
        self.base = float(base)
        self.height = float(height)
    
    def area(self):
        """
        Returns approximate area of the triangle 
        """
        return round(.5 * self.base * self.height,2)
    
    def __str__(self):
        """
        Describes this intance of Triangle.
        """
        return 'Triangle with a base of %0.2f and height of %0.2f.' % (self.base, self.height)
    
    def __eq__(self, other):
        """
        Two triangles are equal if they have the same base and height.
        other: object to check for equality
        """
        return type(other) == Triangle and self.base == other.base and self.height == other.height
    

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self.members = []
        self.index = 0
    
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        if sh not in self.members:
            self.members.append(sh)
            # print sh, "added to set."
    
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        for i in self.members:
            yield i
    
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO
        my_string = ""
        for each in self.members:
            # print each
            my_string += str(each) + "\n"
        return my_string
    
    


#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the largest area.
    
    shapes: ShapeSet
    
    This is a sorting problem
    """
    result = (0,)
    for each in shapes:
        try:
            if each.area() > result[-1].area():
                result = (each,)
            elif each == result[-1]:
                result = (result, each)
        except AttributeError:
            result = (each,)
    return result

#
# Problem 4: Read shapes from a file into a ShapeSet
#

SHAPES_FILENAME = "shapes.txt"

def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file. Creates and returns a ShapeSet with the shapes found. 
    
    filename: string
    """
    ## TO DO
    inFile = open(filename, 'r', 0)
    object_number = -1
    object_dictionary = {}
    for line in inFile:
        line = line.rstrip()
        OBJ_DESC = line.split(',')
        #print OBJ_DESC[0]
        object_number += 1
        if OBJ_DESC[0] == "circle":
            #print "in circle", OBJ_DESC[0],object_number
            name = "circle" + str(object_number)
            #print "name", name
            object_dictionary[name] = Circle(OBJ_DESC[1])
        if OBJ_DESC[0] == "triangle":
            #print "in tri",OBJ_DESC[0],object_number
            name = "triangle" + str(object_number)
            object_dictionary[name] = Triangle(OBJ_DESC[1],OBJ_DESC[2])
        if OBJ_DESC[0] == "square":
            #print "in sqr",OBJ_DESC[0],object_number
            name = "square" + str(object_number)
            object_dictionary[name] = Square(OBJ_DESC[1])
    
    shape_set = ShapeSet()
    #print object_dictionary
    for each in object_dictionary:
        shape_set.addShape(object_dictionary[each])
        # print "each" ,each
    # print "shape set :", shape_set
    return shape_set

circle01 = Circle(5)
square01 = Square(4)
triangle01 = Triangle(4,4)
circle02 = Circle(19)

print circle01.area()
print square01.area()
print triangle01.area()
print circle02.area()
# 
# 
# print triangle01 > square01
# print triangle01 < square01

# print circle01
# print square01
# print triangle01

ss01 = ShapeSet()
ss01.addShape(circle01)
ss01.addShape(triangle01)
ss01.addShape(square01)
ss01.addShape(circle02)

print
print "findLargest(ss01)"
largest = findLargest(ss01)
# print largest
# print circle01
print 
for each in largest:
    print each is circle02
    print each is circle01
    print each is square01
    print each is triangle01
# print largest[0] is circle02
# print largest[1] is circle01
# print largest[2] is circle01
print 
# for each in ss01:
    # print each
# 
# my_ss = readShapesFromFile(SHAPES_FILENAME)
# print my_ss

# my_circle = Circle(2)
# my_square = Square(4)
# my_square2 = Square(1)
# my_triangle = Triangle(1,1)
# 
# my_shapeset = ShapeSet()
#print len(my_shapeset.members)
# 
# print my_triangle
# print my_triangle.area()
# print your_triangle == my_triangle
# print your_triangle == her_triangle
# your_triangle.base = 45
# print my_triangle


# my_shapeset.addShape(Circle(2.25676))
# my_shapeset.addShape(Square(4))
# my_shapeset.addShape(Square(1))
# my_shapeset.addShape(Triangle(1,1))
# 
# print my_shapeset
#print my_shapeset.next()
# print my_shapeset.index
# print my_shapeset.next()
# print my_shapeset.index

#print my_shapeset.__str__()

# findLargest(my_shapeset)
#sorted(my_shapeset.members, key=my_shapeset.area())

def testFindLargest():
    ss = ShapeSet() 
    ss.addShape(Triangle(1.2,2.5)) 
    ss.addShape(Circle(4)) 
    ss.addShape(Square(3.6)) 
    ss.addShape(Triangle(1.6,6.4)) 
    ss.addShape(Circle(2.2)) 
    largest = findLargest(ss)
    print largest
    for e in largest: print e
    
    
    ss = ShapeSet()
    ss.addShape(Triangle(3,8)) 
    ss.addShape(Circle(1)) 
    ss.addShape(Triangle(4,6)) 
    largest = findLargest(ss) 
    print largest
    for e in largest:
        print e

def testSamenes():
    t = Triangle(6,6)
    c = Circle(1)
    ss = ShapeSet()
    ss.addShape(t)
    ss.addShape(c)
    largest = findLargest(ss)
    print largest
    print largest[0] is t
    print largest[0] is c

testFindLargest()

