
from typing import List, Optional
from ..abstract.fortune import FortuneAbstract
from ..abstract.fortune_source import FortuneSource
from .indexer import Indexer
from random import randrange


class Fortune(FortuneAbstract):

    SEPARATOR: str = '%\n'
    indexer: Indexer

    def __init__(self, config, indexer: Indexer):
        self.indexer = indexer

    def get_from_dir(self, path: str) -> str:
        pass

    def get_from_file_list(self, list: List[str]) -> str:
        pass

    def get_from_file(self, file: str) -> str:
        index = self.indexer.index(file)
        i = randrange(0, len(index.indices))
        return self._read_fortune(file, index.indices[i])

    def get(self, list: Optional[List[FortuneSource]]) -> str:
        pass

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
