#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first file')
    parser.add_argument('second file')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
