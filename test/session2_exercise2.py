from regtest import RegressionTestCase

from businessdate import BusinessSchedule

from dcf import FixedCashFlowList, RateCashFlowList, CashFlowLegList
from dcf import get_present_value, get_par_rate, get_basis_point_value

from Derivate import today as start, zero_curve, fwd_curve_1m, \
    fwd_curve_3m, fwd_curve_6m

notional = 1.0
maturities = '2y', '5y', '10y', '20y'


class BasisPointValueRegTests(RegressionTestCase):

    compression = False

    def test_bond_bpv(self):
        for maturity in maturities:
            end = start + maturity
            schedule = BusinessSchedule(start, end, '1y', end)
            rate_flows = RateCashFlowList(schedule, notional, fixed_rate=0.01)
            redemption_flows = FixedCashFlowList([end], [notional])
            zero_pv = get_present_value(redemption_flows, zero_curve, start)
            par_rate = get_par_rate(rate_flows, zero_curve, start, notional - zero_pv)
            rate_flows.fixed_rate = par_rate
            bond = CashFlowLegList([rate_flows, redemption_flows])

            self.assertAlmostRegressiveEqual(par_rate)
            self.assertAlmostEqual(notional, get_present_value(bond, zero_curve, start))
            self.assertAlmostRegressiveEqual(get_basis_point_value(bond, zero_curve, start))

    def test_swap_x_bpv(self):
        for maturity in maturities:
            end = start + maturity
            schedule = BusinessSchedule(start, end, '1y', end)
            schedule_3m = BusinessSchedule(start, end, '3m', end)
            float_leg = RateCashFlowList(schedule_3m, notional, forward_curve=zero_curve)
            float_pv = get_present_value(float_leg, zero_curve, start)
            fixed_leg = RateCashFlowList(schedule, -notional, fixed_rate=0.01)
            par_rate = get_par_rate(fixed_leg, zero_curve, start, -float_pv)
            fixed_leg.fixed_rate = par_rate
            swap = CashFlowLegList([float_leg, fixed_leg])

            self.assertAlmostRegressiveEqual(par_rate)
            self.assertAlmostEqual(0.0, get_present_value(swap, zero_curve, start))
            self.assertAlmostRegressiveEqual(get_basis_point_value(swap, zero_curve, start))

    def test_swap_y_bpv(self):
        for maturity in maturities:
            end = start + maturity
            schedule = BusinessSchedule(start, end, '1y', end)
            schedule_3m = BusinessSchedule(start, end, '3m', end)
            float_leg = RateCashFlowList(schedule_3m, notional, forward_curve=fwd_curve_3m)
            float_pv = get_present_value(float_leg, zero_curve, start)
            fixed_leg = RateCashFlowList(schedule, -notional, fixed_rate=0.01)
            par_rate = get_par_rate(fixed_leg, zero_curve, start, -float_pv)
            fixed_leg.fixed_rate = par_rate
            swap = CashFlowLegList([float_leg, fixed_leg])

            self.assertAlmostRegressiveEqual(par_rate)
            self.assertAlmostEqual(0.0, get_present_value(swap, zero_curve, start))
            self.assertAlmostRegressiveEqual(get_basis_point_value(swap, zero_curve, start))

    def test_swap_z_bpv(self):
        for maturity in maturities:
            end = start + maturity
            schedule_1m = BusinessSchedule(start, end, '1m', end)
            schedule_6m = BusinessSchedule(start, end, '6m', end)
            prime_float_leg = RateCashFlowList(schedule_6m, notional, forward_curve=fwd_curve_6m)
            float_pv = get_present_value(prime_float_leg, zero_curve, start)
            minor_float_leg = RateCashFlowList(schedule_1m, notional, forward_curve=fwd_curve_1m)
            par_rate = get_par_rate(minor_float_leg, zero_curve, start, -float_pv)
            minor_float_leg.fixed_rate = par_rate
            swap = CashFlowLegList([prime_float_leg, minor_float_leg])

            self.assertAlmostRegressiveEqual(par_rate)
            self.assertAlmostEqual(0.0, get_present_value(swap, zero_curve, start))
            self.assertAlmostRegressiveEqual(get_basis_point_value(swap, zero_curve, start))
