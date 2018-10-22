# -*- coding: utf-8 -*-
#
#	Encapsulates actual Creation on Database. 
# 	Can not be Unit-tested (depends on a third-party library: Odoo). 
# 
#	Created: 			14 Aug 2018
# 	Last up: 	 		22 Sep 2018
#
import datetime
import time_funcs
import lib
import user 




# ----------------------------------------------------------- Update Order  ------------------------------------------------------
# Create Order
#def update_order(order, date_order=False):
#def update_order(order, date_order=False, serial_nr=False):
def update_order(order, date_order=False, serial_nr=False, counter=False):
	print
	print 'Update Order'


	# Update  
	if date_order != False: 
		ret = order.write({
							'date_order': date_order,
						})

	if serial_nr != False: 
		ret = order.write({
							'x_serial_nr': serial_nr,
						})


	if counter != False: 
		ret = order.write({
							'x_counter_value': counter,
						})





# ----------------------------------------------------------- Create Order Fast  ------------------------------------------------------
# Create Order
#def create_order_fast(self, patient_id, partner_id, treatment_id, id_doc, id_doc_type, short_name, qty):
def create_order_fast(self, patient_id, partner_id, doctor_id, treatment_id, id_doc, id_doc_type, short_name, qty):
	print
	print 'Create Order Fast'

	# Create Order 
	order = self.env['sale.order'].create({
											'patient': 		patient_id,	
											'partner_id': 	partner_id,
											'treatment': 	treatment_id,
											'x_id_doc': 	id_doc,														
											'x_id_doc_type': id_doc_type,														
											'x_doctor': 	doctor_id,	
											#'state':		'draft',
										})

	# Init 
	price_manual = -1
	price_applied = 0
	reco_id = False


	# Create Order Lines 
	#ret = creates.create_order_lines_micro(order, target_line, price_manual, price_applied, reco_id, qty)
	ret = create_order_lines_micro(order, short_name, price_manual, price_applied, reco_id, qty)




	return order 

# create_order_fast 




# ----------------------------------------------------------- Create Patient  ------------------------------------------------------
# Create Services - For Treatment
def create_patient(self, container_id, test_case, name, sex, address, id_doc_type, id_doc, ruc=False, firm=False, doctor_id=False, name_last='', name_first='', id_code=False, dni=False):
	#print
	#print 'Create Patient'
	#print name 

 	# Clear 
 	#remove_patient(self, name)

	# Init
	street = 	address.split(',')[0]
	street2_char = address.split(',')[1]
	city = 		address.split(',')[2]



	# Create Patient 
	if id_code != False: 	# With Id Code - Nr Historia

		#patient = self.env['oeh.medical.patient'].create({
		patient = self.patient_ids.create({
															'name': 	name,

															'x_last_name': name_last, 
															'x_first_name': name_first, 
															
															'sex': 		sex, 
															'street': 	street, 
															'street2_char': 	street2_char, 
															'city': 	city, 
															'x_ruc': 	ruc, 
															'x_firm': 	firm, 
															'x_first_contact': 'none', 
															'x_id_doc_type':	id_doc_type,
															'x_id_doc':			id_doc,  

															'x_test': 	True, 
															'x_test_case': 	test_case, 

															'x_id_code':		id_code,  
															'x_dni':		dni,  

															'container_id': 	container_id, 
												})

	else: 

		#patient = self.env['oeh.medical.patient'].create({
		patient = self.patient_ids.create({
															'name': 	name,

															'x_last_name': name_last, 
															'x_first_name': name_first, 
															
															'sex': 		sex, 
															'street': 	street, 
															'street2_char': 	street2_char, 
															'city': 	city, 
															'x_ruc': 	ruc, 
															'x_firm': 	firm, 
															'x_first_contact': 'none', 
															'x_id_doc_type':	id_doc_type,
															'x_id_doc':			id_doc,  

															'x_test': 	True, 
															'x_test_case': 	test_case, 

															'x_dni':		dni,  

															'container_id': 	container_id, 
												})


	#print patient





	# Treatment - Create  
	if doctor_id != False: 
		chief_complaint = 'acne_active'
		treatment = patient.treatment_ids.create({
													'patient': 			patient.id, 	
													'physician': 		doctor_id, 
													'chief_complaint': 	chief_complaint,
													
													'x_test': 	True, 
			})

	# Services - Create  
	#ret = cre.create_services(self, treatment)

	return patient






