import unittest
import btree


class TestBTree(unittest.TestCase):
    def test1(self):
        bt = btree.BTree(2)
        keys = [5, 10, 40, 21, 45, 29, 22, 25, 20, 30, 27, 28, 26, 24]
        bt.insert_multiple(keys)
        bt.print()


if __name__ == "__main__":
    unittest.main()
