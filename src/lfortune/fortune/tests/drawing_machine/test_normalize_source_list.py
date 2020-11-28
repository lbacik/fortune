import pytest

from lfortune.abstract.fortune_source import FortuneSource
from lfortune.fortune.drawing_machines.normalize_source_list import normalize_percentage


test_data = [
    ([], []),
    ([
        FortuneSource('foo', 0)
     ],
     [
        FortuneSource('foo', 100)
     ]),
    ([
        FortuneSource('foo', 0),
        FortuneSource('bar', 90),

     ],
     [
        FortuneSource('bar', 90),
        FortuneSource('foo', 10),
     ]),
    ([
        FortuneSource('foo', 10),
        FortuneSource('bar', 0),
        FortuneSource('baz', 0),
     ],
     [
        FortuneSource('foo', 10),
        FortuneSource('bar', 45),
        FortuneSource('baz', 45),
     ]),
    ([
         FortuneSource('foo', 33),
         FortuneSource('bar', 0),
         FortuneSource('baz', 0),
     ],
     [
         FortuneSource('foo', 33),
         FortuneSource('bar', 34),
         FortuneSource('baz', 34),
     ]),
]


@pytest.mark.parametrize("sources, expected", test_data)
def test_normalize_percentage(sources, expected):
    result = normalize_percentage(sources)
    assert expected == result
