from __future__ import print_function
import unittest
from lunisolar import ChineseDate

class LunarDateTestCases(unittest.TestCase):
    def setUp(self):
        self.moon_landing = ChineseDate.from_gregorian(1969, 7, 20)
        self.july_fourth = ChineseDate.from_chinese(2009, 5, 12, True)

    def test_earthly_branch(self):
        self.assertEqual(self.moon_landing._branch, 5)
        self.assertEqual(self.july_fourth._branch, 5)
        print("test_earthly_branch passed!")

    def test_heavenly_stem(self):
        self.assertEqual(self.moon_landing._stem, 9)
        self.assertEqual(self.july_fourth._stem, 1)
        print("test_heavenly_stem passed!")

    def test_convert_to_western(self):
        pass
        #self.assertEqual()


