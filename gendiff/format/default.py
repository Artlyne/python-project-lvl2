def build_difference(difference, depth='  '):
    diff = []
    for key, (status, value) in sorted(difference.items()):
        if status == 'nested':
            subtree = build_difference(value, depth=depth + '    ')
            diff.append(f'{depth}  {key}: {{\n{subtree}\n  {depth}}}')

        elif status == 'same':
            diff.append(f'{depth}  {key}: {value}')

        elif status == 'removed':
            if isinstance(value, dict):
                value = build_subtree(value, depth=depth + '  ')
            diff.append(f'{depth}- {key}: {value}')

        elif status == 'added':
            if isinstance(value, dict):
                value = build_subtree(value, depth=depth + '  ')
            diff.append(f'{depth}+ {key}: {value}')

        elif status == 'changed':
            removed_value = value[0]
            added_value = value[1]
            diff.extend([f'{depth}- {key}: {removed_value}',
                         f'{depth}+ {key}: {added_value}'])

    return '\n'.join(diff)


def build_subtree(dictionary, depth):
    difference = ['{']
    for key, value in dictionary.items():
        difference.append(f'  {depth}{key}: {value}')
    difference.append(f'{depth}}}')
    return '\n'.join(difference)


def format(difference):
    diff = build_difference(difference)
    return f'{{\n{diff}\n}}'
