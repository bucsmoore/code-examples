# you should have one class per file
# Model
class Point:
    # functions inside a class are called methods
    # _ _ name _ _: dunder, special method used by python
    # self: the created object
    def __init__(self, xarg=0, yarg=0, colorarg="red"):
        self.x = xarg
        self.y = yarg
        self.color = colorarg

    # def printme(self):
    #     # print(self.x, self.y, self.color)
    #     print(self.x, self.y, self.color)

    # def mynotmethod():
    #     print()


# what are objects that will change state

# Class 'rules'
# - 1 class per file (unless you have a good reason)
# - filename should be the same the class, all lowercase
# - class names are Titlecase
