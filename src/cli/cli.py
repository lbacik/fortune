
from .arguments import parse
from ..fortune.factory import Factory


def run():
    result = ''
    fortune = Factory.create()
    args = parse()
    if args.file:
        result = fortune.get_from_file(args.file)
    print(result, end='')


if __name__ == '__main__':
    run()
