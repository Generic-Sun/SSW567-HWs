import unittest

def classify_triangle(a, b, c):
    if not (a > 0 or b > 0 or c > 0):
        return 'invalid'
    
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'invalid'
    
    sides = sorted([a,b,c])
    is_right = sides[0]**2 + sides[1]**2 == sides[2]**2
    result = ''
    
    if sides[0] == sides[2]:
        result = 'equilateral'
    elif sides[0] == sides[1] or sides[1] == sides[2]:
        result = 'isosceles'
    else:
        result = 'scalene'
    
    if is_right:
        result += ' & right'
    return result
    
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