# -*- coding: utf-8 -*-
#
# 	*** Procedure 	
#
#
# Created: 				 1 Nov 2016
# Last updated: 	 	 20 Jun 2017

from openerp import models, fields, api

from . import appfuncs
from . import time_funcs
from . import treatment_funcs

from . import procedure_funcs_cos




#------------------------------------------------ Create - Sessions ---------------------------------------------------

@api.multi

def create_sessions_go(self, model):

		from datetime import datetime


		#print 'jx'
		#print 'Create Sessions - Go'
		#print 



# Initial conditions 
		

		procedure_id = self.id 
		patient_id = self.patient.id		
		chief_complaint = self.chief_complaint
		evaluation_type = 'Session'
		product_id = self.product.id
		treatment_id = self.treatment.id
		cosmetology_id = self.cosmetology.id
		laser = self.laser
		

		# Actual Doctor 
		doctor_id = treatment_funcs.get_actual_doctor(self)
	
		if doctor_id == False: 
			doctor_id = self.doctor.id 




		# Appointment 
		duration = 0.5
		x_type = 'session'
		state = 'pre_scheduled'
		x_create_procedure_automatic = False 
		machine = self.machine


		doctor_name = self.doctor.name 


		
		# Date 		
		GMT = time_funcs.Zone(0,False,'GMT')
		evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		app_date = datetime.now(GMT).strftime("%Y-%m-%d ")










# Clean Sessions 
		#rec_set = self.env[model].search([
		#										('procedure', '=', self.id), 
		#									])
		#ret = rec_set.unlink()
		







# Loop 
		# Date dictionary - Number of days for controls 
		k_dic = {
					#0 :	0,
					#1 :	7,
					#2 :	15,
					#3 :	21,
					#3 :	30,
					#4 :	60,
					#5 :	120,

					0 :	0,
					1 :	1,
					2 :	2,
					3 :	3,
					4 :	4,
					5 :	5,

					6 :	6,
					7 :	7,
					8 :	8,
					9 :	9,
					10 :	10,
					11 :	11,
				}




		#print 
		#print 'Loop'



		#for k in range(0,1): 						# Testing 
		for k in range(0,self.number_sessions): 

			#print k

			delta = 0 
			nr_days = k_dic[k] + delta 


			# session date 
			#session_date = procedure_funcs.get_control_date(self, evaluation_start_date, nr_days)
			session_date = get_control_date(self, evaluation_start_date, nr_days)

			session_date_str = session_date.strftime("%Y-%m-%d")		
			



			# First - Today - The app already exists !  
			if k == 0:
				
				appointment_date = session_date_str + ' '
				#print 'appointment_date: ', appointment_date



				# Search Appointment 
				appointment = self.env['oeh.medical.appointment'].search([ 	
																			('appointment_date', 'like', app_date),	

																			('patient', 'like', self.patient.name),	
																			
																			('x_type', 'like', 'procedure'), 

																			('doctor', 'like', self.doctor.name), 																				
																		], 
																			order='appointment_date desc', limit=1)

				#print appointment




			#if appointment == False: 

			else: 	# Create Appointment 
				#print 
				#print 'Create Appointment'


	
				#appointment_date = session_date_str
				#appointment_date_str = session_date_str + ' 14:0:0'
				appointment_date_str = session_date_str + ' 15:0:0'




				# Check and push 
				appointment_date_str = procedure_funcs_cos.check_and_push(self, appointment_date_str, duration, x_type, doctor_name, machine)






				# Create Appointment 
				appointment = self.env['oeh.medical.appointment'].create({

																		'appointment_date': appointment_date_str,
																		'duration': duration,
																		'x_type': x_type,
																		'state': state,
																		'patient': patient_id,	
																		'doctor': doctor_id,
																		'x_create_procedure_automatic': x_create_procedure_automatic,
																		'x_machine': machine,
																		'treatment': treatment_id, 
																		'cosmetology': cosmetology_id, 																		
																		'x_target': self.target,
																		self.key: self.id,

																	})
				#print appointment 

			appointment_id = appointment.id
			#print appointment
			#print appointment_id






# Create Session 
			#print 'Create Session'
			session = self.env[model].create(
												{
													'evaluation_start_date':session_date,

													'patient': patient_id,

													'doctor': doctor_id,													

													'evaluation_type':evaluation_type,

													'product': product_id,
													
													'laser': laser,

													'appointment': appointment_id,

													'treatment': treatment_id,	

													'cosmetology': cosmetology_id,				

													'chief_complaint': chief_complaint,

													'procedure': procedure_id,				
												}
											)
			session_id = session.id 
			#print session
			#print session_id


		ret = 0
		return ret	







#------------------------------------------------ Create - Controls ---------------------------------------------------

#jx 
@api.multi
def create_controls_go(self):

	from datetime import datetime

	#print 
	#print 'Create control Go'
	#print 



# Initial conditions  
	patient_id = self.patient.id	
	doctor_name = self.doctor.name
	product_id = self.product.id
	chief_complaint = self.chief_complaint
	procedure_id = self.id
	treatment_id = self.treatment.id






	# Doctor 
	#doctor_id = self.doctor.id
	doctor_id = treatment_funcs.get_actual_doctor(self)

	if doctor_id == False: 
		doctor_id = self.doctor.id 


	
	#print doctor_id
	#print doctor_name



	# Start date 
	GMT = time_funcs.Zone(0,False,'GMT')
	#evaluation_start_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
	evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")

	ret = 0






		# Clean Appointments 
		#print 
		#print 'Clean Appointments'

		#rec_set = self.env['oeh.medical.appointment'].search([
																#('procedure', '=', self.id), 	
																#('procedure_cos', '=', self.id), 
		#														(self.key, '=', self.id), 
		#													])
		#ret = rec_set.unlink()
		#print "ret: ", ret