# ----------------------------------------------------------- Create Services  ------------------------------------------------------
# Create Services - For Treatment
def create_services(self, treatment):
	#print
	#print 'Create Services'

	# Create Services (Recoms)


	# Product
	service_id = user.get_product(self, 'acneclean')
	service_product = treatment.service_product_ids.create({
														'service': 		service_id, 
														'treatment': 	treatment.id, 
			})		
	#print service_product


	# Co2
	service_id = user.get_product(self, 'co2_nec_rn1_one')

	#zone = 'neck'
	#pathology = 'rejuvenation_neck_1'

	service_co2 = treatment.service_co2_ids.create({
														'service': 		service_id, 
														#'zone': 		zone, 
														#'pathology': 	pathology, 
														'treatment': 	treatment.id, 
			})
	#print service_co2




	# Exc 
	service_id = user.get_product(self, 'exc_bel_alo_15m_one')

	service_exc = treatment.service_excilite_ids.create({
															'service': 		service_id, 
															'treatment': 	treatment.id, 
		})
	#print service_exc




	# Ipl 
	service_id = user.get_product(self, 'ipl_bel_dep_15m_six')

	service_ipl = treatment.service_ipl_ids.create({
										'service': 		service_id, 
										'treatment': 	treatment.id, 
		})
	#print service_ipl




	# Ndyag 
	service_id = user.get_product(self, 'ndy_bol_ema_15m_six')

	service_ndyag = treatment.service_ndyag_ids.create({
										'service': 		service_id, 
										'treatment': 	treatment.id, 
		})
	#print service_ndyag



	# Quick
	service_id = user.get_product(self, 'quick_neck_hands_rejuvenation_1')

	service_quick = treatment.service_quick_ids.create({
														'service': 		service_id, 
														#'patient': 		patient_2.id, 
														#'physician': 	treatment.physician.id, 
														'treatment': 	treatment.id, 
			})
	#print service_quick


	return 0 



# ----------------------------------------------------------- Create Order - Target  ------------------------------------------------------
# Create Order - By Line
def create_order(self, target):
	#print
	#print 'Create Order'
	#print target
	#print 'x_vip_inprog: ', self.x_vip_inprog


	# Init

	# Doctor 
	doctor = user.get_actual_doctor(self)
	doctor_id = doctor.id 
	if doctor_id == False: 
		doctor_id = self.physician.id 




	# Pricelist 
	
	# Vip in Prog 
	if self.x_vip_inprog: 
		#print 'Vip in prog'
		
		pl = self.env['product.pricelist'].search([
															('name', '=', 'VIP'), 
													],
														#order='write_date desc',
														limit=1,
													)

	else: 
		pl = self.pricelist_id


	#print pl
	#print 'pricelist: ', pl.name
	#print pl.id
	


# Update Patient 
		if self.patient.x_id_doc in [False, '']: 
			if self.patient.x_dni not in [False, '']: 
		
				self.patient.x_id_doc_type = 'dni'

				self.patient.x_id_doc = self.patient.x_dni 



	# Create Order 
	order = self.env['sale.order'].create({
													'partner_id': self.partner_id.id,
													'patient': self.patient.id,	
													'state':'draft',
													'x_doctor': doctor_id,	
													'x_family': target, 
													'x_ruc': self.partner_id.x_ruc,
													'pricelist_id': pl.id, 

													'x_dni': self.partner_id.x_dni,	


													'x_id_doc': self.patient.x_id_doc,	
													'x_id_doc_type': self.patient.x_id_doc_type,	


													'treatment': self.id,
												})


# Create order lines 
	if target == 'consultation':
		if self.chief_complaint in ['monalisa_touch']:
			target_line = 'con_gyn'
		else:
			target_line = 'con_med'

		# Init 
		price_manual = -1
		price_applied = 0
		reco_id = False

		# Create 
		ret = create_order_lines_micro(order, target_line, price_manual, price_applied, reco_id)
		

	else:  	# Procedures 
		order_id = order.id

		ret = create_order_lines(self, 'quick', order_id)
		ret = create_order_lines(self, 'co2', order_id)
		ret = create_order_lines(self, 'excilite', order_id)
		ret = create_order_lines(self, 'ipl', order_id)
		ret = create_order_lines(self, 'ndyag', order_id)
		ret = create_order_lines(self, 'medical', order_id)
		ret = create_order_lines(self, 'cosmetology', order_id)
		ret = create_order_lines(self, 'product', order_id)

		#ret = user.create_order_lines(self, 'vip', order_id)

	return order
	
# create_order



#------------------------------------------------ Create Order Lines ---------------------------------------------------

