from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_player()
        self.seth(90)
        self.passed_finish_line = False

    def move_up(self):
        self.new_y = self.ycor() + MOVE_DISTANCE
        self.sety(self.new_y)
        if self.ycor() > FINISH_LINE_Y:
            self.setposition(STARTING_POSITION)
            self.passed_finish_line = True

    def reset_player(self):
        self.setposition(STARTING_POSITION)
