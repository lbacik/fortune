from typing import List, Optional
from ..abstract.fortune_source import FortuneSource


def input_parse(input_db: Optional[List[str]], prefix: str = '') -> List[FortuneSource]:
    result: List[FortuneSource] = []
    probability: int = 0

    if input_db is not None:
        for source in input_db:
            if type(source) == str and len(source) > 0:
                if source[-1] == '%':
                    probability = int(source[:-1])
                else:
                    item = FortuneSource(source, probability)
                    result.append(item)
                    probability = 0

    return result
