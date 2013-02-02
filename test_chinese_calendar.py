import unittest
from chinese_calendar import LunarDate, ordinal
class LunarDateTestCases(unittest.TestCase):
    def setUp(self):
        self.date_30_12_1924 = LunarDate(1924, 12, 30)

    def test_year(self):
        self.assertEqual(self.date_30_12_1924.year, 1924)
    
    def test_month(self):
        self.assertEqual(self.date_30_12_1924.month, 12)

    def test_day(self):
        self.assertEqual(self.date_30_12_1924.day, 30)

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

