# This function will be sorting the CSV file
import csv

def character_sort(characters: list[dict]) -> list:
    """ This function will turn the list of dictionaries into a list of lists and then sort it by region, then rarity.

    Args:
        characters (list[dict]): The data set in a list format

    Returns:
        Will return a list of each character now sorted first by region then by unit rarity.

    """
    sorted_characters = []
    for character in characters:


        pass

    sorted_char = sorted(characters, key=lambda x: (x[4], x[3]))

    return sorted_char

def alphabetical_sort(characters: list[dict]) -> list:
    """ This function will turn the list of dictionaries into a list of lists and then sort it by alphabet

    Args:
        characters (list[dict]): The data set in a list[dict] format

    Returns:
        Will return a list of each character now sorted by their names alphabetically.

    """
    sorted_char = characters[:1] + sorted(characters[1:], key=lambda x: x[0])

    return sorted_char

def linear_search_character(characters: list[dict], character_name: str) -> dict:
    """ This function will search for a specific character using linear search.

    Args:
        characters (list[dict]): The data set in a list[dict] format
        character_name (str): The name of the character we want to find.

    Returns:
        Will return the row that the character we are looking for is on containing all of their data.

    """

    for index in range(1, len(characters)):
        if characters[index][0] == character_name:
            return characters[index]

    return {}


def binary_search_character(characters: list[dict], character_name: str) -> dict | str:
    """ This function will take in a sorted list and search for a specific character using binary search.

    Args:
        characters (list[dict]): The data set in a list[dict] format
        character_name (str): The name of the character we want to find.

    Returns:
        Will return the row that the character we are looking for is on containing all of their data.

    """
    sorted_alph = alphabetical_sort(characters)

    low = 0
    high = len(sorted_alph) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if sorted_alph[mid][0] < character_name:
            low = mid + 1
        elif sorted_alph[mid][0] > character_name:
            high = mid - 1
        else:
            return sorted_alph[mid]
    return "This character is not in the database!"


def new_csv_sorted(new_filepath: str, characters: list[dict]) -> str:
    """ This function will make a new file containing the sorted data from character_sort.

    Args:
        new_filepath (str): The filepath we want the new file to be stored in.
        characters (list[dict]): The data set in a list[dict] format
        

    Returns:
        A string confirming that a new file was made.

    """

    with open(new_filepath, "w", newline='') as new_csv:
        new_writing = csv.writer(new_csv)

        new_writing.writerows(character_sort(characters))


    return "Made a new region & rarity sorted file!"

def alphabet_csv(new_filepath: str, characters: list[dict]) -> str:
    """ This function will make a new file containing the sorted data from character_sort.

    Args:
        new_filepath (str): The filepath we want the new file to be stored in.
        characters (list[dict]): The data set in a list[dict] format
        

    Returns:
        A string confirming that a new file was made.

    """
    with open(new_filepath, "w", newline='') as new_csv:
        new_writing = csv.writer(new_csv)

        new_writing.writerows(alphabetical_sort(characters))

    return "Made a new alphabetically sorted file!"