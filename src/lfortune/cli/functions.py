from os import makedirs, path, listdir
from shutil import copyfile
from ..fortune.config_values import ConfigValues
from ..fortune.config import Config


def get_config_values(args, config: Config) -> ConfigValues:
    if args.path:
        root_path = args.path
    else:
        root_path = config.fortunes_path()

    return ConfigValues(root_path)


def copy_config_file(args):
    src = 'config.ini'
    dest = path.expanduser(args.copy_config)
    makedirs(path.dirname(dest), exist_ok=True)
    copyfile(src, dest)
    print(f'config copied to {dest}')


def show_config_settings(config: ConfigValues):
    print(config)


def show_fortunes(config: ConfigValues, db):
    fortune_path = config.root_path
    if db and db[0].find('..') == -1:
        fortune_path += f'/{db[0]}'

    print(f'PATH: {fortune_path}')

    if path.isdir(fortune_path):
        for filename in listdir(fortune_path):
            if filename[0] == '.':
                continue
            current_file = f'{fortune_path}/{filename}'
            if path.isfile(current_file):
                filename, file_extension = path.splitext(filename)
                if not file_extension:
                    print(filename)
            elif path.isdir(current_file):
                print(f'{filename}/')

    elif path.isfile(fortune_path):
        file = open(fortune_path, mode='r')
        print(file.read())
        file.close()
