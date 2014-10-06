from pycalcal.wrappers import \
    chinese_from_gregorian, \
    gregorian_from_chinese, \
    chinese_date as CDate, \
    get_branch, \
    get_stem, \
    is_valid_chinese_date

from constants import zodiac, elements, heavenly_stems, earthly_branches
from exceptions import ValueError, TypeError
from datetime import date, timedelta


class ChineseDate():
    '''
    The most important class in this package. ChineseDate contains both the
    Chinese and Gregorian representation of a date.

    ChineseDate should not be directly initialized. ChineseDate should be
    initialized from one of the following:

     - ChineseDate.from_gregorian(year, month, day)
     - ChineseDate.from_chinese(year, month, day, is_leap_month)
     - ChineseDate.today()
     - ChineseDate.fromtimestamp()
     - ChineseDate.fromordinal()
    '''

    def __init__(self, gregorian_date, chinese_date):
        if not (gregorian_date and chinese_date):
            raise ValueError
        if not is_valid_chinese_date(chinese_date):
            raise ValueError("Chinese date is not valid.")

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
        if isinstance(other, timedelta):
            new_date = self.gregorian_date - other
            cdate = chinese_from_gregorian(new_date)
            return ChineseDate(new_date, cdate)
        else:
            return self.gregorian_date - other

    def __rsub__(self, other):
        return other - self.gregorian_date

    def toordinal(self):
        '''
        Returns the ordinal version of the date. Refer to datetime.date.ordinal
        for more information.
        '''
        return self.gregorian_date.toordinal()

    def timetuple(self):
        '''
        Returns the timetuple of the Gregorian year.
        '''
        return self.gregorian_date.timetuple()

    @property
    def year(self):
        return self.chinese_date.year

    @property
    def month(self):
        return self.chinese_date.month

    @property
    def day(self):
        return self.chinese_date.day

    @property
    def is_leap_month(self):
        return self.chinese_date.is_leap_month

    @property
    def element(self):
        '''
        Returns the element of the year.
        '''
        return elements[self._stem]

    @property
    def zodiac(self):
        '''
        Returns the zodiac animal of the year, based on the Chinese zodiac.
        '''
        return zodiac[self._branch]

    @property
    def stem(self):
        '''
        Returns the heavenly stem, AKA the tian-gan, of the year.
        '''
        return heavenly_stems[self._stem]

    @property
    def branch(self):
        '''
        Returns the earthly branch, AKA the di-zhi, of the year
        '''
        return earthly_branches[self._branch]

    def show_zodiac_full(self, show_element=True):
        '''
        Returns the zodiac in the form of "Year of the <element> <zodiac>"
        '''
        el = self.element.title() + ' ' if show_element else ''
        zo = self.zodiac.title()

        res = "Year of the {0}{1}".format(el, zo)
        return res

    @classmethod
    def from_gregorian(cls, year, month, day):
        '''
        Returns an instance of ChineseDate, based on the given date in the
        Gregorian calendar.

        The year parameter must be within [datetime.MINYEAR, datetime.MAXYEAR]
        '''
        gdate = date(year, month, day)
        cdate = chinese_from_gregorian(gdate)
        return cls(gdate, cdate)

    @classmethod
    def from_chinese(cls,
                     chinese_year,
                     chinese_month,
                     chinese_day,
                     is_leap_month=False):
        '''
        Returns an instance of ChineseDate, based on the given date in the
        Chinese calendar.

        A ChineseDate is represented by
        - Year: Same as the Grogorian year.
        - Month: An integer between 1 and 12 inclusive.
        - Day: An integer between 1 and 30 inclusive.
        - is_leap_month: A boolean representing whether the date is in the leap
          month. In the Chinese calendar, the leap month shares the same number
          as the original month. For example, the year 2009 has the following
          months:
          1, 2, 3, 4, 5, 5*, 6, 7, 8, 9, 10, 11, 12; 5* being the leap month.
        '''
        cdate = CDate(chinese_year, chinese_month, chinese_day, is_leap_month)
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
