from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.bgcolor("black")
race_start = True
my_screen.setup(width=800, height=400)

# End line
line = Turtle()
line.penup()
line.color("white")
line.goto(x=380, y=200)
line.right(90)
line.pendown()
line.forward(400)
line.hideturtle()

colors = ["green", "yellow", "red", "blue", "purple", "orange"]
all_turtle = []
y_position = 120

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-380, y=y_position)
    y_position -= 50
    all_turtle.append(new_turtle)

user_bet = my_screen.textinput(title="Your Bet", prompt="What color will win: ")

#displaying the winner
winner_turtle = Turtle()
winner_turtle.hideturtle()
winner_turtle.penup()
winner_turtle.goto(0, 0)
winner_turtle.color("white")

while race_start:
    for turtle in all_turtle:
        if turtle.xcor() > 370:
            turtle_color = turtle.pencolor()
            race_start = False
            if user_bet == turtle_color:
                winner_turtle.write(f"You win! The {turtle_color} turtle is the winner!", align="center", font=("Arial", 20, "normal"))
            else:
                winner_turtle.write(f"You lose! The {turtle_color} turtle is the winner!", align="center", font=("Arial", 20, "normal"))
            break
        forward_step = random.randint(0, 20)
        turtle.forward(forward_step)

my_screen.exitonclick()
