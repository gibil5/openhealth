# -*- coding: utf-8 -*-
"""
    Management Db - Database access

    SRP
        Responsibility of this class:
        Odoo Database implementor

    Pattern
        Bridge

    Interface
        init(env, date_begin, date_end, doctor)
        search_orders_doctor
        count_orders_doctor

    Todo

    Created:             13 dec 2020
    Last up:             13 dec 2020
"""
from __future__ import print_function
from __future__ import absolute_import

#import datetime

# ----------------------------------------------------------- Constants --------

# ------------------------------------------------------------------- Class -----------------------
class OdooDbImpl(object):
    """
    Odoo Database implementor
    """
    #_name = 'openhealth.management_db'

    def __init__(self, env, date_begin, date_end, doctor):
        self.env = env
        self.date_begin = date_begin
        self.date_end = date_end
        self.doctor = doctor


# ---------------------------------------------- search_orders ---
    def search_orders_doctor(self):
        """
        Search objects
        """
        objs = self.env.search([
                                ('state', 'in', ['sale', 'credit_note']),
                                ('date_order', '>=', self.date_begin),
                                ('date_order', '<', self.date_end),
                                ('x_doctor', '=', self.doctor),
                                ('x_legacy', '=', False),
                            ],
                            order='x_serial_nr asc',
                            )
        return objs


# ---------------------------------------------- count_orders ---
    def count_orders_doctor(self):
        """
        Count objects
        """

        count = self.env.search_count([
                                    ('state', 'in', ['sale', 'credit_note']),
                                    ('date_order', '>=', self.date_begin),
                                    ('date_order', '<', self.date_end),
                                    ('x_doctor', '=', self.doctor),
                                    ('x_legacy', '=', False),
                                ],
                                )
        return count
