# -*- coding: utf-8 -*-

from datetime import datetime,tzinfo,timedelta
from openerp import models, fields, api
import time_funcs




#------------------------------------------------ Buttons ---------------------------------------------------

# Create procedure 

@api.multi

def create_procedure_go(self):

	print 
	print 'Create Procedure Go'
	print 

	#name = 'name'

	patient = self.patient.id
	doctor = self.physician.id
	treatment = self.id
	chief_complaint = self.chief_complaint

	GMT = time_funcs.Zone(0,False,'GMT')
	evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")



	appointment = self.env['oeh.medical.appointment'].search([ 	
														
															('patient', 'like', self.patient.name),		
															
															('doctor', 'like', self.physician.name), 	
															
															('x_type', 'like', 'procedure'), 
														
														], 
															order='appointment_date desc', limit=1)

	print appointment
	appointment_id = appointment.id



	ret = 0



	for line in self.sale_ids.order_line:
					
		if self.nr_procedures < self.sale_ids.nr_lines:

			product = line.product_id.id
			

			procedure = self.procedure_ids.create({
											'patient':patient,
											'doctor':doctor,
											'chief_complaint':chief_complaint,
											'treatment':treatment,										
											'product':product,

											'evaluation_start_date':evaluation_start_date,


											'appointment': appointment_id,
									})


			procedure_id = procedure.id

			print 
			print procedure 
			print procedure_id

			self.update_appointment(appointment_id, procedure_id, 'procedure')

			print appointment
			print appointment.procedure
			print appointment.procedure.id

			print 

	return ret	






# Update Appointment

@api.multi

def update_appointment_go(self, appointment_id, owner_id, x_type):

		rec_set = self.env['oeh.medical.appointment'].browse([
																appointment_id																
															])
		print rec_set



		if x_type == 'consultation':
			ret = rec_set.write({
									'consultation': owner_id,
								})
			#print appointment.consultation
			#print appointment.consultation.id



		elif x_type == 'procedure':
			ret = rec_set.write({
									'procedure': owner_id,
								})
			#print appointment.procedure
			#print appointment.procedure.id



		elif x_type == 'session':
			ret = rec_set.write({
									'session': owner_id,
								})
			#print appointment.session
			#print appointment.session.id



		elif x_type == 'control':
			ret = rec_set.write({
									'control': owner_id,
								})
			#print appointment.control
			#print appointment.control.id


		else:
			print 
			print 'This should not happen !!!'
			print 



		print ret 



		return ret




