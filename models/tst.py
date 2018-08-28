# -*- coding: utf-8 -*-
#
# 	tst.py
#  	
# 	Integration Tests for the Treatment Class
#
# Created: 			14 Aug 2018
# Last up: 	 		14 Aug 2018
# 



# ----------------------------------------------------------- Test Integration - Treatment ------------------------------------------------------

# Test - Integration 

def test_integration_treatment(self, date_order_begin, date_order_end):

	print 
	print 'Test Integration'


	# Appointment - Consultation 
	print 
	print 'Create Appointment - Consultation'
	x_type = 'consultation'
	subtype = 'consultation'
	state = 'pre_scheduled'
	self.create_appointment_nex(x_type, subtype, state)


	# Order - Consultation 
	print 
	print 'Create Order - Consultation'
	self.create_order_con()
	for order in self.order_ids: 
		
		#order.pay_myself()

		#date_order = '2018-09-01 14:00:00'

		order.pay_myself(date_order_begin)
		


	# Consultation 
	print 
	print 'Create Consultation'
	self.create_consultation()
	for consultation in self.consultation_ids: 
		consultation.autofill()



	# Recommendations - Order Procedure 
	print 
	print 'Create Recommendations'
	
	if True:
	#if False:
		#self.create_recommendations()
		create_recommendations(self)
		
		self.create_order_pro()
	else: 
		#self.create_order_pro_lines()
		create_order_pro_lines(self)



	# Pay Order Procedure 
	if True: 
	#if False:
		print 
		print 'Create Order - Procedure'
		for order in self.order_ids: 
			#order.pay_myself()
			#date_order = '2018-10-01 02:00:00'
			order.pay_myself(date_order_end)




	# Sessions 
	#if True: 
	if False:	
		print 
		print 'Create Sessions'
		#self.create_sessions()
		for procedure in self.procedure_ids: 
			procedure.create_sessions()



	# Controls 
	#if True: 
	if False:	
		print 
		print 'Create Controls'
		for procedure in self.procedure_ids: 
			procedure.create_controls()
			#procedure.create_sessions()





	#print 
# test_integration_treatment




# ----------------------------------------------------------- Create Recommendations  ------------------------------------------------------

