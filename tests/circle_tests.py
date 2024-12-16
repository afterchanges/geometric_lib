import unittest

from geometric_lib.circle import area, perimeter


class TestCircle(unittest.TestCase):
    def test_area_1(self):
        self.assertAlmostEqual(area(1), 3.141592, places=5)

    def test_area_2(self):
        self.assertAlmostEqual(area(2), 12.566368, places=5)

    def test_perimeter_1(self):
        self.assertAlmostEqual(perimeter(1), 6.283184, places=5)

    def test_perimeter_2(self):
        self.assertAlmostEqual(perimeter(2), 12.566368, places=5)
