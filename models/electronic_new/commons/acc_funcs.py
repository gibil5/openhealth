# -*- coding: utf-8 -*-
"""
	Acc Funcs - Dep ?
	- Used by account_contasis

	Created: 			11 oct 2020
	Last up: 			 5 dec 2020
"""
import datetime

# ----------------------------------------------------------- Get Orders Filter -------------------
def get_orders_filter(self, date_bx, date_ex):
	"""
	Provides sales between begin date and end date.
	Sales and Cancelled also.
	"""
	# Dates
	DATETIME_FORMAT = "%Y-%m-%d"
	date_begin = date_bx + ' 05:00:00'
	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')
	#print date_end_dt

	# Search Orders
	orders = self.env['sale.order'].search([
													('state', 'in', ['sale', 'cancel']),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
											],
												order='x_serial_nr asc',
												#limit=1,
											)
	# Count
	count = self.env['sale.order'].search_count([
													('state', 'in', ['sale', 'cancel']),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	#count = 0
	return orders, count
# get_orders_filter


# ----------------------------------------------------------- Get Net and Tax ---------------------
def get_net_tax(amount):
	"""
	Get Net and Tax
	"""
	#x = amount / 1.18
	net = float("{0:.2f}".format(amount / 1.18))
	# Tax
	#x = amount * 0.18
	tax = float("{0:.2f}".format(amount * 0.18))
	return net, tax
# get_net_tax


#------------------------------------------------ Correct Time ------------------------------------
def correct_time(date, delta):
	"""
	Used by Account Line
	Correct Time
	Format: 	1876-10-10 00:00:00
	"""
	#print
	#print 'Correct'
	#print date
	# Print delta
	#if date != False:
	if date:
		year = int(date.split('-')[0])
		if year >= 1900:
			DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
			DATETIME_FORMAT_sp = "%d/%m/%Y %H:%M"
			date_field1 = datetime.datetime.strptime(date, DATETIME_FORMAT)
			date_corr = date_field1 + datetime.timedelta(hours=delta, minutes=0)
			date_corr_sp = date_corr.strftime(DATETIME_FORMAT_sp)
			return date_corr, date_corr_sp
# correct_time
