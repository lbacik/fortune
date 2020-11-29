from logging import Logger
from typing import Optional

from .config_values import ConfigValues
from .drawing_machines.simple import Simple
from .validators.existence import Existence
from .validators.probability import Probability
from .validators.without_dots import WithoutDots
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
    def create(cls, config: ConfigValues, logger: Optional[Logger] = None) -> FortuneAbstract:
        return Fortune(
            logger,
            config,
            Indexer(Fortune.SEPARATOR),
            [
                Probability(),
                Existence(),
                WithoutDots(),
            ],
            Simple()
        )
