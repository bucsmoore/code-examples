
## SLOC - source lines of code

Unix - 10000 lines
Pacemaker - 40000 lines
Webbrowser - 10 million
OS - >100 million

# Problem to be solved

Complexity


# Objects

Data that has behavior

1: int object that can do arithmetic
"Hello": list of characters that can do lots of stuff

## Types of Programming

- Procedural Programming
  - sequential instructions
- Object Orient Programming

# OOP

- Complex Objects
  - Example: Turtle
  - made up of other objects

- State
  - The values of your data
- Behavior
  - What can your data do?

Objects manage their own data, and hide complexity in functions (methods)



# Model: Graph

```py
class Graph:
  points = []
  boundaries = []

  def add_point(p):
    points.append(p)

class Point:
    x = 0
    y = 0
    color = []
```


# Classes

all objects are created from classes

Classes are data blueprints
like functions are algorithm blueprints

Class == Type

- instance: an object created from a class
- instance variable: an object inside of a class, attribute
- interface: the methods (functions) of a class
