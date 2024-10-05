import unittest
from src.ColorSpaceConversions import rgb_to_hsv, hsv_to_rgb

class MyTestCase(unittest.TestCase):
    def test_rgb_to_hsv(self):
        self.assertEqual(rgb_to_hsv([255, 0, 0]), [0, 1, 1])
        self.assertEqual(rgb_to_hsv([0, 255, 0]), [120, 1, 1])
        self.assertEqual(rgb_to_hsv([0, 0, 255]), [240, 1, 1])

    def test_hsv_to_rgb(self):
        self.assertEqual(hsv_to_rgb([0, 1, 1]), [255, 0, 0])
        self.assertEqual(hsv_to_rgb([120, 1, 1]), [0, 255, 0])
        self.assertEqual(hsv_to_rgb([240, 1, 1]), [0, 0, 255])

    def test_bidirectional(self):
        start = [120, 45, 90]
        self.assertEqual(hsv_to_rgb(rgb_to_hsv(start)), start)
        start = [25, 30, 255]
        self.assertEqual(hsv_to_rgb(rgb_to_hsv(start)), start)
        start = [190, 255, 32]
        self.assertEqual(hsv_to_rgb(rgb_to_hsv(start)), start)