# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime





# ----------------------------------------------------------- Calculate Percentages ------------------------------------------------------

# Provides Percentage

@api.multi
def get_per(self, value, total): 
	per = 0 
	if total != 0: 
		per = ( float(value) / float(total) ) * 100
	return per 






# ----------------------------------------------------------- Get Patients ------------------------------------------------------

# Provides Patients between begin date and end date. 

@api.multi
#def get_patients_filter(self, date_bx, date_ex):
def get_patients_filter(self, date_bx, date_ex, mode):

	print
	print 'Get Patients'


	# Dates	
	DATETIME_FORMAT = "%Y-%m-%d"

	date_begin = date_bx + ' 05:00:00'
	
	date_end_dt  = datetime.datetime.strptime(date_ex, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5,minutes=0)
	
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')



	# Legacy 
	if mode == 'legacy': 

		# Patients 
		patients = self.env['oeh.medical.patient'].search([
															('create_date', '>=', date_begin),													
															('create_date', '<', date_end),

															#('x_date_record', '>=', date_begin),													
															#('x_date_record', '<', date_end),
												],
													order='create_date asc',
													#limit=1,
													#limit=500,
												)

		# Count 
		count = self.env['oeh.medical.patient'].search_count([													
															('create_date', '>=', date_begin),
															('create_date', '<', date_end),
															
															#('x_date_record', '>=', date_begin),
															#('x_date_record', '<', date_end),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)


	# Normal 
	#elif mode == 'normal': 
	else:
		# Patients 
		patients = self.env['oeh.medical.patient'].search([
															#('create_date', '>=', date_begin),													
															#('create_date', '<', date_end),

															('x_date_record', '>=', date_begin),													
															('x_date_record', '<', date_end),
												],
													order='create_date asc',
													#limit=1,
													#limit=500,
												)

		# Count 
		count = self.env['oeh.medical.patient'].search_count([													
															#('create_date', '>=', date_begin),
															#('create_date', '<', date_end),
															
															('x_date_record', '>=', date_begin),
															('x_date_record', '<', date_end),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)



	return patients, count

# get_patients_filter





# ----------------------------------------------------------- Get orders ------------------------------------------------------

# Provides sales between begin date and end date. 
@api.multi
def get_orders_filter(self, date_bx, date_ex):

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
	orders = self.env['sale.order'].search([

													#('state', '=', 'sale'),
													('state', 'in', ['sale','cancel']),


													('date_order', '>=', date_begin),													
													('date_order', '<', date_end),

													#('categ_id', '=', categ_id),
											],
												order='x_serial_nr asc',
												#limit=1,
											)

	# Count 
	count = self.env['sale.order'].search_count([

													#('state', '=', 'sale'),
													('state', 'in', ['sale','cancel']),
													

													('date_order', '>=', date_begin),
													('date_order', '<', date_end),

													#('categ_id', '=', categ_id),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)





	count = 0 

	return orders, count


# get_orders_filter




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

