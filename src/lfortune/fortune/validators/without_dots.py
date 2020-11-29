import os
from typing import Optional, List

from ..validator import Validator
from ...abstract.fortune_source import FortuneSource


class WithoutDots(Validator):

    def validate(self, sources: Optional[List[FortuneSource]] = None) -> Optional[List[FortuneSource]]:
        result: Optional[List[FortuneSource]] = None
        if sources is not None:
            result = []
            for item in sources:
                if item.source.find('.') == -1:
                    result.append(item)

        return result
