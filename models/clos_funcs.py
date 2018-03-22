# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime







# ----------------------------------------------------------- Funcs ------------------------------------------------------

@api.multi
#def get_dates(self, date):
#def get_orders(self, date):
def get_orders(self, date, x_type):


	print 'jx'
	print 'Get Orders'

	print date 


	#DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
	DATETIME_FORMAT = "%Y-%m-%d"

	date_begin = date + ' 05:00:00'


	date_end_dt  = datetime.datetime.strptime(date, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5,minutes=0)
	#print date_end_dt
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')



	if x_type == 'all': 
		
		orders = self.env['sale.order'].search([
												('state', '=', 'sale'),														
																												
												('date_order', '>=', date_begin),

												('date_order', '<', date_end),									
											])


	else: 

		orders = self.env['sale.order'].search([
												('state', '=', 'sale'),														
																												
												('date_order', '>=', date_begin),

												('date_order', '<', date_end),									
												
												('x_type', '=', x_type),																												
											])






	print date_begin
	print date_end
	print orders  
	
	#return date_begin, date_end
	return orders  








# ----------------------------------------------------------- Funcs ------------------------------------------------------
@api.multi
def update_orders(self, date):

	print 'jx'
	print 'Get Orders'


	orders = get_orders(self, date)
	print orders

	for order in orders: 
		order.update_type()
		#print order.x_type 

