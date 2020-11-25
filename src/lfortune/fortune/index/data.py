
from typing import List


class IndexData:

    longest: int = 0
    shortest: int = 0
    indices: List[int]

    def __init__(self):
        self.indices = []
