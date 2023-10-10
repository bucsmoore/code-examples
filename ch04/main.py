#

# mylist = ["a", "b", "c"]
# print(mylist[0])
# print(mylist[0:2])  # ['a','b']
# print(mylist[:-1])  # ['a','b']
# print(mylist[0:10])  # no error, just ignores out of range

# otherlist = ["z", "y"]

# mylist[1:1] = otherlist  # ['a','z', 'y', 'b','c']
# print(mylist)
# mylist[1:-1] = otherlist  # ['a','z', 'y','c']
# print(mylist)

# mylist = ["a", "b", "c"]
# mylist[1:-1] = [3, 2, 3]
# # sorted(mylist)
# print(mylist)

# mylist = ("a", "b", "c")  # tuple
# mylist[0] = "z"

# myval = (5,) * 4
# print(myval)

# x = 5
# y = 6
# temp = x
# x = y
# y = temp

# x, y = y, x

# mytuple = ("red", "green", "blue")

# c1, c2, c3 = mytuple


# contacts = [
#     ("leonardo", 123 - 3456),
#     ("donatello", 987 - 6543),
#     ("raphael", 867 - 5309),
# ]

# name = input("What name whould you like?")

# for person in contacts:
#     if person[0] == name:
#         print(person[1])

# mylist = [
#     "a",
#     "b",
# ]  # [0:a, 1:b]

# dictionary
# contacts = {
#     "leonardo": "123 - 3456",
#     "donatello": "987 - 6543",
#     "raphael": "867 - 5309",
# }
# print(contacts)
# contacts["michelangelo"] = "567-9098"
# print(contacts)
# contacts["leonardo"] = contacts["michelangelo"]
# print(contacts)

# # LVALUE must be immutable
# contacts["leonardo"] = 4  # RVALUE anything

# print(contacts)
# contacts["michelangelo"] = contacts["leonardo"]
# print(contacts)

contacts = {
    "leonardo": "123 - 3456",
    "donatello": "987 - 6543",
    "raphael": "867 - 5309",
}
for contact in contacts:
    print(contact)
    print(contacts[contact])

for key, value in contacts.items():
    print(key)
    print(contacts[key])
    print(value)

# print(contacts["michelangelo"]) ERROR

name = input("enter name")
print(contacts.get(name))  # READ ONLY

contacts[name] = "some value"
# contacts[nome] = "some value" # beware of typos

print(contacts.get("sgdfhj", "return this instead"))
