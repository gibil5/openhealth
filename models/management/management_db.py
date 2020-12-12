# -*- coding: utf-8 -*-
"""
    Management Db - Database access

    SRP
        Responsibility of this class:
        Provide access to the db.

    Interface
		get_orders_filter_by_doctor

    Created:             11 dec 2020
    Last up:             11 dec 2020
"""
from __future__ import print_function
import datetime

# ------------------------------------------------------------- Constants ------
_DATE_FORMAT = "%Y-%m-%d"
_DATE_HOUR_FORMAT = "%Y-%m-%d %H:%M"

# ------------------------------------------------------------------- Class -----------------------
class ManagementDb(object):
    """
    ManagementDb
    """
    _name = 'openhealth.management_db'

# ---------------------------------------------------- Static methods ----------
    # Get
    #@classmethod
    @staticmethod
    def get_orders_filter_by_doctor(obj, date_bx, date_ex, doctor):
    	"""
    	Provides sales between begin date and end date. Filters: by Doctor.
    	Used by - Management
    	"""
    	#print()
    	#print('get_orders_filter_by_doctor')

        env = obj.env['sale.order']

    	# Init
    	# Dates
    	date_begin = date_bx + ' 05:00:00'
    	date_end_dt = datetime.datetime.strptime(date_ex, _DATE_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)
    	date_end = date_end_dt.strftime(_DATE_HOUR_FORMAT)

    	# Search
    	orders = env.search([
								('state', 'in', ['sale', 'credit_note']),
								('date_order', '>=', date_begin),
								('date_order', '<', date_end),
								('x_doctor', '=', doctor),
								('x_legacy', '=', False),
						    ],
							order='x_serial_nr asc',
                            )
    	# Count
    	count = env.search_count([
									('state', 'in', ['sale', 'credit_note']),
									('date_order', '>=', date_begin),
									('date_order', '<', date_end),
									('x_doctor', '=', doctor),
									('x_legacy', '=', False),
    							],
                                )
    	return orders, count

    # get_orders_filter_by_doctor
