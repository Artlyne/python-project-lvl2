import json


def show_difference(difference):
    return json.dumps(difference, sort_keys=True, indent=2)
