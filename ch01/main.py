import math  # math.pi
import random
import turtle

#from math import pi  #pi

# pi = 5
# print(pi)
# print(math.pi)

# myturtle = turtle.Turtle()
# myscreen = turtle.Screen()

# myturtle.color("purple")
# myturtle.shape("turtle")
# myturtle.forward(50)
# myturtle.left(90)
# myturtle.forward(50)
# myturtle.left(90)
# myturtle.up()
# myturtle.forward(50)
# myturtle.left(90)
# myturtle.down()
# myturtle.forward(50)
# myturtle.left(90)

# ## exitonclick() is always the last thing that happens in your program
# myscreen.exitonclick()


# for variable in list:
#     algorithm

# for i in [1,2,3,4]:
#     print(i)
#     i = i + 10
#     print(i)

print(list(range(10)))#stop
print(list(range(1, 10)))#start, stop
print(list(range(1,10, 3))) #start, stop, step


myturtle = turtle.Turtle()
myscreen = turtle.Screen()
myturtle.shape("turtle")
myturtle.xcor = -200

colors = ["purple", "blue", "black", "yellow", "green"]

for color in colors:
    myturtle.down()
    myturtle.color(color)
    
    for i in range(4): #[0]*4
        random.sample("ABCDEF0123456789", k=6)
        myturtle.forward(100)
        myturtle.left(90)
        
    myturtle.up()
    myturtle.forward(15)

myscreen.exitonclick()