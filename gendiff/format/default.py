from gendiff import diff

PREFIXES = (SAME, REMOVED, ADDED) = (' ', '-', '+')


def build_difference(raw_diff, depth='  '):

    lines = []

    for key, (status, value) in sorted(raw_diff.items()):

        if status == diff.NESTED:
            subtree = '\n'.join(build_difference(value, depth=f'{depth}    '))
            lines.extend([f'{depth}  {key}: {{', subtree, f'  {depth}}}'])

        elif status == diff.SAME:
            lines.append(make_line(depth, SAME, key, value))

        elif status == diff.REMOVED:
            lines.append(make_line(depth, REMOVED, key, value))

        elif status == diff.ADDED:
            lines.append(make_line(depth, ADDED, key, value))

        elif status == diff.CHANGED:
            old, new = value
            lines.extend(
                [
                    make_line(depth, REMOVED, key, old),
                    make_line(depth, ADDED, key, new)
                ]
            )

    return lines


def make_line(depth, prefix, key, value):
    if isinstance(value, dict):
        value = build_subtree(value, depth=f'{depth}  ')
    return f'{depth}{prefix} {key}: {value}'


def build_subtree(subtree, depth):
    difference = ['{']
    for key, value in subtree.items():
        difference.append(f'  {depth}{key}: {value}')
    difference.append(f'{depth}}}')
    return '\n'.join(difference)


def format(raw_diff):
    difference = '\n'.join(build_difference(raw_diff))
    return f'{{\n{difference}\n}}'
