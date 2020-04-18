
from ..abstract.fortune import FortuneAbstract
from .fortune import Fortune
from .indexer import Indexer
from .config import Config

class Factory:

    @staticmethod
    def create(config_file: str = None) -> FortuneAbstract:
        config = Config(config_file)
        return Fortune(config, Indexer(Fortune.SEPARATOR))