# Clean Sessions 
	#print 
	#print 'Clean Controls'

	rec_set = self.env['openhealth.control'].search([
														('procedure', '=', self.id), 
													])
	ret = rec_set.unlink()
	#print "ret: ", ret








# Loop 
	# Date dictionary - Number of days for controls 
	k_dic = {
				0 :	7,
				1 :	15,
				2 :	30,
				3 :	60,
				4 :	120,
				5 :	180,
	}



	#for k in range(0,1): 
	#for k in range(0,6): 
	for k in range(0,self.number_controls): 
					

		delta = 0 
		#delta = -7


		#nr_weeks = k 
		nr_days = k_dic[k] + delta 



		# Control date 
		control_date = get_control_date(self, evaluation_start_date, nr_days)
		control_date_str = control_date.strftime("%Y-%m-%d")		
		control_date_str = control_date_str + ' 14:0:0'




		# Create Appointment
		duration = 0.25
		x_type = 'control'
		state = 'pre_scheduled_control'

		appointment_date = control_date_str






		# Create Appointment 
		appointment_date_str = check_max_number(self, appointment_date, x_type, doctor_name)

		appointment_date_str = check_and_push(self, appointment_date_str, duration, x_type, doctor_name)

		appointment = create_appointment_control(self, appointment_date_str, duration, x_type, state, chief_complaint, patient_id, doctor_id, treatment_id)

		appointment_id = appointment.id




		# Create Control 
		control = self.control_ids.create({
											'evaluation_start_date':control_date,
											'patient':patient_id,
											'doctor':doctor_id,
											'product':product_id,
											'chief_complaint':chief_complaint,
											'procedure':procedure_id,										
											'appointment': appointment_id,
											'treatment': treatment_id,

											#'control_nr': k+1, 
											'evaluation_nr': k+1, 
									})



		control_id = control.id

		#print control 
		#print control_id
		#print 



		#ret = jrfuncs.update_appointment_go(self, appointment_id, control_id, 'control')
		rec_set = self.env['oeh.medical.appointment'].browse([appointment_id])
		ret = rec_set.write({
								'control': control_id,
								'procedure': procedure_id,
							})


		#print appointment
		#print appointment.control
		#print appointment.control.id
		#print 

	return ret	







#------------------------------------------------ Check Max Nr Controls ---------------------------------------------------
@api.multi
def	check_max_number(self, appointment_date, x_type, doctor_name):

	import datetime

	#print 
	#print 'Check Max Number'

	date_format = "%Y-%m-%d %H:%M:%S"

	appointment_date_dt = datetime.datetime.strptime(appointment_date, date_format)



	#appointment_date_str = appointment_date[0:10]
	#print appointment_date





	delta_var = datetime.timedelta(days=1)
	#print delta_var

	ret = 1



	while not ret == 0:

		appointment_date = appointment_date_dt.strftime("%Y-%m-%d %H:%M:%S")
		appointment_date_str = appointment_date[2:10]
		
		#print appointment_date
		#print appointment_date_str

		app_ids = self.env['oeh.medical.appointment'].search([
																('appointment_date', 'like', appointment_date_str),  
																('doctor', '=', doctor_name), 

																('x_type', '=', x_type), 

														 	])
		#print app_ids
		#print len(app_ids)




		if len(app_ids) < 4:
			#print 'Max number check - Success !!!'

			ret = 0




		else:
			#print 'Alert. Max reached. Check next day.'

			appointment_date_dt = datetime.datetime.strptime(appointment_date, date_format)

			appointment_date_dt = appointment_date_dt + delta_var

			#print appointment_date_dt

		#print 



	return appointment_date





#------------------------------------------------ Check Push and Create ---------------------------------------------------
@api.multi
def check_and_push(self, appointment_date, duration, x_type, doctor_name):

	import datetime

	#print 
	#print 'Chech and push'
	#print appointment_date


	delta_var = datetime.timedelta(hours=duration)
	date_format = "%Y-%m-%d %H:%M:%S"

	ret = 1




	appointment_date_dt = datetime.datetime.strptime(appointment_date, date_format)
	k = 0

	while not ret == 0:

		appointment_date = appointment_date_dt +  k * delta_var

		appointment_date_str = appointment_date.strftime("%Y-%m-%d %H:%M:%S")




		# Check for collisions 
		#ret, doctor_name, start, end = appfuncs.check_for_collisions(self, appointment_date_str, doctor_name, duration, False, 'doctor')
		ret, doctor_name, start, end = appfuncs.check_for_collisions(self, appointment_date_str, doctor_name, duration, False, 'doctor', x_type)



		if ret == 0: 		# Success ! - No Collisions
			tra = 1 
			#print 'Collision check - Success !!!'
			#print k
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

																'x_chief_complaint': chief_complaint, 

																'x_create_procedure_automatic': x_create_procedure_automatic,



																'treatment': treatment_id, 

																'x_target': 'doctor',
															})




	return appointment










#------------------------------------------------ Get control date ---------------------------------------------------
@api.multi

#def get_control_date(self, evaluation_start_date, nr_weeks):
def get_control_date(self, evaluation_start_date, nr_days):


	import datetime


	#date_format = "%Y-%m-%d"
	date_format = "%Y-%m-%d %H:%M:%S"


	#delta = datetime.timedelta(weeks=nr_weeks)
	delta = datetime.timedelta(days=nr_days)


	#print evaluation_start_date

	sd = datetime.datetime.strptime(evaluation_start_date, date_format)
	

	control_date = delta + sd


	return control_date



