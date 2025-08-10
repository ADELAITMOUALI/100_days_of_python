import turtle
import pandas as pd
import time

my_screen = turtle.Screen()
my_screen.title("Name The States")
image = "blank_states_img.gif"
my_screen.bgpic(image)
my_screen.setup(725, 491)

# # #
states = pd.read_csv("50_states.csv")
question = 0
score = 0
answers = []

while question < 50 :
    ##########################
    question += 1
    input_user = my_screen.textinput(f"U.S. states Guess", f"guess a state      Your score {score}/50  Q:{question}")
    ##########################
    if input_user == None :
        End = turtle.Turtle()
        my_screen.bgpic('')
        my_screen.bgcolor("black")
        End.color("red")
        End.hideturtle()
        End.goto(0, 0)
        End.write(f"Bye , Your score is {score}/50" ,align="center", font=("Arial", 40, "normal"))
        time.sleep(1.5)
        exit()
    ##########################
    for row in states.state:
        if row  == input_user:
            if row not in answers:
                score += 1
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                answers.append(row)
                t.goto(int(states[states.state == input_user]["x"]), int(states[states.state == input_user]["y"]))
                t.write(row, align="center", font=("Arial", 10, "normal")) 
            
            else:
                already = turtle.Turtle()
                already.hideturtle()
                already.penup()
                already.color("green")
                already.write("You've already guessed that state! Try another one.", align="center", font=("Arial", 20, "bold"))
                question -= 1
                time.sleep(2)
                already.clear()
                
        else:
            continue    
    ##########################
    
    if question == 50:
        end = turtle.Turtle()
        end.color("red")
        end.hideturtle()
        end.goto(0, 0)
        end.write(f"Done {score}/50" ,align="center", font=("Arial", 60, "normal"))
        time.sleep(3)
    


my_screen.exitonclick()