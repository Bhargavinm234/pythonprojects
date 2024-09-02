import time
from turtle import Screen , Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0) #tracer is off , nothing happens (to avoid animation we do this)

#
# tim = Turtle("square")
# tim.color("white")
#
# tim1 = Turtle("square")
# tim1.color("white")
# tim1.goto(-20,0) #to set the segment
#
# tim2 = Turtle("square")
# tim2.color("white")
# tim2.goto(20,0)


# # STEP 1 : CREATE SNAKE
# starting_positions = [(0,0), (-20,0), (-40,0)]  #to avoid animation do : (-20,0),(0,0),(20,0)
# segments = []
# for pos in starting_positions:
#     segment = Turtle("square")
#     segment.up()
#     segment.color("white")
#     segment.goto(pos)
#     segments.append(segment)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right , "Right")


#STEP 2 : MOVE SNAKE [ 3 to 2, 2 to 1, 1 moves]
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) #to provide delayy betwedn each square block
    # for seg_no in range(len(segments)-1, 0, -1):#accessing in reverse order
    #     new_x = segments[seg_no -1].xcor()
    #     new_y =segments[seg_no -1].ycor()#to go to 2nd last position
    #     segments[seg_no].goto(x=new_x, y=new_y)
    # segments[0].forward(10)
    snake.move()

    #To detect collision with food. FOOD SIZE : 10 * 10
    if snake.head.distance(food) < 15: # 15 determines whether simple
        # collision is like eaten or just head touch or full touch , we can change the value
        food.refresh()
        snake.extend() # to extend snake each time
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        scoreboard.reset()
        snake.reset_segment()

    #detect snake tail [if head hits any other segment} then trigger game over
    for segment in snake.segments[1:]:
        #this at initially shows that game iver cz head is the first segment
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset()
            snake.reset_segment()

screen.exitonclick()