import random
import turtle

t = turtle.Turtle()
t.speed(0)
win = turtle.Screen()
wh = win.window_height() / 2
ww = win.window_width() / 2
print(wh, ww)
while abs(t.xcor()) < ww and abs(t.ycor()) < wh:
    coin = random.randint(0, 1)
    if coin:
        t.right(90)
    else:
        t.left(90)

    # shorcut if/else
    # t.right(90) if coin else t.left(90)

    t.forward(50)
