import turtle

# Set up the turtle screen
screen = turtle.Screen()

# Create a turtle instance
pen = turtle.Turtle()

# Move the turtle to a position
pen.penup()
pen.goto(0, 0)
pen.pendown()

screen.bgcolor("white")  # Set the background color
pen.color("black")  # Set the pen color
pen.write("Hello, World!")

# Keep the window open until clicked
screen.exitonclick()
