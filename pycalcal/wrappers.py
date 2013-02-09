from pycalcal import chinese_from_fixed, fixed_from_chinese, \
                     gregorian_from_fixed, fixed_from_gregorian, \
                     chinese_new_year
from datetime import date
from collections import namedtuple

chinese_date_rec = namedtuple('chinese_date_rec', 'year, month, day, is_leap_month')

def _tuple_from_pcc_chinese(pcc_cdate):
    cycle, offset, month, leap, day = pcc_cdate
    year = cycle*60 + offset - 2697
    return chinese_date_rec(year, month, day, leap)

def _pcc_chinese_from_tuple(cdate):
    year, month, day, leap = cdate
    cycle, offset = divmod(year + 2697, 60)
    return [cycle, offset, month, leap, day]

def _date_from_pcc_gregorian(pcc_gdate):
    year, month, day = pcc_gdate
    return date(year, month, day)

def _pcc_gregorian_from_date(gdate):
    year = gdate.year
    month = gdate.month
    day = gdate.day
    return [year, month, day]

def gregorian_from_chinese(cdate):
    pcc_cdate = _pcc_chinese_from_tuple(cdate)
    pcc_gdate = gregorian_from_fixed(fixed_from_chinese(pcc_cdate))
    return _date_from_pcc_gregorian(pcc_gdate)

def chinese_from_gregorian(gdate):
    pcc_gdate = _pcc_gregorian_from_date(gdate)
    pcc_cdate = chinese_from_fixed(fixed_from_gregorian(pcc_gdate))
    return _tuple_from_pcc_chinese(pcc_cdate)

def get_branch(cdate):
    return (cdate.year - 4) % 12

def get_stem(cdate):
    return (cdate.year - 4) % 10

def is_valid_chinese_date(cdate):
    pcc_cdate = _pcc_chinese_from_tuple(cdate)
    cdate2 = chinese_from_fixed(fixed_from_chinese(pcc_cdate))
    return cdate2 == pcc_cdate

