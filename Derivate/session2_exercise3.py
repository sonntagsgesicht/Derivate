# -*- coding: utf-8 -*-

# Derivate
# --------
# Derivative Finanzinstrumente (created by auxilium)
#
# Author:   Jan-Philipp Hoffmann
# Version:  0.1, copyright Tuesday, 16 November 2021
# Website:  https://www.h-da.de
# License:  Apache License 2.0 (see LICENSE file)


from dcf import ZeroRateCurve, CashRateCurve
from businessdate import BusinessDate, BusinessPeriod

# --- businessdate version ---

today = BusinessDate(20211201)
tenor_1m = BusinessPeriod('1m')
tenor_3m = BusinessPeriod('3m')
tenor_6m = BusinessPeriod('6m')

zeros_term = '1y', '2y', '5y', '10y', '15y', '20y', '30y'
fwd_term = '2d', '3m', '6m', '1y', '2y', '5y', '10y'

# --- year fraction version ---

# today = 0.0
# tenor_1m = 1 / 12
# tenor_3m = 3 / 12
# tenor_6m = 6 / 12
#
# zeros_term = 1, 2, 5, 10, 15, 20, 30
# fwd_term = 2 / 365.25, 3 / 12, 6 / 12, 1, 2, 5, 10

zeros = -0.0084, -0.0079, -0.0057, -0.0024, -0.0008, -0.0001, 0.0003
fwd_1m = -0.0057, -0.0057, -0.0053, -0.0036, -0.0010, 0.0014, 0.0066
fwd_3m = -0.0056, -0.0054, -0.0048, -0.0033, -0.0002, 0.0018, 0.0066
fwd_6m = -0.0053, -0.0048, -0.0042, -0.0022, 0.0002, 0.0022, 0.0065

zero_curve = ZeroRateCurve([today + t for t in zeros_term], zeros,
                           origin=today)
fwd_curve_1m = CashRateCurve([today + t for t in fwd_term], fwd_1m,
                             origin=today, forward_tenor=tenor_1m)
fwd_curve_3m = CashRateCurve([today + t for t in fwd_term], fwd_3m,
                             origin=today, forward_tenor=tenor_3m)
fwd_curve_6m = CashRateCurve([today + t for t in fwd_term], fwd_6m,
                             origin=today, forward_tenor=tenor_6m)
