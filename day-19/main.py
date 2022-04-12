from turtle import Turtle, Screen

delmar = Turtle()
screen = Screen()
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black']
selected_colour = 0
delmar.pensize(5)


delmar.write("Use w,a,s,d to move. \nc to clear the screen. \nspace to change colours.")

def cycle_colours():
    global selected_colour
    if selected_colour < len(colours) -1:
        selected_colour += 1
    else:
        selected_colour = 0
    delmar.color(colours[selected_colour])

def move_forwards():
    delmar.forward(20)


def move_backwards():
    delmar.backward(20)


def rotate_left():
    delmar.left(45)


def rotate_right():
    delmar.right(45)

def reset():
    delmar.reset()

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=rotate_left, key="a")
screen.onkey(fun=rotate_right, key="d")
screen.onkey(fun=reset, key="c")
screen.onkey(fun=cycle_colours, key='space')
screen.exitonclick()
