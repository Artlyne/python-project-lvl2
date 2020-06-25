import argparse
from gendiff import format


def formatter(name):
    if name == format.DEFAULT:
        return format.default
    elif name == format.PLAIN:
        return format.plain
    elif name == format.JSON:
        return format.json
    raise argparse.ArgumentTypeError(f'Unknown formatter: {name}')


def parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default=format.DEFAULT,
        # choices=format.FORMATTERS,
        type=formatter,
    )
    args = parser.parse_args()
    return args
