from simple_value_object import ValueObject, invariant


class FortuneSource(ValueObject):

    source: str = ''
    percentage: int

    def __init__(self, source, percentage=0):
        pass

    @invariant
    def source_is_string(cls, instance):
        return type(instance.source) == str

    @invariant
    def percentage_value(cls, instance):
        return 0 <= instance.percentage <= 100
