import unittest

from square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(2), 4)

    def test_area_2(self):
        self.assertEqual(area(3), 9)

    def test_perimeter_1(self):
        self.assertEqual(perimeter(2), 8)

    def test_perimeter_2(self):
        self.assertEqual(perimeter(3), 12)
