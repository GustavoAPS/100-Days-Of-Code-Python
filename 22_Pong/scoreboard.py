from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-50, 125)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(50, 125)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def add_l_point(self):
        self.l_score += 1

    def add_r_point(self):
        self.r_score += 1
