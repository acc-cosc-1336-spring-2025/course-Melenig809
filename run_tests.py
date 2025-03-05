import unittest
'''
the file in /tests/homework/c_decisions/tests_decisions.py
has the test functions
'''
import unittest
from tests.homework.c_decisions import tests_decisions

suite = unittest.TestLoader().loadTestsFromModule(tests_decisions)
runner = unittest.TextTestRunner()
runner.run(suite)