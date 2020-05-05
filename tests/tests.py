from gendiff import engine

file1 = './fixtures/before.json'
file2 = './fixtures/after.json'
result = open('fixtures/expected_result.txt')


def test():
    assert engine.generate_diff(file1, file2) == result.read()
