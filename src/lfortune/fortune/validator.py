from abc import ABC, abstractmethod
from typing import Optional, List

from ..abstract.fortune_source import FortuneSource


class Validator(ABC):

    @abstractmethod
    def validate(self, list: Optional[List[FortuneSource]] = None) -> List[FortuneSource]:
        pass
