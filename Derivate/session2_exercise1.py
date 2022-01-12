# -*- coding: utf-8 -*-

# Derivate
# --------
# Derivative Finanzinstrumente (created by auxilium)
#
# Author:   Jan-Philipp Hoffmann
# Version:  0.1, copyright Tuesday, 16 November 2021
# Website:  https://www.h-da.de
# License:  Apache License 2.0 (see LICENSE file)


from businessdate import BusinessDate as _BusinessDate
from dcf import get_present_value as _get_present_value
from dcf import CashFlowLegList as _CashFlowLegList
from dcf import ZeroRateCurve as _ZeroRateCurve, \
    CashRateCurve as _CashRateCurve


def get_basis_point_value(cashflow_list, discount_curve,
                          valuation_date=None, delta_curve=None,
                          **kwargs):
    # tested by `test_bond_bpv()` in `regtests.py`
    """ value of one basis point change in interest rates

    :param cashflow_list: cashflow product for valuation
    :param discount_curve: discount curve for valuation
    :param valuation_date: date of valuation
    :param delta_curve: interest rate curve to change interest rates
    :param kwargs: additional argument for *get_present_value* function
    :return:
    """
    if isinstance(cashflow_list, _CashFlowLegList):
        return sum(get_basis_point_value(leg, discount_curve, delta_curve,
                                         valuation_date, **kwargs)
                   for leg in cashflow_list.legs)
    # check if curve is CashRateCurve
    basis_point_curve_type = _CashRateCurve \
        if isinstance(delta_curve, _CashRateCurve) else _ZeroRateCurve

    pv = _get_present_value(cashflow_list, discount_curve,
                            valuation_date, **kwargs)

    delta_curve = discount_curve if delta_curve is None else delta_curve
    shifted_curve = delta_curve + basis_point_curve_type(
        [_BusinessDate()], [0.0001])

    fwd_curve = getattr(cashflow_list, 'forward_curve', None)
    if fwd_curve == delta_curve:
        # replace delta_curve by shifted_curve
        cashflow_list.forward_curve = shifted_curve
    if delta_curve == discount_curve:
        sh = _get_present_value(cashflow_list, shifted_curve,
                                valuation_date, **kwargs)
    else:
        sh = _get_present_value(cashflow_list, discount_curve,
                                valuation_date, **kwargs)
    if fwd_curve == delta_curve:
        # restore delta_curve by shifted_curve
        cashflow_list.forward_curve = shifted_curve

    return sh - pv
