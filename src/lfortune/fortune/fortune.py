
import os
from typing import List, Optional

from .config_values import ConfigValues
from .drawing_machine import DrawingMachine
from ..abstract.fortune import FortuneAbstract
from ..abstract.fortune_data import FortuneData
from ..abstract.fortune_source import FortuneSource
from .indexer import Indexer
from random import randrange
from logging import Logger


class Fortune(FortuneAbstract):

    SEPARATOR: str = '%\n'

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

    def get(self, sources: Optional[List[FortuneSource]] = None, index: Optional[int] = None) -> FortuneData:
        validated_list = self._validate(sources)
        source = self._chose_source(validated_list)
        if source is None:
            raise ValueError('ERROR: Source is empty :(')
        result_with_full_path_to_source: FortuneData = self._get_from_source(source.source, index)

        return self._remove_root_path_from_source(result_with_full_path_to_source)

    def _remove_root_path_from_source(self, fortune_data: FortuneData) -> FortuneData:
        source = fortune_data.file
        source = source.replace(self.config.root_path, '', 1)
        if source[0] == '/':
            source = source[1:]
        return FortuneData(
            fortune_data.fortune,
            source,
            fortune_data.index
        )

    def _get_from_source(self, source: str, index: Optional[int] = None) -> FortuneData:
        full_path: str = self.config.root_path
        if source:
            if full_path[-1] == '/':
                full_path += source
            else:
                full_path += f"/{source}"

        if os.path.isdir(full_path):
            return self._get_from_dir(full_path)
        elif os.path.isfile(full_path):
            return self._get_from_file(full_path, index)
        raise Exception(f"Cannot find db: {source}")

    def _chose_source(self, sources):
        if sources is None or sources == []:
            result = FortuneSource('')
        elif self.drawing_machine is not None:
            result = self.drawing_machine.get(sources)
        else:
            raise NotImplementedError()
        return result

    def _validate(self, sources: Optional[List[FortuneSource]] = None) -> List[FortuneSource]:
        result = sources
        for validator in self.validators:
            result = validator.validate(result, self.config)
        return result

    def _chose_path(self, sources: Optional[List[FortuneSource]] = None):
        result = None
        if sources:
            result = sources[0].source

        if not result:
            result = self.config.root_path

        return result

    def _get_from_file(self, file: str, index_requested: Optional[int] = None) -> FortuneData:
        i = index_requested
        index = self.indexer.index(file)
        if i is None:
            i = randrange(0, len(index.indices))
        fortune: str = self._read_fortune(file, index.indices[i])
        return FortuneData(fortune, file, i)

    def _get_from_dir(self, path: str) -> FortuneData:
        files = self._all_files_in_directory(path)
        if len(files) > 0:
            i = randrange(0, len(files))
            return self._get_from_file(files[i])
        raise AttributeError('Cannot find any fortunes dbs in provided directory')

    def _all_files_in_directory(self, path: str) -> List[str]:
        list_of_files = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            for file in filenames:
                if self._file_is_fortune_db(file):
                    list_of_files.append(os.path.join(dirpath, file))
        return list_of_files

    def _file_is_fortune_db(self, file: str) -> bool:
        """FIXME: probably it should ignore only 'indices' files (right now it also will ignore files like debian.pl)"""
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
