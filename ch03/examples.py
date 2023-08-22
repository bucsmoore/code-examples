# # bool - boolean value
# # True/False
# # - caps are important

# # True, 1, "Hello"

# print(type(True))

# print(bool(1), bool(-1), bool("hello"))

# print(bool(0), bool(""), bool([]))

# # boolean expressions

# x = 5
# y = 10

# print(x == y)  # equality, == boolean equality test, = is assignment
# print(x > y)
# print(x < y)
# print(x >= y)  # => - ERROR!
# print(x <= y)  # =< - ERROR!
# print(x != y)  # not equal

# # and, or, not - semantic operators

# # and: and == True, when x and y are both True

# print(True and True)  # true
# print(True and False)  # false
# print(False and True)
# print(False and False)

# # or - at least one True

# print(True or True)  # true
# print(True or False)  # true
# print(False or True)  # true
# print(False or False)  # false

# # not - negation

# print(not True)  # false

# print("apple" == "apple")

# print("apple" < "Apple Pie")
# print(ord("a"), ord("A"))

# print(1 == 1.0)
# print(1 is 1.0)

# print(1 is 5 / 5)
# print(1 is 5 // 5)

# mynums = [1, 2, 3, 4, 5, 6, 7]
# print(1.0 in mynums)
# # print(10 in mynums)

# a = int(input("num:"))

# if a < 0:  # colon
#     a = abs(a)  # indentation
# else: # no condition, always optional
#     print("positive")

# print(a)  # de-indentation to eend the if statment

# a = int(input("num:"))
# if a > 5:
#     if a > 10:
#         print("x is greater than 10")
#     else:
#         print("x is greater than 5")
# else:
#     print("x is less than or equal to 5")

# elif
# always goes between the if and else
# is optional
# can have as many as you like

# if statements - only one condition will execute

# a = int(input("num:"))
# if a > 5:
#     print("x is greater than 5")
# elif a > 10: # will never run
#     print("x is greater than 10")
# else:
#     print("x is less than or equal to 5")


# a = int(input("num:"))

# if a > 10:  # will never run
#     print("x is greater than 10")
# elif a > 5:
#     print("x is greater than 5")
# else:
#     print("x is less than or equal to 5")

# if <boolean condition>: #required
#   # do something
# elif <boolean condition>: #optional
#   # do something
# else: #optional
#   # do something


### Fizzbuzz

# - loop through a range of values supplied by the user
# - for each value in the range
# - if the value is divisible by 3, print "fizz"
# - if the value is divisible by 5, print "buzz"
# - if the value is divisible by 3 and 5, print "fizzbuzz"

# num = int(input("enter an upper limit:"))
# for i in range(num + 1):
#     print("number: ", i, "another", i, "and another", i)
#     # if not i % 3:
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         # else: error
#         print("buzz")

# print("Hi", "Goodbye", 456, sep=",")

# 1 and 1
# 0 and 1

# 1 or 1
# 0 or 1
# 1 or 0
# 0 or 0


if True:
    print("True")

if 6 < 5:
    print("6 is less than 5, everything is broken")
elif 6 == 5:
    print("math is still broken")
else:
    print("math is correct")

x = "a"
# only one condition will execute
if x < "y":
    print("yup")
elif x < "m":  # optional
    print("more yup")
else:  # optional
    print("nope")
