from pycalcal import chinese_from_fixed, fixed_from_chinese, \
                     gregorian_from_fixed, fixed_from_gregorian
from constants import zodiac, elements, heavenly_stems, earthly_branches
from collections import namedtuple
from datetime import date
from exceptions import ValueError

class ChineseDate():
    def __init__(self, 
                 chinese_year, 
                 chinese_month=1, 
                 leap_month=False,
                 chinese_day=1):
        if not 1 <= chinese_month <= 12:
            raise ValueError, 'Chinese month must be between 1 and 12.'
        if not 1 <= chinese_day <= 30:
            raise ValueError, 'Chinese day must be between 1 and 30.'
 
        self.chinese_year = chinese_year
        self.chinese_month = chinese_month
        self.chinese_day = chinese_day
        self.leap_month = leap_month
        self.gregorian_date = to_gregorian_date(chinese_year, 
                                                chinese_month, 
                                                leap_month, 
                                                chinese_day)
        self._stem = get_stem(self.chinese_year)
        self._branch = get_branch(self.chinese_year)

    def __str__(self):
        return 'Year {0}, {1} month{2}, {3} day'.\
        format(self.chinese_year,
               ordinal(self.chinese_month),
               ' (leap)' if self.leap_month else '',
               ordinal(self.chinese_day))

    __repr__ = __str__

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

    @property
    def year_type(self):
        return 'Year of the {0} {1}'.format(self.element.title(), 
                                            self.zodiac.title())

    @property
    def chinese_new_year(self):
        return gregorian_from_fixed(chinese_new_year(self.chinese_new_year(self._year)

    @classmethod
    def from_gregorian_date(cls, year, month=1, day=1):
        _chinese_date = chinese_from_fixed(fixed_from_gregorian([year, month, day]))
        chinese_year = cycles_to_year(_chinese_date[0], _chinese_date[1]) 
        return cls(chinese_year=chinese_year,
                   chinese_month=_chinese_date[2],
                   leap_month=_chinese_date[3],
                   chinese_day=_chinese_date[4])
        
def ordinal(value):
    str_val = str(value)
    ordvals = {'1':'st', '2':'nd', '3':'rd'}
    suffix = ordvals.get(str_val[-1], 'th')
    return "{0}{1}".format(str_val, suffix)

def get_branch(chinese_year):
    return (chinese_year - 4) % 12

def get_stem(chinese_year):
    return (chinese_year - 4) % 10

def to_gregorian_date(chinese_year, chinese_month, leap_month, chinese_day):
    cycle, offset = year_to_cycles(chinese_year)
    arg = [cycle, offset, chinese_month, leap_month, chinese_day]
    g_date = gregorian_from_fixed(fixed_from_chinese(arg))
    return date(*g_date)

def cycles_to_year(cycle, offset):
    return cycle * 60 + offset - 2697

def year_to_cycles(year):
    return divmod(year + 2697, 60) #(cycle, offset)
