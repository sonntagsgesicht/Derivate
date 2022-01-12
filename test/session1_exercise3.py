# -*- coding: utf-8 -*-

# auxilium
# --------
# A Python project for an automated test and deploy toolkit - 100%
# reusable.
#
# Author:   sonntagsgesicht
# Version:  0.1.4, copyright Sunday, 11 October 2020
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from unittest import TestCase
from businessdate import BusinessDate, BusinessPeriod, BusinessSchedule

from Derivate import BondCashFlowLegList


class BondCashFlowLegListUnitTests(TestCase):
    def test_bond(self):
        s, e = 20211027, 20261027
        payment_date_list = BusinessSchedule(
            start=BusinessDate(s),
            end=BusinessDate(e),
            step=BusinessPeriod('3m')
        )
        start_date = payment_date_list[0] - BusinessPeriod('3m')
        bond = BondCashFlowLegList(payment_date_list, 1, start_date=start_date)
        self.assertEqual(len(payment_date_list) + 1, len(bond.domain))
