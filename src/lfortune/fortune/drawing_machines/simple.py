import random
from typing import Optional, List
from ...abstract.fortune_source import FortuneSource
from ..drawing_machines import DrawingMachine


class Simple(DrawingMachine):

    def get(self, sources: Optional[List[FortuneSource]] = None) -> FortuneSource:
        result = None
        number = random.randint(0, 100)
        progress = 0
        for item in sources:
            progress += item.percentage
            if number < progress:
                result = item
                break

        return result
