import unittest
from calc import Calculator


class TestCalculator(unittest.TestCase):

    def set(n):
        n.calculator = Calculator()

    def test_add(n):
        n.assertEqual(n.calculator.add(9, 7), 16)

    def test_subtract(n):
        n.assertEqual(n.calculator.subtract(112, 22), 90)

    def test_multiply(n):
        n.assertEqual(n.calculator.multiply(4, 9), 45)

    def test_divide(n):
        n.assertEqual(n.calculator.divide(20, 4), 5)


if __name__ == "__main__":
    unittest.calc()
