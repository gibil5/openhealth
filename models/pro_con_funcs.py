# -*- coding: utf-8 -*-
#
# 	*** Procedure Control Funcs 
#
#
# Created: 				  1 Nov 2016
# Last updated: 	 	 26 Jun 2018
#

from openerp import models, fields, api
from . import treatment_funcs
from . import appfuncs
from . import procedure_funcs

import datetime



#------------------------------------------------ Create - Controls ---------------------------------------------------

# Create Controls 
@api.multi
def create_controls(self):

	#from datetime import datetime

	#print 
	#print 'Create control Go'
	#print 


	# Clean 
	rec_set = self.env['openhealth.control'].search([
														('procedure', '=', self.id), 
													])
	ret = rec_set.unlink()



	# Initial conditions  
	patient_id = self.patient.id	
	doctor_name = self.doctor.name
	product_id = self.product.id
	chief_complaint = self.chief_complaint
	procedure_id = self.id
	treatment_id = self.treatment.id

	# Start date 
	evaluation_start_date = self.evaluation_start_date

	# Doctor 
	doctor_id = procedure_funcs.get_actual_doctor(self)

	# Date dictionary - Days between controls 
	k_dic = {
				0 :		0,
				1 :		1,
				#0 :	7,
				#1 :	15,
				2 :	30,
				3 :	60,
				4 :	120,
				5 :	180,
		}

	ret = 0



	# Loop 
	#for k in range(0,self.number_controls): 
	for k in range(0,len(k_dic)): 

		# Init 					
		delta = 0 
		nr_days = k_dic[k] + delta 


		# Control date 
		control_date = procedure_funcs.get_next_date(self, evaluation_start_date, nr_days)

		control_date_str = control_date.strftime("%Y-%m-%d")		
		control_date_str = control_date_str + ' 14:00:00'			# 09:00:00





		# Create Appointment
		duration = 0.25
		x_type = 'control'
		state = 'pre_scheduled_control'
		

		#appointment_date_str = check_and_push(self, appointment_date_str, duration, x_type, doctor_name)
		appointment_date_str = procedure_funcs.check_and_push(self, control_date_str, duration, x_type, doctor_name)

		#appointment_date_str = control_date_str


		appointment = self.env['oeh.medical.appointment'].create({
																	'appointment_date': appointment_date_str,

																	'patient': patient_id,	
																	'doctor': doctor_id,
																	'duration': duration,
																	'state': state,

																	'x_type': x_type,
																	'x_chief_complaint': chief_complaint, 
																	'x_create_procedure_automatic': False,
																	'x_target': 'doctor',

																	'treatment': treatment_id, 
																})
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

											'evaluation_nr': k+1, 
									})
		control_id = control.id




		# Update Appointments 
		#ret = jrfuncs.update_appointment_go(self, appointment_id, control_id, 'control')
		rec_set = self.env['oeh.medical.appointment'].browse([appointment_id])
		ret = rec_set.write({
								'control': control_id,
								'procedure': procedure_id,
							})

	return ret	

# create_controls

