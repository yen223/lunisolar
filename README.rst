Lunisolar
=========

Lunisolar is a Python package for handling Chinese calendars. Lunisolar contains a set of helper functions designed to make it easy to convert between the Gregorian (Western) calendar and the Chinese calendar.

Based on the works of `Helmer Aslaksen`_. Built on top of `PyCalCal`_, the Python implementation of Calendrica 3.0, a set of calendar-related algorithms as described in `Dershowitz and Reingold’s book “Calendrical Calculations” <http://www.amazon.com/Calendrical-Calculations-Millennium-Edward-Reingold/dp/0521777526>`_.

Usage
-----
Initializing a Chinese date:

    >>> from lunisolar import ChineseDate
    >>> mid_autumn = ChineseDate.from_chinese(chinese_year=2013, 
                                              chinese_month=8, 
                                              chinese_day=15, 
                                              is_leap_month=False)
    >>> mid_autumn
    chinese_date(year=2013, month=8, day=15, is_leap_month=False)
    >>> mid_autumn.gregorian_date
    datetime.date(2013, 9, 19)

A Chinese date object can be initialized from a Gregorian (western) date:

    >>> from lunisolar import ChineseDate
    >>> moon_landing = ChineseDate.from_gregorian(1969, 7, 20)
    >>> moon_landing
    chinese_date(year=1969, month=6, day=7, is_leap_month=False)

The ChineseDate class shares the same constructors as datetime.date:

    >>> ChineseDate.today()
    chinese_date(year=2012, month=12, day=29, is_leap_month=False)
    
    >>> timestamp = 1360414893.724195
    >>> ChineseDate.fromtimestamp(timestamp)
    chinese_date(year=2012, month=12, day=29, is_leap_month=False)
    
    >>> ordinal = 734908
    >>> ChineseDate.fromordinal(ordinal)
    chinese_date(year=2012, month=12, day=29, is_leap_month=False)

Retrieving properties of the Chinese calendar:

    >>> moon_landing = ChineseDate.from_gregorian(1969, 7, 20)
    >>> moon_landing.year
    1969
    >>> moon_landing.month
    6
    >>> moon_landing.day
    7
    >>> moon_landing.is_leap_month
    False
    >>> moon_landing.zodiac
    rooster
    >>> moon_landing.element
    earth
    >>> moon_landing.heavenly_stem
    ji
    >>> moon_landing.earthly_branch
    you

The add, subtract, and comparison operators for `ChineseDate` is similar to that of the `datetime.date` object. For subtraction and comparison, ChineseDate and datetime.date can be used interchangeably.

    >>> from datetime import timedelta
    >>> cdate = ChineseDate.from_gregorian(1969, 7, 20)
    >>> gdate = datetime.date(2013, 2, 10)
    >>> cdate > gdate
    False
    >>> gdate - cdate
    datetime.timedelta(15911)
    >>> diff = timedelta(200)
    >>> cdate + diff
    chinese_date(year=1969, month=12, day=29, is_leap_month=False)

.. _`Helmer Aslaksen`: http://www.math.nus.edu.sg/aslaksen/calendar/chinese.shtml
  
.. _pycalcal: https://github.com/espinielli/pycalcal
