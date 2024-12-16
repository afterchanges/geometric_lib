import unittest

from geometric_lib.triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(2, 3), 3)

    def test_area_2(self):
        self.assertEqual(area(3, 4), 6)

    def test_perimeter_1(self):
        self.assertEqual(perimeter(2, 3, 4), 9)

    def test_perimeter_2(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
