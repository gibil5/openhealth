# -*- coding: utf-8 -*-
"""
	Mgt Db
        Database search and count for the models:
            SaleOrder

	Created: 		26 oct 2020
	Last up: 		26 oct 2020

	Signature
		get_orders_filter_fast
		get_orders_filter
		get_orders_filter_by_doctor
"""
from __future__ import print_function
import datetime

# ------------------------------------------------------------- Constants ------
_DATE_FORMAT = "%Y-%m-%d"
_DATE_HOUR_FORMAT = "%Y-%m-%d %H:%M"
_MODEL_SALE = "sale.order"


# -------------------------------------------------------- Get Orders Fast -----
# States: In State Array
def get_orders_filter_fast(self, date_bx, date_ex):
	"""
	Used by: 
		management
		day_line
		productivity
	"""
	#print('')
	#print('Get Orders - Fast')

	# Init
	DATETIME_FORMAT = _DATE_FORMAT
	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)
	date_begin = date_bx + ' 05:00:00'
	date_end = date_end_dt.strftime(_DATE_HOUR_FORMAT)

	# Search
	orders = self.env[_MODEL_SALE].search([
													('state', 'in', ['sale', 'credit_note']),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_legacy', '=', False),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	# Count
	count = self.env[_MODEL_SALE].search_count([
													('state', 'in', ['sale', 'credit_note']),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_legacy', '=', False),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	return orders, count
# get_orders_filter_fast


# ---------------------------------------------- Get orders - Filter -----------
def get_orders_filter(self, date_bx, date_ex, state_arr, type_arr):
	"""
	Used by 
		management
	"""
	#print()
	#print('Get Orders - Filter')
	#print(date_bx)
	#print(date_ex)
	#print(state_arr)
	#print(type_arr)

	# Init
	DATETIME_FORMAT = _DATE_FORMAT
	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)
	date_begin = date_bx + ' 05:00:00'
	date_end = date_end_dt.strftime(_DATE_HOUR_FORMAT)

	_dic_states = {
					'sale,cancel,credit_note': 	['sale', 'cancel', 'credit_note'],
					'sale,cancel': 	['sale', 'cancel'],
					'sale': 		['sale'],
					'cancel': 		['cancel'],
	}

	_dic_types = {
					'ticket_receipt,ticket_invoice,receipt,invoice,sale_note,advertisement': ['ticket_receipt', 'ticket_invoice', 'receipt', 'invoice', 'sale_note', 'advertisement'],
					'ticket_receipt,ticket_invoice': 	['ticket_receipt', 'ticket_invoice'],
					'ticket_receipt': 					['ticket_receipt'],
					'ticket_invoice': 					['ticket_invoice'],
					'ticket_receipt,ticket_invoice,receipt,invoice': \
																	['ticket_receipt', 'ticket_invoice', 'receipt', 'invoice'],
	}


	if state_arr in _dic_states and type_arr in _dic_types:

		# Search
		orders = self.env[_MODEL_SALE].search([
													('state', 'in', _dic_states[state_arr]),
													('x_type', 'in', _dic_types[type_arr]),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_legacy', '=', False),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)
		# Count
		count = self.env[_MODEL_SALE].search_count([
														('state', 'in', _dic_states[state_arr]),
														('x_type', 'in', _dic_types[type_arr]),
														('date_order', '>=', date_begin),
														('date_order', '<', date_end),
														('x_legacy', '=', False),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)
	else:
		# Search
		orders = self.env[_MODEL_SALE].search([
													('name', '=', 'This does note exist !'),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)
		# Count
		count = 0

	return orders, count
# get_orders_filter


# ----------------------------------------------------------- Get orders - By Doctor --------------
def get_orders_filter_by_doctor(self, date_bx, date_ex, doctor):
	"""
	Provides sales between begin date and end date. Filters: by Doctor.
	Used by
		management
	"""
	#print()
	#print('PL - Get Orders Filter - By Doctor')

	# Init
	# Dates
	#DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
	date_begin = date_bx + ' 05:00:00'
	DATETIME_FORMAT = _DATE_FORMAT
	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)
	date_end = date_end_dt.strftime(_DATE_HOUR_FORMAT)

	# Prints
	#print date_end_dt

	# Search
	orders = self.env[_MODEL_SALE].search([
													('state', 'in', ['sale', 'credit_note']),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_doctor', '=', doctor),
													('x_legacy', '=', False),
											],
												order='x_serial_nr asc',
												#limit=1,
											)
	# Count
	count = self.env[_MODEL_SALE].search_count([
													('state', 'in', ['sale', 'credit_note']),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_doctor', '=', doctor),
													('x_legacy', '=', False),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	return orders, count

# get_orders_filter_by_doctor