"""
Unit test for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_substraction(self):
        assert 3 == calculator.subtract(6, 3)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)
