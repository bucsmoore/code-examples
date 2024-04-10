# SINGLE RESPONSIBILITY PRINCIPLE
# objects and functions should do one thing


class Blanket:
    # fancy dictionary
    def __init__(self, shape, color, pattern):
        self.shape = shape
        self.color = color
        self.pattern = pattern

    # def __dunder__(self):
    # used by python

    # must a string
    def __str__(self):
        return f"{self.color} {self.shape} Blanket"


class EBlanket(Blanket):
    def __init__(self, shape, color, pattern):
        super().__init__(shape, color, pattern)
        self.on = False

    # Method is a function that belongs to a class
    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False


# instance of the Blanket class
eblanket = Blanket("square", "red", "argyle")
# call a method on that instance
eblanket.turn_on()

# another instance of the Blanket class
eblanket2 = Blanket("square", "red", "argyle")
# call a method on that instance
eblanket2.turn_off()

value = str(eblanket)
# print(eblanket, eblanket2)

print(vars(eblanket))
print(eblanket.__dict__)
