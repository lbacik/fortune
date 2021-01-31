import os
from typing import Optional, List

from ..config_values import ConfigValues
from ..validator import Validator
from ...abstract.fortune_source import FortuneSource


class Existence(Validator):

    def validate(self,
                 sources: Optional[List[FortuneSource]] = None,
                 config: Optional[ConfigValues] = None
                 ) -> Optional[List[FortuneSource]]:
        result: Optional[List[FortuneSource]] = None
        root_path: str = config.root_path if config is not None else ''
        if sources is not None:
            result = []
            for item in sources:
                if os.path.exists('/'.join([root_path, item.source])):
                    result.append(item)
                else:
                    raise FileNotFoundError(f"ERROR: Cannot find db: {item.source}")

        return result
