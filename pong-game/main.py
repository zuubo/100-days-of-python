from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

# GOTTA FIX THE BALL BOUNCE PHYSICS, IT'S KINDA BUGGY

SCREEN_TOP = 290
SCREEN_BOTTOM = -SCREEN_TOP

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Ponggers')
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')

game_is_on = True
while game_is_on:
    sleep(0.05)
    screen.update()
    ball.ball_move()

    # detects ball collision with top or bottom of screen
    if ball.ycor() > SCREEN_TOP or ball.ycor() < SCREEN_BOTTOM:
        ball.ball_bounce()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 335 or ball.distance(l_paddle) < 60 and ball.xcor() < -335:
        ball.ball_bounce()

    # detect if ball goes off-screen right
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_point()
        ball.status()

    # detect if ball goes off-screen left
    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()
        ball.status()

screen.exitonclick()
