import unittest
Rachel_sort import list_sort
class RachelsortTest(unittest.TestCase):

    def test_integer_input(self):
        self.assertEqual(list_sort(5), 'Invalid Input')

    def test_string_input(self):
        self.assertEqual(list_sort('string'), 'Invalid Input')

    def test_empty_list(self):
        self.assertEqual(list_sort([]), {'evens': [], 'odds': [], 'chars': []})

    def test_no_string(self):
        self.assertEqual(
            list_sort[6, 24, 'x', 15, -6,'z', -5, 1, 4, 0, 3, 5],
            {'evens': [6, 24, -6, 4, 0], 'odds': [15, -5, 1, 3, 5], 'chars': ['x', 'z']}
        )

    def test_no_even(self):
        self.assertEqual(
            list_sort([6, 24, 'x', 15,]),
            {'evens': [6, 24], 'odds': [15], 'chars': ['x']}
        )

    def test_no_odd(self):
        self.assertEqual(
            list_sort(['a', 'z', 6]),
            {'evens': [6], 'odds': [], 'chars': ['a', 'z']}
        )

    def test_complete_list(self):
        self.assertEqual(
            list_sort([4, 9, 2, 3, 5, 1, 'd', 'a', 'c', 'f']),
            {'evens': [2, 4], 'odds': [1, 3, 5, 9], 'chars': ['a', 'c', 'd', 'f']})


if __name__ == '__main__':
    unittest.main()
