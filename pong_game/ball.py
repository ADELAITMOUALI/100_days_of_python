from turtle import Turtle
from time import sleep




class Ball(Turtle):
    def __init__(self) :
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.goto(0, 0)
        self.x_move = 4
        self.y_move = 4
        self.speed_ball = 0.01
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    #detect colision with the top of screen ant the buttom
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.speed_ball *= 0.1  
        self.x_move *= -1
        
    def reset_ball(self):
        self.speed_ball = 0.01
        self.hideturtle()
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1
        self.showturtle()
        sleep(2)
           
        
        
    
        
        
        

