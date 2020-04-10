
from ..abstract.fortune import FortuneAbstract
from .fortune import Fortune
from .indexer import Indexer


class Factory:

    @staticmethod
    def create(config = None) -> FortuneAbstract:
        return Fortune(config, Indexer(Fortune.SEPARATOR))
