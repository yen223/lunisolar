from __future__ import print_function
import unittest
from lunisolar import ChineseDate

class LunarDateTestCases(unittest.TestCase):
    def setUp(self):
        self.moon_landing = ChineseDate.from_gregorian(1969, 7, 20)
        self.july_fourth = ChineseDate.from_chinese(2009, 5, 12, True)

    def test_construction_from_gregorian(self):
        moon_landing_gdate = self.moon_landing.gregorian_date
        self.assertEqual(moon_landing_gdate.year, 1969)
        self.assertEqual(moon_landing_gdate.month, 7)
        self.assertEqual(moon_landing_gdate.day, 20)

        moon_landing_cdate = self.moon_landing.chinese_date
        self.assertEqual(moon_landing_cdate.year, 1969)
        self.assertEqual(moon_landing_cdate.month, 6)
        self.assertEqual(moon_landing_cdate.day, 7)
        self.assertEqual(moon_landing_cdate.is_leap_month, False)

    def test_construction_from_chinese(self):
        july_fourth_gdate = self.july_fourth.gregorian_date
        self.assertEqual(july_fourth_gdate.year, 2009)
        self.assertEqual(july_fourth_gdate.month, 7)
        self.assertEqual(july_fourth_gdate.day, 4)

        july_fourth_cdate = self.july_fourth.chinese_date
        self.assertEqual(july_fourth_cdate.year, 2009)
        self.assertEqual(july_fourth_cdate.month, 5)
        self.assertEqual(july_fourth_cdate.day, 12)
        self.assertEqual(july_fourth_cdate.is_leap_month, True)

    def test_properties(self):
        moon_landing = self.moon_landing
        self.assertEqual(moon_landing.year, 1969)
        self.assertEqual(moon_landing.month, 6)
        self.assertEqual(moon_landing.day, 7)
        self.assertEqual(moon_landing.is_leap_month, False)

    def test_heavenly_stem(self):
        self.assertEqual(self.moon_landing._stem, 5)
        self.assertEqual(self.july_fourth._stem, 5)
        print("test_heavenly_stem passed!")

    def test_earthly_branch(self):
        self.assertEqual(self.moon_landing._branch, 9)
        self.assertEqual(self.july_fourth._branch, 1)
        print("test_earthly_branch passed!")

    def test_compare_chinese_date_with_builtin_date(self):
        from datetime import date
        old_date = date(1969, 7, 19)
        self.assertTrue(old_date < self.moon_landing)
        self.assertFalse(old_date > self.moon_landing)
        self.assertTrue(old_date <= self.moon_landing)
        self.assertFalse(old_date >= self.moon_landing)
        self.assertFalse(old_date == self.moon_landing)
        self.assertTrue(old_date != self.moon_landing)

        self.assertFalse(self.moon_landing < old_date)
        self.assertTrue(self.moon_landing > old_date)
        self.assertFalse(self.moon_landing <= old_date)
        self.assertTrue(self.moon_landing >= old_date)
        self.assertFalse(self.moon_landing == old_date)
        self.assertTrue(self.moon_landing != old_date)

    def test_compare_chinese_date_with_chinese_date(self):
        earlier = self.moon_landing
        later = self.july_fourth

        self.assertTrue(earlier < later)
        self.assertFalse(earlier > later)
        self.assertTrue(earlier <= later)
        self.assertFalse(earlier >= later)
        self.assertFalse(earlier == later)
        self.assertTrue(earlier != later)

        self.assertFalse(later < earlier)
        self.assertTrue(later > earlier)
        self.assertFalse(later <= earlier)
        self.assertTrue(later >= earlier)
        self.assertFalse(later == earlier)
        self.assertTrue(later != earlier)

    def test_show_full_zodiac_name(self):
        self.assertEqual(self.moon_landing.show_zodiac_full(), 
                "Year of the Earth Rooster")
        self.assertEqual(self.july_fourth.show_zodiac_full(show_element=False),
                "Year of the Ox")
