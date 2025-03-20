import pytest
from app.calc import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    def test_multiply(self): # Умножение
        assert self.calc.multiply(3, 4) == 12  # 3 * 4 = 12

    def test_division(self): # Деление
        assert self.calc.division(10, 2) == 5  # 10 / 2 = 5

    def test_subtraction(self): # Вычитание
        assert self.calc.subtraction(10, 4) == 6  # 10 - 4 = 6

    def test_adding(self): # Прибавление
        assert self.calc.adding(7, 3) == 10  # 7 + 3 = 10

    def teardown_mathod(self):
            print("Выполнение метода Teardown")
