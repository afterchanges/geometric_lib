import unittest

from geometric_lib.rectangle import area, perimeter


class TestRectangle(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(2, 3), 6)

    def test_area_2(self):
        self.assertEqual(area(3, 4), 12)

    def test_perimeter_1(self):
        self.assertEqual(perimeter(2, 3), 10)

    def test_perimeter_2(self):
        self.assertEqual(perimeter(3, 4), 14)
