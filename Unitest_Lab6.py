import unittest
from Lab6 import*

class Test(unittest.TestCase):
    def test_add(seft):
        seft.assertEqual(add(9, 6), 15)
        seft.assertEqual(add(9, 1), 10)

    def test_subtract(seft):
        seft.assertEqual(subtract(9, 6), 3)
        seft.assertEqual(subtract(-1, 1), -2)

    def test_multiply(seft):
        seft.assertEqual(multiply(100, 1), 100)
        seft.assertEqual(multiply(9, 1), 9)

    def test_divide(seft):
        seft.assertEqual(divide(9, 3), 3)
        seft.assertEqual(divide(8, 4), 2)
unittest.main()