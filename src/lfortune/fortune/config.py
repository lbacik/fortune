
import os
from configparser import ConfigParser


class Config:

    SECTION_FORTUNES = 'fortunes'
    ENVITONMENT_VAR_FORTUNES_DIR = 'FORTUNES'

    parser: ConfigParser

    def __init__(self, config_file: str):
        self.parser = ConfigParser()
        if config_file:
            self.parser.read(config_file)

    def fortunes_path(self) -> str:
        if self.ENVITONMENT_VAR_FORTUNES_DIR in os.environ:
            result = os.environ.get(self.ENVITONMENT_VAR_FORTUNES_DIR)
        else:
            try:
                result = self.parser[self.SECTION_FORTUNES]['root']
            except KeyError:
                result = self._default_fortunes_path()
        return result

    @staticmethod
    def _default_fortunes_path() -> str:
        path = os.path.abspath(__file__)
        path = os.path.abspath(os.path.dirname(path) + '/../data')
        return path
