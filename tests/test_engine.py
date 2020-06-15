from gendiff.engine import generate_diff

json_flat_file1 = './tests/fixtures/test_flat_before.json'
json_flat_file2 = './tests/fixtures/test_flat_after.json'
yaml_flat_file1 = './tests/fixtures/test_flat_before.yaml'
yaml_flat_file2 = './tests/fixtures/test_flat_after.yaml'
extended_flat_result = open(
    './tests/fixtures/test_extended_flat_result.txt').read()
plain_flat_result = open('./tests/fixtures/test_plain_flat_result.txt').read()
json_flat_result = open('./tests/fixtures/test_json_flat_result.json').read()


def test_flat_files():
    assert generate_diff(json_flat_file1, json_flat_file2,
                         'extended') == extended_flat_result
    assert generate_diff(yaml_flat_file1, yaml_flat_file2,
                         'extended') == extended_flat_result
    assert generate_diff(json_flat_file1, json_flat_file2,
                         'plain') == plain_flat_result
    assert generate_diff(yaml_flat_file1, yaml_flat_file2,
                         'plain') == plain_flat_result
    assert generate_diff(json_flat_file1, json_flat_file2,
                         'json') == json_flat_result
    assert generate_diff(yaml_flat_file1, yaml_flat_file2,
                         'json') == json_flat_result


json_nested_file1 = './tests/fixtures/test_nested_before.json'
json_nested_file2 = './tests/fixtures/test_nested_after.json'
yaml_nested_file1 = './tests/fixtures/test_nested_before.yaml'
yaml_nested_file2 = './tests/fixtures/test_nested_after.yaml'
extended_nested_result = open(
    './tests/fixtures/test_extended_nested_result.txt').read()
plain_nested_result = open(
    './tests/fixtures/test_plain_nested_result.txt').read()
json_nested_result = open(
    './tests/fixtures/test_json_nested_result.json').read()


def test_nested_files():
    assert generate_diff(json_nested_file1, json_nested_file2,
                         'extended') == extended_nested_result
    assert generate_diff(yaml_nested_file1, yaml_nested_file2,
                         'extended') == extended_nested_result
    assert generate_diff(json_nested_file1, json_nested_file2,
                         'plain') == plain_nested_result
    assert generate_diff(yaml_nested_file1, yaml_nested_file2,
                         'plain') == plain_nested_result
    assert generate_diff(json_nested_file1, json_nested_file2,
                         'json') == json_nested_result
    assert generate_diff(yaml_nested_file1, yaml_nested_file2,
                         'json') == json_nested_result
