# -*- coding: utf-8 -*-
"""
	Management Db - Database access

	SRP
		Responsibility of this class:
		Encapsulates implementation of the access to the database (using Odoo ORM).

	Pattern
		Bridge

	Interface
		get_orders_filter_fast(management, date_bx, date_ex)
		get_orders_filter(management, date_bx, date_ex, state_arr, type_arr)
		get_orders_filter_by_doctor(management, date_bx, date_ex, doctor)
		get_orders_filter_by_patient(obj, patient)

	Todo
		Create a similar class for TinyDb.
		Create a superclass for both.

	Created:             11 dec 2020
	Last up:             13 dec 2020
"""
from __future__ import print_function
import datetime
from .odoo_db import OdooDbImpl

# ----------------------------------------------------------- Constants --------
_DATE_FORMAT = "%Y-%m-%d"
_DATE_HOUR_FORMAT = "%Y-%m-%d %H:%M"


# ------------------------------------------------------------------- Class -----------------------
class ManagementDb(object):
	"""
	ManagementDb
	"""
	_name = 'openhealth.management_db'


# ---------------------------------------------- get_orders_filter_by_doctor ---
	# Get
	@staticmethod
	def get_orders_filter_by_doctor(management, date_bx, date_ex, doctor):
		"""
		Provides sales between begin date and end date. Filters: by Doctor.
		Used by - Management
		"""
		#print()
		#print('get_orders_filter_by_doctor')

		env = management.env['sale.order']

		# Init
		# Dates
		date_begin = date_bx + ' 05:00:00'
		date_end_dt = datetime.datetime.strptime(date_ex, _DATE_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)
		date_end = date_end_dt.strftime(_DATE_HOUR_FORMAT)

		implementor = OdooDbImpl(env, date_begin, date_end, doctor)

		# Search
		#orders = env.search([
		orders = implementor.search_orders_doctor()

		# Count
		#count = env.search_count([
		count = implementor.count_orders_doctor()

		return orders, count

	# get_orders_filter_by_doctor


# -------------------------------------------------------- get_orders_filter ---
	@staticmethod
	def get_orders_filter(management, date_bx, date_ex, state_arr, type_arr):
		"""
		Used by
			Management
		"""
		#print()
		#print('Get Orders - Filter')
		#print(date_bx)
		#print(date_ex)
		#print(state_arr)
		#print(type_arr)

		# Init
		env = management.env['sale.order']

		date_end_dt = datetime.datetime.strptime(date_ex, _DATE_FORMAT) + \
																			datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)
		date_begin = date_bx + ' 05:00:00'
		date_end = date_end_dt.strftime(_DATE_HOUR_FORMAT)

		_dic_states = {
						'sale,cancel,credit_note':     ['sale', 'cancel', 'credit_note'],
						'sale,cancel':     ['sale', 'cancel'],
						'sale':         ['sale'],
						'cancel':         ['cancel'],
		}

		_dic_types = {
						'ticket_receipt,ticket_invoice,receipt,invoice,sale_note,advertisement': ['ticket_receipt', 'ticket_invoice', 'receipt', 'invoice', 'sale_note', 'advertisement'],
						'ticket_receipt,ticket_invoice':     ['ticket_receipt', 'ticket_invoice'],
						'ticket_receipt':                     ['ticket_receipt'],
						'ticket_invoice':                     ['ticket_invoice'],
						'ticket_receipt,ticket_invoice,receipt,invoice': \
																		['ticket_receipt', 'ticket_invoice', 'receipt', 'invoice'],
		}

		if state_arr in _dic_states and type_arr in _dic_types:

			#implementor = OdooDbImpl(env, date_begin, date_end, doctor)

			# Search
			#orders = implementor.search_orders_doctor()

			# Search
			orders = env.search([
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
			count = env.search_count([
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
			orders = env.search([
														('name', '=', 'This does note exist !'),
													],
														#order='x_serial_nr asc',
														#limit=1,
													)
			# Count
			count = 0

		return orders, count
	# get_orders_filter


# -------------------------------------------------- get_orders_filter_fast ----
	# States: In State Array
	@staticmethod
	def get_orders_filter_fast(management, date_bx, date_ex):
		"""
		Used by:
			Management
			Day_line
			Productivity
		"""
		#print('')
		#print('Get Orders - Fast')

		# Init
		env = management.env['sale.order']

		date_end_dt = datetime.datetime.strptime(date_ex, _DATE_FORMAT) + \
																			datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)
		date_begin = date_bx + ' 05:00:00'
		date_end = date_end_dt.strftime(_DATE_HOUR_FORMAT)

		# Search
		#orders = self.env[_MODEL_SALE].search([
		orders = env.search([
														('state', 'in', ['sale', 'credit_note']),
														('date_order', '>=', date_begin),
														('date_order', '<', date_end),
														('x_legacy', '=', False),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)
		# Count
		#count = self.env[_MODEL_SALE].search_count([
		count = env.search_count([
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


# --------------------------------------------- get_orders_filter_by_patient ---
	# Provides sales between begin date and end date. Filters: by patient.
	@staticmethod
	def get_orders_filter_by_patient(obj, patient):
		"""
		Sales.
		Must include Credit Notes.
		Used by - mgt_patient_line
		"""
		#print()
		#print('Get Orders Filter - By patient')

		env = obj.env['sale.order']

		# Search

		# Orders
		#orders = self.env['sale.order'].search([
		orders = env.search([
														#('state', '=', 'sale'),
														('state', 'in', ['sale', 'credit_note']),

														('patient', '=', patient),
												],
													order='x_serial_nr asc',
													#limit=1,
												)
		# Count
		#count = self.env['sale.order'].search_count([
		count = env.search_count([
														#('state', '=', 'sale'),
														('state', 'in', ['sale', 'credit_note']),

														('patient', '=', patient),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)
		return orders, count
	# get_orders_filter_by_patient_fast
