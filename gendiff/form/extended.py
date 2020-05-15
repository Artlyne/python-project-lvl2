def generate(difference, depth='  '):
    result = []
    for key, value in sorted(difference.items(), key=lambda x: x[0][2:]):
        # sorts lexicographically by key
        # we need to skip the first two characters [2:] in the key x[0],
        # because they mean the difference
        if isinstance(value, dict):
            subtree = generate(value, depth=depth + '    ')
            result.append(f'{depth}{key}: {{\n'
                          f'{subtree}\n'
                          f'  {depth}}}')
        else:
            result.append(f'{depth}{key}: {value}')

    return '\n'.join(result)


def show(difference):
    return f'{{\n{generate(difference, depth="  ")}\n}}'
