# This python file will be doin data reading

import csv

sample_characters = [
{
        "Name": "Amber",
        "Rarity": "4",
        "Element": "Pyro",
        "Weapon": "Bow",
        "Region": "Mondstadt",
        "Model": "Medium Female"
    },
    {
        "Name": "Zhongli",
        "Rarity": "5",
        "Element": "Geo",
        "Weapon": "Polearm",
        "Region": "Liyue",
        "Model": "Tall Male"
    },
    {
        "Name": "Raiden Shogun",
        "Rarity": "5",
        "Element": "Electro",
        "Weapon": "Polearm",
        "Region": "Inazuma",
        "Model": "Tall Female"
    }
]


def read_file(csv_file: str) -> list[dict]:
    """ This function will read the data file
    
    Args:
        csv_file (str): This represents the directory of the file we will be using

    Returns:
        Will return a list with each row as a sublist

    """

    character_list = []

    with open(csv_file) as genshin_file:

        read_gi = csv.DictReader(genshin_file)

        for line in read_gi:
            character_list.append(line)

    return character_list



def return_sample_characters() -> list[dict]:
    """ This function will return a few hard coded character from my data set

    Returns:
        list[dict]: A small sample list of characters

    """
    print("This code has run")

    return sample_characters