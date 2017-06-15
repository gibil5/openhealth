# -*- coding: utf-8 -*-

from datetime import datetime,tzinfo,timedelta
from openerp import models, fields, api



from . import time_funcs
from . import jrfuncs




#------------------------------------------------ Create Order Lines ---------------------------------------------------

@api.multi

def create_order_lines(self, laser, order_id):

	#print 
	#print 'Create Order Lines'

	order = self.env['sale.order'].search([(
												'id','=', order_id),
												],
												#order='appointment_date desc',
												#limit=1,						
											)		

	#print laser
	#print order



	_model = {

				'co2':			'openhealth.service.co2',
				'excilite':		'openhealth.service.excilite',
				'ipl':			'openhealth.service.ipl',
				'ndyag':		'openhealth.service.ndyag',
				'medical':		'openhealth.service.medical',


	}

	#print _model[laser]

	#print 


	rec_set = self.env[_model[laser]].search([(
																		'treatment','=', self.id),
																	],
																		#order='appointment_date desc',
																		#limit=1,						
																	)		

	if rec_set != False: 

		for service in rec_set: 

			target_line = service.service.x_name_short
					
			ret = order.x_create_order_lines_target(target_line)
					
			#print ret 


	return 0



#------------------------------------------------ Create Procedure ---------------------------------------------------

# Create procedure 

@api.multi

#def create_procedure_go(self, process):
def create_procedure_go(self):


	#print 
	#print 'Create Procedure Go'
	#print 

	#name = 'name'


	#treatment = False
	#cosmetology = False
	#if process == 'treatment':
	#	treatment = self.id
	#if process == 'cosmetology':
	#	cosmetology = self.id




	treatment = self.id

	patient = self.patient.id


	#therapist = self.therapist.id
	doctor = self.physician.id



	chief_complaint = self.chief_complaint




	GMT = time_funcs.Zone(0,False,'GMT')
	evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")


	appointment = self.env['oeh.medical.appointment'].search([ 	
															('patient', 'like', self.patient.name),		
															('doctor', 'like', self.physician.name), 	
															('x_type', 'like', 'procedure'), 
														], 
															order='appointment_date desc', limit=1)

	#print appointment
	appointment_id = appointment.id



	ret = 0





	# Chief complaint 
	#for sale in self.order_ids:
	#	chief_complaint = sale.x_chief_complaint
	#	#print 'chief_complaint:', chief_complaint





	#for line in self.order_ids.order_line:
	for line in self.order_pro_ids.order_line:


		#if self.nr_procedures < self.order_ids.nr_lines:
		if self.nr_procedures < self.order_pro_ids.nr_lines:

			product = line.product_id.id
			

			if line.product_id.type == 'service':
				
				procedure = self.procedure_ids.create({
														'patient':patient,

														'doctor':doctor,
														#'therapist':therapist,
														
														'treatment':treatment,		
														#'cosmetology':cosmetology,		

														'product':product,
														'evaluation_start_date':evaluation_start_date,



														'chief_complaint':chief_complaint,



														'appointment': appointment_id,
													})


				procedure_id = procedure.id

				#print 
				#print procedure 
				#print procedure_id


				#self.update_appointment(appointment_id, procedure_id, 'procedure')
				ret = jrfuncs.update_appointment_go(self, appointment_id, procedure_id, 'procedure')


				#print appointment
				#print appointment.procedure
				#print appointment.procedure.id

				#print 

	return ret	