# Create Order Lines 
def create_order_lines(self, laser, order_id):

	#print 
	#print 'User - Create Order Lines'
	#print laser 

	order = self.env['sale.order'].search([(
												'id','=', order_id),
											],
											#order='appointment_date desc',
											#limit=1,						
										)		
	_model = {
				'quick':		'openhealth.service.quick',
				'co2':			'openhealth.service.co2',
				'excilite':		'openhealth.service.excilite',				
				'ipl':			'openhealth.service.ipl',
				'ndyag':		'openhealth.service.ndyag',
				'medical':		'openhealth.service.medical',
				'cosmetology':		'openhealth.service.cosmetology',
				#'vip':			'openhealth.service.vip',
				'product':		'openhealth.service.product',
	}


	# Recommendations
	rec_set = self.env[_model[laser]].search([
														('treatment','=', self.id),
														('state','=', 'draft'),
											],
											#order='appointment_date desc',
											#limit=1,						
										)		

	# Recommendations
	for reco in rec_set: 

		#print 'Gotcha !'

		# Init 
		reco_id = reco.id
		name_short = reco.service.x_name_short		
		price_manual = reco.price_manual
		price_applied = reco.price_applied


		# Create the Order Line 
		ret = create_order_lines_micro(order, name_short, price_manual, price_applied, reco_id)


		# Update Recommendation State 
		reco.state = 'budget'


	return 0	# Always returns the same value 

# create_order_lines






# ----------------------------------------------------------- Create order lines ------------------------------------------------------
# Create Order Lines 
#def create_order_lines_micro(self, name_short, price_manual, price_applied, reco_id):		
def create_order_lines_micro(self, name_short, price_manual, price_applied, reco_id, qty=1):		
	print 
	print 'Create Order Lines - Micro'
	print 'name_short: ', name_short
	#print 'price_manual: ', price_manual
	#print 'price_applied:', price_applied
	#print 'reco_id: ', reco_id
	#print 


	# Init

	_h_field = {
					'consultation' : 	'service_consultation_id',
					'laser_co2' : 		'service_co2_id',
					'laser_quick' : 	'service_quick_id',
					'laser_excilite' : 	'service_excilite_id',
					'laser_ipl' : 		'service_ipl_id',
					'laser_ndyag' : 	'service_ndyag_id',
					'medical' : 		'service_medical_id',
					'cosmetology' : 	'service_cosmetology_id',
					'product' : 		'service_product_id',
			}

	# Product 
	product = self.env['product.product'].search([
													('x_name_short','=', name_short),
													('x_origin','=', False),
											])
	print product 
	print product.name 
	print product.type
	print product.x_family
	print product.x_treatment


	# Reco field 
	if product.type == 'service': 
		if product.x_family in ['laser', 'consultation', 'consultation_gyn']:
			categ = product.x_treatment
		else: 
			categ = product.x_family
	else: 
			categ = 'product'
	reco_field = _h_field[categ]


	# Print 
	#print product
	#print product.name
	#print product.x_treatment
	#print categ
	#print 



# Create Order Line


	# With the correct price 
	order_id = self.id


	# Manual Price  
	#if price_manual != 0: 
	if price_manual != -1: 

		#print 'Manual Price'

		ol = self.order_line.create({
										'name': 		product.name, 
										'product_id': 	product.id,
										'order_id': 	order_id,										
										'x_price_manual': price_manual, 
										'price_unit': 	price_manual,
										reco_field: reco_id, 

										'product_uom_qty': qty, 
									})



	# Quick Laser - With Price Applied 
	#elif product.x_treatment == 'laser_quick': 	
	elif product.x_treatment == 'laser_quick' 		and 	price_applied != -1: 

		#print 'Quick Laser Price - W Price Applied'
		
		price_quick = price_applied

		ol = self.order_line.create({
										'name': 		product.name, 
										'product_id': 	product.id,
										'order_id': 	order_id,
										'price_unit': 	price_quick,
										reco_field: 	reco_id, 

										'product_uom_qty': qty, 
									})




	# Normal case
	else: 
		
		#print 'Normal Price'

		ol = self.order_line.create({
										'name': 		product.name, 
										'product_id': 	product.id,
										'order_id': 	order_id,
										reco_field: 	reco_id, 

										'product_uom_qty': qty, 
								})

	# Update Order line
	#ol.update_fields(categ)

	return self.nr_lines

# create_order_lines_micro	






