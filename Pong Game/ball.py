from turtle import Turtle

STEP = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.step_x = STEP
        self.step_y = STEP
        self.penup()
        self.shape("circle")
        self.color("white")
        self.move_speed = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.step_x *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.step_y *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
