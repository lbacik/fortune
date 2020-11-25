from lfortune.fortune.config import Config
from lfortune.fortune.config_values import ConfigValues
from .arguments import parse
from .input_parser import input_parse
from ..fortune.factory import Factory


def get_config_values(args, config: Config) -> ConfigValues:
    if args.path:
        root_path = args.path
    else:
        root_path = config.fortunes_path()

    return ConfigValues(root_path)


def run():
    args = parse()
    config = Config(args.config)
    config_values = get_config_values(args, config)

    fortune = Factory.create(config_values)
    sources = input_parse(args.db, config_values.root_path)

    result = fortune.get(sources)
    print(result, end='')


if __name__ == '__main__':
    run()
