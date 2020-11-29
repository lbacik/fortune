from math import ceil
from typing import Optional, List
from lfortune.abstract.fortune_source import FortuneSource


def normalize_percentage(sources: List[FortuneSource]) -> List[FortuneSource]:
    percentage: int = 0
    sources_without_percentage: List[FortuneSource] = []
    sources_copy: List[FortuneSource] = []

    for source in sources:
        if source.percentage > 0:
            percentage += source.percentage
            sources_copy.append(source)
        else:
            sources_without_percentage.append(source)

    if len(sources_without_percentage) > 0:
        per_source = int(ceil((100 - percentage) / len(sources_without_percentage)))
        for s in sources_without_percentage:
            sources_copy.append(FortuneSource(s.source, per_source))

    return sources_copy
