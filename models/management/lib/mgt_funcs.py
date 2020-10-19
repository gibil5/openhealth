# -*- coding: utf-8 -*-
"""
	Mgt Funcs

	Created: 			28 May 2018
	Last mod: 			12 Dec 2019

	- The goal of functions is to hide Implementation.
"""
from __future__ import print_function
import datetime
from openerp.addons.price_list.models.lib import test_funcs


# ----------------------------------------------------------- Set Ratios --------------------------------------------
def set_ratios(self):
	"""
	Set Ratios
	"""
	#print()
	#print('Set Ratios')

	# Set Ratios
	if self.nr_consultations != 0:
		self.ratio_pro_con = (float(self.nr_procedures) / float(self.nr_consultations))

# set_ratios


# ----------------------------------------------------------- Set Totals --------------------------------------------
def set_totals(self, tickets):
	"""
	Set Totals
	"""
	#print()
	#print('Set Totals')

	# Set Totals
	self.total_amount = self.amo_products + self.amo_services + self.amo_other + self.amo_credit_notes
	self.total_count = self.nr_products + self.nr_services
	self.total_tickets = tickets

# set_totals


# ----------------------------------------------------------- Set Percentages --------------------------------------------
def set_percentages(self):
	"""
	Set Percentages
	"""
	#print()
	#print('Set Percentages')

	# Set Percentages


	# By Month
	if self.total_amount != 0:

		self.per_amo_other = (self.amo_other / self.total_amount)


		# Families
		self.per_amo_credit_notes = (self.amo_credit_notes / self.total_amount)

		self.per_amo_products = (self.amo_products / self.total_amount)
		self.per_amo_consultations = (self.amo_consultations / self.total_amount)
		self.per_amo_procedures = (self.amo_procedures / self.total_amount)


		# Sub Families
		self.per_amo_sub_con_med = (self.amo_sub_con_med / self.total_amount)
		self.per_amo_sub_con_gyn = (self.amo_sub_con_gyn / self.total_amount)
		self.per_amo_sub_con_cha = (self.amo_sub_con_cha / self.total_amount)


		self.per_amo_echo = (self.amo_echo / self.total_amount)
		self.per_amo_gyn = (self.amo_gyn / self.total_amount)
		self.per_amo_prom = (self.amo_prom / self.total_amount)

		self.per_amo_topical = (self.amo_topical / self.total_amount)
		self.per_amo_card = (self.amo_card / self.total_amount)
		self.per_amo_kit = (self.amo_kit / self.total_amount)

		self.per_amo_co2 = (self.amo_co2 / self.total_amount)
		self.per_amo_exc = (self.amo_exc / self.total_amount)
		self.per_amo_ipl = (self.amo_ipl / self.total_amount)
		self.per_amo_ndyag = (self.amo_ndyag / self.total_amount)
		self.per_amo_quick = (self.amo_quick / self.total_amount)

		self.per_amo_medical = (self.amo_medical / self.total_amount)
		self.per_amo_cosmetology = (self.amo_cosmetology / self.total_amount)


	# By Year - Dep !!!
	#if self.total_amount_year != 0:
	#		self.per_amo_total = self.total_amount / self.total_amount_year

# set_percentages



# ----------------------------------------------------------- Set Averages --------------------------------------------
def set_averages(self):
	"""
	Set Averages
	"""
	#print()
	#print('Set Averages')


# Families
	if self.nr_other != 0:
		self.avg_other = self.amo_other / self.nr_other

	if self.nr_products != 0:
		self.avg_products = self.amo_products / self.nr_products

	if self.nr_services != 0:
		self.avg_services = self.amo_services / self.nr_services

	if self.nr_consultations != 0:
		self.avg_consultations = self.amo_consultations / self.nr_consultations

	if self.nr_procedures != 0:
		self.avg_procedures = self.amo_procedures / self.nr_procedures


# Subfamilies
	if self.nr_topical != 0:
		self.avg_topical = self.amo_topical / self.nr_topical

	if self.nr_card != 0:
		self.avg_card = self.amo_card / self.nr_card

	if self.nr_kit != 0:
		self.avg_kit = self.amo_kit / self.nr_kit

	if self.nr_co2 != 0:
		self.avg_co2 = self.amo_co2 / self.nr_co2

	if self.nr_exc != 0:
		self.avg_exc = self.amo_exc / self.nr_exc

	if self.nr_ipl != 0:
		self.avg_ipl = self.amo_ipl / self.nr_ipl

	if self.nr_ndyag != 0:
		self.avg_ndyag = self.amo_ndyag / self.nr_ndyag

	if self.nr_quick != 0:
		self.avg_quick = self.amo_quick / self.nr_quick

	if self.nr_medical != 0:
		self.avg_medical = self.amo_medical / self.nr_medical

	if self.nr_cosmetology != 0:
		self.avg_cosmetology = self.amo_cosmetology / self.nr_cosmetology

	if self.nr_echo != 0:
		self.avg_echo = self.amo_echo / self.nr_echo

	if self.nr_gyn != 0:
		self.avg_gyn = self.amo_gyn / self.nr_gyn

	if self.nr_prom != 0:
		self.avg_prom = self.amo_prom / self.nr_prom

