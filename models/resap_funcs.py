# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime









# ----------------------------------------------------------- Get orders ------------------------------------------------------
@api.multi
#def get_orders(self, date):
def get_orders_filter(self, date_bx, date_ex):

	print
	print 'Get Orders Two'




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





	count = 0 

	return orders, count






# ----------------------------------------------------------- Get orders ------------------------------------------------------

@api.multi
#def get_orders(self, date, categ_name):
def get_orders(self, date):


	print
	print 'Get Orders One'
	#print date 


	count = 0 




	# Date 
	#DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
	DATETIME_FORMAT = "%Y-%m-%d"

	date_begin = date + ' 05:00:00'

	date_end_dt  = datetime.datetime.strptime(date, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5,minutes=0)
	#print date_end_dt
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')






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

