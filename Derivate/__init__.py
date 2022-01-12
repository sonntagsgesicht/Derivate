# -*- coding: utf-8 -*-

# Derivate
# --------
# Derivative Finanzinstrumente (created by auxilium)
#
# Author:   Jan-Philipp Hoffmann
# Version:  0.1, copyright Tuesday, 16 November 2021
# Website:  https://www.h-da.de
# License:  Apache License 2.0 (see LICENSE file)


import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

__doc__ = 'Derivative Finanzinstrumente (created by auxilium)'
__license__ = 'Apache License 2.0'

__author__ = 'Jan-Philipp Hoffmann'
__email__ = 'jan-philipp.hoffmann@h-da.de'
__url__ = 'https://www.h-da.de'

__date__ = 'Wednesday, 12 January 2022'
__version__ = '0.1'
__dev_status__ = '3 - Alpha'  # '4 - Beta'  or '5 - Production/Stable'

__dependencies__ = 'businessdate', 'dcf'
__dependency_links__ = ()
__data__ = ()
__scripts__ = ()
__theme__ = ''


from .session1_exercise3 import BondCashFlowLegList # noqa F402
from .session2_exercise1 import get_basis_point_value # noqa F402
from .session2_exercise3 import * # noqa F402
from .session2_exercise4 import get_bucketed_delta # noqa F402

# this is just an example to demonstrate the auxilium workflow
# it can be removed safely


class Line(object):
    r""" This a example class (by auxilium)

    The |Line| objects implements a straight line,
    i.e. a function $y = f(x)$ with

    $$  f(x) = a + b \\cdot x  $$

    where $a$ and $b$ are numbers.

    >>> from Derivate import Line
    >>> a, b = 1, 2
    >>> line = Line(a, b)
    >>> line.y(x=3)
    7
    >>> line(3)  # Line objects are callable
    7
    >>> line.a
    1
    >>> line.b
    2

    """
    def __init__(self, a=0, b=1):
        r"""
        :param a: a value
        :param b: another value
        """
        self._a = a
        self._b = b

    @property
    def a(self):
        """ a value """
        return self._a

    @property
    def b(self):
        """ b value """
        return self._b

    def y(self, x=1):
        """ gives y value depending on x value argument

        :param x: x value
        :return: $a + b * x$

        """
        return self._a + self._b * x

    def __call__(self, x=1):
        return self.y(x)
