# Author Dawson Richey
"""A class that can be a user"""


class User:

    def __init__(self, first_name, last_name, username, password, current_time):
        """Initialize attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.current_time = current_time

    def get_full_name(self):
        """Return full name."""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.title()

    def new_user(self, first_name, last_name, username, password):
        """ new user input """
        self.first_name = input(f'Username: {first_name}')
        self.last_name = input(f'Password: {last_name}')
        self.username = input(f'Username: {username}')
        self.password = input(f'Password: {password}')
