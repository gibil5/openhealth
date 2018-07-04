# -*- coding: utf-8 -*-
#
# 		** Procedure Funcs 
#
# Created: 				 25 Jun 2018
# Last updated: 	 	 25 Jun 2018
#
from openerp import models, fields, api

#from datetime import datetime
import datetime



#------------------------------------------------ Check and Push ---------------------------------------------------
@api.multi
#def check_and_push(self, appointment_date, duration, x_type, doctor_name):
def check_and_push(self, appointment_date, duration, x_type, doctor_name, states):

	#import datetime

	#print 
	#print 'Chech and push'
	#print appointment_date
	#print duration
	#print x_type
	#print doctor_name
	#print states
	#print 


	# Init 
	delta_var = datetime.timedelta(hours=duration)

	date_format = "%Y-%m-%d %H:%M:%S"
	appointment_date_dt = datetime.datetime.strptime(appointment_date, date_format)
	

	# Loop 
	k = 0
	ret = 1
	while not ret == 0:

		# Increase 
		appointment_date = appointment_date_dt +  k * delta_var
		appointment_date_str = appointment_date.strftime("%Y-%m-%d %H:%M:%S")

		appointment_end = appointment_date_dt +  (k + 1) * delta_var 
		appointment_end_str = appointment_end.strftime("%Y-%m-%d %H:%M:%S")

		#print appointment_date_str
		#print appointment_end_str



		# Search
		if states == False: 

			appointment = self.env['oeh.medical.appointment'].search([ 	
																		('appointment_date', '=', appointment_date_str),	
																		#('doctor', '=', self.doctor.name), 																				
																		('doctor', '=', doctor_name), 
																		#('x_type', '=', x_type), 
																		#('state', 'in', '['pre_scheduled_control']'), 
																	], 
																	#order='appointment_date desc', 
																	limit=1
																	)

			appointment_bis = self.env['oeh.medical.appointment'].search([ 	
																			('appointment_end', '=', appointment_end_str),	
																			#('doctor', '=', self.doctor.name), 
																			('doctor', '=', doctor_name), 
																		], 
																		#order='appointment_date desc', 
																		limit=1
																	)

			


		else: 

			appointment = self.env['oeh.medical.appointment'].search([ 	
																		#('state', '=', state), 
																		('state', 'in', states), 

																		('appointment_date', '=', appointment_date_str),	
																		('doctor', '=', self.doctor.name), 
																	], 
																	#order='appointment_date desc', 
																	limit=1
																)
		

			appointment_bis = self.env['oeh.medical.appointment'].search([ 	
																			#('state', '=', state), 
																			('state', 'in', states), 

																			('appointment_end', '=', appointment_end_str),	
																			('doctor', '=', self.doctor.name), 
																		], 
																		#order='appointment_date desc', 
																		limit=1
																	)
		#print appointment
		#print appointment_bis
		#print 


		# Check 
		#if appointment.name == False: 	# Success
		if (appointment.name == False)		and 	(appointment_bis.name == False)	: 	# Success
			#print 'Success'
			ret = 0 
		else: 
			#print 'Error. Repeat.'
			k = k + 1					# Error. Repeat. 

	return appointment_date_str

# check_and_push










#------------------------------------------------ Get Next Date ---------------------------------------------------

# Adds Nr to start date 
@api.multi
def get_next_date(self, evaluation_start_date, nr_days):

	import datetime

	date_format = "%Y-%m-%d %H:%M:%S"

	delta = datetime.timedelta(days=nr_days)

	start = datetime.datetime.strptime(evaluation_start_date, date_format)
	
	next_date = delta + start

	return next_date

# get_next_date





#------------------------------------------------ Get Actual Doctor ---------------------------------------------------

# Get Actual Doctor 
@api.multi
def get_actual_doctor(self):

	#print 'jx'
	#print 'Get Actual Doctor'

	user_name =  self.env.user.name 	
	doctor = self.env['oeh.medical.physician'].search([ 	
																('x_user_name', '=', user_name),		
															], 
															#order='appointment_date desc', 
															limit=1
															)
	doctor_id = doctor.id 

	#print user_name
	#print doctor.id 
	#print doctor.name 

	if doctor_id == False: 
		doctor_id = self.doctor.id 

	return doctor_id
