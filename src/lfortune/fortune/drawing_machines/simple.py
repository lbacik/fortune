import random
from typing import Optional, List

from .normalize_source_list import normalize_percentage
from ...abstract.fortune_source import FortuneSource
from ..drawing_machine import DrawingMachine


class Simple(DrawingMachine):

    def get(self, sources: List[FortuneSource]) -> Optional[FortuneSource]:
        sources_copy: List[FortuneSource] = normalize_percentage(sources)
        result: Optional[FortuneSource] = None
        number: int = random.randint(0, 100)
        progress: int = 0

        for item in sources_copy:
            progress += item.percentage
            if number < progress:
                result = item
                break

        return result
