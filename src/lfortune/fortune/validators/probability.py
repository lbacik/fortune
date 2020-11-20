from typing import Optional, List
from ..validator import Validator
from ...abstract.fortune_source import FortuneSource


class Probability(Validator):
    def validate(self, list: Optional[List[FortuneSource]] = None) -> List[FortuneSource]:
        total = 0
        for item in list:
            if item.percentage > 0:
                total += item.percentage
                if total > 100:
                    raise Exception('percentage is over 100%!')
        return list
