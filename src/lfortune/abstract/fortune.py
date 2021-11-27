
from abc import ABC
from abc import abstractmethod
from typing import List, Optional

from .fortune_data import FortuneData
from .fortune_source import FortuneSource


class FortuneAbstract(ABC):

    @abstractmethod
    def get(self, list: Optional[List[FortuneSource]] = None, index: Optional[int] = None) -> FortuneData:
        pass
