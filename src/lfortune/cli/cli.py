
from ..cli.arguments import parse
from ..fortune.factory import Factory
from ..abstract.fortune_source import FortuneSource


def run():
    args = parse()
    fortune = Factory.create(args.config)
    if args.path:
        result = fortune.get_from_path(args.path)
    elif args.db:
        l = []
        for name in args.db:
            l.append(FortuneSource(name))
        result = fortune.get(l)
    else:
        result = fortune.get()

    print(result, end='')


if __name__ == '__main__':
    run()
