
import os
from typing import List, Optional
from ..abstract.fortune import FortuneAbstract
from ..abstract.fortune_source import FortuneSource
from .indexer import Indexer
from random import randrange
from .config import Config


class Fortune(FortuneAbstract):

    SEPARATOR: str = '%\n'
    config: Config
    indexer: Indexer

    def __init__(self, config: Config, indexer: Indexer):
        self.config = config
        self.indexer = indexer

    def get(self, list: Optional[List[FortuneSource]] = None) -> str:
        path = self.config.fortunes_path()
        if list:
            path = os.path.join(path, list.pop().source)
        return self.get_from_path(path)

    def get_from_path(self, path: str) -> str:
        if os.path.isdir(path):
            return self._get_from_dir(path)
        elif os.path.isfile(path):
            return self._get_from_file(path)
        raise Exception(f"Path {path} is not a file or directory")

    def _get_from_file(self, file: str) -> str:
        index = self.indexer.index(file)
        i = randrange(0, len(index.indices))
        return self._read_fortune(file, index.indices[i])

    def _get_from_dir(self, path: str) -> str:
        files = self._all_files_in_directory(path)
        i = randrange(0, len(files))
        return self._get_from_file(files[i])

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
