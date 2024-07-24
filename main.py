from turtle import Turtle, Screen

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍🐍🐍 Snake Game 🐍🐍🐍")



# Set x_coor for body part:
# Use tuple to create starting positions of each body segment
starting_segment = [(0, 0), (-20, 0), (-40, 0)]

# Create a snake body --> 3 white squares line starts at (0,0)
snake_body = []
for snake_body_i in range(0,3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.goto(starting_segment[snake_body_i])
    snake.pensize(20)
    snake_body.append(snake)




screen.exitonclick()