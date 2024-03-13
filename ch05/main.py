
# definition of a function
# f(x) = y

# 5 + 6

# Vending Machine

# built-in functions
# print("Hello")
# result = input("Give me a numbr")

# var = 0
# def myfunc():
#   var = int(input("input a number"))
#   #var = int(var)
#   var = var * var
#   print(var)

# #call
# myfunc()
# print("Nice job, try again")
# myfunc()

# print(var)


# def add(x, y): #parameters num, num
#   return x + y

# def letter_grade(percentage): #92
#   letter=""
#   if 90 <= percentage:
#     letter = "A"
#   elif 80 <= percentage:
#     letter = "B"
#   elif 70 <= percentage:
#     letter="C"
#   else:
#     letter = "F"
   
#   print(letter)

# def hello():
#   print("hello")

# def execute(f, params=None):
#   if params:
#     f(*params)
#   else:
#     f()

# execute(letter_grade, [92])
# execute(hello)


# def recur(num=1):
#   """
  
#   """
#   var = "some data"
#   print(num, var)
#   recur(num=num+1)


# recur()

# global_var = "Don't do this once you learn about main functions"
# # f(x) = y 

# def foo(num, var):
#   var = 8
#   y = num ** 2
#   print(y)
  
# def bar(num, num2):
#   y = num * num2
#   print(y)

# foo(5, global_var) #num= 5
# foo(6)
# bar(7, 9) #another_random_variable_name=7, another_another_random_variable_name = 9
# bar()
# foo()
# bar()

# red_sqyare = ...
# blue_square = ...

# while True:
#   for event in pygame...events():
#     if quit:
#       pass
#     elif event == pygame.MOUSEBUTTONDOWN:
#       if red_sqyare.collidepoint(event.pos):
#         winner = "red"
#       else:
#         winner = "blue" 


#     if red_points > blue_points:
#       print("red won")
#       if winner == "red":
#          print("correct")
#       else:
#         print("no")
#     elif red_points < blue_points:
#       print("blue won")
#       if winner == "blue":
#          print("correct")
#       else:
#         print("no")


import turtle


def draw_butterfly():
    window = turtle.Screen()
    window.bgcolor("white")

    butterfly = turtle.Turtle()
    butterfly.speed(1)

    butterfly.fillcolor("purple")
    butterfly.begin_fill()

    for _ in range(2):
        butterfly.circle(50, 180)
        butterfly.right(60)
        butterfly.circle(50, 180)

    butterfly.right(120)

    for _ in range(2):
        butterfly.circle(50, 180)
        butterfly.right(60)
        butterfly.circle(50, 180)

    butterfly.end_fill()

    window.exitonclick()

draw_butterfly()