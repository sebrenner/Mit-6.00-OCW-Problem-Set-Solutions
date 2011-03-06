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
        self.members = []
        self.index = 0
        ## TO DO
    
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        if sh not in self.members:
            self.members.append(sh)
    
    def __getitem__(self, int):
        """
        Returns the shape at the given index
        """
        return self.members[int]
    
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        return self
    
    def next(self):
        if self.index == len(self.members):
            raise StopIteration
        current_index = self.index
        self.index = self.index + 1
        return self.members[current_index]
    
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO
        taco = ''
        for each in my_shapeset.members:
            taco = taco + "\n" + each.__str__()
        return taco
    
    

#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the largest area.
    
    shapes: ShapeSet
    
    This is a sorting problem
    """
    ## TO DO
    my_list = []
    #sort list by area function
    for each in shapes:
        #print each
        my_list.append((each.area(), shapes.index))
    #print my_list
    my_list.sort()
    my_list.reverse()
    #print my_list
    result = []
    for each in my_list:
        # print "each", each
        # print "each0", each[0]
        # print "each1", each[1]
        # print "mlys" ,my_list[0][0]
        # print
        if my_list[0][0] == each[0]:
            result.append(each[1])
    return tuple(result)
    
    

#
# Problem 4: Read shapes from a file into a ShapeSet
#

def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file. Creates and returns a ShapeSet with the shapes found. 
    
    filename: string
    """
    ## TO DO



my_circle = Circle(2)
my_square = Square(4)
my_square2 = Square(1)
my_triangle = Triangle(1,1)

my_shapeset = ShapeSet()
#print len(my_shapeset.members)
# 
# print my_triangle
# print my_triangle.area()
# print your_triangle == my_triangle
# print your_triangle == her_triangle
# your_triangle.base = 45
# print my_triangle


my_shapeset.addShape(Circle(2.25676))
my_shapeset.addShape(Square(4))
my_shapeset.addShape(Square(1))
my_shapeset.addShape(Triangle(1,1))

#print my_shapeset.members
#print my_shapeset.next()
# print my_shapeset.index
# print my_shapeset.next()
# print my_shapeset.index

#print my_shapeset.__str__()

findLargest(my_shapeset)
#sorted(my_shapeset.members, key=my_shapeset.area())


ss = ShapeSet() 
ss.addShape(Triangle(1.2,2.5)) 
ss.addShape(Circle(4)) 
ss.addShape(Square(3.6)) 
ss.addShape(Triangle(1.6,6.4)) 
ss.addShape(Circle(2.2)) 
largest = findLargest(ss)
for e in largest: print e