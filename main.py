from turtle import Turtle, Screen
from snake import Snake
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # turn off the animation ---> use update method for redraw the screen 
screen.bgcolor("black")
screen.title("🐍🐍🐍 Snake Game 🐍🐍🐍")


# Create snake from class Snake
snake = Snake()


# when the game is on ---> graphic runs an update, sleep for 0,2 second 
# ONLY WHEN all the segments have moved forward
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.2)
    snake.move()

screen.exitonclick()