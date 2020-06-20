import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='extended',
                        choices=['extended', 'plain', 'json'])
    args = parser.parse_args()
    return args
