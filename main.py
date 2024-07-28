from turtle import Screen, Turtle
from paddle import Paddle
from pong import Pong
from scoreboard import Scoreboard
import time
time_sleep = 0.1
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Pong Game!! ")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong = Pong()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_on_game = True
while is_on_game:
    time.sleep(time_sleep)
    screen.update()
    pong.move()
    #detect collision with wall
    if (pong.ycor() == 280 or pong.ycor() == -280):
        pong.bounce_y()
    #detect collision with paddle
    if (pong.xcor() > 330 and pong.distance(r_paddle) < 50 or pong.xcor() < -330 and pong.distance(l_paddle) < 50):
        pong.bounce_x()
        if time_sleep > 0.04:
            time_sleep -= 0.02
    #detect collision with R miss
    if (pong.xcor() > 360):
        pong.reset_position()
        scoreboard.left_point()
        if (scoreboard.left_score == 5):
            scoreboard.game_over()
            is_on_game = False

    #detect collision with L miss
    if (pong.xcor() < - 360):
        pong.reset_position()
        scoreboard.right_point()
        if (scoreboard.right_score == 5):
            scoreboard.game_over()
            is_on_game = False

screen.exitonclick()
