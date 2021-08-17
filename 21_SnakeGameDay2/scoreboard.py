from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        score_text = "Score: "+str(self.score)
        self.write(arg=score_text, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_score()
