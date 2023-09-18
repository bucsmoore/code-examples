import turtle  # 1.  import the modules

wn = turtle.Screen()  # 2.  Create a screen
wn.bgcolor("green")
donatello = turtle.Turtle()
donatello.shape("turtle")
colors = ["purple", "red", "yellow", "blue"]
for c in colors:
    donatello.color(c)
    for _ in range(4):
        donatello.left(90)
        donatello.forward(50)
    donatello.up()
    donatello.forward(100)
    donatello.down()

wn.exitonclick()
