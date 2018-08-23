

# ----------------------------------------------------------- Get orders ------------------------------------------------------

@api.multi
def get_orders(self, date):

	print
	print 'Get Orders One'

	count = 0 

	# Date 
	#DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
	DATETIME_FORMAT = "%Y-%m-%d"
	date_begin = date + ' 05:00:00'
	date_end_dt  = datetime.datetime.strptime(date, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5,minutes=0)
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')
	#print date 
	#print date_end_dt


	# Categ 
	#categ_name = 'Cremas'
	#categ =  self.env['product.category'].search([
	#												('name', '=', categ_name),
	#										],
												#order='x_serial_nr asc',
	#											limit=1,
	#										)
	#categ_id = categ.id 


	# Orders 
	orders = self.env['sale.order'].search([
													('state', '=', 'sale'),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),

													#('categ_id', '=', categ_id),
											],
												order='x_serial_nr asc',
												#limit=1,
											)

	count = self.env['sale.order'].search_count([
													('state', '=', 'sale'),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),

													#('categ_id', '=', categ_id),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)

	#print date_begin
	#print date_end
	#print orders  
	
	return orders, count



