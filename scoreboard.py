from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class ScoreBoard(Turtle):    
    # store points

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("orange")
        self.setposition(-10, 265) # determine the position of the score
        self.write(arg="SCORE: 0", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        
    def update_score(self):
        # update score when snake hits food
        self.score += 1
        self.write(arg="SCORE: " + str(self.score), move=False, align=ALIGNMENT, font=FONT)

    def end_game(self):
        self.setposition(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)