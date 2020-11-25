from .config_values import ConfigValues
from .validators.existence import Existence
from .validators.probability import Probability
from ..abstract.fortune import FortuneAbstract
from ..fortune.fortune import Fortune
from ..fortune.indexer import Indexer
from ..fortune.config import Config


class Factory:

    # @classmethod
    # def create_config_path(cls, config_file: str = None) -> FortuneAbstract:
    #     config = Config(config_file)
    #     return cls.create(config)

    @classmethod
    def create(cls, config: ConfigValues) -> FortuneAbstract:
        return Fortune(
            config,
            Indexer(Fortune.SEPARATOR),
            [
                Probability(),
                Existence(),
            ]
        )
