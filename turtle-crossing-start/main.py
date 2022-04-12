import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_man = CarManager()
scoreboard = Scoreboard()

game_tick = 6  # Angela uses a randint(0,6) in the car manager module, might be a better idea
target_tick = 6


def increase_level():
    global target_tick
    scoreboard.level += 1
    scoreboard.update_score()
    player.passed_finish_line = False
    car_man.increase_car_speed()
    if target_tick > 1:
        target_tick -= 1


screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkey(increase_level, "l")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # print(game_tick)

    if player.passed_finish_line:
        increase_level()

    if game_tick != 0:
        game_tick -= 1
    else:
        game_tick = target_tick
        car_man.create_cars()

    car_man.move_cars()
    for car in car_man.cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    screen.update()

screen.exitonclick()
