"""Finds the difference between two JSON files."""
from gendiff import file_loader


SAME, REMOVED, ADDED = '   ', '  -', '  +'


def generate_diff(path_to_file1, path_to_file2):
    """Find the difference between two JSON files.

    Args:
        path_to_file1 (str): specify the path to the file1
        path_to_file2 (str): specify the path to the file2

    Returns:
        str: difference between files, where first symbols in string means:
            '   ' - same item
            '  -' - removed item
            '  +' - added item
    """
    before = file_loader.load(open(path_to_file1))
    after = file_loader.load(open(path_to_file2))

    same_keys = sorted(before.keys() & after.keys())
    removed_keys = sorted(before.keys() - after.keys())
    added_keys = sorted(after.keys() - before.keys())

    difference = ['{']

    for key in same_keys:
        if before[key] == after[key]:
            difference.append(f'{SAME} {key}: {before[key]}')
        else:
            difference.extend([
                f'{ADDED} {key}: {after[key]}',
                f'{REMOVED} {key}: {before[key]}'
            ])

    for key in removed_keys:
        difference.append(f'{REMOVED} {key}: {before[key]}')

    for key in added_keys:
        difference.append(f'{ADDED} {key}: {after[key]}')

    difference.append('}')
    return '\n'.join(difference)
