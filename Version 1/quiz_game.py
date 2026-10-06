# This function will contain the main body of the quiz game

import random

def pick_random_character(characters: list[dict]) -> dict:
    """ This function will use random to pick a random character in the data set.
    
    Args:
        characters (list[dict]): The data set in a list[dict] format

    Returns:
        will return the row of data the character is on

    """

    return {}

def give_hint(character: dict, attempt: int) -> str:

    """ This function will give another data type of the character chosen if user answers wrong
    
    Args:
        character (dict): The dictionary gotten from pick_random_character()
        attempt (int): An attempt counter that will be tracked inside run_quiz() that will dictate which hint you receive
                 (attempt 1 = region, attempt 2 = element, attempt 3 = weapons, etc)

    Returns:
        will return a character attribute based on the attempt count

    """
    # the attempt will be the index of the dictionary is the idea. If it goes out of bounds, 
    # then the player loses and program will tell user the character.

    return "4 star"

def run_quiz(characters: list[dict]) -> None:
    """ The command center of the game. Will run pick_random_character() and tell user it picked one, then it will
        constantly run an input() to guess the character name. If user guesses wrong, it will give a hint depending
        on the index/position of the dictionary length.
    
    Args:
        characters (list[dict]): The data set in a list[dict] format

    Returns:
        None

    """



    # character = pick_random_character(characters)

    # Uses for i in range(len(character)) to dictate how many hints/attempts are given.
    # If attempts go beyond the length, the user will fail and program will tell the user who was the character.
    # It will then ask if they want to play again, which will call run_quiz() if they say yes.



    print("A character has been picked!")