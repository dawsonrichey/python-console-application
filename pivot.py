import os

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
        q1_2 = int(input("How much would you like to borrow? "))
    print(f"Let's see what you can buy with ${q1_2}\n")
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
    nerd_q1 = "What part of the plant conducts photosynthesis? "
    nerd_q2 = "Frog is a reptile or amphibian? "
    nerd_q3 = "Which scientist proposed the three laws of motion? "
    nerd_q4 = "The standard unit of measurement for energy is ____."

    nerd_a1 = "leaf"
    nerd_a2 = "amphibian"
    nerd_a3 = "isaac newton"
    nerd_a4 = "joule"

    nerd_g1 = input(nerd_q1).lower()
    nerd_g2 = input(nerd_q2).lower()
    nerd_g3 = input(nerd_q3).lower()
    nerd_g4 = input(nerd_q4).lower()

    score = 0
    if nerd_g1 == nerd_a1:
        score += 1
    if nerd_g2 == nerd_a2:
        score += 1
    if nerd_g3 == nerd_a3:
        score += 1
    if nerd_g4 == nerd_a4:
        score += 1

    print(f'You answered {score} answers correct')


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
