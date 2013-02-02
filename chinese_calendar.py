from constants import zodiac
from datetime import date as base_date
from exceptions import ValueError

class LunarDate(base_date):
    def __init__(self, lunar_year, lunar_month=1, lunar_day=1):
        print "I'm in the init!"
        if not 1 <= lunar_month <= 13:
            raise ValueError, 'Lunar month must be between 1 and 13.'
        if not 1 <= lunar_day <= 30:
            raise ValueError, 'Lunar day must be between 1 and 30.'

        self.year = lunar_year
        self.month = 1
        self.day = 1
        self.lunar_year = lunar_year
        self.lunar_month = lunar_month
        self.lunar_day = lunar_day
        super(LunarDate, self).__init__(lunar_year, month=10, day=10)

    def __repr__(self):
        return 'Year {0}, {1} month, {2} day'.format(self.lunar_year,
                                                     ordinal(self.lunar_month),
                                                     ordinal(self.lunar_day))

    def zodiac(self):
        return zodiac[3]

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
