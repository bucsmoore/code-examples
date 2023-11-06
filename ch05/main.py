# # import turtle

# # def draw(pen, num_sides, length=50):
# #     angle = 360 / num_sides
# #     for _ in range(num_sides):
# #         pen.forward(length)
# #         pen.right(angle)


# # sides = int(input("How many sides?"))
# # length = int(input("What length?"))
# # t = turtle.Turtle()
# # s = turtle.Screen()

# # t.color("green")
# # t.shape("turtle")

# # draw(t, sides, length)
# # draw(t, sides)

# # s.exitonclick()


# def foo(x):  # standard generic functions in CS
#     y = x
#     return y, x


# def bar(x):
#     pass

# a, b = foo(5)  # functin becomes it's output

# print(a, b)


# print(max(abs(-5), abs(-7)))

# print(max(abs(-5), 7))
# print(max(5, 7))
# print(7)


# def foo(): #defined in a function is limited to that function
#     res = max(abs(-5), abs(-7))
#     return res


# output = foo()
# print(output)

# COLOR = "green"


# def powerof(x=0, y=0):  # definition
#     p = p + y
#     y = x**p
#     return y


# p = 3
# result = powerof(10, 2)  # execution
# var = CONSTANT + 1
# var = CONSTANT + 3
# print(result)


# f(x) = y
def foo(num=0):
    return num + num


# f(x) = y
def bar(num=0):
    print("inside", num + num)


# Print vs Return
# Return gives the result of an algorithm
# Print does nothing

result = foo()
print(result)
result = bar()
print(result)
