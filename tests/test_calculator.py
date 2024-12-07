import unittest
from src.calculator import sum, subtract, multiply, divide

class calculatorTest(unittest.TestCase):
    def test_sum(self):
        assert sum(1, 2) == 3
    def test_subtract(self):
        assert subtract(4, 5) == -1
    def test_multiply(self):
        assert multiply(6, 7) == 42
    def test_divide(self):
        assert divide(80, 9) == 8.888888888888889
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)






