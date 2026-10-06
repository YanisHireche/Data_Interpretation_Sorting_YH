# Main file, prolly gonna have it be just handling UI and prompting user

import character_analyze
import data_loader
import sort_file
import quiz_game

def main():
    # will build UI by prompting user

    """
    choice = input(dialogue that will ask user what they wanna do with function)
    They will answer with a number, 1 or 2.
    Decisions will range from:
    1. Get Statistics
    2. Sort data
    3. Play quiz


    If they pick 1. Get statistics, they will be given two choices. They will be asked if they want a specific character,
    or if they want general data of the entire file. If they ask for a specific character, it will return all data related
    to that character. If they want general data, it will give stuff like the most common weapon type, most common model type, 
    rarest model + element combination, etc. These statistics will be ran in character_analyze and be returned back to 
    this main file.

    If they pick 2. Sort data, the sort_file.py file will be used to return two new sorted csv files that has been sorted.
    Linear and Binary searches will be used to find informtion from sorted data.

    If they pick 3. Play quiz, it will use the quiz_game.py file and play a little game where you have to guess a character using
    information the program will give you every time you guess wrong.

    """
    # 
    print("test")
    

if __name__ == "__main__":
    main()