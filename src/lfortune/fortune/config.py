
import os
from configparser import ConfigParser
from typing import Optional


class Config:

    SECTION_FORTUNES = 'fortunes'
    ENVIRONMENT_VAR_FORTUNES_DIR = 'FORTUNES'

    parser: ConfigParser

    def __init__(self, config_file: Optional[str]):
        self.parser = ConfigParser()
        if config_file:
            self.parser.read(config_file)

    def fortunes_path(self) -> str:
        if self.ENVIRONMENT_VAR_FORTUNES_DIR in os.environ:
            result = os.environ.get(self.ENVIRONMENT_VAR_FORTUNES_DIR)
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
