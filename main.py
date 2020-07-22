# Dawson Richey
# This will serve as the main app file for the project

import os
from datetime import datetime, date
import os

import scraper

now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")
# Month abbreviation, day and year
current_date = today.strftime("%b-%d-%Y")

full_datetime = print("Datetime =", current_time, current_date)


# FUNCTIONS
def welcome_message():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
    print("********************************************************")
    print("***                      WELCOME                     ***")
    print("***            before you can get started            ***")
    print("***             you need to have account             ***")
    print("********************************************************")
    print("***    please enter the number that best applies     ***")
    print("********************************************************")
    print("***               1. Sign In                         ***")
    print("***               2. New User Registration           ***")
    print("***               3. Forgot Your Username            ***")
    print("***               4. Forgot Your Password            ***")
    print("********************************************************\n")


def menu_options():
    # this is the menu of options to keep the app running
    os.system('clear')
    print("\nPlease select a number from the following: ")
    print("0 = Sign-up")
    print("1 = Sign-in")
    print("2 = Log-out")
    print("(enter 'q'' at any time'to quit)")


def asking_questions():
    answer1 = input(welcome_message())
    print(answer1)
    answer2 = input(menu_options())
    print(answer2)
# welcome_message()
# login_option = int(input())
# # print('Something has gone wrong please try again')
# if 1 <= login_option >= 8:
#     print('Something has gone wrong please try again')
#     welcome_message()
# else:
#     menu_options()
#     login_option = input('Please enter your number now:')
#
# print(login_option)


asking_questions()

