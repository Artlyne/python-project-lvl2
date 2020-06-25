def build_difference(difference, path=''):
    diff = []
    for key, (status, value) in sorted(difference.items()):
        if status == 'nested':
            diff.append(build_difference(value, path=path + f'{key}.'))

        elif status == 'removed':
            diff.append(f"Property '{path}{key}' was removed")

        elif status == 'added':
            if isinstance(value, dict):
                value = 'complex value'
            diff.append(f"Property '{path}{key}' was added with value: "
                        f"'{value}'")

        elif status == 'changed':
            removed_value = value[0]
            added_value = value[1]
            diff.append(f"Property '{path}{key}' was changed. "
                        f"From '{removed_value}' to '{added_value}'")

    return '\n'.join(diff)


def format(difference):
    diff = build_difference(difference)
    return diff
