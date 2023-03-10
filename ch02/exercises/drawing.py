import turtle

my_turtle = turtle.Turtle()
window = turtle.Screen()

window.bgcolor("white")

my_turtle.color("pink")
my_turtle.shape("turtle")

sides = int(input("number of sides:"))
length = int(input("length of each side:"))

for i in range(sides):
    my_turtle.left(360 / sides)
    my_turtle.forward(length)

window.exitonclick()
