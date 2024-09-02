from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]  #to avoid animation do : (-20,0),(0,0),(20,0)
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
            # segment = Turtle("square")
            # segment.up()
            # segment.color("white")
            # segment.goto(pos)
            # self.segments.append(segment)

    def add_segment(self,position):
        segment = Turtle("square")
        segment.up()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def reset_segment(self):
        for segment in self.segments:
            segment.goto(1000,1000) #hence snake goes out of the door
        self.segments.clear()#HERE OLD SNAKE STILL EXISTS
        self.createSnake()
        self.head = self.segments[0]


    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):  # accessing in reverse order
            new_x = self.segments[seg_no - 1].xcor()
            new_y = self.segments[seg_no - 1].ycor()  # to go to 2nd last position
            self.segments[seg_no].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN: #if current heading is pointed down it cant move up
            self.segments[0].setheading(UP)


    def down(self):
        if self.head.heading() != UP: #this way snake wont go in backward direction
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)







