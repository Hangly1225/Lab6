import unittest
from main import Calculator


class TestCalculator(unittest.TestCase):

    def set(n):
        n.calculator = Calculator()

    def test_add(n):
        self.assertEqual(self.calculator.add(9, 7), 16)

    def test_subtract(n):
        self.assertEqual(self.calculator.subtract(112, 22), 90)

    def test_multiply(n):
        self.assertEqual(self.calculator.multiply(4, 9), 45)

    def test_divide(n):
        self.assertEqual(self.calculator.divide(20, 4), 5)


if __name__ == "__main__":
    unittest.main()
