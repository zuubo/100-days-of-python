from turtle import Turtle
import random as r
SPEED = 20
STARTING_ANGLE = 45


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.seth(STARTING_ANGLE)

    def ball_move(self):
        # print(self.position(), self.heading()) # for debugging
        self.fd(SPEED)

    def ball_bounce(self):
        self.seth(self.heading() + 270)
        self.status()

    def reset_ball(self):
        self.goto(0, 0)
        self.seth(45)

    def status(self):
        print(self.pos(), self.heading())
