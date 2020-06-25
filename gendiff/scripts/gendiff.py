#!/usr/bin/env python3
from gendiff.engine import generate_diff
from gendiff.cli import parse_args


def main():
    print(
        generate_diff(
            parse_args().first_file,
            parse_args().second_file,
            parse_args().format
        )
    )


if __name__ == '__main__':
    main()
