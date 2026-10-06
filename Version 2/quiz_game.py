# This function will contain the main body of the quiz game

import random
from typing import Any

def pick_random_character(characters: list[dict]) -> dict[Any, Any]:
    """ This function will use random to pick a random character in the data set.
    
    Args:
        characters (list[dict]): The data set in a list format

    Returns:
        will return the row of data the character is on

    """

    character_index = random.randint(0, len(characters) - 1)

    print(characters[character_index])
    return characters[character_index]

def give_hint(character: dict, attempt: int) -> tuple:

    """ This function will give another data type of the character chosen if user answers wrong
    
    Args:
        character (list[dict]): The list gotten from pick_random_character()
        attempt (int): An attempt counter that will be tracked inside run_quiz() that will dictate which hint you receive
                 (attempt 1 = region, attempt 2 = element, attempt 3 = weapons, etc)

    Returns:
        will return a character attribute based on the attempt count as well as the new attempt count

    """
    
    #len(character) - 1
    set_to_return = ()

    hints = ["primary_role", "gender", "model_type", "rarity", "region", "element", "weapon_type"]

    try:
        set_to_return = (character[hints[attempt]], attempt + 1)
    except:
        set_to_return = (f"You're out of guesses! The answer was {character['character_name']}", -1)

    # the attempt will be the index of the dictionary is the idea. If it goes out of bounds,
    # then the player loses and program will tell user the character.

    return set_to_return


def play_again(characters: list[dict]) -> bool | None:

    playing = True

    while playing:
        print("Would you like to play again?:\n1. Yes\n2. No")
        try:
            answer = int(input())

            if answer == 1:
                playing = False
                return True

            elif answer == 2:
                playing = False
                return False

            else:
                print("You must pick either choice 1 or 2!")
        except:
            print("You must pick either choice 1 or 2!")
    return None


def run_quiz(characters: list) -> None:
    """ The command center of the game. Will run pick_random_character() and tell user it picked one, then it will
        constantly run an input() to guess the character name. If user guesses wrong, it will give a hint depending
        on the index/position of the dictionary length.
    
    Args:
        characters (list[dict]): The data set in a list[dict] format

    Returns:
        None

    """


    playing = True
    character = pick_random_character(characters)
    attempt_count = 0

    while playing:

        if attempt_count == 0:
            print("---")
            print("Welcome to the character guesser!")

            print("Your first hint: ")
        
        hint_info = give_hint(character, attempt_count)

        print("--")
        print(f"hint: {hint_info[0]}")

        attempt_count = hint_info[1]

        
        if attempt_count == -1 or attempt_count == 8:

            if play_again(characters):
                run_quiz(characters)

            break


        guess = input("Guess: ")
        guess = guess.title()

        if guess != character['character_name']:
            print("Wrong!\n--\n")
        else:
            print(f"\nYou guessed correct! Your attempts: {attempt_count - 1}!\n")
            play_again(characters)
            break
            



    # Uses for i in range(len(character)) to dictate how many hints/attempts are given.
    # If attempts go beyond the length, the user will fail and program will tell the user who was the character.
    # It will then ask if they want to play again, which will call run_quiz() if they say yes.