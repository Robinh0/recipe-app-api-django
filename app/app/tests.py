"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc


class TestCalc(SimpleTestCase):
    """Test the calc module"""

    def test_add(self):
        """Test adding two numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract(self):
        """Test subtracting two numbers"""
        res = calc.subtract(5, 6)

        self.assertEqual(res, -1)
