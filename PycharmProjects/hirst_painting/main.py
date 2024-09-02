import turtle
import colorgram
from turtle import Turtle,Screen
import random

colors = colorgram.extract('images.jpg',20)
rgb_colors = []
#To extraxt colors from colorgram
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple = (r,g,b)
#     rgb_colors.append(tuple)
#
# print(rgb_colors) #The below list is extracted colors
turtle.colormode(255)
tim = Turtle()
tim.up()
tim.hideturtle()
tim.speed("fastest")
color_list = [(236, 35, 108), (145, 28, 66), (230, 237, 232), (239, 75, 36), (7, 148, 95), (222, 170, 45), (183, 158, 47), (44, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 92), (244, 219, 53), (178, 40, 98), (40, 168, 117), (208, 131, 165), (205, 56, 35)]

#To make the starting postion too be left
tim.setheading(225)
tim.forward(250) #5 dots * 50 = 250
tim.setheading(0)

number_of_dots = 100
for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
    #to come back to left in next position
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

























my_screen = turtle.Screen()
my_screen.exitonclick()
