# -*- coding: utf-8 -*-

from openerp import models, fields, api

#from datetime import datetime,tzinfo,timedelta
import datetime


import time_funcs

import jrfuncs

import appfuncs



#------------------------------------------------ Buttons ---------------------------------------------------

# Create control 

@api.multi

def create_controls_go(self):

	print 
	print 'Create control Go'
	print 


	# Initialize 
	patient_id = self.patient.id
	
	doctor_id = self.doctor.id	
	doctor_name = self.doctor.name

	procedure_id = self.id
	treatment_id = self.treatment.id
	product_id = self.product.id
	chief_complaint = self.chief_complaint

	GMT = time_funcs.Zone(0,False,'GMT')
	evaluation_start_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")

	ret = 0



	# Number of days for controls 
	k_dic = {
				0 :	7,
				1 :	15,
				2 :	30,
				3 :	60,
				4 :	120,
				5 :	180,
	}



	#for k in range(0,1): 
	#for k in range(0,3): 
	for k in range(0,6): 
					

		#delta = 0 
		delta = -7


		#nr_weeks = k 
		nr_days = k_dic[k] + delta 



		# Control date 
		#control_date = get_control_date(self, evaluation_start_date, nr_weeks)
		control_date = get_control_date(self, evaluation_start_date, nr_days)



		control_date_str = control_date.strftime("%Y-%m-%d")		
		#control_date_str = control_date_str + ' 0:0:0'
		#control_date_str = control_date_str + ' 5:0:0'
		control_date_str = control_date_str + ' 14:0:0'




		# Create Appointment
		duration = 0.25
		x_type = 'control'
		#state = 'Pre-scheduled'
		state = 'pre_scheduled_control'

		appointment_date = control_date_str






		# Core 


		appointment_date_str = check_max_number(self, appointment_date, x_type, doctor_name)



		#appointment_date_str = check_and_push(self, appointment_date, duration, x_type, doctor_name)
		appointment_date_str = check_and_push(self, appointment_date_str, duration, x_type, doctor_name)


		appointment = create_appointment_control(self, appointment_date_str, duration, x_type, state, chief_complaint, patient_id, doctor_id, treatment_id)






		appointment_id = appointment.id

		# Create Control 
		control = self.control_ids.create({
											'patient':patient_id,
											'doctor':doctor_id,
											'procedure':procedure_id,										

											'product':product_id,

											'chief_complaint':chief_complaint,

											'evaluation_start_date':control_date,

											'appointment': appointment_id,
									})


		control_id = control.id

		#print control 
		#print control_id
		#print 



		ret = jrfuncs.update_appointment_go(self, appointment_id, control_id, 'control')

		#print appointment
		#print appointment.control
		#print appointment.control.id
		#print 

	return ret	







#------------------------------------------------ Check Max Nr Controls ---------------------------------------------------
@api.multi
def	check_max_number(self, appointment_date, x_type, doctor_name):

	print 
	print 'Check Max Number'

	date_format = "%Y-%m-%d %H:%M:%S"

	appointment_date_dt = datetime.datetime.strptime(appointment_date, date_format)



	#appointment_date_str = appointment_date[0:10]
	print appointment_date





	delta_var = datetime.timedelta(days=1)
	print delta_var

	ret = 1



	while not ret == 0:

		appointment_date = appointment_date_dt.strftime("%Y-%m-%d %H:%M:%S")
		appointment_date_str = appointment_date[2:10]
		
		print appointment_date
		print appointment_date_str

		app_ids = self.env['oeh.medical.appointment'].search([
																('appointment_date', 'like', appointment_date_str),  
																('doctor', '=', doctor_name), 

																('x_type', '=', x_type), 

														 	])
		print app_ids
		print len(app_ids)




		if len(app_ids) < 4:
			print 'Max number check - Success !!!'

			ret = 0




		else:
			print 'Alert. Max reached. Check next day.'

			appointment_date_dt = datetime.datetime.strptime(appointment_date, date_format)

			appointment_date_dt = appointment_date_dt + delta_var

			print appointment_date_dt

		print 



	return appointment_date




#------------------------------------------------ Check Push and Create ---------------------------------------------------
@api.multi
def check_and_push(self, appointment_date, duration, x_type, doctor_name):

	print 
	print 'Chech and push'
	print appointment_date


	delta_var = datetime.timedelta(hours=duration)
	date_format = "%Y-%m-%d %H:%M:%S"

	ret = 1




	appointment_date_dt = datetime.datetime.strptime(appointment_date, date_format)
	k = 0

	while not ret == 0:

		appointment_date = appointment_date_dt +  k * delta_var

		appointment_date_str = appointment_date.strftime("%Y-%m-%d %H:%M:%S")



		# Check for collisions 
		ret, doctor_name, start, end = appfuncs.check_for_collisions(self, appointment_date_str, doctor_name, duration)



		if ret == 0: 		# Success ! - No Collisions
			

			print 'Collision check - Success !!!'
			print k



		else:				# Collision - Keep going... 
			k = k + 1






	#appointment_date_str = appointment_date.strftime("%Y-%m-%d %H:%M:%S")

	#return appointment_date
	return appointment_date_str







#------------------------------------------------ Create Appointment  ---------------------------------------------------

@api.multi
def create_appointment_control(self, appointment_date, duration, x_type, state, chief_complaint, patient_id, doctor_id, treatment_id):


	x_create_procedure_automatic = False 


	appointment = self.env['oeh.medical.appointment'].create({
																'appointment_date': appointment_date,

																'duration': duration,
															

																'x_type': x_type,

																'state': state,


																'patient': patient_id,	
																'doctor': doctor_id,
																'treatment': treatment_id, 

																'x_chief_complaint': chief_complaint, 

																'x_create_procedure_automatic': x_create_procedure_automatic,
															})


	return appointment










#------------------------------------------------ Get control date ---------------------------------------------------
@api.multi

#def get_control_date(self, evaluation_start_date, nr_weeks):
def get_control_date(self, evaluation_start_date, nr_days):

	#date_format = "%Y-%m-%d"
	date_format = "%Y-%m-%d %H:%M:%S"


	#delta = datetime.timedelta(weeks=nr_weeks)
	delta = datetime.timedelta(days=nr_days)


	#print evaluation_start_date

	sd = datetime.datetime.strptime(evaluation_start_date, date_format)
	

	control_date = delta + sd


	return control_date



