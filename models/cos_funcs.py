# -*- coding: utf-8 -*-

from datetime import datetime,tzinfo,timedelta
from openerp import models, fields, api
from . import time_funcs
from . import jrfuncs

#------------------------------------------------ Create Procedure ---------------------------------------------------

@api.multi

def create_procedure_go(self):

	cosmetology = self.id
	patient = self.patient.id
	chief_complaint = self.chief_complaint
	#therapist = self.therapist.id
	doctor = self.physician.id
	GMT = time_funcs.Zone(0,False,'GMT')
	evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")

	appointment = self.env['oeh.medical.appointment'].search([ 	
															('patient', 'like', self.patient.name),	
															('doctor', 'like', self.physician.name), 																
															('x_type', 'like', 'procedure'), 
														], 
														order='appointment_date desc', limit=1)
	appointment_id = appointment.id

	ret = 0



	for line in self.order_ids.order_line:
		if self.nr_procedures < self.order_ids.nr_lines:
			product = line.product_id.id
			if line.product_id.type == 'service':
				procedure = self.procedure_ids.create({

														'patient':patient,
														'doctor':doctor,														
														'cosmetology':cosmetology,		
														'product':product,
														'evaluation_start_date':evaluation_start_date,
														'chief_complaint':chief_complaint,
														'appointment': appointment_id,
													})

				procedure_id = procedure.id

	return ret	

# create_procedure_go


