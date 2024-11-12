import time
import uuid


class Animal:
    def __init__(self, name, type="dog"):
        self.name = name
        self.type = type
        #
        self.id = uuid.uuid4()
        self.arrived = time.strftime("%d/%m/%Y")  # string formatted time

    def __str__(self):
        return f"{self.name}: {self.type}, {self.id}, {self.arrived}"


def main():
    a = Animal("zelda")
    print(a)
    a = Animal("cat", type="cat")
    print(a)
    print(a.name, a.type)


main()
