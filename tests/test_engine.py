import pytest
from gendiff import engine

file1 = './tests/fixtures/test_before.json'
file2 = './tests/fixtures/test_after.json'
result = open('./tests/fixtures/test_expected_result.txt')


def test():
    assert engine.generate_diff(file1, file2) == result.read()
