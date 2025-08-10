from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score
#########################################

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.title("Snake Game")
my_screen.bgcolor("black")
my_screen.tracer(0)
#########################################
food = Food()
snake = Snake()
score = Score()

#controle
my_screen.listen()
my_screen.onkeypress(snake.up, "Up")
my_screen.onkeypress(snake.down, "Down")
my_screen.onkeypress(snake.left, "Left")
my_screen.onkeypress(snake.right, "Right")

# Start  the game
game_on = True
while game_on:
    my_screen.update()
    time.sleep(0.05) 
    snake.move()
    #detect food
    if snake.head.distance(food) < 15 :
        snake.extende()
        food.refresh()
        score.update_score()
    #Game Over
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score.game_over()
        game_on = False
    #detect collision with tail
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10 :
            score.game_over()
            game_on = False    
        
my_screen.exitonclick()