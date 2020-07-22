# Dawson Richey
# This will serve as the main app file for the project
import datetime
import os
from datetime import time, date
# from fake_website import User
# from user import get_full_name

time = datetime.time()
date = datetime.date()
# Time abbreviation, hour min, and second
current_time = time.strftime("%H:%M:%S")
# Date abbreviation, day and year
current_date = date.strftime("%b-%d-%Y")

full_datetime = print("Time and Date =", current_time, current_date)


# FUNCTIONS
def program_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
    print("****************************************************************")
    print("***      You are about to enter another dimension.           ***")
    print("***   A dimension not only of sight and sound, but of mind.  ***")
    print("***       A journey into a wondrous land of imagination.     ***")
    print("****************************************************************")


def menu_options():
    # this is the menu of options to keep the app running
    print("\nPlease select a number from the following: ")
    print("0 = Sign-up")
    print("1 = Sign-in")
    print("2 = Log-out")
    print("(enter 'q' at any time to quit)")


print(full_datetime)

program_title_bar()
menu_selection = input(menu_options())
# This is an infinite loop!

while menu_selection != 'q':
    num_selected = int(input("select one number from the following list"))
    user.new_user()




# class User:
#
#     def __init__(self, first_name, last_name, username, password, current_time):
#         """Initialize attributes to describe a user."""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username
#         self.password = password
#         self.current_time = current_time
#
#     def get_full_name(self):
#         """Return full name."""
#         full_name = f"{self.first_name} {self.last_name}"
#         return full_name.title()
#
#     def new_user(self, first_name, last_name, username, password):
#         """ new user input """
#         self.first_name = input(f'Username: {first_name}')
#         self.last_name = input(f'Password: {last_name}')
#         self.username = input(f'Username: {username}')
#         self.password = input(f'Password: {password}')
