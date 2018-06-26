# -*- coding: utf-8 -*-
#
# 	*** Procedure Session Funcs 
#
#
# Created: 				  1 Nov 2016
# Last updated: 	 	 26 Jun 2018
#

from openerp import models, fields, api
from . import treatment_funcs
from . import time_funcs
from datetime import datetime

from . import procedure_funcs
from . import procedure_funcs_cos


#------------------------------------------------ Create - Sessions ---------------------------------------------------

@api.multi
def create_sessions(self):

	#from datetime import datetime

	#print 'jx'
	#print 'Create Sessions - Go'
	#print 



	# Clean 
	rec_set = self.env['openhealth.session.med'].search([
															('procedure', '=', self.id), 
													])
	ret = rec_set.unlink()



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
	#doctor_id = treatment_funcs.get_actual_doctor(self)
	doctor_id = procedure_funcs.get_actual_doctor(self)


	# Appointment 
	duration = 0.5
	x_type = 'session'
	state = 'pre_scheduled'
	#x_create_procedure_automatic = False 
	machine = self.machine


	doctor_name = self.doctor.name 

	
	# Date 		
	GMT = time_funcs.Zone(0,False,'GMT')
	evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
	app_date = datetime.now(GMT).strftime("%Y-%m-%d ")




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
				#10 :	10,
				#11 :	11,
			}




	#print 
	#print 'Loop'



	#for k in range(0,1): 						# Testing 
	for k in range(0,self.number_sessions): 

		# Init 
		delta = 0 
		nr_days = k_dic[k] + delta 

		# Session date 
		session_date = procedure_funcs.get_next_date(self, evaluation_start_date, nr_days)
		session_date_str = session_date.strftime("%Y-%m-%d")		
		


		# First - Today - The app already exists !  
		if k == 0:
			
			appointment_date = session_date_str + ' '

			# Search Appointment 
			appointment = self.env['oeh.medical.appointment'].search([ 	
																		('appointment_date', 'like', app_date),	
																		('patient', 'like', self.patient.name),	
																		('x_type', 'like', 'procedure'), 
																		('doctor', 'like', self.doctor.name), 																				
																	], 
																		order='appointment_date desc', limit=1)
			#print appointment



		else: 	# Create Appointment 

			#appointment_date_str = session_date_str + ' 14:0:0'
			appointment_date_str = session_date_str + ' 15:0:0'


			# Check and push 
			#appointment_date_str = procedure_funcs_cos.check_and_push(self, appointment_date_str, duration, x_type, doctor_name, machine)
			appointment_date_str = procedure_funcs.check_and_push(self, appointment_date_str, duration, x_type, doctor_name)



			# Create Appointment 
			appointment = self.env['oeh.medical.appointment'].create({
																		'appointment_date': appointment_date_str,
																		'patient': patient_id,	
																		'doctor': doctor_id,

																		'duration': duration,
																		'x_type': x_type,
																		'state': state,
																		#'x_create_procedure_automatic': x_create_procedure_automatic,
																		'x_create_procedure_automatic': False,
																		'x_machine': machine,
																		
																		'procedure': self.id,
																		'treatment': treatment_id, 

																		#'x_target': 'doctor',
																		#'cosmetology': cosmetology_id,																			
																})
			#print appointment 
		appointment_id = appointment.id



		# Create Session 
		session = self.env['openhealth.session.med'].create(
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


	ret = 0
	return ret	

# create_sessions_go
