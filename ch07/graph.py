import point


class Graph:
    def __init__(self):
        self.points = []
        self.limits = (100, 100)

    def addpoint(self, x, y, color="purple"):
        p = point.Point(x, y, color)
