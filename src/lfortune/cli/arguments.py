import argparse

from lfortune.fortune.config import Config


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
        help='file/directory to get random fortune from (overrides the root_path, '
             f'it can be also set as {Config.ENVIRONMENT_VAR_FORTUNES_DIR} environment variable)'
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
        help=f'copy config file. You can provide the dest, the default is {Arguments.config}'
    )
    parser.add_argument(
        '--show-config',
        action='store_true',
        help='show settings and exit'
    )
    parser.add_argument(
        '--show-fortunes',
        action='store_true',
        help='show fortunes (only the first positional argument is used)'
    )
    parser.add_argument(
        '--show-fortune-data',
        action='store_true',
        help='show additional information about displayed fortune (file/index)'
    )
    parser.add_argument(
        '--index',
        nargs='?',
        help='index of the fortune in the provided fortune\'s db'
    )
    parser.add_argument(
        'db',
        nargs='*',
        help='''fortunes db(s) - file(s)/directory(ies) (without root_path), 
             optionally prepended with a percentage chance of a hit, e.g:
             lfortune 50%% computers art 40%% tao (in this example art will have 10%%)'''
    )

    return parser.parse_args(namespace=Arguments)
