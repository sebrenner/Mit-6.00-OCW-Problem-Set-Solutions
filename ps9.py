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
        return self.side**2
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
        return 3.14159*(self.radius**2)
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
        return .5 * self.base * self.height
        
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
        ## TO DO
    
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        self.members.append(sh)
    
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        for shape in self.members:
            return shape
               
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO
        result = 'This list contains the following shapes:',
        for each in self:
            result += each
    

#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    pass
    
 
#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO


my_triangle = Triangle(6,7)
your_triangle = my_triangle
her_triangle = Triangle(6,7)

my_shapeset = ShapeSet()


print my_triangle
print my_triangle.area()
print your_triangle == my_triangle
print your_triangle == her_triangle
your_triangle.base = 45
print my_triangle

my_shapeset.addShape(my_triangle)
print my_shapeset