import unittest
from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

class Test_Config(unittest.TestCase):

    # Test cases for get_factorial function
    def test_get_factorial(self):
        self.assertEqual(get_factorial(4), 24)  
        self.assertEqual(get_factorial(5), 120) 
        self.assertEqual(get_factorial(6), 720) 
        self.assertEqual(get_factorial(0), 1)   
        self.assertEqual(get_factorial(1), 1)   
        self.assertIsNone(get_factorial(-3))  

    # Test cases for sum_odd_numbers function
    def test_sum_odd_numbers(self):
        self.assertEqual(sum_odd_numbers(7), 16)  
        self.assertEqual(sum_odd_numbers(9), 25)  
        self.assertEqual(sum_odd_numbers(10), 25)  
        self.assertEqual(sum_odd_numbers(1), 1)    
        self.assertEqual(sum_odd_numbers(0), 0)   
        self.assertEqual(sum_odd_numbers(2), 1)  

if __name__ == "__main__":
    unittest.main()
