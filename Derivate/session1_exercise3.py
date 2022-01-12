# -*- coding: utf-8 -*-

# Derivate
# --------
# Derivative Finanzinstrumente (created by auxilium)
#
# Author:   Jan-Philipp Hoffmann
# Version:  0.1, copyright Tuesday, 16 November 2021
# Website:  https://www.h-da.de
# License:  Apache License 2.0 (see LICENSE file)


from dcf import CashFlowLegList as _CashFlowLegList, \
    FixedCashFlowList as _FixedCashFlowList, \
    RateCashFlowList as _RateCashFlowList


class BondCashFlowLegList(_CashFlowLegList):
    # tested by `test_bond()` in `unittests.py`

    def __init__(self, payment_date_list, notional_amount=1.0, fixed_rate=0.0,
                 forward_curve=None, day_count=None, start_date=None):
        r""" Simple fixed rate bond

            :param payment_date_list: list of payment dates,
                last date in list sets the bond maturity
            :param notional_amount: bond notional amount
            :param fixed_rate: fixed interest rate
            :param forward_curve: InterestRateCurve
            :param day_count: day count convention function
                to calculate year fractions between two dates
            :param start_date: issue date of the bond

        """
        if start_date is None:
            # not very reasonable
            start_date = payment_date_list[0]

        end_date = payment_date_list[-1]
        notional_payment_date_list = start_date, end_date
        notional_amount_list = -notional_amount, notional_amount
        notional_leg = _FixedCashFlowList(
            payment_date_list=notional_payment_date_list,
            amount_list=notional_amount_list,
            origin=start_date
        )
        coupon_leg = _RateCashFlowList(
            payment_date_list=payment_date_list,
            amount_list=[notional_amount] * len(payment_date_list),
            fixed_rate=fixed_rate,
            forward_curve=forward_curve,
            day_count=day_count,
            origin=start_date
        )
        legs = notional_leg, coupon_leg
        super().__init__(legs)
