from abc import ABC, abstractmethod
from typing import Optional, List
from ..abstract.fortune_source import FortuneSource


class DrawingMachine(ABC):

    @abstractmethod
    def get(self, sources: Optional[List[FortuneSource]] = None) -> FortuneSource:
        pass
