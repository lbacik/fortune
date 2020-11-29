
import os
from typing import List, Optional

from .config_values import ConfigValues
from .drawing_machine import DrawingMachine
from ..abstract.fortune import FortuneAbstract
from ..abstract.fortune_source import FortuneSource
from .indexer import Indexer
from random import randrange
from logging import Logger


class Fortune(FortuneAbstract):

    SEPARATOR: str = '%\n'
    # logger: Logger
    # config: ConfigValues
    # indexer: Indexer
    # drawing_machine: DrawingMachine

    def __init__(self,
                 logger: Optional[Logger],
                 config: ConfigValues,
                 indexer: Indexer,
                 validators: list,
                 drawing_machine: DrawingMachine = None
                 ):
        self.logger = logger
        self.config = config
        self.indexer = indexer
        self.validators = validators
        self.drawing_machine = drawing_machine

    def get(self, sources: Optional[List[FortuneSource]] = None) -> str:
        validated_list = self._validate(sources)
        source = self._chose_source(validated_list)
        if source is None:
            raise ValueError('ERROR: Source is empty :(')
        fortune_str = self.get_from_path(source.source)
        return fortune_str

    def get_from_path(self, path: str) -> str:
        if os.path.isdir(path):
            return self._get_from_dir(path)
        elif os.path.isfile(path):
            return self._get_from_file(path)
        raise Exception(f"Path {path} is not a file or directory")

    def _chose_source(self, sources):
        if sources is None or sources == []:
            result = FortuneSource(self.config.root_path)
        elif self.drawing_machine is not None:
            result = self.drawing_machine.get(sources)
        else:
            raise NotImplementedError()
        return result

    def _validate(self, sources: Optional[List[FortuneSource]] = None) -> List[FortuneSource]:
        result = sources
        for validator in self.validators:
            result = validator.validate(result)
        return result

    def _chose_path(self, sources: Optional[List[FortuneSource]] = None):
        result = None
        if sources:
            result = sources[0].source

        if not result:
            result = self.config.root_path

        return result

    def _get_from_file(self, file: str) -> str:
        index = self.indexer.index(file)
        i = randrange(0, len(index.indices))
        return self._read_fortune(file, index.indices[i])

    def _get_from_dir(self, path: str) -> str:
        files = self._all_files_in_directory(path)
        if len(files) > 0:
            i = randrange(0, len(files))
            return self._get_from_file(files[i])
        return ''

    def _all_files_in_directory(self, path: str) -> List[str]:
        list_of_files = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            for file in filenames:
                if self._file_is_fortune_db(file):
                    list_of_files.append(os.path.join(dirpath, file))
        return list_of_files

    def _file_is_fortune_db(self, file: str) -> bool:
        result = True
        filename, file_extension = os.path.splitext(file)
        if file_extension:
            result = False
        return result

    def _read_fortune(self, file: str, i: int) -> str:
        result: str = ''
        file = open(file, 'r')
        file.seek(i)
        fortune_end = False
        while not fortune_end:
            line = file.readline()
            if line and line != self.SEPARATOR:
                result += line
            else:
                fortune_end = True
        return result

