from abc import ABC, abstractmethod
from typing import Optional, List
from ..abstract.fortune_source import FortuneSource


class DrawingMachine(ABC):

    @abstractmethod
    def get(self, sources: List[FortuneSource]) -> Optional[FortuneSource]:
        pass
