import json
import yaml
import os


SAME, REMOVED, ADDED, CHANGED, NESTED = (
    'same', 'removed', 'added', 'changed', 'nested')


def load(filename):

    _, ext = os.path.splitext(filename)
    type = ext.lower()

    if type == '.json':
        return json.load(open(filename))
    elif type == '.yaml' or type == '.yml':
        return yaml.load(open(filename), Loader=yaml.SafeLoader)
    else:
        raise ValueError(f'Unknown file type: {filename}')


def compare(old_data, new_data):

    same_keys = old_data.keys() & new_data.keys()
    removed_keys = old_data.keys() - new_data.keys()
    added_keys = new_data.keys() - old_data.keys()

    difference = {}

    for key in same_keys:

        old_value = old_data[key]
        new_value = new_data[key]

        if isinstance(old_value, dict) and isinstance(new_value, dict):
            difference[key] = (NESTED, compare(old_value, new_value))
        elif old_value == new_value:
            difference[key] = (SAME, old_value)
        else:
            difference[key] = (CHANGED, (old_value, new_value))

    for key in removed_keys:
        value = old_data[key]
        difference[key] = (REMOVED, value)

    for key in added_keys:
        value = new_data[key]
        difference[key] = (ADDED, value)

    return difference


def generate_diff(old_config, new_config, format):
    old_data = load(old_config)
    new_data = load(new_config)
    difference = format(compare(old_data, new_data))
    return difference
