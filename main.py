# Dawson Richey
# This will serve as the main app file for the project

import os

from datetime import datetime, date

import self as self

now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")
# Month abbreviation, day and year
current_date = today.strftime("%b-%d-%Y")

full_datetime = print("Time and Date =", current_time, current_date)

# FUNCTIONS
def welcome_message():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
    print("********************************************************")
    print("***                 Welcome                          ***")
    print("***                 have a                           ***")
    print("***                 good time                        ***")
    print("********************************************************")


def menu_options():
    # this is the menu of options to keep the app running
    print("\nPlease select a number from the following: ")
    print("0 = Sign-up")
    print("1 = Sign-in")
    print("2 = Log-out")
    print("(enter 'q' at any time to quit)")
    menu_selection = input('here')


welcome_message()
menu_options()
#
# while menu_selection != 'q':
#     if menu_selection == '0':
#         print('you put 0')
#     elif menu_selection == '1':
#         print('you put 1')
#     elif menu_selection == '2':
#         print('you put 2')


# def menu_selection():
#     pass


