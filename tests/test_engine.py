from gendiff.engine import generate_diff


json_flat_file1 = './tests/fixtures/test_flat_before.json'
json_flat_file2 = './tests/fixtures/test_flat_after.json'
yaml_flat_file1 = './tests/fixtures/test_flat_before.yaml'
yaml_flat_file2 = './tests/fixtures/test_flat_after.yaml'
flat_result = open('./tests/fixtures/test_flat_result.txt').read()


def test_flat_files():
    assert generate_diff(json_flat_file1, json_flat_file2) == flat_result
    assert generate_diff(yaml_flat_file1, yaml_flat_file2) == flat_result


json_nested_file1 = './tests/fixtures/test_nested_before.json'
json_nested_file2 = './tests/fixtures/test_nested_after.json'
yaml_nested_file1 = './tests/fixtures/test_nested_before.yaml'
yaml_nested_file2 = './tests/fixtures/test_nested_after.yaml'
nested_result = open('./tests/fixtures/test_nested_result.txt').read()


def test_nested_files():
    assert generate_diff(json_nested_file1, json_nested_file2) == nested_result
    assert generate_diff(yaml_nested_file1, yaml_nested_file2) == nested_result
