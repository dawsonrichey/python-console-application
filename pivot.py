import os
# importing datetime module for now()
from datetime import datetime
from datetime import date
now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")
# Month abbreviation, day and year
current_date = today.strftime("%b-%d-%Y")
full_datetime = print("Time and Date =", current_time, current_date)



# creating a dictionary of items to sell in the shop
# The 1 will skip 0 when listing the item number
wands = {'Oak': 23, 'Pine': 99, 'Maple': 837}


# FUNCTIONS
def program_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
    print("****************************************************************")
    print("***      You are about to enter another dimension.           ***")
    print("***   A dimension not only of sight and sound, but of mind.  ***")
    print("***       A journey into a wondrous land of imagination.     ***")
    print("****************************************************************")


def store_title_bar():
    # Clears the terminal screen, and displays a Store title bar.
    os.system('clear')
    print("****************************************************************")
    print("***                   Oleanders Wand Shop                    ***")
    print("****************************************************************")


def riddle_game():
    answer = "teeth"
    riddle = "Thirty white horses on a red hill, First they champ, Then they stamp, Then they stand still."
    riddle_guess = int(input(riddle))

    while riddle_guess != answer:
        bad_guess = "Guess Again "
        riddle_guess = int(input(bad_guess))

    print("Impressive! You guessed right.")


def shopping_spree():
    purchase = []
    print('I hope you love to shop...because you have no other options!')
    q1 = input("Do you have any money? ")
    if q1 == 'y':
        q1_2 = int(input("How much? "))
    elif q1 == 'n':
        q1_2 = int(input('How much would you like to borrow? '))
        print(f"Lets see what you can buy with $ {q1_2}")
    store_title_bar()
    for i, (k, v) in enumerate(wands.items()):
        print(f"[{i}]  {k} ${v}")
    owner_q1 = input('Would you like to buy something? ')
    if owner_q1 == 'y':
        purchase_number = int(input('Please Enter the Number of the item you would like to buy at this time? '))
        purchase.append(purchase_number)
        print()
    elif owner_q1 == 'n':
        print('no')


def nerd_quiz():
    # questions dict.items()
    nerd_questions = {"What part of the plant conducts photosynthesis? ": "leaf",
                      "Frog is a reptile or amphibian? ": "amphibian",
                      "Which scientist proposed the three laws of motion? ": "isaac newton",
                      "The standard unit of measurement for energy is ____. ": "joule"}
    # guesses
    nerd_guesses = []
    score = 0
    for x in nerd_questions.keys():
        nerd_guess = input(x)
        nerd_guesses.append(nerd_guess.lower())

    for x, y in nerd_questions.items():
        for i in nerd_guesses:
            if i == y:
                score += 1
            nerd_guesses.pop(0)
            break;

    print(f'You answered {score} answers correct')
    # Open the coffee.txt file in append mode.
    quiz_file = open('quiz.txt', 'a')
    save_results = input('Would you like to save your results? ')

    if save_results == 'y':
        # Append the data to the file.
        quiz_file.write(user + ': scored ' + str(score) + ' points : ' + str(current_time) + ' ' + str(current_date)  + '\n')
        # Close the file.
    quiz_file.close()
    print('Data appended to coffee.txt.')



def get_user_choice():
    # Let users know what they can do.
    print("\n[1] Answer My Riddle")
    print("[2] Go Shopping")
    print("[3] Take a quiz")
    # print("[4] User Quest Tracker")
    print("[e] Exit\n")

    return input("What would you like to do? ")


# MAIN PROGRAM
# Set up a loop where users can choose what they'd like to do.
users = []
user = input('Please Enter Your Name: ')
users.append(user)
print(users)
choice = ''
program_title_bar()
print(f"\nWelcome, '{user}!")
while choice != 'e':

    choice = get_user_choice()

    # Respond to the user's choice.
    if choice == '1':
        riddle_game()
    elif choice == '2':
        shopping_spree()
    elif choice == '3':
        nerd_quiz()
    elif choice == '4':
        print("\nPLEASE TRY AGAIN LATER\n")
    elif choice == 'e':
        print("\nSorry.\nBut up can never leave.\nYou live here now.\nGoodBye.")
    else:
        print("\nI didn't understand that choice.\n")
