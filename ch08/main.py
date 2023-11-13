import turtle

# x = 5
# x.forward() #error

# t = turtle.Turtle()
# t.forward(50) #method

# class Foo:
#     def __init__(self):
#         self.x = 5

#     #define a method
#     #first parameter is self
#     def double(self): 
#         return self.x * 2

# foo = Foo()
# num = foo.x + 1

# foo = {"x":5}
# num = foo['x'] + 1
# foo.double()

class Point:

    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y
        z = 6 #not a instance attribute, no self.

    def __str__(self):
        return self

    def halfway(self, point):
        """
        arg:
          - point: must be a Point object
        """
        print(self)
        print(point)
        
        mx = (self.x - point.x) / 2
        my = (self.y - point.y) / 2
        return Point(mx, my)

#object instance of the Point Class
pointA = Point()
pointB = Point(4, 6)


pointC = pointA.halfway(pointB) # halfway(pointA, pointB)
print(pointC)

print()
print(pointC.__dict__)


import turtle

t = turtle.Turtle()
print(t.__dict__)