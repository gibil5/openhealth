# 13 Dec 2019




# ----------------------------------------------------------- Mkt - Get Orders Faster -------------------
# States: In State Array
def get_orders_filter_fast_fast(self, date_bx, date_ex):
	"""
	Only Used by Marketing ?

	Only Sales and Canceled. Not Credit Notes. 
	"""
	#print()
	#print('Pl - Get Orders - Fast Fast')


	# Init
	DATETIME_FORMAT = "%Y-%m-%d"

	date_end_dt = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + \
																		datetime.timedelta(hours=24) + datetime.timedelta(hours=5, minutes=0)

	date_begin = date_bx + ' 05:00:00'
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')


	print(date_begin)
	print(date_end)


	# Orders
	orders = self.env['sale.order'].search([
													#('state', 'in', ['sale']),
													('state', 'in', ['sale', 'draft']),

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
													('state', 'in', ['sale', 'draft']),

													('date_order', '>=', date_begin),
													('date_order', '<', date_end),

													('x_legacy', '=', False),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
	return orders, count

# get_orders_filter_fast_fast
