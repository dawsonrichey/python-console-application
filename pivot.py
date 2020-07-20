import os


# creating a dictionaly of items to sell in the shop
# The 1 will skip 0 when listing the item number
wands = {'Oak': 23, 'Pine': 99, 'Maple': 837}
# FUNCTIONS
# This file is a terminal application that goes on and on my friends


def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')

    print("****************************************************************")
    print("***      You are about to enter another dimension.           ***")
    print("***   A dimension not only of sight and sound, but of mind.  ***")
    print("***       A journey into a wondrous land of imagination.     ***")
    print("****************************************************************")

def store_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')

    print("****************************************************************")
    print("***                 Olivander's Wand Shop                    ***")
    print("****************************************************************")

def riddle_game():

    answer = 5
    riddle = "How many woods can a woodchuck chuck? "
    riddle_guess = int(input(riddle))

    while riddle_guess != answer:
        bad_guess = "Guess Again "
        riddle_guess = int(input(bad_guess))

    print("Impressive! You guessed right.")


def shopping_spree():
    print('I hope you love to shop...because you have no other options!')
    q1 = input("Do you have any money? ")
    if q1 == 'y':
        q1_2 = int(input("How much? "))
    elif q1 == 'n':
        q1_2 = int(input("How much would you like to borrow? "))
    print(f"Let's see what you can buy with ${q1_2}\n")
    store_title_bar()
    for i, (k, v) in enumerate(wands.items()):
        print(f"[{i}]  {k} ${v}")
    owner_q1 = input('Would you like to buy something? ')
    if owner_q1 == 'y':
        print('no')
    elif owner_q1 == 'n':
        print('no')

def get_user_choice():
    # Let users know what they can do.
    print("\n[1] Answer my riddle")
    print("[2] Go shopping")
    print("[3] Play a game")
    print("[e] Exit")

    return input("What would you like to do? ")

# MAIN PROGRAM
# Set up a loop where users can choose what they'd like to do.


choice = ''
display_title_bar()
while choice != 'e':

    choice = get_user_choice()

    # Respond to the user's choice.
    if choice == '1':
        riddle_game()
    elif choice == '2':
        shopping_spree()
    elif choice == '3':
        print("\nSORRY BUT THE GAME HAS NOT YET BEEN BUILT.\nPLEASE TRY AGAIN LATER\n")
    elif choice == 'e':
        print("\nSorry.\nBut up can never leave.\nYou live here now.\nGoodBye.")
    else:
        print("\nI didn't understand that choice.\n")

