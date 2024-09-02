import turtle
from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter the color:")
colors = ["red", "orange", "purple", "green", "blue", "black"]
y_positions = [-120, -70, -20, 30, 80, 130]
all_turtles = []

for t_index in range(0,6):
    tim = Turtle("turtle")
    tim.up()
    tim.color(colors[t_index])
    tim.goto(x=-230, y=y_positions[t_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won . The {winning_color} turtle won the race")
            else:
                print(f"You lost . The {winning_color} turtle won the race")
        random_dist = random.randint(0,10)
        turtle.forward(random_dist)
