import os
from typing import Optional, List

from ..validator import Validator
from ...abstract.fortune_source import FortuneSource


class Existence(Validator):

    def validate(self, list: Optional[List[FortuneSource]] = None) -> List[FortuneSource]:
        result = []
        for item in list:
            if os.path.exists(item.source):
                result.append(item)

        return result
