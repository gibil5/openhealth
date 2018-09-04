

# 1 Sep 2018 


# ----------------------------------------------------------- Get orders - All ------------------------------------------------------

def get_orders_filter_all(self, date_bx, date_ex):

	# Dates	
	DATETIME_FORMAT = "%Y-%m-%d"
	date_begin = date_bx + ' 05:00:00'
	date_end_dt  = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5,minutes=0)
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')


	# Orders 
	orders = self.env['sale.order'].search([
													#('state', '=', 'sale'),
													#('state', 'in', ['sale','cancel']),
													('state', 'in', ['sale','cancel','validated']),
													
													('date_order', '>=', date_begin),													
													('date_order', '<', date_end),
													
													#('x_type', '=', x_type),
													#('x_doctor', '=', doctor),
											],
												order='x_serial_nr asc',
												#limit=1,
											)

	# Count 
	count = self.env['sale.order'].search_count([
													#('state', '=', 'sale'),
													#('state', 'in', ['sale','cancel']),
													('state', 'in', ['sale','cancel','validated']),
													
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													
													#('x_type', '=', x_type),
													#('x_doctor', '=', doctor),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)

	return orders, count

# get_orders_filter_all



# ----------------------------------------------------------- Get orders - By Type ------------------------------------------------------

def get_orders_filter_type(self, date_bx, date_ex, x_type):


	# Dates	
	DATETIME_FORMAT = "%Y-%m-%d"
	date_begin = date_bx + ' 05:00:00'
	date_end_dt  = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5,minutes=0)
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')






	# Orders 
	orders = self.env['sale.order'].search([
													#('state', '=', 'sale'),
													('state', 'in', ['sale','cancel']),
													
													('x_type', '=', x_type),

													('date_order', '>=', date_begin),													
													('date_order', '<', date_end),
													#('x_doctor', '=', doctor),
											],
												order='x_serial_nr asc',
												#limit=1,
											)

	# Count 
	count = self.env['sale.order'].search_count([
													#('state', '=', 'sale'),
													('state', 'in', ['sale','cancel']),
													
													('x_type', '=', x_type),

													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													#('x_doctor', '=', doctor),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)





	#count = 0 

	return orders, count

# get_orders_filter_type




# ----------------------------------------------------------- Get orders - By Doctor ------------------------------------------------------
# Provides sales between begin date and end date. Filters: by Doctor. 
def get_orders_filter_by_doctor(self, date_bx, date_ex, doctor):
	#print
	#print 'Get Orders - By Doctor'

	# Orders 
	if doctor == 'all': 

		# Orders 
		orders = self.env['sale.order'].search([
														('state', '=', 'sale'),
														('date_order', '>=', date_begin),													
														('date_order', '<', date_end),
														('x_legacy', '=', False),
												],
													order='x_serial_nr asc',
													#limit=1,
												)
		# Count 
		count = self.env['sale.order'].search_count([
														('state', '=', 'sale'),
														('date_order', '>=', date_begin),
														('date_order', '<', date_end),
														('x_legacy', '=', False),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)

	else:		# By Doctor 





