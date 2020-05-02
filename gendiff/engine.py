import json
SAME, ADDED, REMOVED = ' ', '+', '-'


def generate_diff(path_to_file1, path_to_file2):
    file1 = json.load(open(path_to_file1))
    file2 = json.load(open(path_to_file2))

    result = ''
    for key, value in file1.items():
        if key not in file2.keys():
            result += f'{REMOVED} {key}: {value}\n'
            continue

        if value == file2[key]:
            result += f'{SAME} {key}: {value}\n'
        elif value != file2[key]:
            result += f'{ADDED} {key}: {file2[key]}\n'
            result += f'{REMOVED} {key}: {value}\n'

    for key, value in file2.items():
        if key not in file1.keys():
            result += f'{ADDED} {key}: {value}\n'

    print(result)
    return result
