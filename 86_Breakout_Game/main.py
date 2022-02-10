from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600

screen = Screen()
screen.tracer(0)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.listen()
screen.bgcolor("black")
screen.title("PONG")

player_paddle = Paddle()
ball = Ball()

screen.onkey(player_paddle.go_right, "Right")
screen.onkey(player_paddle.go_left, "Left")

game_is_on = True

while game_is_on:

    screen.update()
    ball.move()

    if ball.ycor() > (SCREEN_HEIGHT/2):
        ball.vertical_bounce()

    if ball.distance(player_paddle) < 50:
        ball.vertical_bounce()

    if ball.xcor() > SCREEN_WIDTH/2 or ball.xcor() < -1 * (SCREEN_WIDTH/2):
        ball.horizontal_bounce()

    #if ball.ycor() > 300:
    #    ball.reset_position()

    #if ball.xcor() < -300:
    #    ball.reset_position()

    time.sleep(0.1)

screen.exitonclick()