# set_averages



# ----------------------------------------------------------- Get orders - By Patient - Drafts --------------
def get_orders_filter_fast_patient_draft(self, date_bx, date_ex, patient):
	"""
	Only Drafts.
	"""
	#print()
	#print('Pl - Get Orders Filter Fast - Patient - Draft')


	# Init
	# Dates
	#DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
	date_begin = date_bx + ' 05:00:00'
	DATETIME_FORMAT = "%Y-%m-%d"

	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)

	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')

	# Prints
	#print date_end_dt


	# Search

	# Orders
	orders = self.env['sale.order'].search([
													('state', 'in', ['draft']),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('patient', '=', patient),
													('x_legacy', '=', False),
											],
												order='x_serial_nr asc',
												#limit=1,
											)
	# Count
	count = self.env['sale.order'].search_count([
													('state', 'in', ['draft']),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('patient', '=', patient),
													('x_legacy', '=', False),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	return orders, count

# get_orders_filter_fast_patient_draft



# ----------------------------------------------------------- Get orders - By Patient --------------
def get_orders_filter_fast_patient(self, date_bx, date_ex, patient):
	"""
	Only Sales.
	"""
	#print()
	#print('Pl - Get Orders Filter Fast - Patient')


	# Init
	# Dates
	#DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
	date_begin = date_bx + ' 05:00:00'
	DATETIME_FORMAT = "%Y-%m-%d"

	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)

	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')

	# Prints
	#print date_end_dt


	# Search

	# Orders
	orders = self.env['sale.order'].search([
													#('state', 'in', ['sale', 'credit_note']),
													#('state', '=', 'sale'),
													('state', 'in', ['sale']),

													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													
													('patient', '=', patient),
													('x_legacy', '=', False),
											],
												order='x_serial_nr asc',
												#limit=1,
											)
	# Count
	count = self.env['sale.order'].search_count([
													#('state', 'in', ['sale', 'credit_note']),
													#('state', '=', 'sale'),
													('state', 'in', ['sale']),

													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													
													('patient', '=', patient),
													('x_legacy', '=', False),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	return orders, count

# get_orders_filter_fast_patient




# ----------------------------------------------------------- Get Orders Fast -------------------
# States: In State Array
def get_orders_filter_fast(self, date_bx, date_ex):
	"""
	high level support for doing this and that.
	"""
	#print('')
	#print('Get Orders - Fast')


	# Init
	DATETIME_FORMAT = "%Y-%m-%d"

	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)

	date_begin = date_bx + ' 05:00:00'
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')



	# Orders
	orders = self.env['sale.order'].search([
													#('state', 'in', ['sale']),
													('state', 'in', ['sale', 'credit_note']),

													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_legacy', '=', False),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	# Count
	count = self.env['sale.order'].search_count([
													#('state', 'in', ['sale']),
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




# ---------------------------------------------- Get orders - Filter ------------------------------
# States: In State Array
def get_orders_filter(self, date_bx, date_ex, state_arr, type_arr):
	"""
	high level support for doing this and that.
	"""
	#print()
	#print('Get Orders - Filter')
	#print(date_bx)
	#print(date_ex)
	#print(state_arr)
	#print(type_arr)

	# Init
	DATETIME_FORMAT = "%Y-%m-%d"

	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)

	date_begin = date_bx + ' 05:00:00'
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')

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
		orders = self.env['sale.order'].search([
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
		count = self.env['sale.order'].search_count([
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
		orders = self.env['sale.order'].search([
													('name', '=', 'This does note exist !'),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)
		# Count
		count = 0

	return orders, count
# get_orders_filter




# ----------------------------------------------------------- Get Orders By Type ------------------

def get_orders_filter_type(self, date_bx, date_ex, x_type):
	"""
	high level support for doing this and that.
	"""

	# Dates
	DATETIME_FORMAT = "%Y-%m-%d"
	date_begin = date_bx + ' 05:00:00'

	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)

	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')


	# Orders
	orders = self.env['sale.order'].search([
													('state', 'in', ['sale', 'cancel']),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_type', '=', x_type),
											],
												#order='x_serial_nr asc',
												order='x_counter_value asc',
												#limit=1,
											)

	# Count
	count = self.env['sale.order'].search_count([
													('state', 'in', ['sale', 'cancel']),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_type', '=', x_type),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)

	return orders, count

# get_orders_filter_type






# ----------------------------------------------------------- Get orders - By Doctor --------------
# Provides sales between begin date and end date. Filters: by Doctor.
def get_orders_filter_by_doctor(self, date_bx, date_ex, doctor):
	"""
	Sales.
	Must include Credit Notes.
	"""
	#print()
	#print('PL - Get Orders Filter - By Doctor')


	# Init
	# Dates
	#DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
	date_begin = date_bx + ' 05:00:00'
	DATETIME_FORMAT = "%Y-%m-%d"

	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)

	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')

	# Prints
	#print date_end_dt


	# Search

	# Orders
	orders = self.env['sale.order'].search([
													#('state', '=', 'sale'),
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
	count = self.env['sale.order'].search_count([
													#('state', '=', 'sale'),
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
