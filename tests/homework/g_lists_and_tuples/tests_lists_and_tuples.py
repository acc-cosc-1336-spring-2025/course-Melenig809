import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from src.homework.g_lists_and_tuples.lists import get_p_distance
from src.homework.g_lists_and_tuples.lists import get_p_distance_matrix

class Test_Config(unittest.TestCase):

    def test_p_distance(dna):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']
        result = get_p_distance(list1, list2)
        dna.assertAlmostEqual(result, 0.4, places=5)

    def test_get_p_distance_matrix(dna):
        sequences = [
            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A']
        ]

        expected_matrix = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]

        result = get_p_distance_matrix(sequences)
        for i in range(len(expected_matrix)):
            for j in range(len(expected_matrix[i])):
                dna.assertAlmostEqual(result[i][j], expected_matrix[i][j], places=5)

if __name__ == '__main__':
    unittest.main()