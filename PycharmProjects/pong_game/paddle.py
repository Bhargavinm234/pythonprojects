from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(pos)

    def up(self):
        # here x position doesnt change only y pos changes
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        # here x position doesnt change only y pos changes
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
