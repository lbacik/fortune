import pytest
from lfortune.abstract.fortune_source import FortuneSource
from lfortune.fortune.validators.probability import Probability


def test_empty_list():
    probability = Probability()
    result = probability.validate()
    assert result is None


def test_below_the_limit():
    probability = Probability()
    sources = [
        FortuneSource('a', 20),
        FortuneSource('b', 20),
        FortuneSource('c', 20),
    ]
    result = probability.validate(sources)
    assert result == sources


def test_above_the_limit():
    probability = Probability()
    sources = [
        FortuneSource('a', 40),
        FortuneSource('b', 70),
    ]
    with pytest.raises(Exception):
        probability.validate(sources)
