import pytest
from unittest.mock import patch

from lfortune.abstract.fortune_data import FortuneData
from lfortune.abstract.fortune_source import FortuneSource
from lfortune.fortune.config_values import ConfigValues
from lfortune.fortune.fortune import Fortune
from lfortune.fortune.indexer import Indexer


@pytest.fixture
def fortune_without_drawing_machine():
    config = ConfigValues('/')
    indexer = Indexer(Fortune.SEPARATOR)
    validators = []
    return Fortune(None, config, indexer, validators)


@pytest.fixture
def fortune():
    config = ConfigValues('/')
    indexer = Indexer(Fortune.SEPARATOR)
    validators = []

    with patch('lfortune.fortune.drawing_machine.DrawingMachine') as MockClass:
        drawing_machine = MockClass.return_value
        drawing_machine.get.return_value = FortuneSource('test', 100)

    return Fortune(None, config, indexer, validators, drawing_machine)


def test_get(fortune_without_drawing_machine, fs):
    fs.create_file('test')
    result = fortune_without_drawing_machine.get()
    assert isinstance(result, FortuneData)
    assert result.fortune == ''
    assert result.file == 'test'
    assert result.index == 0


def test_get_0(fortune_without_drawing_machine, fs):
    fs.create_file('test')
    result = fortune_without_drawing_machine.get([])
    assert result.fortune == ''
    assert result.file == 'test'
    assert result.index == 0


def test_get_2(fortune_without_drawing_machine):
    with pytest.raises(NotImplementedError):
        fortune_without_drawing_machine.get([FortuneSource('', 0)])


def test_get_3(fortune, fs):
    fs.create_file('test')
    result = fortune.get([FortuneSource('test', 100)])
    assert result.fortune == ''
    assert result.file == 'test'
    assert result.index == 0


def test_get_4(fortune, fs):
    fs.create_dir('test')
    with pytest.raises(AttributeError):
        fortune.get([FortuneSource('test', 100)])


def test_get_5(fortune, fs):
    file_contents = "fortune_1"
    fs.create_file('test', contents=file_contents)
    fs.create_file('test2')

    result = fortune.get([
        FortuneSource('test', 100),
        FortuneSource('test2', 0),
    ])

    assert result.fortune == file_contents
    assert result.file == 'test'
    assert result.index == 0


def test_get_6(fortune, fs):
    file_contents = "fortune_1"
    fs.create_file('test/foo', contents=file_contents)
    fs.create_file('test2')

    result = fortune.get([
        FortuneSource('test', 100),
        FortuneSource('test2', 0),
    ])

    assert result.fortune == file_contents
    assert result.file == 'test/foo'
    assert result.index == 0
