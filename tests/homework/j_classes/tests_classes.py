import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from src.homework.j_classes import class_a

class TestDie(unittest.TestCase):

    def test_roll_value_within_range(self):
        die = class_a.Die()  
        for _ in range(3):  
            die.roll()  
            rolled_value = die.get_rolled_value()  
            self.assertGreaterEqual(rolled_value, 1)  
            self.assertLessEqual(rolled_value, 6)
if __name__ == '__main__':
    unittest.main()
