import unittest
from src.ColorEncodingConversions import hex_to_rgb, rgb_to_hex

class MyTestCase(unittest.TestCase):
    def test_hex_to_rgb(self):
        self.assertEqual(hex_to_rgb("FF00FF"), [255, 0, 255])
        self.assertEqual(hex_to_rgb("00FF00"), [0, 255, 0])
        self.assertEqual(hex_to_rgb("FFFFFF"), [255, 255, 255])
        self.assertEqual(hex_to_rgb("000000"), [0, 0, 0])

    def test_rgb_to_hex(self):
        self.assertEqual(rgb_to_hex((255, 0, 1)), "FF0001")
        self.assertEqual(rgb_to_hex((255, 255, 255)), "FFFFFF")
        self.assertEqual(rgb_to_hex((0, 0, 255)), "0000FF")

    def test_bidirectional(self):
        self.assertEqual(rgb_to_hex(hex_to_rgb("FFA320")), "FFA320")
        self.assertEqual(rgb_to_hex(hex_to_rgb("01AEF6")), "01AEF6")