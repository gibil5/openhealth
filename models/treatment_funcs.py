# -*- coding: utf-8 -*-
#
# 		*** Treatment Funcs
# 
# Created: 			26 Aug 2016
# Last up: 	 		 7 Jul 2018
#


from openerp import models, fields, api
from datetime import datetime,tzinfo,timedelta
from . import time_funcs
from . import jrfuncs

import appfuncs



#------------------------------------------------ Create Procedure ---------------------------------------------------

# Create procedure 
@api.multi
def create_procedure_go(self, app_date_str, subtype, product_id):

	#print
	#print 'Create Procedure - Go'
	#print app_date_str 
	#print subtype
	#print product_id


	# Init 
	treatment = self.id
	patient = self.patient.id
	chief_complaint = self.chief_complaint
	#treatment = treatment_id
	#patient = patient_id
	#chief_complaint = chief_complaint

	#print treatment
	#print patient
	#print chief_complaint

	# Doctor 
	#doctor = self.physician.id
	doctor = get_actual_doctor(self)
	if doctor == False: 
		doctor = self.physician.id 

	# Time 
	GMT = time_funcs.Zone(0,False,'GMT')
	evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")




	# Appointment 


	# Search
	#print 'Search App'
	appointment = self.env['oeh.medical.appointment'].search([ 	
																('patient', '=', 	self.patient.name),		
																('doctor', '=', 	self.physician.name), 

																('x_type', '=', 	'procedure'), 
																('x_subtype', '=', 	subtype), 
														], 
															order='appointment_date desc', limit=1)
	#print appointment



	# Check if existing App is in the Future 
	if appointment.name != False: 
	
		# Delta 
		future = appointment.appointment_date
		delta, delta_sec = appfuncs.get_delta_now(self, future)
		
		#print future
		#print delta 
		#print delta_sec 





	# Create App 
	#if appointment.name == False: 
	if appointment.name == False    or   delta_sec < 0: 		# If no appointment or appointment in the past 

		#print 'Create App'

		doctor_available = appfuncs.doctor_available(self, app_date_str)
		
		#print doctor_available


		if doctor_available: 

			appointment = self.env['oeh.medical.appointment'].create({
																		'appointment_date': app_date_str, 

																		'patient':			self.patient.id,
																		'doctor':			self.physician.id,
																		'state': 			'pre_scheduled', 

																		'x_type': 			'procedure', 
																		'x_subtype': 		subtype, 

																		'treatment':	self.id, 
																})

	appointment_id = appointment.id
	#print appointment





	# Loop - Create Procedures 
	#ret = 0
	#for order in self.order_pro_ids:
		#if order.state == 'sale' 	and 	not order.x_procedure_created: 
			# Update 
			#order.x_procedure_created = True
			# Loop
			#for line in order.order_line:
	# Init 
	#product_product = line.product_id
	#product_product = product_id





	# Search 
	product_product = self.env['product.product'].search([
																('id','=', product_id),
																#('x_name_short','=', product_product.x_name_short),
																#('x_origin','=', False),
								])


	# Search 
	product_template = self.env['product.template'].search([
																('x_name_short','=', product_product.x_name_short),
																('x_origin','=', False),
								])
	
	

	# Create - If Service 
	#if line.product_id.type == 'service':



	#print 'Create Proc'

	procedure_id = False
	ret = 0 


	doctor_available = appfuncs.doctor_available(self, app_date_str)

	if doctor_available: 

		procedure = self.procedure_ids.create({
												'evaluation_start_date':app_date_str,

												'patient':patient,
												'doctor':doctor,														
												'product':product_template.id,																
												'chief_complaint':chief_complaint,
												'appointment': appointment_id,

												'treatment':treatment,	
											})
		procedure_id = procedure.id




	# Update Appointment 
	if procedure_id != False: 
		ret = jrfuncs.update_appointment_go(self, appointment_id, procedure_id, 'procedure')



	return ret	
# create_procedure_go





#------------------------------------------------ Create Order Lines ---------------------------------------------------

# Create Order Lines 
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
	_model = {
				'quick':		'openhealth.service.quick',
				'vip':			'openhealth.service.vip',
				'co2':			'openhealth.service.co2',
				'excilite':		'openhealth.service.excilite',
				'ipl':			'openhealth.service.ipl',
				'ndyag':		'openhealth.service.ndyag',
				'medical':		'openhealth.service.medical',
	}

	# Services 
	rec_set = self.env[_model[laser]].search([
														('treatment','=', self.id),
														('state','=', 'draft'),
											
												],
											#order='appointment_date desc',
											#limit=1,						
											)		

	if rec_set != False: 
		for service in rec_set: 
			target_line = service.service.x_name_short
			price_manual = service.price_manual
			price_applied = service.price_applied

			ret = order.x_create_order_lines_target(target_line, price_manual, price_applied)

			# Update state 
			service.state = 'budget'
	return 0

# create_order_lines




#------------------------------------------------ Get Actual Doctor ---------------------------------------------------

# Get Actual Doctor 
@api.multi
def get_actual_doctor(self):

	#print 'jx'
	#print 'Get Actual Doctor'

	user_name =  self.env.user.name 	
	doctor = self.env['oeh.medical.physician'].search([ 	
																('x_user_name', '=', user_name),		
															], 
															#order='appointment_date desc', 
															limit=1
															)
	doctor_id = doctor.id 

	return doctor_id

# get_actual_doctor


