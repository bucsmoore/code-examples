

class Foo:
    def __init__(self):
        self.num = 5

    def addone(self):
        self.num += 1


class Bar(Foo):

    def addsub(self):
        self.num += 1


b = Bar()

b.addone()
b.addsub()

f = Foo()
f.addone()
f.addsub()        



