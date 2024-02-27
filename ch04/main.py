import turtle
myturtle = turtle.Turtle()
myturtle.speed(0) #makes turtle go faster
screen = turtle.Screen()
width = screen.window_width()
height = screen.window_height()

xcoor, ycoor = myturtle.pos()

horizontal_valid = abs(xcoor) < width/2
vertical_valid = abs(ycoor) < height/2
