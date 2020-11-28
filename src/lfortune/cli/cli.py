from os import makedirs, path
from shutil import copyfile
from .arguments import parse
from .input_parser import input_parse
from ..fortune.config import Config
from ..fortune.config_values import ConfigValues
from ..fortune.factory import Factory


def get_config_values(args, config: Config) -> ConfigValues:
    if args.path:
        root_path = args.path
    else:
        root_path = config.fortunes_path()

    return ConfigValues(root_path)


def run():
    args = parse()

    if args.copy_config:
        copy_config_file(args)
        exit(0)

    config = Config(path.expanduser(args.config))
    config_values = get_config_values(args, config)

    fortune = Factory.create(config_values)
    sources = input_parse(args.db, config_values.root_path)

    result = fortune.get(sources)
    print(result, end='')


def copy_config_file(args):
    src = 'config.ini'
    dest = path.expanduser(args.copy_config)
    makedirs(path.dirname(dest), exist_ok=True)
    copyfile(src, dest)


if __name__ == '__main__':
    run()
