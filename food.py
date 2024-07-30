import random
from snake import Snake
from turtle import Turtle 

# Food inherited Turtle class

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color("pink")
        self.refresh()



    def refresh(self):
        random_position_x = random.randint(-280, 280)
        random_position_y = random.randint(-280, 260)
        food_position = (random_position_x, random_position_y)
        self.goto(food_position)
