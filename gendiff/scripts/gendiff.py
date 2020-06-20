#!/usr/bin/env python3
import argparse
from gendiff.engine import generate_diff
from gendiff.parser import parse_args


def main():
    generate_diff(parse_args().first_file,
                  parse_args().second_file,
                  parse_args().format)


if __name__ == '__main__':
    main()
