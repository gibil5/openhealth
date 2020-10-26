# -*- coding: utf-8 -*-
"""
	Mgt Funcs
	Should be unit testable - independent from openerp

	Created: 			28 May 2018
	Last updated: 		26 oct 2020

	- Use functional programming - ie pure functions.
	- Use lambda funcs, map, filter, reduce, decorators, generators, etc.
"""
from __future__ import print_function
import datetime

# ------------------------------------------------------------- Constants ------
_DATE_FORMAT = "%Y-%m-%d"
_DATE_HOUR_FORMAT = "%Y-%m-%d %H:%M"
_MODEL_SALE = "sale.order"


# --------------------------------------------------------------- Division -----
def division(amo, nr):
    return round(float(amo) / float(nr), 2) if nr else 0


# ----------------------------------------------------------- Set Averages -----
def averages_pure(vector, func=division):
	"""
	Set Averages Pure 
	Using functional programming
	Used by: Management
	"""
	print("\n")
	print(averages_pure)
	ave = []

	for data in vector: 
		tag = data[0]
		amo = data[1]
		nr = data[2]

		#ave.append(func(amo, nr))
		ave.append((tag, func(amo, nr)))

		print(amo, nr)
	
	print(ave)

	return ave
# averages_pure


# --------------------------------------------------------- Set Percentages ----
#def set_percentages(self):
def set_percentages(self, total_amount):
	"""
	Set Percentages
	Used by 
		Management
	"""
	# By Month
	if total_amount != 0:
		self.per_amo_other = (self.amo_other / total_amount)

		# Families
		self.per_amo_credit_notes = (self.amo_credit_notes / total_amount)
		self.per_amo_products = (self.amo_products / total_amount)
		self.per_amo_consultations = (self.amo_consultations / total_amount)
		self.per_amo_procedures = (self.amo_procedures / total_amount)

		# Sub Families
		self.per_amo_sub_con_med = (self.amo_sub_con_med / total_amount)
		self.per_amo_sub_con_gyn = (self.amo_sub_con_gyn / total_amount)
		self.per_amo_sub_con_cha = (self.amo_sub_con_cha / total_amount)

		self.per_amo_echo = (self.amo_echo / total_amount)
		self.per_amo_gyn = (self.amo_gyn / total_amount)
		self.per_amo_prom = (self.amo_prom / total_amount)

		self.per_amo_topical = (self.amo_topical / total_amount)
		self.per_amo_card = (self.amo_card / total_amount)
		self.per_amo_kit = (self.amo_kit / total_amount)

		self.per_amo_co2 = (self.amo_co2 / total_amount)
		self.per_amo_exc = (self.amo_exc / total_amount)
		self.per_amo_ipl = (self.amo_ipl / total_amount)
		self.per_amo_ndyag = (self.amo_ndyag / total_amount)
		self.per_amo_quick = (self.amo_quick / total_amount)

		self.per_amo_medical = (self.amo_medical / total_amount)
		self.per_amo_cosmetology = (self.amo_cosmetology / total_amount)
# set_percentages


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



	# Orders
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

		# Orders
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

		# Orders
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

	# Orders
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
