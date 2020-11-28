# -*- coding: utf-8 -*-
"""
    MgtProductCounter Class

    OpenErp independent

    Created:             31 oct 2020
    Last up:             31 oct 2020
"""

class MgtProductCounter():
    """
    Used by Management
    """

    def __init__(self, name):
        print()
        print('ProductCounter  -  init')
        print(name)
        self.name = name
        self.amount = 0.
        self.count = 0.


    def inc_amount(self, amount):
        self.amount += amount

    def inc_count(self, count):
        self.count += count

