import os
from typing import Optional, List

from ..config_values import ConfigValues
from ..validator import Validator
from ...abstract.fortune_source import FortuneSource


class WithoutDots(Validator):

    def validate(self,
                 sources: Optional[List[FortuneSource]] = None,
                 config: Optional[ConfigValues] = None
                 ) -> Optional[List[FortuneSource]]:
        result: Optional[List[FortuneSource]] = None
        if sources is not None:
            result = []
            for item in sources:
                if item.source.find('..') == -1:
                    result.append(item)
                else:
                    raise AttributeError('ERROR: Two dots in db name are not allowed')

        return result
