# -*- coding: utf-8 -*-
#
# 	*** Procedure Session Funcs 
#
# Created: 				  1 Nov 2016
# Last updated: 	 	 15 Aug 2018
#
from openerp import models, fields, api
from datetime import datetime
import time_funcs

import user
import lib


#------------------------------------------------ Create Sessions ---------------------------------------------------

@api.multi
def create_sessions(self, nr_sessions, nr_ses_created):

	print
	print 'Create Sessions - Go'


	# Init
	procedure_id = self.id 
	patient_id = self.patient.id		
	chief_complaint = self.chief_complaint
	evaluation_type = 'Session'
	product_id = self.product.id
	treatment_id = self.treatment.id
	cosmetology_id = self.cosmetology.id
	laser = self.laser
	
	# Actual Doctor 
	#doctor_id = procedure_funcs.get_actual_doctor(self)
	doctor_id = user.get_actual_doctor_pro(self)

	# Appointment 
	duration = 0.5
	machine = self.machine
	x_type = 'session'
	subtype = self.product.x_treatment 


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

				0 : 0,
				
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



	#for k in range(0,1): 						# Testing 
	#for k in range(0,self.number_sessions): 
	for k in range(0, nr_sessions): 

		print k 


		# Init 
		#delta = 0 
		#nr_days = k_dic[k] + delta 
		nr_days = nr_ses_created


		# Session date 
		#session_date = procedure_funcs.get_next_date(self, evaluation_start_date, nr_days)
		session_date = lib.get_next_date(self, evaluation_start_date, nr_days)

		session_date_str = session_date.strftime("%Y-%m-%d")		


		# First - Today - The app already exists !  
		if k == 0:
			
			appointment_date = session_date_str + ' '

			print app_date
			print appointment_date

			# Search Appointment 
			appointment = self.env['oeh.medical.appointment'].search([ 	
																		#('appointment_date', '=', app_date),
																		('appointment_date', 'like', app_date),
																		('patient', '=', self.patient.name),	
																		('doctor', '=', self.doctor.name),
																		#('x_type', '=', 'session'), 
																		('x_type', '=', 'procedure'), 
																		('x_subtype', '=', subtype), 
																	], 
																		order='appointment_date desc', limit=1)
			#print appointment



		else: 	# Create Appointment 

			#appointment_date_str = session_date_str + ' 14:0:0'
			appointment_date_str = session_date_str + ' 15:0:0'


			states = False

			# Check and push 
			#appointment_date_str = procedure_funcs.check_and_push(self, appointment_date_str, duration, x_type, doctor_name, states)
			appointment_date_str = user.check_and_push(self, appointment_date_str, duration, x_type, doctor_name, states)



			# Create Appointment 
			#state = 'pre_scheduled_control'
			state = 'pre_scheduled_session'

			appointment = self.env['oeh.medical.appointment'].create({
																		'appointment_date': appointment_date_str,
																		'patient': patient_id,
																		'doctor': doctor_id,
																		'duration': duration,
																		'state': state,
																		'x_type': x_type,
																		'x_subtype': subtype,

																		'procedure': self.id,
																		'treatment': treatment_id, 
																})
		
		appointment_id = appointment.id
		print appointment 
		print appointment_id



		# Create Session 
		session = self.env['openhealth.session.med'].create({
																'evaluation_start_date':session_date,																
																'patient': patient_id,
																'doctor': doctor_id,													
																'evaluation_type':evaluation_type,
																'product': product_id,
																'laser': laser,
																'chief_complaint': chief_complaint,
																
																'appointment': appointment_id,																
																'procedure': procedure_id,				
																'treatment': treatment_id,	
											})
		session_id = session.id 


	ret = 0
	return ret	

# create_sessions_go

