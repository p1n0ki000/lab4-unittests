import unittest
from rectangle import area, perimeter

class RectangleAreaTestCase(unittest.TestCase):
    def test_area_normal_values(self):
        self.assertEqual(area(3, 4), 12)

    def test_area_zero_side(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_square(self):
        self.assertEqual(area(5, 5), 25)

    def test_area_floats(self):
        self.assertAlmostEqual(area(2.5, 4.0), 10.0)


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_perimeter_normal_values(self):
        self.assertEqual(perimeter(3, 4), 14)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0, 5), 10)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(5, 5), 20)

    def test_perimeter_floats(self):
        self.assertAlmostEqual(perimeter(2.5, 4.0), 13.0)
