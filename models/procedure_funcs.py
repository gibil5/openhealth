# -*- coding: utf-8 -*-

from openerp import models, fields, api

#from datetime import datetime,tzinfo,timedelta
import datetime


import time_funcs

import jrfuncs




#------------------------------------------------ Buttons ---------------------------------------------------

# Create control 

@api.multi

def create_controls_go(self):

	print 
	print 'Create control Go'
	print 

	#name = 'name'

	patient_id = self.patient.id
	doctor_id = self.doctor.id
	
	procedure_id = self.id
	treatment_id = self.treatment.id

	product_id = self.product.id

	chief_complaint = self.chief_complaint




	GMT = time_funcs.Zone(0,False,'GMT')
	evaluation_start_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")



	#appointment = self.env['oeh.medical.appointment'].search([ 															
	#														('patient', 'like', self.patient.name),		
	#														('doctor', 'like', self.doctor.name), 	
	#														('x_type', 'like', 'control'), 
	#													], 
	#														order='appointment_date desc', limit=1)
	#print appointment
	#appointment_id = appointment.id



	ret = 0

	#for line in self.sale_ids.order_line:
	#for k in [0:6]:
	for k in range(0,3): 
	#for k in range(1,4): 
					
		nr_weeks = k 

		control_date = get_control_date(self, evaluation_start_date, nr_weeks)
		#control_date_str = control_date.strftime("%Y-%m-%d %H:%M:%S")
		control_date_str = control_date.strftime("%Y-%m-%d")
		control_date_str = control_date_str + ' 0:0:0'

		# Create Appointment
		print control_date
		print control_date_str
		#appointment_date = control_date
		appointment_date = control_date_str



		duration = 0.25
		x_type = 'control'
		state = 'Pre-scheduled'

		appointment = create_appointment_control(self, appointment_date, duration, x_type, state, chief_complaint, patient_id, doctor_id, treatment_id)

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

		print control 
		print control_id
		print 



		#ret = jrfuncs.update_appointment_go(self, appointment_id, control_id, 'control')
		#print appointment
		#print appointment.control
		#print appointment.control.id
		#print 

	return ret	








@api.multi

def create_appointment_control(self, appointment_date, duration, x_type, state, chief_complaint, patient_id, doctor_id, treatment_id):

	appointment = self.env['oeh.medical.appointment'].create({
																'appointment_date': appointment_date,

																'duration': duration,
															

																'x_type': x_type,
																'state': state,


																'patient': patient_id,	
																'doctor': doctor_id,
																'treatment': treatment_id, 

																#'x_create_procedure_automatic': x_create_procedure_automatic,
																'x_chief_complaint': chief_complaint, 

															})


	return appointment










@api.multi

def get_control_date(self, evaluation_start_date, nr_weeks):

	#date_format = "%Y-%m-%d"
	date_format = "%Y-%m-%d %H:%M:%S"


	delta = datetime.timedelta(weeks=nr_weeks)

	print evaluation_start_date

	sd = datetime.datetime.strptime(evaluation_start_date, date_format)
	

	control_date = delta + sd


	return control_date



