from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time



# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # turn off the animation ---> use update method for redraw the screen 
screen.bgcolor("black")
screen.title("🐍🐍🐍 Snake Game 🐍🐍🐍")


# Create snake from class Snake
snake = Snake()

#Create food 
food = Food()

#Create point tracker
point = ScoreBoard()

# Listen to key strokes

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


# when the game is on ---> graphic runs an update, sleep for 0,2 second 
# ONLY WHEN all the segments have moved forward
game_is_on = True

while game_is_on:

    screen.update() # Refresh the screen
    time.sleep(0.1) # Delay the refresh to control the frequency of the refresh
    snake.move()
    
    # Detect collisions with food --> use distance method (turtle)
    # If snake collides w food --> update score

    if snake.head.distance(food) < 15: #check the distance bt food and the snake head is less than 15
        food.refresh()
        point.clear()
        point.update_score()

    # Detect collisions with walls
    # If snake hits wall --> end game
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        point.end_game()

 
screen.exitonclick()