# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime




# ----------------------------------------------------------- Get orders ------------------------------------------------------

# Provides sales between begin date and end date. 
@api.multi
#def get_orders_filter(self, date_bx, date_ex):
def get_orders_filter(self, date_bx, date_ex, doctor):

	#print
	#print 'Get Orders Two'



	# Dates	
	#DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
	DATETIME_FORMAT = "%Y-%m-%d"

	#date_begin = date + ' 05:00:00'
	date_begin = date_bx + ' 05:00:00'

	#date_end_dt  = datetime.datetime.strptime(date, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5,minutes=0)
	date_end_dt  = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5,minutes=0)
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')
	#print date_end_dt






	# Orders 
	if doctor == 'all': 
	
		orders = self.env['sale.order'].search([
														('state', '=', 'sale'),

														('date_order', '>=', date_begin),													
														('date_order', '<', date_end),

														#('categ_id', '=', categ_id),
												],
													order='x_serial_nr asc',
													#limit=1,
												)

		# Count 
		count = self.env['sale.order'].search_count([
														('state', '=', 'sale'),

														('date_order', '>=', date_begin),
														('date_order', '<', date_end),

														#('categ_id', '=', categ_id),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)


	else:

		orders = self.env['sale.order'].search([
														('state', '=', 'sale'),

														('date_order', '>=', date_begin),													
														('date_order', '<', date_end),

														('x_doctor', '=', doctor),
												],
													order='x_serial_nr asc',
													#limit=1,
												)

		# Count 
		count = self.env['sale.order'].search_count([
														('state', '=', 'sale'),

														('date_order', '>=', date_begin),
														('date_order', '<', date_end),

														('x_doctor', '=', doctor),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)





	#count = 0 

	return orders, count


# get_orders_filter

