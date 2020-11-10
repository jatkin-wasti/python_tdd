# This file will have our tests written to test our simple calculator
# importing necessary modules/libraries and frameworks
from simple_calc import SimpleCalc
import unittest
import pytest


# Let's create a class to write our tests
class CalcTest(unittest.TestCase):  # unittest.TestCase works with unittest frame work as a parent class
    # Creating an object of our class
    calc = SimpleCalc()

    # IMPORTANT - we must use TEST word in our functions so the python interpreter knows what we are testing
    def test_add(self):
        # What are we asking python to test for us?
        # We are asking python to test/check if 2+4 = 6 If True pass the test if False fail the test
        self.assertEqual(self.calc.add(2, 4), 6)  # boolean returned

    def test_subtract(self):
        # Testing if 4 - 2 = 2 If True pass the test if False fail the test
        self.assertEqual(self.calc.subtract(4, 2), 2)  # boolean returned

    def test_multiple(self):
        # Testing if 2 * 2 = 4 If True pass the test if False fail the test
        self.assertEqual(self.calc.multiply(2, 2), 4)  # boolean returned

    def test_divide(self):
        # Testing if 9 / 3 = 3 If True pass the test if False fail the test
        self.assertEqual(self.calc.divide(9, 3), 3)  # boolean returned
