"""This module contains the logic to classify a triangle by its side lengths."""
def classify_triangle(a, b, c):
    """Evaluates the sides of a triangle and returns its classification."""
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
