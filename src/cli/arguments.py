
import argparse


class Arguments:

    path: str = None
    config: str = 'config.ini'


def parse():
    parser = argparse.ArgumentParser(
        epilog='2020 Łukasz Bacik <mail@luka.sh> https://github.com/lbacik'
    )

    parser.add_argument(
        '-p',
        '--path',
        nargs='?',
        default=Arguments.path,
        help='file to random fortune from'
    )
    parser.add_argument(
        '-c',
        '--config',
        nargs='?',
        default=Arguments.config,
        help='config file'
    )
    parser.add_argument(
        'db',
        nargs='*',
        help='fortunes db'
    )

    return parser.parse_args(namespace=Arguments)
