import turtle as t
import random
screen = t.Screen()
screen.setup(1800,900,0,0)

t.colormode(255)

delvin = t.Turtle()
delvin.shape("turtle")
delvin.speed(3)

melvin = t.Turtle()
melvin.hideturtle()
melvin.penup()

# colours = ['pink', 'orange', 'red', 'blue', 'yellow']
colours = ['azure', 'aquamarine', 'beige', 'burlywood', 'cadetblue', 'chocolate', 'coral', 'cornflowerblue', 'darkgrey',
           'darksalmon', 'cyan4', 'khaki', 'lightblue', 'lightpink']
directions = [0, 90, 180, 270]


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_colour = (r, g, b)
    return rand_colour


def draw_a_square(distance=100):
    """Makes the cursor draw a square. Default size is 100."""
    delvin.pu()
    delvin.setx(distance * (-0.5))
    delvin.sety(distance * 0.5)
    delvin.pd()
    for _ in range(4):
        delvin.forward(distance)
        delvin.right(90)


def draw_dashed_line():
    for _ in range(15):
        delvin.forward(10)
        delvin.pu()
        delvin.forward(10)
        delvin.pd()


def draw_dif_shapes(max_sides=10):
    if max_sides >= 20:
        delvin.speed('fastest')
    sides = 3
    while sides <= max_sides:
        delvin.pencolor(random_colour())
        angle = 360 / sides
        for _ in range(sides):
            delvin.right(angle)
            delvin.forward(15)
        sides += 1


def random_walk(steps=50):
    delvin.pensize(10)
    if steps >= 100:
        delvin.speed("normal")
    elif steps >= 150:
        delvin.speed(7)
    elif steps >= 200:
        delvin.speed(8)
    elif steps >= 250:
        delvin.speed(9)
    for _ in range(steps):
        delvin.color(random_colour())
        delvin.setheading(random.choice(directions))
        delvin.forward(25)


def spirograph(num_circles):
    delvin.speed(0)
    angle = 360 / num_circles
    melvin.goto(150,-150)
    delvin.width(10)
    for _ in range(num_circles):
        delvin.color(random_colour())
        delvin.circle(200)
        delvin.left(angle)
        melvin.clear()
        melvin.write(f"{_ + 1}", font=('Arial', 14, 'normal'))

# delvin.width(5)
# delvin.penup()
# delvin.sety(200)
# delvin.pendown()

spirograph(150)

screen.exitonclick()