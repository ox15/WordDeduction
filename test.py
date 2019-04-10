import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        g = Game()
        g.word = "TREE"
        self.assertEqual(g.word, "TREE", "Should be TREE")

    """def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")"""

if __name__ == '__main__':
    unittest.main()
