from simple_value_object import ValueObject, invariant


class FortuneData(ValueObject):

    fortune: str
    file: str
    index: int

    def __init__(self, fortune, file, index):
        pass

    @invariant
    def fortune_is_string(cls, instance):
        return type(instance.fortune) == str

    @invariant
    def file_is_string(cls, instance):
        return type(instance.file) == str

    @invariant
    def index_is_integer(cls, instance):
        return type(instance.index) == int
