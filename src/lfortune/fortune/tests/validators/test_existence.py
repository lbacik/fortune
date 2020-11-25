from lfortune.abstract.fortune_source import FortuneSource
from lfortune.fortune.validators.existence import Existence


def test_none():
    assert Existence().validate(None) is None


def test_empty():
    assert [] == Existence().validate([])


def test_file_exists(fs):
    fs.create_file('/test.txt')
    fs.create_file('/test2/foo.txt')
    sources = [
        FortuneSource('/test.txt'),
        FortuneSource('/test2'),
    ]
    assert sources == Existence().validate(sources)


def test_file_doesnt_exist(fs):
    assert [] == Existence().validate([
        FortuneSource('/test.txt'),
        FortuneSource('/test/foo.txt'),
    ])


def test_mixed(fs):
    fs.create_file('/test.txt')
    fs.create_file('/test2/foo.txt')
    sources = [
        FortuneSource('/test.txt'),
        FortuneSource('/test3'),
    ]
    assert [FortuneSource('/test.txt')] == Existence().validate(sources)
