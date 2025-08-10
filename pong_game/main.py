from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scorboard import Scoreboard


##screen 
my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.tracer()
my_screen.listen()

####
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

my_screen.onkeypress(r_paddle.go_up, "Up")
my_screen.onkeypress(r_paddle.go_down, "Down")

my_screen.onkeypress(l_paddle.go_up, "w")
my_screen.onkeypress(l_paddle.go_down, "s")

####
ball = Ball()


  

####
game_is_on = True

score = Scoreboard()


while game_is_on :
    my_screen.update()
    time.sleep(ball.speed_ball)
    ball.move()
   
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    #detectio collition with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
    
    # detect the ball if out the right or left side 
    if ball.xcor() > 360 :
        score.r_gool()
        ball.reset_ball()
        
        
    if ball.xcor() < -360 :
        score.l_gool()

        ball.reset_ball()


my_screen.exitonclick()