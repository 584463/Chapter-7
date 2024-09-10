import random
from datetime import datetime

# Function to check if age is 21 or older
def check_age_21() -> bool:
    """
    Ask the user for their age and implement a loop to keep asking until a valid integer is provided.
    Return True if the age is 21 or older, otherwise return False.
    """
    while True:
        age = input("Please enter your age: ")
        try:
            age = int(age)
            # Check if age is 21 or older
            return False # Change this
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to check the grade level
def check_grade_level() -> bool:
    """
    Ask the user for their grade level (between 9 and 12) and keep asking until a valid grade is provided.
    Print the grade level like freshman, sophomore, junior, or senior if valid.
    Return True if the grade is valid, otherwise return False.
    """
    while True:
        grade = input("Please enter your grade level (9-12): ")
        # Implement logic here

# Function to check if date of birth is valid
def check_date_of_birth() -> bool:
    """
    Ask the user for their year of birth and keep asking until a valid year is provided.
    Return True if the year is between 1900 and the current year, otherwise return False.
    """
    current_year = datetime.now().year
    while True:
        date_of_birth = input("Please enter your birth year: ")
        # Implement logic here

# Function to check if list contains at least 3 cars of different models
def check_the_list_of_cars() -> bool:
    """
    Ask the user for a list of cars (at least 3 different models).
    Keep asking until the input is valid.
    Return True if there are at least 3 cars with different models.
    """
    while True:
        car_list = input("Please enter a list of car models (comma separated): ").split(",")
        # Implement logic here

# Function to check if user can drive
def check_if_you_can_drive() -> bool:
    """
    Ask the user if they can drive (yes or no) and keep asking until a valid response is provided.
    Return True if the response is valid, otherwise return False.
    """
    while True:
        can_drive = input("Can you drive (yes or no)? ").lower()
        # Implement logic here

# Function to check weather conditions
def check_weather() -> bool:
    """
    Ask the user for the weather condition and keep asking until a valid input is provided.
    Valid weather conditions are ['sunny', 'rainy', 'snowy', 'wind'].
    Return True if the weather is valid.
    """
    while True:
        weather = input("Please enter the weather condition (sunny, rainy, snowy, wind): ").lower()
        # Implement logic here

# Function to check if user can play a game (random boolean value)
def check_if_you_can_play_game() -> bool:
    """
    Ask the user if they can play a game.
    Randomly generate True or False and return 'You can play game' if True.
    """
    while True:
        can_play = input("Do you want to check if you can play the game? (yes or no): ").lower()
        # Implement logic here

# Function to check study or play time
def check_study_time_or_play_time() -> bool:
    """
    Ask the user if it's study time or play time.
    Valid inputs are ['study', 'play'].
    Return True if the input is valid, otherwise return False.
    """
    while True:
        study_or_play = input("Is it study time or play time? ").lower()
        # Implement logic here

# Function to store input in a variable
def make_the_input_store_in_variable() -> str:
    """
    Ask the user for an input and store it in a variable.
    Use if-else statements to check the type of the input and convert it to the appropriate data type.
    Return the input.
    """
    user_input = input("Please enter something: ")
    # Implement logic here

# Function to check if a number is even
def check_if_the_number_is_even() -> bool:
    """
    Ask the user for a number and keep asking until a valid integer is provided.
    Return True if the number is even, otherwise return False.
    """
    while True:
        number = input("Please enter a number: ")
        try:
            number = int(number)
            # Implement logic here
        except ValueError:
            print("Invalid input. Please enter a valid number.")
