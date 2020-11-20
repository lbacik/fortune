
from ..fortune.index.data import IndexData


class Indexer:

    separator: str

    def __init__(self, separator: str):
        self.separator = separator

    def index(self, file: str) -> IndexData:
        data = IndexData()
        file = open(file, 'r')
        line = file.readline()
        data.indices.append(0)
        while line:
            if line == self.separator:
                data.indices.append(file.tell())
            line = file.readline()
        file.close()
        return data

    def create_index_file(self, file):
        pass
