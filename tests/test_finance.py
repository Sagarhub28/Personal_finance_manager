import unittest
from src.utils import validate_amount, validate_date, validate_category
from src.expense import Expense
from src.reports import generate_category_summary

class TestFinanceManager(unittest.TestCase):

    def test_validate_amount(self):
        """Test that amount validation only accepts positive numbers."""
        self.assertTrue(validate_amount("1500"))
        self.assertTrue(validate_amount("10.50"))
        self.assertFalse(validate_amount("-50"))
        self.assertFalse(validate_amount("abc"))
        self.assertFalse(validate_amount("0"))

    def test_validate_date(self):
        """Test that dates are strictly validated in YYYY-MM-DD format."""
        self.assertTrue(validate_date("2026-08-10"))
        self.assertFalse(validate_date("10-08-2026"))
        self.assertFalse(validate_date("2026/08/10"))
        self.assertFalse(validate_date("2026-13-40"))  # Invalid month/day

    def test_validate_category(self):
        """Test that category validation is case-insensitive and standardizes names."""
        self.assertEqual(validate_category("food"), "Food")
        self.assertEqual(validate_category("  Shopping  "), "Shopping")
        self.assertIsNone(validate_category("Luxury"))  # Not in predefined list

    def test_category_summary(self):
        """Test that calculations group amounts correctly by category."""
        expenses = [
            Expense(100, "Food", "2026-08-10", "Lunch"),
            Expense(200, "Food", "2026-08-10", "Dinner"),
            Expense(150, "Transport", "2026-08-10", "Taxi")
        ]
        summary = generate_category_summary(expenses)
        self.assertEqual(summary["Food"], 300.0)
        self.assertEqual(summary["Transport"], 150.0)

if __name__ == "__main__":
    unittest.main()