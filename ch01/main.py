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


# # for variable in list:
# #     algorithm

# # for i in [1,2,3,4]:
# #     print(i)
# #     i = i + 10
# #     print(i)
# # number_of_nums = 10
# # print(list(range(number_of_nums)))#stop
# # print(list(range(1, 10)))#start, stop
# # print(list(range(1,10, 3))) #start, stop, step


# myturtle = turtle.Turtle()
# myscreen = turtle.Screen()
# myturtle.shape("turtle")
# myturtle.xcor = -200

# colors = ["purple", "blue", "black", "yellow", "green"]

# for color in colors:
#     myturtle.down()
#     myturtle.color(color)
    
#     for i in range(4): #[0]*4
#         myturtle.forward(100)
#         myturtle.left(90)
        
#     myturtle.up()
#     myturtle.forward(15)

# # myscreen.exitonclick()


# # FOR LOOPs

# mylist = ['a', 'b', 'c']
# mystr = "abc"

# for element in mylist:
#     print(element)

# for char in mystr:
#     next_char = ord(char) + 1
#     next_char = chr(next_char)
#     print(next_char)

# msg = "Happy Birthday!"

# for _ in range(4): #[0,1,2,3]
#     print(msg)


# # For Loop

# # 1. Loop through a list of objects and apply an algorithm to each one
# # 2. Loop a specified number of times and perform an algorithm for each loop (i.e. iterations)

# print( list(range(10)) )
# print( list(range(5, 10)) )
# print( list(range(5, 10, 5)) )

# mylist = ['a', 'b', 'c', 'd']
# for x in range(0, 4, 2):
#     print(mylist[x])

hex_chars = "ABCDEF0123456789"

# color_str = "#"
# for _ in range(6):
#     color_str.append(random.choice(hex_chars))

# list comprehension
color_char_list = [random.choice(hex_chars) for _ in range(6)]

color_str = "".join(color_char_list)

color_str = "#"+color_str
print(color_str)


import pygame

pygame.init()
screen = pygame.display.set_mode()

wsize = pygame.display.get_window_size()
x_size = wsize[0]
y_size = wsize[1]
center_coor = [x_size/2, y_size/2]

while True:  
    # check for events since the last time through the loop
    for event in pygame.event.get():
        pass

    #code 
    
    pygame.display.flip()
    
    break