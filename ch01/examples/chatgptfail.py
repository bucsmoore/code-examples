import turtle

# Asked ChatGPT to draw a Cat with Turtle and Python.
# The result is below.

# Create a turtle object
my_turtle = turtle.Turtle()

# Draw the cat's head
my_turtle.circle(50)

# Draw the cat's ears
my_turtle.left(90)
my_turtle.forward(75)
my_turtle.right(90)
my_turtle.forward(25)
my_turtle.right(90)
my_turtle.forward(25)
my_turtle.left(180)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(75)

# Draw the cat's eyes
my_turtle.penup()
my_turtle.goto(-25, 50)
my_turtle.pendown()
my_turtle.circle(5)
my_turtle.penup()
my_turtle.goto(25, 50)
my_turtle.pendown()
my_turtle.circle(5)

# Draw the cat's nose
my_turtle.penup()
my_turtle.goto(0, 25)
my_turtle.pendown()
my_turtle.circle(5)

# Draw the cat's mouth
my_turtle.penup()
my_turtle.goto(-15, 0)
my_turtle.pendown()
my_turtle.right(45)
my_turtle.forward(15)
my_turtle.left(90)
my_turtle.forward(15)
my_turtle.right(45)

# Hide the turtle and exit
my_turtle.hideturtle()
turtle.exitonclick()