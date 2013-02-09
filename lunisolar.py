from pycalcal.wrappers import chinese_from_gregorian, \
                           gregorian_from_chinese, \
                           chinese_date_rec, \
                           get_branch, \
                           get_stem, \
                           is_valid_chinese_date

from constants import zodiac, elements, heavenly_stems, earthly_branches
from exceptions import ValueError, TypeError
from datetime import date

class ChineseDate():
    def __init__(self, gregorian_date, chinese_date):
        if not (gregorian_date and chinese_date):
            raise ValueError
        if not is_valid_chinese_date(chinese_date):
            raise ValueError, "Chinese date is not valid."

        self.gregorian_date = gregorian_date
        self.chinese_date = chinese_date
        self._stem = get_stem(self.chinese_date)
        self._branch = get_branch(self.chinese_date)

    def __repr__(self):
        return repr(self.chinese_date)

    def __eq__(self, other):
        return self.toordinal() == other.toordinal()

    def __ne__(self, other):
        return self.toordinal() != other.toordinal()

    def __lt__(self, other):
        return self.toordinal() < other.toordinal()

    def __gt__(self, other):
        return self.toordinal() > other.toordinal()

    def __le__(self, other):
        return self.toordinal() <= other.toordinal()

    def __ge__(self, other):
        return self.toordinal() >= other.toordinal()

    def __add__(self, other):
        new_date = self.gregorian_date + other
        cdate = chinese_from_gregorian(new_date)
        return ChineseDate(new_date, cdate)
    
    __radd__ = __add__

    def __sub__(self, other):
        return self.gregorian_date - other

    def __rsub__(self, other):
        return other - self.gregorian_date

    def toordinal(self):
        return self.gregorian_date.toordinal()

    def timetuple():
        return self.gregorian_date.timetuple()

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


