
from ..abstract.fortune import FortuneAbstract
from ..fortune.fortune import Fortune
from ..fortune.indexer import Indexer
from ..fortune.config import Config

class Factory:

    @staticmethod
    def create(config_file: str = None) -> FortuneAbstract:
        config = Config(config_file)
        return Fortune(config, Indexer(Fortune.SEPARATOR))
