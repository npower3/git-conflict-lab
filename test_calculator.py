import unittest

from calculator import add, format_result


class CalculatorTests(unittest.TestCase):
    def test_adds_two_numbers(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_formats_result_to_two_decimal_places(self) -> None:
        self.assertEqual(format_result(12.5), "Result: 12.50")


if __name__ == "__main__":
    unittest.main()
