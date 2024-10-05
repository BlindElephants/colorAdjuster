import unittest
from main import is_value_rgb_or_hex

class MyTestCase(unittest.TestCase):
    def test_is_value_rgb_or_hex(self):
        self.assertEqual(is_value_rgb_or_hex("255,0,0"), "rgb")
        self.assertEqual(is_value_rgb_or_hex("0, 120, 3"), "rgb")
        self.assertEqual(is_value_rgb_or_hex("00FF21"), "hex")
        self.assertEqual(is_value_rgb_or_hex("001122"), "hex")
        self.assertEqual(is_value_rgb_or_hex("#443391"), "hex")