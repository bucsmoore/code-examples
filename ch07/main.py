# # top level class: object
# class Animal:  # blueprint for data
#     # #dunder
#     aid = 0
#     def __init__(self, name, type="dog"):
#         # instance variable
#         self.name = name
#         self.type = type
#         self.id = id(self)
#         self.arrived_date = time.strftime("%d/%m/%Y")  # string formatted time
#     def calcid(self):
#         Animal.aid += 1
#         key = self.type[0].upper()
#         return f"{key}-{Animal.aid}"
# my_animal = Animal("zelda")
# my_animal2 = Animal(
#     "sansa",
#     "cat",
# )
# print(
#     my_animal.name,
#     my_animal.type,
#     my_animal.id,
#     my_animal.arrived_date,
# )
# print(
#     my_animal2.name,
#     my_animal2.type,
#     my_animal2.id,
#     my_animal2.arrived_date,
# )
import json
import random
import string


def generate_random_string(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


name = "A"
people = {}
for _ in range(1000):
    length = random.randint(5, 20)
    key = generate_random_string(length)
    people[key] = random.randint(1, 10)

print(people)
fptr = open("people.json", "w")
json.dump(people, fptr)
