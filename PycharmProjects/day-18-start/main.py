import turtle
from turtle import Turtle,Screen
# import turtle as t

timmy = Turtle()
turtle.colormode(255) #to get random colors
tom = Turtle
timmy.shape("turtle")
timmy.color("red")

# #Draw a square
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# import heroes
# print(heroes.gen())

# for _ in range(15):
#     tom.forward(10)
#     tom.penup()
#     tom.forward(10)
#     tom.pendown()
import random
colors =["lime green","aquamarine","red","magenta","medium violet red","medium orchid","pink"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     timmy.color(random.choice(colors))
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for shape_side_n in range(3,11):
#     # timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

# timmy.pensize(8) #Thickness
# timmy.speed("fastest") #integer or string can be passed
# directions = [0, 90, 180, 270]
# for i in range(200):
#     timmy.color(random_colors())
#     timmy.forward(10)
#     timmy.setheading(random.choice(directions))

### tuples are immutable
timmy.speed("fastest")
def draw_spiral_graph(size):
    for _ in range (int(360/ size)):
        timmy.color(random_colors())
        timmy.circle(80)
        timmy.setheading(timmy.heading() + size)

draw_spiral_graph(5)















my_screen= Screen()
my_screen.exitonclick()