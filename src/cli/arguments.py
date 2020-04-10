
import argparse


class Arguments():
    file: str = None

def parse():
    parser = argparse.ArgumentParser(
        epilog='2020 Łukasz Bacik <mail@luka.sh> https://github.com/lbacik'
    )

    parser.add_argument(
        '-f',
        '--file',
        nargs='?',
        default=Arguments.file,
        help='file to random fortune from'
    )

    return parser.parse_args(namespace=Arguments)
