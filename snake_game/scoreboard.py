from turtle import Turtle

FONT = ("Arial", 25, "normal")
FONT_END = ("Solid", 55, "bold")
ALIGHN = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.update_score()
        
    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER",align=ALIGHN, font=FONT_END)

        
    def update_score(self):
        self.clear()  
        self.score += 1
        self.write(f"score: {self.score}",align=ALIGHN, font=FONT)
