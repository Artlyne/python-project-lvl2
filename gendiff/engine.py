import json
import yaml
from gendiff.form import extended, plain, json_format

SAME, REMOVED, ADDED, CHANGED, NESTED = \
    'same', 'removed', 'added', 'changed', 'nested'

FORMATS = {'extended': extended.show_difference,
           'plain': plain.show_difference,
           'json': json_format.show_difference}


def load_file(file):
    if file.endswith('.json'):
        return json.load(open(file))
    if file.endswith('.yaml'):
        return yaml.load(open(file), Loader=yaml.FullLoader)


def diff(first_dict, second_dict):
    same_keys = first_dict.keys() & second_dict.keys()
    removed_keys = first_dict.keys() - second_dict.keys()
    added_keys = second_dict.keys() - first_dict.keys()

    difference = {}

    for key in same_keys:
        value_of_first = first_dict[key]
        value_of_second = second_dict[key]

        if isinstance(value_of_first, dict) and \
                isinstance(value_of_second, dict):
            difference[key] = (NESTED, diff(value_of_first, value_of_second))

        elif value_of_first == value_of_second:
            difference[key] = (SAME, value_of_first)

        else:
            difference[key] = (CHANGED, (value_of_first, value_of_second))

    for key in removed_keys:
        value = first_dict[key]
        difference[key] = (REMOVED, value)

    for key in added_keys:
        value = second_dict[key]
        difference[key] = (ADDED, value)

    return difference


def generate_diff(first_file, second_file, form):
    first_dict = load_file(first_file)
    second_dict = load_file(second_file)
    difference = FORMATS[form](diff(first_dict, second_dict))
    print(difference)
    return difference
