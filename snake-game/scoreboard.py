from turtle import Turtle
with open("data.txt", mode="r") as data:
    saved_high_score = data.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.high_score = int(saved_high_score)
        self.color("white")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as new_data:
                new_data.write(str(self.high_score))  # could use an f string to write as well
                print("Saved new high score")
        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 14, "bold"))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game over sucka", align="center")
