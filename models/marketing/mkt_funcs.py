# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime




# ----------------------------------------------------------- Calculate Percentages ------------------------------------------------------

# Provides Percentage
@api.multi
def get_per(self, value, total): 
	per = 0 
	if total != 0: 
		#per = ( float(value) / float(total) ) * 100
		per = float(value) / float(total)
	return per 
# get_per



# ----------------------------------------------------------- Get Patients ------------------------------------------------------

# Provides Patients between begin date and end date. 
@api.multi
def get_patients_filter(self, date_bx, date_ex, mode):

	#print
	#print 'Get Patients'


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
												],
													order='create_date asc',
													#limit=1,
													#limit=500,
												)
		# Count 
		count = self.env['oeh.medical.patient'].search_count([													
																('create_date', '>=', date_begin),
																('create_date', '<', date_end),															
												],
													#order='x_serial_nr asc',
													#limit=1,
												)

	# Normal 
	else:
		# Patients 
		patients = self.env['oeh.medical.patient'].search([
															('x_date_record', '>=', date_begin),													
															('x_date_record', '<', date_end),
												],
													order='create_date asc',
													#limit=1,
													#limit=500,
												)
		# Count 
		count = self.env['oeh.medical.patient'].search_count([																												
																('x_date_record', '>=', date_begin),
																('x_date_record', '<', date_end),
												],
													#order='x_serial_nr asc',
													#limit=1,
												)

	return patients, count

# get_patients_filter

