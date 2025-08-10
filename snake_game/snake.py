from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]
        
        
    def creat_snake(self):
        
        for position in STARTING_POSITION:
            self.add_segment(position)
            
    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
        
    def extende(self) :
        self.add_segment(self.segments[-1].position())
                   
    def move(self):
        
        for segment in range(len(self.segments) -1 , 0, -1):
            new_x = self.segments[segment -1].xcor() 
            new_y = self.segments[segment -1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_SPEED)
    
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)                
        

