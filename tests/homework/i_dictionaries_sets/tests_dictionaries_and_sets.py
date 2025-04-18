import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(dictionary):
        inventory = {}
        
        add_inventory(inventory, "Widget1", 10)
        dictionary.assertEqual(inventory["Widget1"], 10)

        add_inventory(inventory, "Widget1", 25)
        dictionary.assertEqual(inventory["Widget1"], 35)

        add_inventory(inventory, "Widget1", -10)
        dictionary.assertEqual(inventory["Widget1"], 25)

    def test_remove_inventory_widget(dictionary):
        inventory = {
            "Widget1": 10,
            "Widget2": 20
        }

        result = remove_inventory_widget(inventory, "Widget1")
        dictionary.assertEqual(result, "Record deleted")
        dictionary.assertEqual(len(inventory), 1)
        dictionary.assertIn("Widget2", inventory)

if __name__ == "__main__":
    unittest.main()
