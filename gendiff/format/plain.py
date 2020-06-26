from gendiff import diff


def build_difference(raw_diff, path=''):

    lines = []

    for key, (status, value) in sorted(raw_diff.items()):

        prefix = f"Property '{path}{key}' was"

        if status == diff.NESTED:
            lines.extend(build_difference(value, path=f'{path}{key}.'))

        elif status == diff.REMOVED:
            lines.append(f"{prefix} removed")

        elif status == diff.ADDED:
            if isinstance(value, dict):
                value = 'complex value'
            lines.append(f"{prefix} added with value: '{value}'")

        elif status == diff.CHANGED:
            old, new = value
            lines.append(f"{prefix} changed. From '{old}' to '{new}'")

    return lines


def format(raw_diff):
    difference = build_difference(raw_diff)
    return '\n'.join(difference)
