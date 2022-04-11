from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.width(10)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0,-280)
        self.seth(90)
        for _ in range(10):
            self.pendown()
            self.fd(30)
            self.penup()
            self.fd(30)
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 70, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()