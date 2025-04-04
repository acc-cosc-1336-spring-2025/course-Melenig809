def get_lowest_list_value(numbers_list):
    lowest = numbers_list[0]  
    
    for num in numbers_list:  
        if num < lowest:  
            lowest = num  
    
    return lowest  

def get_highest_list_value(numbers_list):
    highest = numbers_list[0]  
    
    for num in numbers_list:  
        if num > highest:  
            highest = num  
    
    return highest  

import unittest

from lists import get_lowest_list_value, get_highest_list_value

class TestListFunctions(unittest.TestCase):
    
    def test_get_lowest_list_value(self):
        test_list = [8, 10, 1, 50, 20]
        result = get_lowest_list_value(test_list)
        self.assertEqual(result, 1)
    
    def test_get_highest_list_value(self):
        test_list = [8, 10, 1, 50, 20]
        result = get_highest_list_value(test_list)
        self.assertEqual(result, 50)

if __name__ == '__main__':
    unittest.main()

