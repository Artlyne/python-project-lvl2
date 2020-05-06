"""File loader for JSON and YAML files"""
import json
import yaml


def load(file):
    """Deserialize JSON or YAML file to a Python object.

    Parameters:
        file (str): file or path file

    Returns:
        dict: deserialized JSON or YAML file
    """
    if file.endswith('.json'):
        return json.load(open(file))
    if file.endswith('.yaml'):
        return yaml.load(open(file), Loader=yaml.FullLoader)
