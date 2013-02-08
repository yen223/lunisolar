from pycalcal.tools import chinese_from_gregorian, \
                           gregorian_from_chinese, \
                           chinese_date_rec, \
                           get_branch, \
                           get_stem
from constants import zodiac, elements, heavenly_stems, earthly_branches
from exceptions import ValueError
from datetime import date

class ChineseDate():
    def __init__(self, gregorian_date, chinese_date):
        if not (gregorian_date and chinese_date):
            raise ValueError

        self.gregorian_date = gregorian_date
        self.chinese_date = chinese_date
        self._stem = get_stem(self.chinese_date)
        self._branch = get_branch(self.chinese_date)

    def __repr__(self):
        return repr(self.chinese_date)

    @property
    def element(self):
        return elements[self._stem]

    @property
    def zodiac(self):
        return zodiac[self._branch]

    @property
    def stem(self):
        return heavenly_stems[self._stem]

    @property
    def branch(self):
        return earthly_branches[self._branch]

    @classmethod
    def from_gregorian(cls, year, month, day):
        gdate = date(year, month, day)
        cdate = chinese_from_gregorian(gdate)
        return cls(gdate, cdate)

    @classmethod
    def from_chinese(cls, chinese_year, chinese_month, chinese_day, is_leap):
        cdate = chinese_date_rec(chinese_year, chinese_month, chinese_day, is_leap)
        gdate = gregorian_from_chinese(cdate)
        return cls(gdate, cdate)

    @classmethod
    def today(cls):
        gdate = date.today()
        cdate = chinese_from_gregorian(gdate)
        return cls(gdate, cdate)

    @classmethod
    def fromtimestamp(cls, timestamp):
        gdate = date.fromtimestamp(timestamp)
        cdate = chinese_from_gregorian(gdate)
        return cls(gdate, cdate)

    @classmethod
    def fromordinal(cls, ordinal):
        gdate = date.fromordinal(ordinal)
        cdate = chinese_from_gregorian(gdate)
        return cls(gdate, cdate)


