
import unittest
from library_system.fine_calculator import FineCalculator


class TestFineCalculator(unittest.TestCase):

    def test_no_fine(self):
        # Arrange
        calc = FineCalculator()
        days = 0
        expected = 0

        # Act
        actual = calc.calculate(days)

        # Assert
        self.assertEqual(expected, actual)

    def test_normal_fine(self):
        # Arrange
        calc = FineCalculator()
        days = 5
        expected = 25000

        # Act
        actual = calc.calculate(days)

        # Assert
        self.assertEqual(expected, actual)

    def test_heavy_fine(self):
        # Arrange
        calc = FineCalculator()
        days = 11
        expected = 66000

        # Act
        actual = calc.calculate(days)

        # Assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
