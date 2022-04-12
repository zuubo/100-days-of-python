from turtle import Turtle


class Snake:
    def __init__(self):
        self.starting_x = 0
        self.segments = []

        for _ in range(3):
            snake_segment = Turtle(shape="square")
            snake_segment.penup()
            snake_segment.color("white")
            snake_segment.setx(self.starting_x)
            self.starting_x -= 20
            self.segments.append(snake_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
        self.segments[0].left(90)
