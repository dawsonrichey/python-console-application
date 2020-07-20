import os

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


def riddle_game():

    answer = 5
    riddle = "How many woods can a woodchuck chuck? "
    riddle_guess = int(input(riddle))

    while riddle_guess != answer:
        bad_guess = "Guess Again "
        riddle_guess = int(input(bad_guess))

    print("Impressive! You guessed right.")


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
        print("\nSORRY BUT YOU HAVE NO MONEY\n")
    elif choice == '3':
        print("\nSORRY BUT THE GAME HAS NOT YET BEEN BUILT.\nPLEASE TRY AGAIN LATER\n")
    elif choice == 'e':
        print("\nSorry.\nBut up can never leave.\nYou live here now.\nGoodBye.")
    else:
        print("\nI didn't understand that choice.\n")

