import math
import random
import turtle

pi = "raspberry"
# modulename.attribute
print(math.pi)
# input("This will not save anywhere")
# abs(-5)
print(random.randint(1, 1000000))

pen = turtle.Turtle()  # complex type

window = turtle.Screen()
num = 1  # primitive type

pen.shape("turtle")
pen.color("purple")
pen.forward(50)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(50)
pen.right(90)

pen.up()

pen.forward(100)

pen.down()
pen.forward(100)

# this always has to be the last line executed
window.exitonclick()
