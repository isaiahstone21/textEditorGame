# Isaiah Stone

# Get name of user 
from multiprocessing import set_forkserver_preload


name = input("Enter your name:")

# Variables to be used later
coins = 0
backpack = []
win = False

# Functions
def check_win():
    if coins >= 3:
        print("Congratulations! You have finally collected enough coins to get your first ever car!")

def check_coins(coins):
    print("You have " + str(coins) + " coins.")

def open_backpack(backpack):
    print("Your backpack consists of: ")
    print(backpack)

def introduction(coins, backpack):
    print("Hello " + name + '!\n' "You just turned 16 years old and are saving up money to buy a new car that costs 3 coins.\nYou are able to perform various different actions that will influence the amount of coins you have.\nYou can view how many coins you have by performing the action 'check coins'\nYou can view the items in your backback by performing the action 'Open backpack'.\nGood Luck!")

def run():
    print("You have successfully acquired a coin that the rich man dropped and ran back home.")
    global win
    win = True
        
def walk(coins, backpack):
    while win == False:
        print("As you go for a walk you see a wealthy man flaunting his wealth. As he is antagonizing the neighborhood, he trips on a tree stump and drops a coin on the ground.")
        print("Will you 'run for the coin', 'Check coins', or 'Open backpack'?")
        walk_response = input()
        if walk_response == 'run for the coin':
            coins += 1
            run()
        elif walk_response == 'Check coins':
            check_coins(coins)
        elif walk_response == 'Open backpack':
            open_backpack(backpack)
        else:
            print("Invalid input")
            continue
    return coins, backpack
def lockbox(coins, backpack):
    while win == False:
        print("You have unlocked the box! You found a coin inside of it.")
        print("You can now either 'go for a walk', 'Check coins', or 'Open backpack'.")
        lockbox_response = input()
        if lockbox_response == 'go for a walk':
            coins, backpack = walk(coins, backpack)
        elif lockbox_response == 'Check coins':
            check_coins(coins)
        elif lockbox_response == 'Open backpack':
            open_backpack(backpack)
        else:
            print("Invalid input")
            continue
    return coins, backpack
def return_home(coins, backpack):
    while win == False:
        print("You have returned home and are in your living room.")
        print("You notice that there is a lockbox tucked away in the corner of your room.")
        print("What will you do? 'try key on lockbox' or 'Check coins'.")
        return_home_response = input()
        if return_home_response == 'try key on lockbox':
            backpack.remove("Key")
            coins += 1
            coins, backpack = lockbox(coins, backpack)
        elif return_home_response == 'Check coins':
            check_coins(coins)
        elif return_home_response == 'Open backpack':
            open_backpack(backpack)
        else:
            print("Invalid Input")
            continue
    return coins, backpack
def search_key(coins, backpack):
    while win == False:
        print("You have found a key! It has been added to your backpack.")
        print("You can now either 'return home', 'Check coins', or 'Open backpack'.")
        search_key_response = input()
        if search_key_response == 'return home':
            coins, backpack = return_home(coins, backpack)
        elif search_key_response == 'Check coins':
            check_coins(coins)
        elif search_key_response == 'Open backpack':
            open_backpack(backpack)
        else:
            print("Invalid Input")
            continue
    return coins, backpack
def walk_store(coins, backpack):
    while win == False:
        print("You have arrived at the store. You can either 'search for the key', 'Check coins', or 'Open backpack'.")
        store_response = input()
        if store_response == 'search for the key':
            backpack.append("Key")
            coins, backpack = search_key(coins, backpack)
        elif store_response == 'Check coins':
            check_coins(coins)
        elif store_response == 'Open backpack':
            open_backpack(backpack)
        else:
            print("Invalid input")
            continue
    return coins, backpack
def leave_house(coins, backpack):
    while win == False:
        print("You have left your house. You can now 'walk to the store', 'Check coins', or 'Open backpack'.")
        leave_house_response = input()
        if leave_house_response == 'walk to the store':
            coins, backpack = walk_store(coins, backpack)
        elif leave_house_response == 'Check coins':
            check_coins(coins)
        elif leave_house_response == 'Open backpack':
            open_backpack(backpack)
        else:
            print("Invalid input")
            continue
    return coins, backpack
def eat_breakfast(coins, backpack):
    while win == False:
        print("You ate the screambled eggs and toast that your mother prepared for you.")
        print("You can now 'Leave house', 'Check coins', or 'Open backpack'.")
        eat_breakfast_response = input()
        if eat_breakfast_response == 'Leave house':
            coins, backpack = leave_house(coins, backpack)
        elif eat_breakfast_response == 'Check coins':
            check_coins(coins)
        elif eat_breakfast_response == 'Open backpack':
            open_backpack(backpack)
        else:
            print("Invalid Input")
            continue
    return coins, backpack

