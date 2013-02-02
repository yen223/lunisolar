import unittest
from chinese_calendar import LunarDate, ordinal
class LunarDateTestCases(unittest.TestCase):
    def setUp(self):
        self.date_30_12_1924 = LunarDate(1924, 12, 30)
        self.date_15_1_2014 = LunarDate(2014, 1, 15)

    def test_year(self):
        self.assertEqual(self.date_30_12_1924.lunar_year, 1924)
        self.assertEqual(self.date_15_1_2014.lunar_year, 2014)

    def test_month(self):
        self.assertEqual(self.date_30_12_1924.lunar_month, 12)
        self.assertEqual(self.date_15_1_2014.lunar_month, 1)

    def test_day(self):
        self.assertEqual(self.date_30_12_1924.lunar_day, 30)
        self.assertEqual(self.date_15_1_2014.lunar_day, 15)

    def test_earthly_branch(self):
        self.assertEqual(self.date_30_12_1924._branch, 0)
        self.assertEqual(self.date_15_1_2014._branch, 6)

    def test_convert_to_western(self):
        pass
        #self.assertEqual()

class OrdinalTestCase(unittest.TestCase):
    def test_proper_ordinal(self):
        test_values = { 145: "145th",
                        2012: "2012nd",
                        101: "101st",
                        3: "3rd"
                      }
        for key, val in test_values.iteritems():
            self.assertEqual(ordinal(key), val)

