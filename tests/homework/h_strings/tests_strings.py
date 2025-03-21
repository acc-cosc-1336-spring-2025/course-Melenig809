import unittest
from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement

class Test_Config(unittest.TestCase):
    
    def test_get_hamming_distance(self):
        # Test input DNA strings
        dna1 = "GAGCCTACTAACGGGAT"
        dna2 = "CATCGTAATGACGGCCT"
        # Expected output is 7
        self.assertEqual(get_hamming_distance(dna1, dna2), 7)
    
    # Test case for get_dna_complement function
    def test_get_dna_complement(self):
        dna = "AAAACCCGGT"
        self.assertEqual(get_dna_complement(dna), "ACCGGGTTTT")

if __name__ == '__main__':
    unittest.main()
