from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=400)
screen.listen()
screen.bgcolor("black")
screen.title("PONG")
right_paddle = Paddle(side="right")
left_paddle = Paddle(side="left")
ball = Ball()

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.bounce()

    time.sleep(0.1)
screen.exitonclick()
