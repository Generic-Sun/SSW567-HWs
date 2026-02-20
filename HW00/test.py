"""This module contains unit tests for the classify_triangle function."""
import unittest
from triangle import classify_triangle
class TestTriangle(unittest.TestCase):
    """Test cases for the classify_triangle function."""
    def test_right(self):
        """Test that a 3, 4, 5 triangle returns 'scalene & right'."""
        self.assertEqual(classify_triangle(3, 4, 5), 'scalene & right')
    def test_equilateral(self):
        """Test that a 4, 4, 4 triangle returns 'equilateral'."""
        self.assertEqual(classify_triangle(4, 4, 4), 'equilateral')
    def test_isosceles(self):
        """Test that a 5, 5, 6 triangle returns 'isosceles'."""
        self.assertEqual(classify_triangle(5, 5, 6), 'isosceles')
    def test_invalid_a(self):
        """Test that a triangle with a side of 0 returns 'invalid'."""
        self.assertEqual(classify_triangle(0, 4, 5), 'invalid')
    def test_invalid_b(self):
        """Test that a triangle violating the triangle inequality returns 'invalid'."""
        self.assertEqual(classify_triangle(4, 4, 10), 'invalid')
if __name__ == '__main__':
    unittest.main()
