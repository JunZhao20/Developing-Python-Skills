import turtle
import prettytable as pt
"""player = turtle.Turtle()

player.shape('turtle')
player.forward(100)
screen = turtle.Screen()

screen.exitonclick()
"""

table = pt.PrettyTable()


table.add_column("pokemon name", ["c", "b"])
table.add_column("type", ['d', 'v'])
table.align["pokemon name", "type"] = "l"


print(table)
