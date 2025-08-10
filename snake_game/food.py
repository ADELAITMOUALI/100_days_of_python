from turtle import Turtle, Screen
from random import randint
from scoreboard import Score
SCORE = 0
class Food(Turtle):
    
    def __init__(self):
        self.score = SCORE
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.shapesize(0.8,0.8)
        self.color("yellow")
        x_label = randint(-280,280)
        y_label = randint(-280,280)
        self.goto(x_label, y_label)
        self.refresh()
        
    def refresh(self):
        x_label = randint(-280,280)
        y_label = randint(-280,280)
        self.goto(x_label, y_label)
        
        