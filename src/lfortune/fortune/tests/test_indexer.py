
import pytest

from ..indexer import Indexer
from ..fortune import Fortune


def test_index_file_not_exists(fs):
    with pytest.raises(FileNotFoundError):
        indexer = Indexer(Fortune.SEPARATOR)
        indexer.index('test')


def test_index_file_empty(fs):
    fs.create_file('test')
    indexer = Indexer(Fortune.SEPARATOR)
    data = indexer.index('test')
    assert data.longest == 0
    assert data.shortest == 0
    assert data.indices == [0]


def test_index_file(fs):
    file_contents = """
    fortune 1
    %
    fortune 2
    %
    fortune 3
    """.replace(' ', '')
    fs.create_file('test', contents=file_contents)
    indexer = Indexer(Fortune.SEPARATOR)
    data = indexer.index('test')
    assert data.longest == 0
    assert data.shortest == 0
    assert data.indices == [0, 12, 23]
