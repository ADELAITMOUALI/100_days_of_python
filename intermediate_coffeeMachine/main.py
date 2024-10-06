from logo import logo
import os
import time 
import sys
import itertools
import threading
import platform


MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 3,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 6,
    }
}

resources = {
    'water': 400,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

#Creat a clear screen fonction for any OS 
def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux and macOS



# TODO: 1 - start the machine
user_price = 0
user_order = ''
def start_machine():
    print(logo)
    global user_price 
    while True:  
        user_input = input('Enter money: ')  
        try:
            user_price = int(user_input)  
            break 
        except ValueError:
            print('That\'s not a valid number. Please enter a valid number.')
            time.sleep(2)
            clear_screen() 
            print(logo)
    
    if user_price >= 3:
        global resources
        resources['money'] = user_price
        get_order()
    else:
        print(f'{user_price}DH will not buy for you anything ')
        time.sleep(2)
        clear_screen()
        start_machine()
#TODO: 2 - ask the user and list the report 
def report():
    global user_price
    print('water:', resources['water'], 'mL')
    print('milk:', resources['milk'], 'mL')
    print('coffee:', resources['coffee'], 'mg')
    print('money:', user_price, 'DH')
def get_order():
    global user_order 
    user_order = input('what do you like to drink  espresso/latte/cappuccino : [report to see report] --> ')
    
    if user_order == 'report':
        clear_screen()
        report()
        get_order()
    elif user_order in ['espresso', 'latte', 'cappuccino']:
        check_resources(user_order)
    else:
        print('we don\'t have this order')
        get_order()    
#TODO: 3 - calculate the resources with orders and money 

def check_resources(order):
    global MENU
    global resources
    if order == 'espresso':
        if MENU[order]['ingredients']['water'] <= resources['water'] and MENU[order]['ingredients']['coffee'] <= resources['coffee']:
            print('wait a sec till your coffee prepared ')
            done = False
            # the animation
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    sys.stdout.write('\rpreparing ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rYour coffee is redy enjoy')

            t = threading.Thread(target=animate)
            t.start()

            #long process here
            time.sleep(5)
            done = True
            #
            resources['water'] = resources['water'] - MENU[order]['ingredients']['water']
            resources['coffee'] = resources['coffee'] - MENU[order]['ingredients']['coffee']
            resources['money'] = resources['money'] - MENU[order]['cost']
            if resources['money'] > 0:
                print('\n')
                clear_screen()
                print(f'Please don\'t forget the rest {resources["money"]} DH .')
                time.sleep(5)
                clear_screen()
                start_machine()
            else:
                time.sleep(3)
                clear_screen()
                start_machine()
        else:
            print('Sorry we don\'t have enough resources')
            time.sleep(3)
            clear_screen()
            start_machine()
    else:
        if MENU[order]['ingredients']['water'] <= resources['water'] and MENU[order]['ingredients']['coffee'] <= resources['coffee'] and MENU[order]['ingredients']['milk'] <= resources['milk']: 
            if resources['money'] >= MENU[order]['cost']:
                print('wait a sec till your coffee prepared ')
                done = False
                #the animation
                def animate():
                    for c in itertools.cycle(['|', '/', '-', '\\']):
                        if done:
                            break
                        sys.stdout.write('\rpreparing ' + c)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    sys.stdout.write('\rYour coffee is redy enjoy')

                t = threading.Thread(target=animate)
                t.start()

                #long process here
                time.sleep(5)
                done = True
                #write in MENU
                resources['water'] = resources['water'] - MENU[order]['ingredients']['water']
                resources['coffee'] = resources['coffee'] - MENU[order]['ingredients']['coffee']
                resources['milk'] = resources['milk'] - MENU[order]['ingredients']['milk']
                resources['money'] = resources['money'] - MENU[order]['cost'] 
                if resources['money'] > 0:
                    print('\n')
                    print(f'Please don\'t forget the rest {resources["money"]} DH .')
                    time.sleep(5)
                    clear_screen()
                    start_machine()
                else:
                    time.sleep(3)
                    clear_screen()
                    start_machine()
            else:
                print(f'Sorry you need {MENU[order]["cost"]}DH to buy {order} ')
                time.sleep(3)
                clear_screen()
                start_machine()
        else:
            print('Sorry we don\'t have enough resources')
            time.sleep(3)
            clear_screen()
            start_machine()
clear_screen()
start_machine()
