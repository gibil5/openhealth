# -*- coding: utf-8 -*-
"""
		Lib - 3rd Level
		Used by Clos Funcs

 		Created: 			30 Dec 2019
		Last up: 	 		30 Dec 2019

		Abstract, General purpose. Provider of services.
"""
from __future__ import print_function
import datetime



# ----------------------------------------------------------- Get Orders By State -----------------
def get_orders_by_state_all(self, date):
	"""
	26 Nov 2019: Only used by Closings
	To include Credit notes in Closing generation.
	"""
	#print()
	#print('2019 - Get Orders State')


	# Init
	count = 0
	DATETIME_FORMAT = "%Y-%m-%d"
	date_begin = date + ' 05:00:00'
	date_end_dt = datetime.datetime.strptime(date, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')

	# Search
	orders = self.env['sale.order'].search([
												#('state', '=', state),
												('state', 'in', ['sale', 'credit_note']),

												('date_order', '>=', date_begin),
												('date_order', '<', date_end),
										])
	count = self.env['sale.order'].search_count([
												#('state', '=', state),
												('state', 'in', ['sale', 'credit_note']),

												('date_order', '>=', date_begin),
												('date_order', '<', date_end),
										])
	return orders, count

# get_orders_by_state_all




# ----------------------------------------------------------- Get Orders --------------------------

def get_orders(self, date, x_type):
	"""
	15 Feb 2019: Added Filter Block
	"""
	#print()
	#print('Get Orders')
	#print(date)
	#print(x_type)


	# Init
	count = 0
	DATETIME_FORMAT = "%Y-%m-%d"
	date_begin = date + ' 05:00:00'
	date_end_dt = datetime.datetime.strptime(date, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')


	# Search If All
	if x_type == 'all':
		orders = self.env['sale.order'].search([
													('state', '=', 'sale'),

													('x_block_flow', 'not in', [True]),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
											])
		count = self.env['sale.order'].search_count([
													('state', '=', 'sale'),

													('x_block_flow', 'not in', [True]),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
											])


	# Search If Other
	else:
		orders = self.env['sale.order'].search([
													('x_block_flow', 'not in', [True]),

													('state', '=', 'sale'),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_type', '=', x_type),
											],
												order='x_serial_nr asc',
												#limit=1,
											)
		count = self.env['sale.order'].search_count([
													('x_block_flow', 'not in', [True]),

													('state', '=', 'sale'),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_type', '=', x_type),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)


	return orders, count

# get_orders










# ----------------------------------------------------------- Get Orders By State -----------------
def get_orders_by_state(self, date, state):
	"""
	"""
	#print()
	#print('Get Orders State')


	# Init
	count = 0
	DATETIME_FORMAT = "%Y-%m-%d"
	date_begin = date + ' 05:00:00'
	date_end_dt = datetime.datetime.strptime(date, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')

	# Search
	orders = self.env['sale.order'].search([
												('state', '=', state),

												('date_order', '>=', date_begin),
												('date_order', '<', date_end),
										])
	count = self.env['sale.order'].search_count([
												('state', '=', state),

												('date_order', '>=', date_begin),
												('date_order', '<', date_end),
										])
	return orders, count

# get_orders_by_state





# ----------------------------------------------------------- Get Gen Totals Proof ---------------------------
#def get_gen_totals(self):
def get_gen_totals(self, date, x_type):
	"""
	For an order type. 
	Returns total and serial numbers
	"""
	#print()
	#print('Get Generic Totals')


	# Get
	#orders, count = get_orders(self, self.date, self.x_type)
	orders, count = get_orders(self, date, x_type)


	# Init
	total = 0


	# Loop
	for order in orders:
		# Filter Block
		#if not order.x_block_flow:	
		total = total + order.amount_untaxed


	# Assign
	gen_tot = total

	if count != 0:
		serial_nr_first = orders[0].x_serial_nr
		serial_nr_last = orders[-1].x_serial_nr
	else:
		serial_nr_first = ''
		serial_nr_last = ''

	return gen_tot, serial_nr_first, serial_nr_last

	# get_gen_totals



