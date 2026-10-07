# This python file will have all functions that analyze data
import sort_file

def header(characters: list[dict]):

    return list(characters[0].keys())



def character_report(character_name: str, characters: list[dict]) -> str:
    """ This function will use sort_file.py to find the character and formats their information.
    
    Args:
        character_name (str): This is the character name that the user wants the data of. Does not need to be case sensitive.
        characters (list): The data set in a list format

    Returns:
        Will return a clean string containing all the info about the character.

    """

    character_row = sort_file.linear_search_character(characters, character_name)
    head = header(characters)
    line = ""

    for title_index in range(len(head)):
        line = line + head[title_index] + ": " + character_row[title_index] + "\n"


    # "Will return a string containing character data ex."
    return line

def most_common_region(characters: list[dict]) -> list[str]:
    """ This function will check all the characters and tally up which region is the most common

    Args:
        characters (list): The data set in a list format

    Returns:
        Will return a list of the most common to least common regions in order.

    """
    count_dict = {}
    common_regions = []

    for row in characters:
        region = row['region']
        if region not in count_dict:
            count_dict[region] = 0
        count_dict[region] += 1


    pairs = []
    for region, count in count_dict.items():
        pairs.append((count, region))

    pairs.sort(reverse=True)

    for count, region in pairs:
        if region != "":
            common_regions.append(f"{region}: {count}")
        else:
            common_regions.append(f"Unknown: {count}")

    return common_regions

def character_rarity_check(characters: list) -> str:
    """ This function will tally up the total amount of 5 and 4 star characters in the game.

    Args:
        characters (list): The data set in a list format

    Returns:
        Returns how many 4 stars and 5 stars are in the game and then the total amount of characters in the game.

    """
    count_dict = {}

    for row in characters:
        rarity = row['rarity']

        if rarity not in count_dict:
            count_dict[rarity] = 0
        count_dict[rarity] += 1


    five_star = count_dict["5-star"]
    four_star = count_dict["4-star"]
    
        

    return f"There are {five_star} 5-stars and {four_star} 4-stars in the game. Together, there are {five_star + four_star} characters in the game!"