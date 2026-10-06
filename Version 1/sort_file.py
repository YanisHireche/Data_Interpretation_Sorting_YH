# This function will be sorting the CSV file


def character_sort(characters: list[dict]) -> list[dict]:
    """ This function will sort the data by region first and then by rarity.

    Args:
        characters (list[dict]): The data set in a list[dict] format

    Returns:
        Will return a list of each character now sorted first by region then by unit rarity.

    """
    return []

def alphabetical_sort(characters: list[dict]) -> list[dict]:
    """ This function will sort the data alphabetically by a character's name.

    Args:
        characters (list[dict]): The data set in a list[dict] format

    Returns:
        Will return a list of each character now sorted by their names alphabetically.

    """


    return []

def linear_search_character(characters: list[dict], character_name: str) -> dict:
    """ This function will search for a specific character using linear search.

    Args:
        characters (list[dict]): The data set in a list[dict] format
        character_name (str): The name of the character we want to find.

    Returns:
        Will return the row that the character we are looking for is on containing all of their data.

    """

    return {}


def binary_search_character(characters: list[dict], character_name: str) -> dict:
    """ This function will take in a sorted list and search for a specific character using binary search.

    Args:
        characters (list[dict]): The data set in a list[dict] format
        character_name (str): The name of the character we want to find.

    Returns:
        Will return the row that the character we are looking for is on containing all of their data.

    """
    return {}


def new_csv_sorted(new_filepath: str, characters: list[dict]) -> str:
    """ This function will make a new file containing the sorted data from character_sort.

    Args:
        new_filepath (str): The filepath we want the new file to be stored in.
        characters (list[dict]): The data set in a list[dict] format
        

    Returns:
        A string confirming that a new file was made.

    """
    return "Made new file!"