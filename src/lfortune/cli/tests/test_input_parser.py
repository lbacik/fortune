from ..input_parser import input_parse
from ...abstract.fortune_source import FortuneSource


# def _test_input_parser_with_one_param():
#     result = input_parse('foo')
#     assert len(result) == 1
#     assert isinstance(result[0], FortuneSource)
#     assert result[0] == FortuneSource('foo', 0)
#
#
# def _test_input_parser_with_one_param_and_percentage():
#     result = input_parse('50%', 'foo')
#     assert len(result) == 1
#     assert isinstance(result[0], FortuneSource)
#     assert result[0] == FortuneSource('foo', 50)
#
#
# def _test_input_parser_with_two_param_and_percentage():
#     result = input_parse('50%', 'foo', 'bar')
#     assert len(result) == 2
#     assert isinstance(result[0], FortuneSource)
#     assert isinstance(result[1], FortuneSource)
#     assert result[0] == FortuneSource('foo', 50)
#     assert result[1] == FortuneSource('bar', 50)
#
#
# def _test_input_parser_5():
#     result = input_parse('50%', 'foo', '10%', 'bar')
#     assert len(result) == 2
#     assert isinstance(result[0], FortuneSource)
#     assert isinstance(result[1], FortuneSource)
#     assert result[0] == FortuneSource('foo', 50)
#     assert result[1] == FortuneSource('bar', 10)


expectation = [
    [
        None,
        [],
    ],
    [
        '',
        [],
    ],
    [
        'foo',
        [
            FortuneSource('foo', 0)
        ],
    ],
    [
        '50% foo',
        [
            FortuneSource('foo', 50)
        ],
    ],
    [
        '50% foo bar',
        [
            FortuneSource('foo', 50),
            FortuneSource('bar', 0),
        ],
    ],
    [
        '20% foo bar',
        [
            FortuneSource('foo', 20),
            FortuneSource('bar', 0),
        ],
    ],
    [
        'foo 80% bar',
        [
            FortuneSource('foo', 0),
            FortuneSource('bar', 80),
        ],
    ],
    [
        '20% foo bar baz',
        [
            FortuneSource('foo', 20),
            FortuneSource('bar', 0),
            FortuneSource('baz', 0),
        ],
    ],
    [
        '10% foo bar 40% baz',
        [
            FortuneSource('foo', 10),
            FortuneSource('bar', 0),
            FortuneSource('baz', 40),
        ],
    ],
    [
        '10% foo 30% bar 40% baz',
        [
            FortuneSource('foo', 10),
            FortuneSource('bar', 30),
            FortuneSource('baz', 40),
        ],
    ],
    [
        'foo bar baz',
        [
            FortuneSource('foo', 0),
            FortuneSource('bar', 0),
            FortuneSource('baz', 0),
        ],
    ],
]


def test_data():
    for input_db, expected in expectation:
        if input_db is not None:
            result = input_parse(input_db.split())
        else:
            result = input_parse(input_db)
        assert result == expected


def test_path():
    result = input_parse(['foo'], '/bar')
    assert result == [
        FortuneSource('foo')
    ]
