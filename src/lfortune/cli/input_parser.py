from typing import List, Optional
from ..abstract.fortune_source import FortuneSource


def input_parse(input_db: Optional[List[str]], prefix: str = '') -> List[FortuneSource]:
    result: List[FortuneSource] = []
    probability: int = 0

    if input_db is not None:
        for string in input_db:
            if type(string) == str and len(string) > 0:
                if string[-1] == '%':
                    probability = int(string[:-1])
                else:
                    path = '/'.join([prefix, string]) if prefix != '' else string
                    item = FortuneSource(path, probability)
                    result.append(item)
                    probability = 0

    return result
