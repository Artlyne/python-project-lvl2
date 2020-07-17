from gendiff.diff import generate_diff
from gendiff import format
import json
import pytest
import os


PATH = './testsgit/fixtures/'
OLD_CONFIG = f'{PATH}test_old_config.json'
NEW_CONFIG = f'{PATH}test_new_config.json'

test_cases_diff = [
    (
        generate_diff(OLD_CONFIG, NEW_CONFIG, format.default),
        f'{PATH}test_result_default.txt'
    ),
    (
        generate_diff(OLD_CONFIG, NEW_CONFIG, format.plain),
        f'{PATH}test_result_plain.txt'
    ),
    (
        generate_diff(OLD_CONFIG, NEW_CONFIG, format.json),
        f'{PATH}test_result_json.json'
    )
]


@pytest.mark.parametrize('test_input, expected_result', test_cases_diff)
def test_generate_diff(test_input, expected_result):
    _, ext = os.path.splitext(expected_result)
    if ext == '.json':
        assert json.loads(test_input) == json.loads(
            open(expected_result).read())
    else:
        assert test_input == open(expected_result).read()
