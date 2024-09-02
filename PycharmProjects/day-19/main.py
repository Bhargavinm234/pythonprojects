import turtle
from turtle import Turtle,Screen

tim = Turtle()
my_screen = Screen()
def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)


def turn_left():
    tim.setheading(tim.heading() + 10)

def turn_right():
    tim.setheading(tim.heading() - 10)

def draw_circle():
    tim.circle(10)
def clear():
    tim.reset()
#tim.clear()v, tim.home()



my_screen.listen()
my_screen.onkey(key="w", fun=move_forwards)
my_screen.onkey(move_backwards,"s")
my_screen.onkey(turn_left,"a")
my_screen.onkey(turn_right,"d")
my_screen.onkey(draw_circle ,"r" )
my_screen.onkey(clear, "c")


my_screen.exitonclick()