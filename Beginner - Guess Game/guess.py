import random 
import os 

#creat  random number 
number = int(random.randint(1, 100))
#creat easy mode and hard level

def level(lvl):
    if lvl in ["easy","EASY"]:
        
        os.system("clear")
        print("welcom to the easy level")
        #10 loop times for easy level function
        for i in range(10):
              print(f"[+] you have {10 - i} attempt")
              user_input = int(input("your guess:"))
              
              match(user_input, number)

    elif lvl in ["hard","HARD"] :
        
             
        os.system("clear")
        print("welcom to the hard level")
        #5 loop times for hard level function 
        for i in range(5):
            print(f"[+] you have {5 - i} attempt")
            user_input = int(input("your guess:"))
            match(user_input, number)

#function for match the guss user is it too low or too high 
def match(user, guess):
      if user > guess :
            print("too high")
      elif user < guess :
            print("too low")
      elif user == guess :
            print("great you got it ") 
            exit()
      else:
            print("please enter a number ")
            level(input_levle)
            
#printing the welcome text
print('''
##################################################################
##in this game you will try to guess a number between 0 and 100 ##
##################################################################
''')

input_levle = input("please chose a level to start, hard or easy ? : ")
level(input_levle)

