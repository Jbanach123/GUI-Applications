from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 260)
        self.level = 0
        self.write(f"Level: {self.level}", font=FONT)

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.goto(-270, 260)
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
