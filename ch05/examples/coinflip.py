import random
import turtle

# functions


def is_in_screen(w, t):
    left_bound = -w.window_width() / 2
    right_bound = w.window_width() / 2
    top_bound = w.window_height() / 2
    bottom_bound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    still_in = True
    if turtleX > right_bound or turtleX < left_bound:
        still_in = False
    if turtleY > top_bound or turtleY < bottom_bound:
        still_in = False

    return True  # still_in


myt = turtle.Turtle()
myt.shape("turtle")
myt.speed(0)

wn = turtle.Screen()
wn.bgcolor("yellow")

distance = 10
angle = 90
# is_in_screen = True

colors = ["red", "green", "blue", "purple", "red"]

# top down programming
while is_in_screen(wn, myt):
    coin = random.randrange(0, 2)
    if coin:  # heads
        myt.right(angle)
    else:  # tails
        myt.left(angle)
    myt.forward(distance)

# wn.exitonclick()

# is_in_screen(wn, myt)
