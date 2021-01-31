from abc import ABC, abstractmethod
from typing import Optional, List

from .config_values import ConfigValues
from ..abstract.fortune_source import FortuneSource


class Validator(ABC):

    @abstractmethod
    def validate(self,
                 list: Optional[List[FortuneSource]] = None,
                 config: Optional[ConfigValues] = None
                 ) -> List[FortuneSource]:
        pass
