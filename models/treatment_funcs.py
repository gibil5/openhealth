# -*- coding: utf-8 -*-

from openerp import models, fields, api

from datetime import datetime,tzinfo,timedelta
from . import time_funcs
from . import jrfuncs



#------------------------------------------------ Create Order Lines ---------------------------------------------------

# Create Order Lines 
@api.multi
def create_order_lines(self, laser, order_id):


	#print 'jx'
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

				'quick':		'openhealth.service.quick',

				'vip':			'openhealth.service.vip',


				'co2':			'openhealth.service.co2',
				'excilite':		'openhealth.service.excilite',
				'ipl':			'openhealth.service.ipl',
				'ndyag':		'openhealth.service.ndyag',
				'medical':		'openhealth.service.medical',


	}


	#print _model[laser]
	#print 



	# Services 
	rec_set = self.env[_model[laser]].search([
											
														('treatment','=', self.id),

														('state','=', 'draft'),
											
												],
											#order='appointment_date desc',
											#limit=1,						
											)		



	if rec_set != False: 



#jxx
		for service in rec_set: 


			target_line = service.service.x_name_short

			price_manual = service.price_manual

			price_applied = service.price_applied


					
			ret = order.x_create_order_lines_target(target_line, price_manual, price_applied)




			# Update state 
			service.state = 'budget'

					
			#print ret 
	return 0






#------------------------------------------------ Get Actual Doctor ---------------------------------------------------

# Get Actual Doctor 
@api.multi
def get_actual_doctor(self):


	print 'jx'
	print 'Get Actual Doctor'

	
	#user_id = self.env.user.id 
	user_name =  self.env.user.name 
	
	#print user_name

	doctor = self.env['oeh.medical.physician'].search([ 	
																('x_user_name', '=', user_name),		
															], 
															#order='appointment_date desc', 
															limit=1
															)

	#print doctor.id 
	#print doctor.name 
	
	doctor_id = doctor.id 
	
	return doctor_id




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
	chief_complaint = self.chief_complaint




	# Doctor 
	#doctor = self.physician.id

	doctor = get_actual_doctor(self)

	if doctor == False: 
		doctor = self.physician.id 





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




		#if order.state == 'sale': 
		if order.state == 'sale' 	and 	not order.x_procedure_created: 

			
			order.x_procedure_created = True



	
			for line in order.order_line:



				#if self.nr_procedures < order.nr_lines:			# ?



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

