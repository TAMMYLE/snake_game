from turtle import Turtle, Screen

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍🐍🐍 Snake Game 🐍🐍🐍")



# Set x_coor for body part:
x_coor = [0, -20, -40]

# Create a snake body --> 3 white squares line starts at (0,0)
snake_body = []
for snake_body_i in range(0,3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.setpos(0 + x_coor[snake_body_i],0)
    snake.pensize(20)
    snake_body.append(snake)




screen.exitonclick()