# Create Recommendations 
#@api.multi 
def create_recommendations(self):

	print 
	print 'Create Recommendations'


	# Quick 
	if self.qui_create: 
		print 'Quick'
		service = self.env['product.template'].search([
															('x_name_short', '=', 'quick_neck_hands_rejuvenation_1'),
											],
												#order='date_order desc',
												limit=1,
											)
		service_id = service.id
		#print service
		self.service_quick_ids.create({
											'service': 		service_id, 
											'patient': 		self.patient.id, 
											'physician': 	self.physician.id, 
											'treatment': 	self.id, 
			})


	# Co2 
	if self.co2_create: 
		print 'Co2'

		zone = 'neck'

		service = self.env['product.template'].search([
															('x_name_short', '=', 'co2_nec_rn1_one'),
											],
												#order='date_order desc',
												limit=1,
											)
		service_id = service.id
		#print service
		self.service_co2_ids.create({
											'service': 		service_id, 
											'zone': 		zone, 
											'treatment': 	self.id, 
			})



	# Excilite 
	if self.exc_create: 
		print 'Exc'

		zone = 'belly'

		service = self.env['product.template'].search([
															('x_name_short', '=', 'exc_bel_alo_15m_one'),
											],
												#order='date_order desc',
												limit=1,
											)
		service_id = service.id
		#print service
		self.service_excilite_ids.create({
											'service': 		service_id, 
											'zone': 		zone, 
											'treatment': 	self.id, 
			})


	# Ipl 
	if self.ipl_create: 
		print 'Ipl'

		zone = 'belly'

		service = self.env['product.template'].search([
															('x_name_short', '=', 'ipl_bel_dep_15m_six'),
											],
												#order='date_order desc',
												limit=1,
											)
		service_id = service.id
		#print service
		self.service_ipl_ids.create({
											'service': 		service_id, 
											'zone': 		zone, 
											'treatment': 	self.id, 
			})




	# Ndyag
	if self.ndy_create: 
		print 'Ndyag'

		zone = 'body_local'

		service = self.env['product.template'].search([
															('x_name_short', '=', 'ndy_bol_ema_15m_six'),
											],
												#order='date_order desc',
												limit=1,
											)
		service_id = service.id
		#print service
		self.service_ndyag_ids.create({
											'service': 		service_id, 
											'zone': 		zone, 
											'treatment': 	self.id, 
			})








	# Medical 
	if self.med_create: 
		
		med_short_names = [
								'bot_1zo_rfa_one', 		# Bot
								
								#'cri_faa_acn_ten', 		# Crio
								#'hac_1hy_rfa_one', 		# Hial
								#'infiltration_scar', 	# Infil
								#'infiltration_keloid', 	# Infil

								#'ivc_na_na_one', 		# Intra
								#'lep_faa_acn_one', 		# Lep
								#'pla_faa_rfa', 			# Pla
								#'men_faa_rfa', 			# Meso
								#'scl_leg_var_one', 		# Escl
		]


		print 'Medical'
		
		for short_name in med_short_names: 

			service = self.env['product.template'].search([
																#('x_name_short', '=', 'cri_faa_acn_ten'),
																('x_name_short', '=', short_name),
												],
													#order='date_order desc',
													limit=1,
												)
			service_id = service.id

			#print service

			self.service_medical_ids.create({
												'service': 		service_id, 
												'treatment': 	self.id, 
				})




	# Cosmeto
	if self.cos_create: 

		cos_short_names = [
								'car_bod_rfa_30m_six', 		# Carboxi
								
								#'dit_fac_dfc_30m_one', 		# Diamond tip 
								#'tca_fdn_rfa_30m_six', 		# Triactive Carbo
								#'tcr_boa_rwm_one', 			# Tri Carbo Redu
		]


		print 'Cosmeto'
		
		for short_name in cos_short_names: 
			
			service = self.env['product.template'].search([
																('x_name_short', '=', short_name),
												],
													#order='date_order desc',
													limit=1,
												)
			service_id = service.id

			#print service

			self.service_cosmetology_ids.create({
												'service': 		service_id, 
												'treatment': 	self.id, 
				})





	# Vip
	if self.vip_create: 
		print 'Vip'
		service = self.env['product.template'].search([
															('x_name_short', '=', 'vip_card'),
											],
												#order='date_order desc',
												limit=1,
											)
		service_id = service.id
		#print service
		self.service_vip_ids.create({
											'service': 		service_id, 
											'treatment': 	self.id, 
			})





	# Product
	if self.product_create: 
		print 'Product'

		prod_short_names = [
								'acneclean', 		# Acneclean
								'vip_card', 		# Vip 
		]


		#print 'product'
		
		for short_name in prod_short_names: 

			service = self.env['product.template'].search([
																('x_name_short', '=', short_name),
												],
													#order='date_order desc',
													limit=1,
												)
			service_id = service.id
			#print service
			self.service_product_ids.create({
												'service': 		service_id, 
												'treatment': 	self.id, 
				})

# create_recommendations




# ----------------------------------------------------------- Create Order With Lines ------------------------------------------------------
	
