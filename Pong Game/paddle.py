from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.left(90)
        self.color("white")

    def move_up(self):
        self.forward(25)

    def move_down(self):
        self.backward(25)
