import turtle

import point


class Point:
  def __init__(self, x=0, y=0, color=[255, 0, 0]):
    self.x = x
    self.y = y
    self.color = color

  def set_to_comp_color(self):
    red_comp = 255 - self.color[0]
    blue_comp = 255 - self.color[1]
    green_comp = 255 - self.color[2]
    self.color = [red_comp, blue_comp, green_comp]

class Graph:

    def __init__(self, points=None, width=200, height=200):
        self.width = width
        self.height = height
        self.points = points
        self.window = turtle.Screen()
        self.window.setworldcoordinates(-self.width, -self.height, self.width, self.height)
        self.plotter = turtle.Turtle()

    def drawAxis(self):
        self.plotter.home()
        self.plotter.up()
        self.plotter.hideturtle()
        
        self.plotter.goto(-self.width, 0)
        self.plotter.down()
        
        #draw the x-axis
        self.plotter.forward(self.width*2)
        
        self.plotter.up()
        self.plotter.goto(0, self.height)
        self.plotter.setheading(270)
        self.plotter.down()

        #draw the y axis
        self.plotter.forward(self.height*2)
        
    def plotGraph(self):
        self.drawAxis()
        self.plotter.up()
        for p in self.points:
            self.plotter.goto(p.x, p.y)
            self.plotter.dot(3, p.color)

    def clearGraph(self):
        self.drawAxis()
        self.plotter.clear()
        self.points = []

    def addPoint(self, x=0, y=0, label=""):
        p = point.Point(x, y, label)
        self.points.append(p)