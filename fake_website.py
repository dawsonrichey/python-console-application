# Dawson Richey
# This will serve as the main app file for the project
import os
from datetime import datetime, date

time = datetime.time()
date = date.date()
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


def store_title_bar():
    # Clears the terminal screen, and displays a Store title bar.
    os.system('clear')
    print("****************************************************************")
    print("***                   Oleanders Wand Shop                    ***")
    print("****************************************************************")


"""A class that can be used to represent a car."""


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
