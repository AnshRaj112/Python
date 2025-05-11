# Object and Classes

import matplotlib.pyplot as plt


"""
Every object has:
    A type
    An internal data representation (a blueprint)
    A set of procedures for interacting with object (method)

An object is an instance of a class

We can find the type of an object by using the command type()


"""

print(type(10))

print(type([1, 34, 4]))

print(type("Hello"))

print(type({"dog": 1, "cat": 2}))

# Methods

"""
A class or type's methods are functions that every instance of that class or type provides

It is how we interact with the data in an object

Sorting is an example of a method that interacts with the data in the object

"""

Ratings = [10, 9, 6, 5, 10, 8, 9, 6, 2]

Ratings.sort()

print(Ratings)

Ratings.reverse()

print(Ratings)

# Creating your own types: Defining a class

# class Circle:
#     def __init__(self, radius, color):
#         self.radius = radius
#         self.color = color
        
# # __init__ is a special method that is called when a new instance of the class is created

#     def area(self):
#         return 3.14 * self.radius ** 2
    
    
#     def display(self):
#         print("Circle with radius", self.radius)
#         print("Area of circle is", self.area())





class Rectangle(object):
    def __init__(self, color, height, width):
        self.height = height
        self.width = width
        self.color = color
        
RedRectangle = Rectangle("Red", 10, 20)

print(RedRectangle.color)
print(RedRectangle.height)
print(RedRectangle.width)

# Methods

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius
    
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  
    
C1 = Circle(2, "Red")
print(dir(C1))

print(C1.radius)

print(C1.color)

C1.add_radius(10)

print(C1.radius)

C1.drawCircle()



class Circle(object):
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color
        
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius

CircleObject = Circle()

CircleObject.radius = 10

print(CircleObject.color)
print(CircleObject.radius)

class Vehicle:
    color = "white"


    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None


    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity


V1 = Vehicle(150, 25)

print(V1.color)


class Graph():
    def __init__(self, id):
        self.id = id
        self.id = 80


val = Graph(200)
print(val.id)