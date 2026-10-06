# Main file, prolly gonna have it be just handling UI and prompting user

import character_analyze
import data_loader
import sort_file
import quiz_game


def user_inputs(characters: list[dict]) -> None:
    question = int(input("Choose an integer input!\n1. Get Statistics\n2. Sort data\n3. Play Quiz\n Choice: "))

    if question == 1:
        statistic_question = int(input("--\n1. General Information\n2. Search Character Info"))
    elif question == 2:
        sort_question = int(input)

        return
    elif question == 3:
        #
        quiz_game.run_quiz(characters)

        return


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
     
    characters = data_loader.read_file("genshin_character_list.csv")

    #print(characters[1][0])
    #print(character_analyze.character_report("Vesna", characters))
    #print(character_analyze.most_common_region(characters))
    #print(character_analyze.character_rarity_check(characters))

    #print(sort_file.new_csv_sorted("sorted_region_rarity.csv", characters))

    #print(sort_file.alphabet_csv("alphabetical.csv", characters))

    #print(sort_file.binary_search_character(characters, "Zhongli"))

    user_inputs(characters)

    #print(quiz_game.pick_random_character(characters))
    

if __name__ == "__main__":
    main()