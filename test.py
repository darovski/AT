import unittest
from main import add, subtract, multiply, divide, rest

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(3, 7), 10)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertEqual(subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)
        self.assertEqual(multiply(3, 6), 18)

    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)

    def test_positive_numbers(self):
        self.assertEqual(rest(10, 3), 1, "Ошибка: 10 % 3 должно быть равно 1")
        self.assertEqual(rest(20, 5), 0, "Ошибка: 20 % 5 должно быть равно 0")

    def test_negative_numbers(self):
        self.assertEqual(rest(-10, 3), 2, "Ошибка: -10 % 3 должно быть равно 2")
        self.assertEqual(rest(10, -3), -2, "Ошибка: 10 % -3 должно быть равно -2")
        self.assertEqual(rest(-10, -3), -1, "Ошибка: -10 % -3 должно быть равно -1")

    def test_dividend_less_than_divisor(self):
        self.assertEqual(rest(2, 3), 2, "Ошибка: 2 % 3 должно быть равно 2")
        self.assertEqual(rest(-2, 3), 1, "Ошибка: -2 % 3 должно быть равно 1")

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            rest(10, 0)
        self.assertEqual(str(context.exception), "Деление на ноль невозможно",
                         "Ошибка: Сообщение об ошибке должно быть 'Деление на ноль невозможно'")

if __name__ == '__main__':
    unittest.main()