# import turtle, another_module
#
# print(another_module.another_variable)
# klev = turtle.Turtle()
# turt = turtle.Turtle()
# # print(turt)
# turt.shape("turtle")
# turt.color("red")
# turt.fd(100)
#
# klev.color("turquoise")
# klev.shape("turtle")
# klev.turtlesize(2,2)
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

# table = PrettyTable()
table = ColorTable(theme=Themes.OCEAN)


table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

table.align = "l"
print(table)

