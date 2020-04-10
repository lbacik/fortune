
from abc import ABC
from abc import abstractmethod
from typing import List, Optional
from .fortune_source import FortuneSource


class FortuneAbstract(ABC):

    @abstractmethod
    def get_from_dir(self, path: str) -> str:
        pass

    @abstractmethod
    def get_from_file_list(self, list: List[str]) -> str:
        pass

    @abstractmethod
    def get_from_file(self, file: str) -> str:
        pass

    @abstractmethod
    def get(self, list: Optional[List[FortuneSource]]) -> str:
        pass
