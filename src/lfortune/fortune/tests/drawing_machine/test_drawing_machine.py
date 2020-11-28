import random
import pytest

from lfortune.abstract.fortune_source import FortuneSource
from lfortune.fortune.drawing_machines.simple import Simple

test_data = [
    ([FortuneSource('foo', 100)], 0),
    ([FortuneSource('foo', 80), FortuneSource('bar', 20)], 0),
    ([FortuneSource('foo', 20), FortuneSource('bar', 80)], 1),
    ([FortuneSource('foo', 90), FortuneSource('bar', 10)], 0),
    ([FortuneSource('foo', 70), FortuneSource('bar', 10), FortuneSource('bar', 20)], 1),
    ([FortuneSource('foo', 76), FortuneSource('bar', 24)], 1),
]


@pytest.fixture(autouse=True)
def randint(monkeypatch):
    monkeypatch.setattr(random, "randint", lambda x, y: 76)


def test_drawing_machine_simple_empty_sources():
    result = Simple().get([])
    assert result is None


@pytest.mark.parametrize("sources, expected_index", test_data)
def test_drawing_machine_simple(sources, expected_index):
    result = Simple().get(sources)
    assert result == sources[expected_index]
