
from abc import ABC
from abc import abstractmethod
from typing import List, Optional
from .fortune_source import FortuneSource


class FortuneAbstract(ABC):

    @abstractmethod
    def get(self, list: Optional[List[FortuneSource]] = None) -> str:
        pass

    @abstractmethod
    def get_from_path(self, path: str) -> str:
        pass
