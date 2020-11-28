
import argparse


class Arguments:

    path: str = None
    config: str = "~/.config/lfortune/config.ini"


def parse():
    parser = argparse.ArgumentParser(
        epilog='2020 Łukasz Bacik <mail@luka.sh> https://github.com/lbacik/fortune'
    )

    parser.add_argument(
        '-p',
        '--path',
        nargs='?',
        default=Arguments.path,
        help='file to random fortune from (overrides the root_path)'
    )
    parser.add_argument(
        '-c',
        '--config',
        nargs='?',
        default=Arguments.config,
        help='config file to use'
    )
    parser.add_argument(
        '--copy-config',
        nargs='?',
        const=Arguments.config,
        help=f"copy config file. You can provide the dest, the default is {Arguments.config}"
    )
    parser.add_argument(
        '--show-config',
        action='store_true',
        help='show settings and exit'
    )
    parser.add_argument(
        '--show-fortunes',
        action='store_true',
        help='show fortunes'
    )
    parser.add_argument(
        'db',
        nargs='*',
        help='fortunes db (only the first positional argument is used)'
    )

    return parser.parse_args(namespace=Arguments)
