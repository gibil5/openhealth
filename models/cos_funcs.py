# -*- coding: utf-8 -*-

from datetime import datetime,tzinfo,timedelta
from openerp import models, fields, api
import time_funcs

import jrfuncs





#------------------------------------------------ Create Procedure ---------------------------------------------------

# Create procedure 

@api.multi

def create_procedure_go(self):

	print 
	print 'Create Procedure Cos - Go'
	print 

	#name = 'name'



	cosmetology = self.id

	patient = self.patient.id

	therapist = self.therapist.id

	#chief_complaint = self.chief_complaint




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





	# Chief complaint 
	for sale in self.sale_ids:
		chief_complaint = sale.x_chief_complaint
		print 'chief_complaint:', chief_complaint





	for line in self.sale_ids.order_line:
					
		if self.nr_procedures < self.sale_ids.nr_lines:

			product = line.product_id.id
			

			if line.product_id.type == 'service':
				
				procedure = self.procedure_ids.create({

														'patient':patient,

														#'doctor':doctor,

														'therapist':therapist,
														
														#'treatment':treatment,		
														
														'cosmetology':cosmetology,		

														'product':product,
														
														'evaluation_start_date':evaluation_start_date,
														
														#'chief_complaint':chief_complaint,


														'appointment': appointment_id,
													})


				procedure_id = procedure.id

				print 
				print procedure 
				print procedure_id



				#self.update_appointment(appointment_id, procedure_id, 'procedure')
				ret = jrfuncs.update_appointment_go(self, appointment_id, procedure_id, 'procedure')


				print appointment
				print appointment.procedure
				print appointment.procedure.id

				print 

	return ret	


