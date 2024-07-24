from turtle import Turtle

# Use tuple to create starting positions of each body segment
STARTING_SEGMENTS = [(0, 0), (-20, 0), (-40, 0)]
# create constant of move
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake_body = [] # Create a snake body --> 3 white squares line starts at (0,0)
        self.create_snake()

    # Create 3 different segment of a snake
    def create_snake(self):
        for position in STARTING_SEGMENTS:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.pensize(20)
            snake.penup()
            snake.goto(position)
            self.snake_body.append(snake)

    # Move the snake forward automatically
    # setup snake movements:
    # move 3rd segment of the snake to the 2nd segment
    # move 2nd segment to the 1st
    # move 1st segment to new position based on keypress
    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1): # start = len - 1, stop at 1, step: -1 --->  3, 2, 1
            # create position(x, y) holder for segment 2
            new_segment_x = self.snake_body[seg_num - 1].xcor()
            new_segment_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_segment_x, new_segment_y) #move 3rd segment to 2nd segment coordinates
        self.snake_body[0].forward(MOVE_DISTANCE) # move 1st segment forward       