import unittest
from tests.homework.d_repetition import tests_repetition

suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
runner = unittest.TextTestRunner()
runner.run(suite)
