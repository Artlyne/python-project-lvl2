import json


def format(difference):
    return json.dumps(difference, sort_keys=True, indent=2)
