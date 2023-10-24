import unittest
from model import Vector2d

class TestVector2d(unittest.TestCase):

    def test_precedes(self):
        vec1 = Vector2d(2, 3)
        vec2 = Vector2d(4, 5)
        self.assertTrue(vec1.precedes(vec2))
        self.assertFalse(vec2.precedes(vec1))

    def test_follows(self):
        vec1 = Vector2d(2, 3)
        vec2 = Vector2d(4, 5)
        self.assertFalse(vec1.follows(vec2))
        self.assertTrue(vec2.follows(vec1))

    def test_add(self):
        vec1 = Vector2d(2, 3)
        vec2 = Vector2d(4, 5)
        result = vec1.add(vec2)
        self.assertEqual(result.x, 6)
        self.assertEqual(result.y, 8)

    def test_subtract(self):
        vec1 = Vector2d(4, 5)
        vec2 = Vector2d(2, 3)
        result = vec1.subtract(vec2)
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 2)

    def test_upperRight(self):
        vec1 = Vector2d(2, 3)
        vec2 = Vector2d(4, 5)
        result = vec1.upperRight(vec2)
        self.assertEqual(result.x, 4)
        self.assertEqual(result.y, 5)

    def test_lowerLeft(self):
        vec1 = Vector2d(2, 3)
        vec2 = Vector2d(4, 5)
        result = vec1.lowerLeft(vec2)
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 3)

    def test_opposite(self):
        vec1 = Vector2d(2, 3)
        result = vec1.opposite()
        self.assertEqual(result.x, -2)
        self.assertEqual(result.y, -3)

    def test_eq(self):
        vec1 = Vector2d(2, 3)
        vec2 = Vector2d(2, 3)
        vec3 = Vector2d(4, 5)
        self.assertTrue(vec1 == vec2)
        self.assertFalse(vec1 == vec3)

if __name__ == '__main__':
    unittest.main()
