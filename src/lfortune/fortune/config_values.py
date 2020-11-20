from simple_value_object import ValueObject, invariant


class ConfigValues(ValueObject):

    root_path: str

    def __init__(self, root_path):
        pass

    @invariant
    def root_path_is_string(self, instance):
        return type(instance.root_path) == str
