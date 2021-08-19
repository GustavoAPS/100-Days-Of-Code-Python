from turtle import Turtle


class Paddle:
    def __init__(self, side):
        self.new_paddle = Turtle()
        self.new_paddle.penup()
        self.new_paddle.shape("square")
        self.new_paddle.color("white")
        self.new_paddle.shapesize(stretch_wid=5, stretch_len=1)

        if side == "right":
            self.new_paddle.goto(280, 0)
        if side == "left":
            self.new_paddle.goto(-280, 0)

    def go_up(self):
        new_y = self.new_paddle.ycor() + 20
        self.new_paddle.goto(self.new_paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.new_paddle.ycor() - 20
        self.new_paddle.goto(self.new_paddle.xcor(), new_y)
