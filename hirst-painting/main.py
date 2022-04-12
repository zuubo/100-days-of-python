import turtle as t
import random

colours = [(19, 21, 26), (24, 20, 16), (25, 18, 23), (16, 23, 19), (205, 152, 99), (197, 216, 228), (229, 227, 208),
           (130, 161, 183), (222, 214, 111), (202, 225, 213), (139, 100, 67), (41, 107, 162), (201, 145, 163),
           (180, 171, 35), (231, 221, 228), (143, 74, 116), (200, 97, 77), (60, 168, 120), (115, 191, 175),
           (82, 112, 92), (151, 204, 225), (84, 77, 20), (168, 100, 146), (31, 156, 202), (131, 215, 196),
           (219, 171, 192), (37, 61, 97), (83, 51, 65), (33, 82, 60), (95, 50, 40), (179, 190, 212), (109, 130, 150),
           (224, 213, 12), (27, 80, 96), (210, 185, 175)]

t.colormode(255)
dilmar = t.Turtle()
dilmar.penup()
dilmar.hideturtle()
dilmar.speed(9)

x = -250
y = -225

for _ in range(100):
    if x == 250:
        x = -250
        y += 50
    dilmar.setposition(x, y)
    dilmar.dot(20, random.choice(colours))
    x += 50

screen = t.Screen()
screen.exitonclick()

# Angela didn't use setposition(), I think the way she did it is pretty janky