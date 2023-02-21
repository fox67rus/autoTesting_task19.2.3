import pytest

from app.calculator import Calculator


class TestCalculator:
    def setup_method(self):
        self.calc = Calculator

    def test_add(self):
        assert self.calc.add(self, 1, 2) == 3

    def test_subtract(self):
        assert self.calc.subtract(self, 2, 1) == 1

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division(self):
        assert self.calc.division(self, 10, 2) == 5
