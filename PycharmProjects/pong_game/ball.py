from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        # print(f"{new_x}    {new_y}")
        self.goto(new_x,new_y)

    def bounce_y(self):
        # new_y =  self.ycor() - self.y_move change y direction
        self.y_move *= -1
        # print(f"{self.y_move}")

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed * 0.9   #speed increases as ball bounces

    def restart(self):
        self.goto(0,0)
        self.move_speed = 0.1 #so that speed doesnt increase indefinitely
        self.bounce_x() #This is beacuse it needs to move to the other player side



