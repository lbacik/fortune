

class FortuneSource:

    source: str = ''
    probability: int = -1

    def __init__(self, source: str, probability: int = -1):
        self.source = source
        self.probability = probability
