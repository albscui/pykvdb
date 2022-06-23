import pickle

from pykvdb.btree import BTree, NodeKey


class KV(BTree):
    def __init__(self, type_, values=None):
        self.type = type_
        super().__init__(10)

    def get(self, key):
        value = self.search(self.root, key)
        if value is None:
            raise KeyError('There is no value for key "{}"'.format(key))
        return value

    def set(self, key, value):
        if value is None:
            raise ValueError("Cannot store None values")
        if not isinstance(key, self.type):
            raise KeyError("Key must be of type {}".format(self.type))
        exists = self.search(self.root, key)
        if exists is not None:
            raise ValueError("Cannot store duplicate key values")

        node = NodeKey(key, value)
        self.insert(node)

    def range_query(self, interval, inclusive=False):
        if not isinstance(interval, (list, tuple)) and len(interval) != 2:
            raise ValueError("The first argument must be a list or tuple of length 2")

        lower, upper = interval
        if lower is None:
            return self.less_than(self.root, upper, inclusive=inclusive)
        return self.greater_than(
            self.root, lower, upper_bound=upper, inclusive=inclusive
        )

    def save(self, filename):
        filename = filename + ".pykvdb"
        with open(filename, "wb") as f:
            pickle.dump(self, f)
            return True
        return False

    def load_from_dict(self, dictionary):
        for key, value in dictionary.items():
            self.set(key, value)

    @staticmethod
    def load(filename):
        filename = filename + ".pykvdb"
        with open(filename, "rb") as f:
            return pickle.load(f)