#------------------------------------------------ Create Procedure ---------------------------------------------------
# Create procedure 
#@api.multi
def create_procedure_go(self, app_date_str, subtype, product_id):

	#print
	#print 'Create Procedure - Go'
	#print app_date_str 
	#print subtype
	#print product_id


	# Init 
	treatment_id = self.id
	patient = self.patient.id
	chief_complaint = self.chief_complaint
	

	# Print 
	#print treatment
	#print patient
	#print chief_complaint


	# Doctor 
	doctor = user.get_actual_doctor(self)
	doctor_id = doctor.id 
	if doctor_id == False: 
		doctor_id = self.physician.id 


	# Time 
	GMT = time_funcs.Zone(0,False,'GMT')
	evaluation_start_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")




# Appointment 

	# Search
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
		delta, delta_sec = lib.get_delta_now(self, future)
		

	if appointment.name == False    or   delta_sec < 0: 		# If no appointment or appointment in the past 

		# Is the hour before 21:00
		app_date_ok = lib.doctor_available(self, app_date_str)
		
		if app_date_ok: 

			# Create App 
			appointment = self.env['oeh.medical.appointment'].create({
																		'appointment_date': app_date_str, 
																		'patient':			self.patient.id,
																		'doctor':			self.physician.id,
																		'state': 			'pre_scheduled', 
																		'x_type': 			'procedure', 
																		'x_subtype': 		subtype, 

																		'treatment':		self.id, 
																})
	appointment_id = appointment.id
	#print appointment





	# Search Product Product 
	product_product = self.env['product.product'].search([
																('id','=', product_id),
								])
	# Search Product Template 
	product_template = self.env['product.template'].search([
																('x_name_short','=', product_product.x_name_short),
																('x_origin','=', False),
								])
	
	

# Create Proc

	# Init 
	consultation_id = False
	procedure_id = False
	session_id = False
	control_id = False
	
	ret = 0 


	app_date_ok = lib.doctor_available(self, app_date_str)

	if app_date_ok: 

		# Create Procedure 
		procedure = self.procedure_ids.create({
												'evaluation_start_date':app_date_str,
												'appointment': appointment_id,
												'patient':patient,
												'doctor':doctor_id,														
												'product':product_template.id,																
												'chief_complaint':chief_complaint,

												'treatment':treatment_id,	
											})
		procedure_id = procedure.id



		# Create Session - New 
		session = self.env['openhealth.session.med'].create({
																'evaluation_start_date':app_date_str,
																'appointment': appointment_id,
																'patient': patient,
																'doctor': doctor_id,													
																'product': product_template.id,
																'chief_complaint': chief_complaint,
																#'evaluation_type':evaluation_type,
																#'laser': laser,

																'procedure': procedure_id,				
																'treatment': treatment_id,	
														})
		session_id = session.id 



	# Update Appointment 
	if procedure_id != False: 

		ret = user.update_appointment_handlers(self, appointment_id, consultation_id, procedure_id, session_id, control_id)


	return ret	
# create_procedure_go



# ----------------------------------------------------------- Create Procedure ------------------------------------------------------
# Create Procedure With Appoointment   
def create_procedure_wapp(self, subtype, product_id):
	#print 
	#print 'Create Proc - With App'

	# Init 
	duration = 0.5
	x_type = 'procedure'
	doctor_name = self.x_doctor.name
	states = False

	# Date 
	date_format = "%Y-%m-%d %H:%M:%S"
	dt = datetime.datetime.strptime(self.date_order, date_format) + datetime.timedelta(hours=-5,minutes=0)		# Correct for UTC Delta 

	# Get Next Slot - Real Time version 
	#appointment_date = dt.strftime("%Y-%m-%d") + " 14:00:00"			# Early strategy: 09:00 am
	appointment_date_str = lib.get_next_slot(self)						# Next Slot

	# Prints 
	#print product_id
	#print subtype
	#print appointment_date_str
	#print self.date_order
	#print date_early
	#print 

	# If slot available 
	if appointment_date_str != False: 
		
		# Check and Push if not Free !
		appointment_date_str = user.check_and_push(self, appointment_date_str, duration, x_type, doctor_name, states)

		# Create Procedure 
		self.treatment.create_procedure(appointment_date_str, subtype, product_id)

# create_procedure_wapp


# ----------------------------------------------------------- Remove Patient  ------------------------------------------------------
def remove_patient(self, name):
	#print 
	#print 'Remove Patient'
	#print name 

	# Unlink Patient
	patients = self.env['oeh.medical.patient'].search([
															('name', '=', name), 
														],).unlink()

	# Unlink Partner 
	partners = self.env['res.partner'].search([
														('name', '=', name), 
													],).unlink()


	# Unlink - Card
 	#cards = self.env['openhealth.card'].search([
	#													('patient_name', '=', name), 	
	#												],)
 	#for card in cards: 
 	#	if card.name != False: 
 	#		card.unlink()

