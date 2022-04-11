from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snakey snake")

snake = Snake()
food = Food()
boardy = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    boardy.show_score()

    # detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        boardy.score +=1
        print("yum")
        snake.extend()

    # detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # boardy.game_over()
        boardy.reset()
        snake.reset()

    # detect tail collision
    for segment in snake.segments[1:]: # loop through every item in segments list excluding the first one
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # boardy.game_over()
            boardy.reset()
            snake.reset()
    # if head collides with any segment in the tail:
        # trigger game_over

screen.exitonclick()
