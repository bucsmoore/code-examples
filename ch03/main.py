# Selection

# # Booleans
# bool
# True
# False

# print(bool(0))
# print(bool(5))
# print(bool("Hello"))

# "True" is True
# "False" is True
# # False is an empty value
# # 0
# # []
# # ""
# # None

# x = 5  # assignment operator
# y = 6

# print(x == y)  # == equality
# print(x != y)  # != bang/no equal
# print(x > y)  #
# print(x < y)  #
# print(x >= y)  #
# print(x <= y)  #
# # print(x => y) ERROR

# print(x and y)  # True and True = True,
# # False and True = False
# # True and False = False
# print(x or y)  # ||
# # True or True = True,
# # False or True = True
# # False or False = False
# print(not y)  # !
# # False = True

# print(x is x)
# print(x is y)

# x = "He"
# y = "Hello"
# print(x in y)
x = 4
print(x < 6 and x > 2)  # True
print(x > 10 or x % 2 == 0)  # True
print(not (x < 6))  # False

mystr = "Hello There"
#mystr = list(mystr)
print("o T" in mystr)  # True
#mystr2 = mystr[:]
mystr2 = mystr
print(mystr, mystr2)
print(mystr is mystr2)
print(mystr == mystr2)  # True
