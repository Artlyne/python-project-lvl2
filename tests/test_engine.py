from gendiff.engine import generate_diff


json_flat_file1 = './tests/fixtures/test_flat_before.json'
json_flat_file2 = './tests/fixtures/test_flat_after.json'
yaml_flat_file1 = './tests/fixtures/test_flat_before.yaml'
yaml_flat_file2 = './tests/fixtures/test_flat_after.yaml'
flat_result = open('./tests/fixtures/test_flat_result.txt').read()


def test_flat_files():
    assert generate_diff(json_flat_file1, json_flat_file2) == flat_result
    assert generate_diff(yaml_flat_file1, yaml_flat_file2) == flat_result
