# This python file will have all functions that analyze data

def character_report(character_name: str, characters: list[dict]) -> str:
    """ This function will use sort_file.py to find the character and formats their information.
    
    Args:
        character_name (str): This is the character name that the user wants the data of. Does not need to be case sensitive.
        characters (list[dict]): The data set in a list[dict] format

    Returns:
        Will return a clean string containing all the info about the character.

    """

    # "Will return a string containing character data ex."
    return "Unit: Amber\nRarity: 4 Star\nElement: Pyro\nWeapon: Bow\nRegion: Mondstadt\nModel: Medium Female" 

def most_common_region(characters: list[dict]) -> list[str]:
    """ This function will check all the characters and tally up which region is the most common using a dictionary variable.

    Args:
        characters (list[dict]): The data set in a list[dict] format

    Returns:
        Will return a list of the most common to least common regions in order.

    """

    return ["Liyue", "Mondstadt", "Sumeru"]

def character_rarity_check(characters: list[dict]) -> str:
    """ This function will tally up the total amount of 5 and 4 star characters in the game.

    Args:
        characters (list[dict]): The data set in a list[dict] format

    Returns:
        Returns how many 4 stars and 5 stars are in the game and then the total amount of characters in the game.

    """
    five_star_total = 3
    four_star_total = 10

    return f"There are {five_star_total} 5 stars and {four_star_total} 4 stars in the game. Together, there are {five_star_total + four_star_total} characters in the game!"