import unittest
from triangle import classify_triangle

class TestTriangle(unittest.TestCase):
    def test_right(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'scalene & right')
    def test_equilateral(self):
        self.assertEqual(classify_triangle(4, 4, 4), 'equilateral')
    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 6), 'isosceles')
    def test_invalid_a(self):
        self.assertEqual(classify_triangle(0, 4, 5), 'invalid')
    def test_invalid_b(self):
        self.assertEqual(classify_triangle(4, 4, 10), 'invalid')
        
        
if __name__ == '__main__':
    unittest.main()