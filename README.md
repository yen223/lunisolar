Lunisolar
=========

Lunisolar is a Python package for handling Chinese calendars.

Based on the works of [Helmer Aslaksen][1]. Built on top of [PyCalCal][2], the Python implementation of Calendrica 3.0, a set of calendar-related algorithms as described in [Dershowitz and Reingold’s book “Calendrical Calculations”](http://www.amazon.com/Calendrical-Calculations-Millennium-Edward-Reingold/dp/0521777526).

Usage
----
Initializing a Chinese date:
``` python
    >>> from lunisolar import ChineseDate
    >>> mid_autumn = ChineseDate.from_chinese(chinese_year=2013, 
                                              chinese_month=8, 
                                              chinese_day=15, 
                                              is_leap_month=False)
    >>> mid_autumn
    chinese_date(year=2013, month=8, day=15, is_leap_month=False)
    >>> mid_autumn.gregorian_date
    datetime.date(2013, 9, 19)
```
A Chinese date object can be initialized from a Gregorian (western) date:

```python
    >>> from lunisolar import ChineseDate
    >>> moon_landing = ChineseDate.from_gregorian(1969, 7, 20)
    >>> moon_landing
    chinese_date(year=1969, month=6, day=7, is_leap_month=False)
```

The ChineseDate class shares the same constructors as datetime.date:

```python
    >>> ChineseDate.today()
    chinese_date(year=2012, month=12, day=29, is_leap_month=False)
    
    >>> timestamp = 1360414893.724195
    >>> ChineseDate.fromtimestamp(timestamp)
    chinese_date(year=2012, month=12, day=29, is_leap_month=False)
    
    >>> ordinal = 734908
    >>> ChineseDate.fromordinal(ordinal)
    chinese_date(year=2012, month=12, day=29, is_leap_month=False)
```

Retrieving properties of the Chinese calendar:

```python
    >>> moon_landing = ChineseDate.from_gregorian(1969, 7, 20)
    >>> moon_landing.zodiac
    rooster
    >>> moon_landing.element
    earth
    >>> moon_landing.heavenly_stem
    ji
    >>> moon_landing.earthly_branch
    you
```

The add, subtract, and comparison operators for `ChineseDate` is similar to that of the `datetime.date` object.

```python
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
```

Installation
--------------
    pip install lunisolar


FAQ
----------
###Q: How does the Chinese calendar work?
A: The Chinese calendar is a lunisolar system - the calendar dates correspond to both the tropical cycle and the lunar cycle.

A Chinese year is known as a nian. One nian consists of 12 lunar months, except for leap years, which consists of 13 months. Each month is either 29 or 30 days long. The length of each month varies from year to year, unlike in the Gregorian calendar. To maintain synchronicity with the solar cycle, a leap month is added about every 3 years.

The lengths of each month is determined astronomically - the first day of every month is guaranteed to be a new moon. As such, future dates in the Chinese calendar may be inaccurate.

For further information, please consult the comprehensive introduction to the Chinese calendar: [http://www.math.nus.edu.sg/aslaksen/calendar/cal.pdf](http://www.math.nus.edu.sg/aslaksen/calendar/cal.pdf)

###Q: Why does `lunisolar` use the Gregorian year to represent the Chinese year?
A: Because the Chinese did not implement a continuous year count.

Historically, the Chinese calendar doesn't have a single epoch - instead it records the number of sexagenarian cycles that has occured since the start of the reign of the current Emperor. 

There is a lot of confusion among scholars about which year should be taken as the reference point. As such, it is more practical to use the Gregorian year to represent the year.

Notes
----------
Lunisolar can handle dates ranging from 1/1/1 to 31/12/9999 (21/11/0 - 3/12/9999 in the Chinese calendar).

References
----------
[The Mathematics of the Chinese Calendar][1]

  [1]: http://www.math.nus.edu.sg/aslaksen/calendar/chinese.shtml
  [2]: https://github.com/espinielli/pycalcal