def kitchen(coins, backpack):
    while win == False:
        print("You have arrived in your kitchen. You can either 'Eat breakfast', 'Read newspaper' 'Check coins', or 'Open backpack'.")
        kitchen_response = input()
        if kitchen_response == 'Eat breakfast':
            coins, backpack = eat_breakfast(coins, backpack)
        elif kitchen_response ==  'Read newspaper':
            print("You have read the newspaper and found out that there is a key at the store.")
            continue
        elif kitchen_response == 'Check coins':
            check_coins(coins)
        elif kitchen_response == 'Open backpack':
            open_backpack(backpack)
        else:
            print("Invalid input")
            continue
    return coins, backpack
def leave_bedroom(coins, backpack):
    while win == False:
        print("Now that you have stolen money from your parents you will now 'go to the kitchen', 'Check coins', or 'Open backpack'.")
        leave_bedroom_command = input()
        if leave_bedroom_command == 'go to the kitchen':
            coins, backpack = kitchen(coins, backpack)
        elif leave_bedroom_command == 'Check coins':
            check_coins(coins)
        elif leave_bedroom_command == 'Open backpack':
            open_backpack(backpack)
        else:
            print("Invalid Input")
            continue
    return coins, backpack
def search(coins, backpack):
    while win == False:
        print("As you snoop through your parents belongings, you find a coin inside of your mother's nightstand.")
        coins += 1
        if win == False:
            print("Now 'Leave'.")
            search_command = input()
            if search_command == 'Leave':
                coins, backpack = kitchen(coins, backpack)
            else:
                print("Invalid Input")
                continue
    return coins, backpack

def enter(coins, backpack):
    while win == False:
        print("You have entered your parents bedroom, you can either 'search' their bedroom 'Check coins', or 'Open backpack'.")
        enter_action = input()
        if enter_action == 'search':
            coins, backpack = search(coins, backpack)
        elif enter_action == 'Check coins':
            check_coins(coins)
        elif enter_action == 'Open backpack':
            open_backpack(backpack)
        else:
            print("Invalid Input")
            continue
    return coins, backpack

def go_left(coins, backpack):
    while win == False:
        print("You have arrived at your parents bedroom. You can either 'Enter' your parents bedroom, 'Check coins' or 'Open backpack'.")
        go_left_action = input()
        if go_left_action == 'Enter':
            coins, backpack = enter(coins, backpack)
        elif go_left_action == 'Check coins':
            check_coins(coins)
        elif go_left_action == 'Open backpack':
            open_backpack(backpack)
        else:
            print("Invalid Input")
            continue
    return coins, backpack
def downstairs(coins, backpack):
    while win == False:
        print("You have gone down the stairs, you can either 'Go left' towards your parents bedroom or 'Go right' to enter the kitchen")
        downstairs_action = input()
        if downstairs_action == 'Go left':
            coins, backpack = go_left(coins, backpack)
            break
        if downstairs_action == 'Go right':
            kitchen()
            break
        else:
            print("Invalid Input")
            continue
    return coins, backpack

def first_room(coins, backpack):
    while win == False:
        print("It is 8:00 AM and you are sitting in your room.\nWhat do you want to do?")
        print("Options: 'Go downstairs', 'Take a shower', 'Check coins', 'Open backpack', 'quit'")
        first_action = input("Enter action: ")
        if first_action == 'Go downstairs':
            coins, backpack = downstairs(coins, backpack)
            break
        elif first_action == 'Take a shower':
            print("Oh no, it appears your brother is in the shower")
            continue
        elif first_action == 'Check coins':
            check_coins(coins)
            continue
        elif first_action == 'Open backpack':
            open_backpack(backpack)
            continue
        elif first_action == 'quit':
            break
        else:
            print("Invalid input")
            continue
    return coins, backpack
# Prints the introduction 
introduction(coins, backpack)

# Prints commands to begin going through the sequence of functions
first_room(coins, backpack)

# Win sequence
win = True
if win == True:
    check_win()
    print("                  _________________")
    print("              _.-'_____  _________ _`.")
    print("            .` ,'      ||         | `.`.")
    print("        .`  /          ||         |  ,' ] `....___")
    print("      _`__.'''''''''''''''''''''''`''''''''|..___ `-.._")
    print("    .'                  [='                '     `'-.._`.")
    print(f" ,:/.'''''''''''''''''''|''''''''''''''''''|'''''''''''\'\")")
    print("  //||    _..._         |                  '    _..._  |)|")
    print(" /|//   ,',---.`.       |                  |  .',---.`.\>|")
    print("(':/   //' .-. `\\      \_________________/  '/' .-. `\\|_)")
    print(" `-...'||  '-'  ||________,,,,,,,,,,,,,,,__.'||  '-'  ||-'")
    print("       '.'.___.','                           '.'.___.','")
    print("  LGB    '-.m.-'                               '-.m.-'")
    print("You have finally bought your brand new car!")
