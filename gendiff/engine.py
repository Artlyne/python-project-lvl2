"""Finds the difference between two configuration files."""
from gendiff import file_loader

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


def rendering(difference, depth='  '):
    result = []
    for key, value in sorted(difference.items(), key=lambda x: x[0][2:]):
        # sorts lexicographically by key
        # we need to skip the first two characters [2:] in the key x[0],
        # because they mean the difference
        if isinstance(value, dict):
            subtree = rendering(value, depth=depth + '    ')
            result.append(f'{depth}{key}: {{\n'
                          f'{subtree}\n'
                          f'  {depth}}}')
        else:
            result.append(f'{depth}{key}: {value}')

    return '\n'.join(result)


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
    return f'{{\n{rendering(diff(first, second))}\n}}'
