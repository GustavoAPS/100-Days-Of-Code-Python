from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.setup(width=600, height=400)
screen.listen()
right_paddle = Paddle(side="right")
left_paddle = Paddle(side="left")
screen.bgcolor("black")
screen.title("PONG")

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.exitonclick()
