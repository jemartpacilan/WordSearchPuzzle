import unittest
from WordSearch import WordSearch

class WordSearchTestNormalDirectionInput(unittest.TestCase):
    def setUp(self):
        search = WordSearch('animals.pzl')
        search.start_search()

    def test_normal_direction_inputs(self):
        expected_results = ['CAT (1,1) (1,3)', 'DOG (2,2) (4,2)', 'COW (2,4) (4,4)']

        output_file = open('animals.out')
        results = output_file.read().splitlines()
        output_file.close()

        self.assertEqual(expected_results, results)

class WordSearchTestBackwardDirectionInput(unittest.TestCase):
    def setUp(self):
        search = WordSearch('search.pzl')
        search.start_search()

    def test_backward_or_forward_direction_inputs(self):
        expected_results = ['DIAMOND (7,1) (1,1)', 'HEART (5,7) (5,3)', 'CUT (1,4) (1,6)']

        output_file = open('search.out')
        results = output_file.read().splitlines()
        output_file.close()

        self.assertEqual(expected_results, results)

class WordSearchTestWithNotFoundInput(unittest.TestCase):
    def setUp(self):
        search = WordSearch('lostDuck.pzl')
        search.start_search()

    def test_not_found_input(self):
        expected_results = ['CAT (1,1) (1,3)', 'DOG (2,2) (4,2)', 'DUCK not found']

        output_file = open('lostDuck.out')
        results = output_file.read().splitlines()
        output_file.close()

        self.assertEqual(expected_results, results)

if __name__ == '__main__':
    unittest.main()