# Iteration
# iterable - you can loop over it

# mystr = "hello"  # special iterable list of characters
# mynums = [1, 2, 3, 4, 5]

# for ch in mystr:
#     print(ch)

# # for num in mynums:
# #     print(num)

# # # anything iterable can be 'indexed' into
# # print(mystr[0], mystr[1], mystr[2], mystr[3], mystr[4])

# # mynums[0] = 5
# # print(mynums)

# # #mystr[0] = "J" # can't do this

# # # mutable = changable
# # # immutable = can't be changed once created

# # num = 5

# # mystr = "hello"  # immutable
# # myotherstring = "hello"

# # mynums = [1, 2, 3, 4, 5] #mutable
# # myothernums = [1, 2, 3, 4, 5] #mutable

# # if mystr == myotherstring:
# #     print("They are the same")

# # if mynums == myothernums:
# #     print("They are the same")

# # if mystr is myotherstring:
# #     print("They are the same")

# # if mynums is myothernums:
# #     print("mynums are the same")

# # # substring
# # mystr = "heLLo"
# # # print(mystr[0])
# # # print(mystr[1:4])

# # # mystr = mystr[1:5] # slicing
# # print(mystr.lower(), mystr.upper(), mystr.capitalize(), mystr)

# # # Iterable objects are not always mutable

# # # slicing with mutable objects
# # mynums = [5, 8, 1, 123456879, 5]

# # # mynums[2:2] = [2.5, 2.6]
# # # print(mynums)

# # # mynums[3:3] = [2.5, 2.6]
# # # for i in mynums:
# # #     print(i)


# # # mynums[2:4] = [2.5, 2.6]
# # # print(mynums)

# # for i in mynums:
# #     i = i * 2
# # print(mynums)

# # # for i in range(len(mynums)):
# # #     mynums[i] = mynums[i] * 2
# # # print(mynums)

# # for i, v in enumerate(mynums):
# #     # i - index location in the list
# #     # v - the value at the index location
# #     print(i, v)
# # print(mynums)

# # index = 0
# # for v in mynums:
# #     mynums[i] = v * 2
# #     index += 2
# # print(mynums)

# # lists are slow

# ## tuple - immutable list
# # mynums = (5, 8, 1, 123456879, 5)  # immutable
# # mynums[2] = 2.5

# # x = 5
# # y = 6

# # x, y = y, x

# # temp = x
# # x = y
# # y = temp

# # num = [5] * 3
# # print(num)

# # num = (5,) * 3 #single element tuples MUST have a trailing comma

# # print(num)

# # mynums = [5, 8, 1, 123456879, 5]
# # print(list(enumerate(mynums)))

# # # x, y = (5, 6)
# # # for i, v in enumerate(mynums):
# # #     print(i, v)

# # contacts = [
# #     ["bill", "867-5309"],
# #     ["jane", "555-1212"],
# #     # ....
# # ]

# # name = input("Enter a name: ")

# # # worst case scenario
# # # looping n times, where n is the number items
# # for contact in contacts:
# #     if contact[0] == name:
# #         print(contact[1])
# #         break

# # # relationship index => value

# # # nums = [0:5, 1:8, 2:1, 3:123456879, 4:5]

# # # NOT VALID PYTHON
# # # contact = [
# # #     "bill": "867-5309",
# # #     "jane": "555-1212",
# # # ]

# # print(contact[name])

# # dictionary

# # print(contact["jane"])
# # print(contact["joe"]) ERROR

# # list[index] = value
# # dictionary[key] = value
# # - key/value pairs
# # - keys must be unique
# # - keys must be immutable


# # print(contact)
# # contact["joe"] = ["555-1212", "555-1213"]
# # print(contact)

# # for c in contact:
# #     print(c)
# #     print(contact[c])

# import json

# contact = {
#     "bill": "867-5309",
#     "jane": "555-1212",
# }
# contact["joe"] = "555-1213"

# # items() - enumerate for dictionaries
# for key, value in contact.items():
#     print(key)
#     print(value)

# for key in contact.keys():
#     print(key)

# for val in contact.values():
#     print(val)

# # print(contact["juan"])

# # get() - only for reading

# if contact.get("juan"):
#     print(contact["juan"])

# # ...

# # Strings
# # Lists
# # Tuples
# # Dictionaries


# class Movie:
#     def __init__(self, title, year, rating):
#         self.title = title
#         self.year = year
#         self.rating = rating


# m = Movie("The Matrix", 1999, "R")
# fptr = open("movies.json", "w")
# json.dump(m.__dict__, fptr)


# # Collection Objects

# # Strings - list characters - immutable
# # Lists - list of any set of objects - mutable
# # Tuples - immutable list of any set of objects
# mytuple = (5, 8, 1, 123456879, 5)
# # mytuple[0] = 1 # ERROR!

# import turtle

# # Dictionaries - used to store key/value pairs
# mydictionary = {"a": 1, "b": 2, "c": 3}
# mydictionary["a"] = turtle.Turtle()
# mydictionary["d"] = 4


# for loop
# 1. a set number of iterations
# 2. iteratiing over a collection

# while
# - more control over the loop

# msg = "Enter a number between 1 and 5:"
# num = int(input(msg))
# # for i in range(1000000):
# #     if num >5 or num < 1:
# #         num = int(input(msg))

# while num > 5 or num < 1:
#     num = int(input(msg))

# print("done")


# While Loop

# - while <boolean condition>:
#       <code block>

# if boolean condition is True, execute the code block
# otherwise skip it

# for i in range(10):
#     print(i)

# i = 0  # iterating variable
# while i < 10:
#     print(i)
#     i += 1 #iterating variable must change

# # get every other object from list
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0  # iterating variable
# while i < len(mylist):
#     print(mylist[i])
#     i += 2 #iterating variable must change


# for i in range(10):
#     print(i)
#     i += 3

# i = 0
# while i < 10:
#     print(i)
#     i += 3


# # Any for loop can be recreated with a while loop
# # Some while loops cannot be recreated with for loops

# print("Enter numbers to sum ['q' to quit]")

# sum = 0
# while sum != "q":
#     value = input("number: ")
#     if value.isdigit():
#         value = int(value)
#         sum += value  # sum = sum + value
#     elif value == "q":
#         print("Your total is:", sum)
#         sum = value

# sum = 0
# while True:
#     value = input("number: ")
#     if value.isdigit():
#         value = int(value)
#         sum += value  # sum = sum + value
#     elif value == "q":
#         break
# print("Your total is:", sum)


import random

i = 0
while i < 5:
    if random.randrange(2):
        i += 1
    print(i)
