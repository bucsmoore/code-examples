import turtle


class Turtle:
    pass


# global scope: anything not in a function


def bar(t, s, l):
    x = foo  # function scope:bar
    for i in range(s):
        t.forward(l)
        t.left(360 / s)


def other():
    y = 0  # fucntion scope: other


# bar() - error
foo = "Hi"

sides = int(input("how many sides"))
length = int(input("length of each side"))
donatello = turtle.Turtle()

bar(donatello, sides, length)
