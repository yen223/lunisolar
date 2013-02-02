from constants import zodiac
from datetime import date as solar_date
from exceptions import ValueError

class LunarDate():
    def __init__(self, lunar_year, lunar_month=1, lunar_day=1):
        if not 1 <= lunar_month <= 13:
            raise ValueError, 'Lunar month must be between 1 and 13.'
        if not 1 <= lunar_day <= 30:
            raise ValueError, 'Lunar day must be between 1 and 30.'

        self.lunar_year = lunar_year
        self.lunar_month = lunar_month
        self.lunar_day = lunar_day

        self.solar_date = solar_date(lunar_year, lunar_month, lunar_day)

        self._branch = self.get_branch(self.lunar_year)

    def __str__(self):
        return 'Year {0}, {1} month, {2} day'.format(self.lunar_year,
                                                     ordinal(self.lunar_month),
                                                     ordinal(self.lunar_day))

    __repr__ = __str__

    @staticmethod
    def get_branch(lunar_year):
        return (lunar_year - 4) % 12
        

    @staticmethod
    def to_solar_date(lunar_year, lunar_month, lunar_day):
        solar_year = lunar_year

    @property
    def zodiac(self):
        return zodiac[self._branch]

def ordinal(value):
    str_val = str(value)
    if str_val[-1] == '1':
        ordval = 'st'
    elif str_val[-1] == '2':
        ordval = 'nd'
    elif str_val[-1] == '3':
        ordval = 'rd'
    else:
        ordval = 'th'
    return "{0}{1}".format(str_val, ordval)
