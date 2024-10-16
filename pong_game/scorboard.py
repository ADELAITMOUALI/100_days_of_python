from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("yellow")
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"  {self.r_score}    {self.l_score}", align="center", font=("Courier", 24, "normal"))
    def l_gool(self):
        self.l_score += 1
        self.update_scoreboard()
    def r_gool(self):
        self.r_score += 1
        self.update_scoreboard()