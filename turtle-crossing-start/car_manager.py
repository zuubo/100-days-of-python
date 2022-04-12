from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X = 300
STARTING_POSITIONS = [(X, -225), (X, -200), (X, -175), (X, -150), (X, -125), (X, -100), (X, -75), (X, -50), (X, -25),
                      (X, 0), (X, 25), (X, 50), (X, 75), (X, 100), (X, 125), (X, 150), (X, 175), (X, 200), (X, 225)]


class CarManager:
    def __init__(self):
        self.cars = []
        self.game_running = True
        self.car_speed = STARTING_MOVE_DISTANCE

    def move_cars(self):
        for car in self.cars:
            if car.xcor() > -330:
                new_x = car.xcor() - self.car_speed
                car.setx(new_x)
            else:
                self.cars.remove(car)
                # print("removed a car")
                print(len(self.cars))

    def create_cars(self):
        car = Turtle('square')
        car.penup()
        car.color(random.choice(COLORS))
        car.turtlesize(1.0, 2.0)
        car.setposition(random.choice(STARTING_POSITIONS))
        # print(car.position())
        self.cars.append(car)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
