import random
from datetime import datetime

# Function to check if age is 21 or older
def check_age_21(age: int) -> bool:
    """
    Checks if the age is 21 or older.
    Return True if the age is 21 or older, otherwise return False.
    """
    return age >= 21

# Function to check the grade level
def check_grade_level(grade: str) -> bool:
    """
    Checks if the grade level is between 9 and 12.
    Return True if the grade is valid, otherwise return False.
    Prints the grade level like freshman, sophomore, junior, or senior if valid.
    """
    grade_dict = {
        '9': 'Freshman',
        '10': 'Sophomore',
        '11': 'Junior',
        '12': 'Senior'
    }
    if grade in grade_dict:
        print(grade_dict[grade])
        return True
    return False

# Function to check if date of birth is valid
def check_date_of_birth(date_of_birth: int) -> bool:
    """
    Checks if the date of birth is between 1900 and the current year.
    Return True if valid, otherwise return False.
    """
    current_year = datetime.now().year
    return 1900 <= date_of_birth <= current_year

# Function to check if list contains at least 3 cars of different models
def check_the_list_of_cars(car_list: list) -> bool:
    """
    Checks if the car list contains at least 3 different car models.
    Return True if valid, otherwise return False.
    """
    return len(set(car_list)) >= 3

# Function to check if user can drive
def check_if_you_can_drive(can_you_drive: str) -> bool:
    """
    Checks if the answer is either 'yes' or 'no'.
    Return True if valid, otherwise return False.
    """
    return can_you_drive.lower() in ['yes', 'no']

# Function to check weather conditions
def check_weather(weather: str) -> bool:
    """
    Checks if the weather condition is valid.
    Valid conditions: ['sunny', 'rainy', 'snowy', 'wind'].
    Return True if valid, otherwise return False.
    """
    valid_weather = ['sunny', 'rainy', 'snowy', 'wind']
    return weather.lower() in valid_weather

# Function to check if user can play a game (random boolean value)
def check_if_you_can_play_game() -> bool:
    """
    Randomly generates True or False.
    Return True if True (you can play the game), otherwise return False.
    """
    return random.choice([True, False])

# Function to check study or play time
def check_study_time_or_play_time(study_time_or_play_time: str) -> bool:
    """
    Checks if the input is either 'study' or 'play'.
    Return True if valid, otherwise return False.
    """
    valid_options = ['study', 'play']
    return study_time_or_play_time.lower() in valid_options

# Function to store input in a variable
def make_the_input_store_in_variable(input_string: str) -> str:
    """
    Takes a string input_string and returns it.
    """
    user_input = input_string
    return user_input

# Function to check if a number is even
def check_if_the_number_is_even(number: int) -> bool:
    """
    Checks if the number is even.
    Return True if even, otherwise return False.
    """
    return number % 2 == 0
