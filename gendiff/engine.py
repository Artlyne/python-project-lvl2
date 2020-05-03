"""Finds the difference between two JSON files."""
import json

SAME, ADDED, REMOVED = ' ', '+', '-'


def generate_diff(path_to_file1, path_to_file2):
    """Find the difference between two JSON files.

    Args:
        path_to_file1 (str): specify the path to the file1
        path_to_file2 (str): specify the path to the file2

    Returns:
        str
    """
    before = json.load(open(path_to_file1))
    after = json.load(open(path_to_file2))

    same_keys = before.keys() & after.keys()
    removed_keys = before.keys() - after.keys()
    added_keys = after.keys() - before.keys()

    difference = ''

    for key in same_keys:
        if before[key] == after[key]:
            difference += f'{SAME} {key}: {before[key]}\n'
        else:
            difference += f'{ADDED} {key}: {after[key]}\n'
            difference += f'{REMOVED} {key}: {before[key]}\n'

    for key in removed_keys:
        difference += f'{REMOVED} {key}: {before[key]}\n'

    for key in added_keys:
        difference += f'{ADDED} {key}: {after[key]}\n'

    return difference
