import pytest
from assignment import check_age_21, check_grade_level, check_date_of_birth, check_the_list_of_cars
from assignment import check_if_you_can_drive, check_weather, check_if_you_can_play_game, check_study_time_or_play_time
from assignment import make_the_input_store_in_variable, check_if_the_number_is_even


def test_check_age_21():
    assert check_age_21(21) is True
    assert check_age_21(25) is True
    assert check_age_21(18) is False


def test_check_grade_level():
    assert check_grade_level('9') is True  # Freshman
    assert check_grade_level('10') is True  # Sophomore
    assert check_grade_level('11') is True  # Junior
    assert check_grade_level('12') is True  # Senior
    assert check_grade_level('8') is False  # Invalid


def test_check_date_of_birth():
    assert check_date_of_birth(1990) is True  # Valid year
    assert check_date_of_birth(2023) is True  # Valid year
    assert check_date_of_birth(1800) is False  # Invalid year


def test_check_the_list_of_cars():
    assert check_the_list_of_cars(['Toyota', 'Honda', 'Ford']) is True  # Valid list
    assert check_the_list_of_cars(['Toyota', 'Toyota', 'Toyota']) is False  # Invalid, all same model
    assert check_the_list_of_cars(['Toyota', 'Honda']) is False  # Less than 3 cars


def test_check_if_you_can_drive():
    assert check_if_you_can_drive('yes') is True  # Valid answer
    assert check_if_you_can_drive('no') is True  # Valid answer
    assert check_if_you_can_drive('maybe') is False  # Invalid answer


def test_check_weather():
    assert check_weather('sunny') is True  # Valid weather
    assert check_weather('rainy') is True  # Valid weather
    assert check_weather('windy') is False  # Invalid (not in the list)
    assert check_weather('stormy') is False  # Invalid (not in the list)


def test_check_if_you_can_play_game():
    assert isinstance(check_if_you_can_play_game(), bool)  # Random True/False
    # No exact True/False because it's randomly generated


def test_check_study_time_or_play_time():
    assert check_study_time_or_play_time('study') is True  # Valid
    assert check_study_time_or_play_time('play') is True  # Valid
    assert check_study_time_or_play_time('sleep') is False  # Invalid


def test_make_the_input_store_in_variable():
    assert make_the_input_store_in_variable('hello') == 'hello'  # Valid string
    assert isinstance(make_the_input_store_in_variable('123'), str)  # Check if it's string


def test_check_if_the_number_is_even():
    assert check_if_the_number_is_even(4) is True  # Even
    assert check_if_the_number_is_even(3) is False  # Odd
    assert check_if_the_number_is_even(0) is True  # Even
