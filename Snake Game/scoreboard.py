from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.score = 0
        self.level = level
        if self.level == "hard":
            with open("data_hard.txt") as f:
                self.high_score = int(f.read())
        else:
            with open("data_eazy.txt") as f:
                self.high_score = int(f.read())
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(0, 275)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            if self.level == "hard":
                with open("data_hard.txt", mode="w") as f:
                    f.write(f"{self.high_score}")
            else:
                with open("data_eazy.txt", mode="w") as f:
                    f.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
