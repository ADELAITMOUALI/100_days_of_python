from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        
        super().__init__()  
        self.speed("fastest")
        self.penup()  
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")


    def go_up(self):
        y_position = self.ycor() + 30
        self.goto(self.xcor(),y_position)
        
    def go_down(self):
        y_position = self.ycor() - 30
        self.goto(self.xcor(),y_position)
    
  


