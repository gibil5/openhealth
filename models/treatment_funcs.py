# -*- coding: utf-8 -*-

from datetime import datetime,tzinfo,timedelta
from openerp import models, fields, api



from . import time_funcs
from . import jrfuncs




#------------------------------------------------ Create Order Lines ---------------------------------------------------

# Create Order Lines 
@api.multi
def create_order_lines(self, laser, order_id):

	print 
	print 'Create Order Lines'


	order = self.env['sale.order'].search([(
												'id','=', order_id),
												],
												#order='appointment_date desc',
												#limit=1,						
											)		

	#print laser
	#print order



	_model = {

				'quick':		'openhealth.service.quick',

				'vip':		'openhealth.service.vip',


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



#jxx
		for service in rec_set: 


			target_line = service.service.x_name_short
					
			#print service
			#print target_line

			ret = order.x_create_order_lines_target(target_line)

					
			#print ret 
	return 0




#------------------------------------------------ Create Procedure ---------------------------------------------------

# Create procedure 
@api.multi
def create_procedure_go(self):


	print 
	print 'jx'
	print 'Create Procedure Go'
	print 


	# Init 
	treatment = self.id
	patient = self.patient.id
	doctor = self.physician.id
	chief_complaint = self.chief_complaint


	# Time 
	GMT = time_funcs.Zone(0,False,'GMT')
	evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")


	# Search App 
	appointment = self.env['oeh.medical.appointment'].search([ 	
																('patient', '=', self.patient.name),		
																('doctor', '=', self.physician.name), 	
																('x_type', '=', 'procedure'), 
														], 
																order='appointment_date desc', limit=1)
	appointment_id = appointment.id




	# Loop - Create Procedures 
	ret = 0
	for order in self.order_pro_ids:

		if order.state == 'sale': 
	
			for line in order.order_line:

				if self.nr_procedures < order.nr_lines:

					product_product = line.product_id


					# Search Product 
					product_template = self.env['product.template'].search([
																				('x_name_short','=', product_product.x_name_short),
																				('x_origin','=', False),
												])
					


					# For Services Create 
					if line.product_id.type == 'service':
			
						procedure = self.procedure_ids.create({
																'patient':patient,
																'doctor':doctor,														
																'treatment':treatment,	
																'product':product_template.id,																
																'evaluation_start_date':evaluation_start_date,
																'chief_complaint':chief_complaint,
																'appointment': appointment_id,
															})

						procedure_id = procedure.id

						ret = jrfuncs.update_appointment_go(self, appointment_id, procedure_id, 'procedure')

	return ret	
	# create_procedure_go