# Create Order Procedure With Lines 
#@api.multi
def create_order_pro_lines(self):

	print 
	print 'Create Order Procedure With Lines'
	


	# Create Order 
	order = self.env['sale.order'].create({
													'partner_id': self.partner_id.id,
													'patient': self.patient.id,	
													'pricelist_id': self.patient.property_product_pricelist.id, 
													'x_doctor': self.physician.id,	
													'x_family': 'procedure', 
													'state':'draft',
													'treatment': self.id,
												}
											)

	# Create Order Lines 
	name_shorts = [	
						'co2_nec_rn1_one',					# Cos 
						'exc_bel_alo_15m_one',				# Exc
						'ipl_bel_dep_15m_six',				# Ipl
						'ndy_bol_ema_15m_six',				# Ndyag 
						'quick_neck_hands_rejuvenation_1',	# Quick
						'bot_1zo_rfa_one', 			# Medical
						'car_bod_rfa_30m_six', 		# Cosmeto
						'acneclean', 				# Product
						'vip_card', 				# Product 
				]

	# Init 
	price_manual = 0
	price_applied = 0 
	reco_id= False

	# Create 
	for name_short in name_shorts: 
		ret = order.x_create_order_lines_target(name_short, price_manual, price_applied, reco_id)

# create_order_pro_lines



# ----------------------------------------------------------- Reset Treatment ------------------------------------------------------

# Reset 
def reset_treatment(self):

	#print 
	#print 'Reset'

	# Consultation 
	self.consultation_ids.unlink()

	# Recos
	self.service_product_ids.unlink()

	self.service_vip_ids.unlink()
	self.service_quick_ids.unlink()
	self.service_co2_ids.unlink()
	self.service_excilite_ids.unlink()
	self.service_ipl_ids.unlink()
	self.service_ndyag_ids.unlink()
	self.service_medical_ids.unlink()
	self.service_cosmetology_ids.unlink()

	self.procedure_ids.unlink()
	self.session_ids.unlink()
	self.control_ids.unlink()

	self.appointment_ids.unlink()

	# Orders 
	for order in self.order_ids:
		order.remove_myself()

	# Alta 
	self.treatment_closed = False


	# Conter Decrease 
	name_ctr = 'advertisement'
	
	counter = self.env['openhealth.counter'].search([
															('name', '=', name_ctr), 
													],
														#order='write_date desc',
														limit=1,
													)
	counter.decrease()
	counter.decrease()

# reset





# ----------------------------------------------------------- Test Appointment  ------------------------------------------------------

# Test - Appointment 
def test_appointment(self):

	print 
	print 'Test Appointment'


	
	# Case 1 - Consultation
	print 'Consultation'
	x_type = 'consultation'
	subtype = 'consultation'
	state = 'pre_scheduled'
	self.create_appointment_nex(x_type, subtype, state)



	# Case 2 - Procedure
	print 
	print 'Procedure'
	x_type = 'procedure'
	subtype = 'laser_co2'
	state = 'Scheduled'	
	self.create_appointment_nex(x_type, subtype, state)



	# Case 3 - Control
	print 
	print 'Control'
	x_type = 'control'
	subtype = 'laser_co2'
	state = 'pre_scheduled_control'	
	self.create_appointment_nex(x_type, subtype, state)



	# Case 4 - Session
	print 
	print 'Session'
	x_type = 'session'
	subtype = 'laser_co2'
	
	#state = 'pre_scheduled_control'	
	state = 'pre_scheduled'	
	
	self.create_appointment_nex(x_type, subtype, state)

# test_appointment




# ----------------------------------------------------------- Create Booleans ------------------------------------------------------
	
# Clear  
#@api.multi 
def clear_all(self):
	#print 
	#print 'Clear'
	if self.patient.x_test: 
		# Clean
		self.co2_create = False
		self.exc_create = False
		self.ipl_create = False
		self.ndy_create = False
		self.qui_create = False		
		self.med_create = False
		self.cos_create = False
		self.vip_create = False
		self.product_create = False
# clear 


# All  
#@api.multi 
def set_all(self):
	#print 
	#print 'All'
	if self.patient.x_test: 
		# All
		self.co2_create = True
		self.exc_create = True
		self.ipl_create = True
		self.ndy_create = True
		self.qui_create = True		
		self.med_create = True
		self.cos_create = True
		self.vip_create = True
		self.product_create = True
# all 


