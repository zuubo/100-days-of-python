from turtle import Turtle


class Paddle(Turtle):  # TBH I'm not sure how this is able to initialize itself as a turtle object

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.goto(position)
        self.left(90)
        self.color('white')
        self.penup()
        self.shapesize(1.0, 5.0)

    def up(self):
        self.fd(20)

    def down(self):
        self.bk(20)

