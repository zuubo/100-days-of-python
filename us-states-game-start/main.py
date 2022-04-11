import turtle, csv

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(750, 750)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

LIST_STATES = []
correct_guesses = []

# Angela used pandas and the methods make this challenge a lot easier lol
with open("50_states.csv", newline="") as states:
    data = csv.reader(states)
    next(data, None)
    for row in data:
        LIST_STATES.append(row)


def check_state(guess):
    #  state[0] is the name, [1][2] are x and y
    for state in LIST_STATES:
        if guess == state[0] and guess not in correct_guesses:
            writer.goto(int(state[1]), int(state[2]))
            writer.write(state[0])
            correct_guesses.append(guess)
            print(correct_guesses)
            return True


while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # print(answer_state)

    if answer_state == "Exit":
        with open("states_to_learn.csv", mode="w", newline="") as learn:
            for state in LIST_STATES:
                if state[0] not in correct_guesses:
                    csv.writer(learn).writerow([state[0]])
        print("Check that CSV file and study harder for next time.")
        break

    if check_state(answer_state):
        print("you got it")

screen.mainloop()

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
