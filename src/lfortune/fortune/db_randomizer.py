from typing import List, Optional
from ..abstract.fortune_source import FortuneSource
import random


def pick_db(source_list: List[FortuneSource]) -> Optional[str]:
    result = None
    number = random.randint(0,100)
    progress = 0
    for item in source_list:
        progress += item.percentage
        if number < progress:
            result = item.source
            break

    return result
