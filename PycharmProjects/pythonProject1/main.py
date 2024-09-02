# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# print(timmy)
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
my_table = PrettyTable()

my_table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
my_table.add_column("Type",["Electric", "Water", "Fire"])

my_table.align="l"
my_table.border = True
print(my_table)

# my_table.field_names= ["Pokemon Type", "Type"]
# my_table.add_rows(
#     [
#         ["Pikachu", "Electric"],
#         ["Squirtle", "Water"],
#         ["Charamander", "Fire"]
#     ]
# )
# print(my_table)



