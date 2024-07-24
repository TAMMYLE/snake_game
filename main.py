from turtle import Turtle, Screen
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # turn off the animation ---> use update method for redraw the screen 
screen.bgcolor("black")
screen.title("🐍🐍🐍 Snake Game 🐍🐍🐍")

# Use tuple to create starting positions of each body segment
starting_segment = [(0, 0), (-20, 0), (-40, 0)]

# Create a snake body --> 3 white squares line starts at (0,0)
snake_body = []
for position in starting_segment:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.pensize(20)
    snake.penup()
    snake.goto(position)
    snake_body.append(snake)

# Get the snake to move 

# when the game is on ---> graphic runs an update, sleep for 0,2 second 
# ONLY WHEN all the segments have moved forward
game_is_on = True


# setup snake movements:
# move 3rd segment of the snake to the 2nd segment
# move 2nd segment to the 1st
# move 1st segment to new position based on keypress

while game_is_on:
    screen.update()
    time.sleep(0.2)

    for seg_num in range(len(snake_body) - 1, 0, -1): # start = len - 1, stop at 1, step: -1 --->  3, 2, 1
        # create position(x, y) holder for segment 2
        new_segment_x = snake_body[seg_num - 1].xcor()
        new_segment_y = snake_body[seg_num - 1].ycor()
        snake_body[seg_num].goto(new_segment_x, new_segment_y) #move 3rd segment to 2nd segment coordinates
    snake_body[0].forward(20) # move 1st segment forward    




screen.exitonclick()