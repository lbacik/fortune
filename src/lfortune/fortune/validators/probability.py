from typing import Optional, List

from ..config_values import ConfigValues
from ..validator import Validator
from ...abstract.fortune_source import FortuneSource


class Probability(Validator):
    def validate(self,
                 sources: Optional[List[FortuneSource]] = None,
                 config: Optional[ConfigValues] = None
                 ) -> Optional[List[FortuneSource]]:
        total = 0
        if sources is not None:
            for item in sources:
                if item.percentage > 0:
                    total += item.percentage
                    if total > 100:
                        raise Exception('percentage is over 100%!')
        return sources
