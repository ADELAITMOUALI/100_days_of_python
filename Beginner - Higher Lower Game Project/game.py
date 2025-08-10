from data import data
from logo import *
import os 
import random

# clear the screen and print the logo 
os.system('clear')

print(logo)
#description 
print( '\n' , " [+] . in this game you will guess who have more followers",'\n')
start = input("Are you ready to start [Y]es [N]o : ")
if start in ["Y","YES","yes","y"]:
    pass
else:
    exit()
#start the Game 
score = 0 
def game():
    global score
    name1 = random.choice(data)
    print(name1['name'])
    print(vs)
    name2 = random.choice(data)
    #same names evasion 
    def same_name():
        if name1['name'] == name2['name']:
            name2 = random.choice(data)
            same_name()  
    print(name2['name'],'\n')
    
    reply = int(input(f"who have more followers [1]--> {name1['name']} or [2]--> {name2['name']}: "))
    if name1['followers'] > name2['followers'] and reply == 1 or name2['followers'] > name1['followers'] and reply == 2:
        score += 1
        os.system('clear')
        print(f"correct your score now is {score}")
        game()
    else:
        os.system('clear')
        print(f"wrong answer your score is {score}")
        score = 0
game()


