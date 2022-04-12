from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colours = ['red', 'green', 'blue', 'purple', 'pink', 'yellow', 'orange', 'black', 'brown', 'grey']
turtle_racers = []



for turtle_index in range(len(colours)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(2,2)
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-200, y=-100 + (30 * turtle_index))
    turtle_racers.append(new_turtle)

turtle_racers[-1].fd(150)
turtle_racers[-4].fd(150)
turtle_racers[0].fd(150)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_racers:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            print(winning_color)
            if user_bet.lower() == winning_color.lower():
                print(f"Nice! The {winning_color} turtle won! You guessed right!")
            else:
                print(f"The {winning_color} turtle won. You picked {user_bet}.")


# franklin = Turtle(shape="turtle")
# franklin.color(colours[0])
# franklin.penup()
# franklin.goto(x=-200, y=-100)



screen.exitonclick()