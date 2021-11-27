from os import path
from .arguments import parse
from .input_parser import input_parse
from .functions import *
from ..fortune.config import Config
from ..fortune.factory import Factory


def run():
    args = parse()

    if args.copy_config:
        copy_config_file(args)
        exit(0)

    config = Config(path.expanduser(args.config))
    config_values = get_config_values(args, config)

    if args.show_config:
        show_config_settings(config_values)
        exit(0)

    if args.show_fortunes:
        show_fortunes(config_values, args.db)
        exit(0)

    fortune = Factory.create(config_values)
    sources = input_parse(args.db, config_values.root_path)

    try:
        result = fortune.get(sources, None if args.index is None else int(args.index))
        print(result.fortune, end='')
        if args.show_fortune_data is True:
            print(f"[{result.file} / {result.index}]")
    except Exception as exception:
        print(exception)


if __name__ == '__main__':
    run()
