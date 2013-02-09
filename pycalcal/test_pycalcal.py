from __future__ import print_function
import unittest
from datetime import date
from wrappers import gregorian_from_chinese, \
                  get_branch, \
                  get_stem, \
                  is_valid_chinese_date, \
                  chinese_date_rec

class PyCalCalTestCases(unittest.TestCase):
    def setUp(self):
        self.moon_landing = date(1969, 7, 20)
        self.july_fourth = chinese_date_rec(2009, 5, 12, True)

    def test_conversions(self):
        from wrappers import gregorian_from_chinese, chinese_from_gregorian

        moon_landing_chinese = chinese_date_rec(1969, 6, 7, False)
        self.assertEqual(chinese_from_gregorian(self.moon_landing),\
                         moon_landing_chinese)
        july_fourth_greg = date(2009, 7, 4)
        self.assertEqual(gregorian_from_chinese(self.july_fourth),\
                         july_fourth_greg)

    def test_valid_function(self):
        from wrappers import is_valid_chinese_date

        valid_dates = [chinese_date_rec(2009, 5, 12, True),
                       chinese_date_rec(1989, 5, 9, False),
                       chinese_date_rec(1969, 6, 7, False)]
        for d in valid_dates:
            print("Validating:",d)
            self.assertTrue(is_valid_chinese_date(d))

        invalid_dates = [chinese_date_rec(1989, 5, 9, True),
                         chinese_date_rec(2010, 15, 3, False),
                         chinese_date_rec(1903, 5, 30, False)]
        for d in invalid_dates:
            print("Validating:",d)
            self.assertFalse(is_valid_chinese_date(d))

