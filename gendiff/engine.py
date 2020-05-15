"""Finds the difference between two configuration files."""
from gendiff import file_loader
from gendiff.form import extended

SAME, REMOVED, ADDED = '  ', '- ', '+ '


def get_same_keys(first_dict, second_dict):
    return first_dict.keys() & second_dict.keys()


def get_removed_keys(first_dict, second_dict):
    return first_dict.keys() - second_dict.keys()


def get_added_keys(first_dict, second_dict):
    return second_dict.keys() - first_dict.keys()


def diff(first_dict, second_dict):
    difference = {}

    for key in get_same_keys(first_dict, second_dict):
        if isinstance(first_dict[key], dict):
            difference[f'{SAME}{key}'] = \
                diff(first_dict[key], second_dict[key])
        elif first_dict[key] == second_dict[key]:
            difference[f'{SAME}{key}'] = first_dict[key]
        else:
            difference[f'{REMOVED}{key}'] = first_dict[key]
            difference[f'{ADDED}{key}'] = second_dict[key]

    for key in get_removed_keys(first_dict, second_dict):
        difference[f'{REMOVED}{key}'] = first_dict[key]

    for key in get_added_keys(first_dict, second_dict):
        difference[f'{ADDED}{key}'] = second_dict[key]

    return difference


def generate_diff(first_file, second_file):
    """Finds the difference between two configuration files.

    Supported YAML and JSON files.

    Args:
        first_file (str): first configuration file
        second_file (str): second configuration file

    Returns:
        str: difference between files, where first symbol in key means:
            ' ' - same item
            '-' - removed item
            '+' - added item
    """
    first = file_loader.load(first_file)
    second = file_loader.load(second_file)
    return extended.show(diff(first, second))
