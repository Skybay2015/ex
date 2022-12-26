import unittest

from pyramid_number import pyramid_number

class TestPyramidNumber(unittest.TestCase):
    def test_first_number(self):
        result = pyramid_number(1)
        self.assertEqual(result, 1)

    def test_second_number(self):
        result = pyramid_number(2)
        self.assertEqual(result, 4)

    def test_third_number(self):
        result = pyramid_number(3)
        self.assertEqual(result, 10)

    def test_large_number(self):
        result = pyramid_number(10)
        self.assertAlmostEqual(result, 285, delta=1e-9)
