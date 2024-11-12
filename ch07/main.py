# class MyClass:
#     def __init__(self):
#         self.x = 10
#         self.y = 7


# # obj is an instance of MyClass()
# obj = MyClass()
# obj2 = MyClass()

# print(obj, obj.__dict__)


# import json

# news = open("news.txt").read()
# subs_file = open("subs.json")
# subs = json.load(subs_file)

# for k, v in subs.items():
#     news = news.replace(k, v)

# betterfptr = open("betternews.txt", "w")
# betterfptr.write(news)
# betterfptr.close()


# def foo(a, b="", c="", selection=None):
#     print(a, type(a), b, c)
#     selection()


# def bar():
#     print("bar is running")


# def car():
#     print("car is running")


# def main():
#     foo(1)
#     foo("1")
#     foo(1, 2, 3, 4, 5)
#     foo(c=4)

#     foo(1, selection=bar)

#     foo(1, selection=car)


# main()


# class Dog:
#     name
#     breed
#     color
#     age


# fido = Dog()

# str

# class str:
#     chars = []
#     length = 0

import graph

# class int:
#     num = 0

graph = graph.Graph()
graph.addpoint(3, 7, "purple")
graph.addpoint(1, 2, "yellow")
graph.addpoint(1, 3)
