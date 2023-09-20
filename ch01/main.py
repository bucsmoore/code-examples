# print("Hello")
# print(5)
# print
# print("gooodbye")

# print(ord("A"))
# print(ord("a"))
# print(chr(97))
# print(chr(65))

# print("Hel'lo")
# print('Hel"lo')
# print("""He"ll'o""")
# print('''He"ll'o''')

# print("5" + "7")
# print(5 - 7)
# # print("5" - "7")

# print("This", "Sunday, " * 3)

# print(5, -1, 0)  # int

# print(5 + 5)
# print(5 - 5)
# print(5 * 5)
# print(5 / 5)
# print(5**5)
# print(5 % 6)

# # str
# "hi"
# # int
# 5
# # float
# 5.0

# variables

# label for some data
# = - assignment operator
# var = 5  # assign the valu

# print(6 + var)
# print(7 - var)
# print(8 * var)

# var = 10

# print(6 + var)
# print(7 - var)
# print(8 * var)

# # v = (v + v)
# var = (var + var * 2) % var

# print(var)

# var1 = []
# var2 = []
# var3 = [1, 3, 4]

5
"Hello"
5.0

# objects
# objects have both a value and a type

# DRY - Don't Repeat Yourself

# print(7 + 7)
# variable = 7
# print(variable + variable)

# container type
# - hold objects

# var = 6

# var = list()
# var = []

# print(var == [])
# print(type(var))

# list_length = len(mynums)
# print(list_length)
# list_length = len(myobjs)
# print(list_length)

# mylist = []
# mynums = [1, 2, 3, 4, 5, 6]
# myobjs = [1, "Hello", 5.6]

# # list are 0 indexed
# # first item is at loccation 0
# val = myobjs[1]
# print(val)
# val = myobjs[0]
# print(val)
# # val = myobjs[3]
# val = myobjs[2]
# print(val)
# # length = len(myobjs)
# # val = myobjs[length - 1]
# val = myobjs[-1]
# print(val)
# myobjs[-1] = "The end"
# myobjs[0] = "The beginning"
# print(myobjs)

# myobjs.append(myobjs)
# myobjs[0] = "This was changed"
# print(myobjs)
# print(myobjs[-1])
# input("Please enter input:") - ERROR!
# var is a str
# var = input("Please enter a number:")
# var = int(var)
# # or
# var = int(input("Please enter a number:"))

# print(var, type(var))
# print(var + 6)

num = -5.0
strnum = str(num)
intnum = int(num)
print(strnum, intnum)

# =====

var = float(strnum)
print(var)
print(float(strnum))

# =====

strnum = "5.0"
float(strnum)
mylist = list(strnum)
print(mylist)


mydict = {"a": 1, "b": 2}
# list
num = 5
letter = "a"
floatingpoint_thisthing = 1.2

my_data = [num, letter, floatingpoint_thisthing]
print(my_data)
print(my_data[1])
print(my_data[-2])

my_data.append("another value")
del my_data[2]


# input

food1 = input("WHat is one of your top 3 foods?")
food2 = input("WHat is another one of your top 3 foods?")
food3 = input("WHat is the last one of your top 3 foods?")

# anti-pattern
# Magic Number / Magic Value
num = input("Enter a number to triple")
num = float(num)

# num = float(input("Enter a number to triple"))

print(num * 3.147)

print(num * 3)  # magic numbers

factor_amt = 3
print(num * factor_amt)
