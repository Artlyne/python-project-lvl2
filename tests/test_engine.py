from gendiff.engine import generate_diff

json_file_before = './tests/fixtures/test_before.json'
json_file_after = './tests/fixtures/test_after.json'
yaml_file_before = './tests/fixtures/test_before.yaml'
yaml_file_after = './tests/fixtures/test_after.yaml'
result = open('./tests/fixtures/test_expected_result.txt').read()


def test_flat_files():
    assert generate_diff(json_file_before, json_file_after) == result
    assert generate_diff(yaml_file_before, yaml_file_after) == result
