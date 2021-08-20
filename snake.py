from turtle import Turtle


class Snake:
    def __init__(self):
        self.starting_pos = [(0, 0), (-20, 0), (-40, 0)]
        self.dots = []
        self.create()
        self.head = self.dots[0]

    def create(self):
        for position in self.starting_pos:
            self.add_segment(position)

    def add_segment(self, position):
        dot = Turtle(shape="square")
        dot.color("white")
        dot.penup()
        dot.setpos(position)
        self.dots.append(dot)

    def extend(self):
        self.add_segment(self.dots[-1].position())

    def move(self):
        for num in range(len(self.dots) - 1, 0, -1):
            new_x = self.dots[num - 1].xcor()
            new_y = self.dots[num - 1].ycor()
            self.dots[num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() == 270.0:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90.0:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0.0:
            pass
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180.0:
            pass
        else:
            self.head.setheading(00)



