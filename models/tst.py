# -*- coding: utf-8 -*-
#
# 	tst.py
#  	
# 	Integration Tests for the Treatment Class
#
#	Created: 			14 Aug 2018
#	Last up: 	 		14 Aug 2018
# 



# ----------------------------------------------------------- Test Integration - Treatment ------------------------------------------------------
# Test - Integration - Treatment 
def test_integration_treatment(self, date_order_begin=False, date_order_end=False):
	print 
	print 'Treatment - Test Integration'


	# Appointment - Consultation 
	print 
	print 'Create App - Consultation'
	x_type = 'consultation'
	subtype = 'consultation'
	state = 'pre_scheduled'
	self.create_appointment_nex(x_type, subtype, state)



	# Sale - Consultation 
	print 
	print 
	print 'Create Order - Consultation'
	
	self.create_order_con()			# Actual Button 

	for order in self.order_ids: 
		if order.state in ['draft']: 
			#order.pay_myself(date_order_begin)
			order.pay_myself()

			print 'Pay'
			print 'Pricelist: ', 			order.pricelist_id.name		# Verify 
			print 'order.amount_total: ', 	order.amount_total		# Verify 
			print 'Assert'
			order.test()
			


	# Consultation 
	print 
	print 
	print 'Create Consultation'
	self.create_consultation()
	for consultation in self.consultation_ids: 
		consultation.autofill()


	# Recommendations 
	# Sale Procedure 
	if True:
		print 
		print 
		print 'Create Recommendations'

		create_recommendations(self)

		self.create_order_pro()			# Actual Button 
	

	else: 
		create_order_pro_lines(self)



	# Pay Order Procedure 
	#if True: 
	#if False:
	print 
	print 
	print 'Create Order - Procedure'
	for order in self.order_ids: 
		if order.state in ['draft']: 
			order.pay_myself()
			print 'Pay'
			print 'Pricelist: ', 	order.pricelist_id.name		# Verify 
			print 'amount_total: ', order.amount_total			# Verify 
			print 'Assert'
			order.test()




	# Sessions 
	if False:
	#if self.ses_create:
		print 
		print 
		print 'Create Sessions'
		for procedure in self.procedure_ids: 
			for _ in range(2): 
				procedure.create_sessions()


	# Controls 
	if False:
	#if self.con_create:
		print 
		print 'Create Controls'
		for procedure in self.procedure_ids: 
			for _ in range(6): 
				procedure.create_controls()

# test_integration_treatment




# ----------------------------------------------------------- Create Recommendations  ------------------------------------------------------

# Create Recommendations 
def create_recommendations(self):
	#print 
	#print 'Create Recommendations'



	# Vip
	if self.vip_create: 
		print 
		print 'Vip'

		product_id = self.env['product.template'].search([
															('x_name_short', '=', 'vip_card'),
											],
												#order='date_order desc',
												limit=1,
											).id
		#service_id = service.id
		#print service
		#self.service_vip_ids.create({
		service = self.service_product_ids.create({
													'service': 		product_id, 
													'treatment': 	self.id, 
			})
		print service.service.name 
		print service.service.list_price




	# Product
	if self.product_create: 
		print 
		print 'Product'

		prod_short_names = [
								'acneclean', 		# Acneclean
								#'vip_card', 		# Vip 
		]


		#print 'product'
		
		for short_name in prod_short_names: 

			product_id = self.env['product.template'].search([
																('x_name_short', '=', short_name),
												],
													#order='date_order desc',
													limit=1,
												).id
			#service_id = service.id
			#print service
			service = self.service_product_ids.create({
														'service': 		product_id, 
														'treatment': 	self.id, 
				})
			print service.service.name 
			print service.service.list_price




	# Co2 
	if self.co2_create: 
		print 
		print 'Co2'

		zone = 'neck'
		product_id = self.env['product.template'].search([
															('x_name_short', '=', 'co2_nec_rn1_one'),
											],
												#order='date_order desc',
												limit=1,
											).id
		#service_id = service.id
		#print service
		service = self.service_co2_ids.create({
											'service': 		product_id, 
											'zone': 		zone, 
											'treatment': 	self.id, 
			})
		#service.test()
		print service.service.name 
		print service.service.list_price
		print service.service.x_price_vip



	# Excilite 
	if self.exc_create: 
		print 'Exc'

		zone = 'belly'

		product_id = self.env['product.template'].search([
															('x_name_short', '=', 'exc_bel_alo_15m_one'),
											],
												#order='date_order desc',
												limit=1,
											).id
		#service_id = service.id
		#print service
		service = self.service_excilite_ids.create({
											'service': 		product_id, 
											'zone': 		zone, 
											'treatment': 	self.id, 
			})
		#service.test()



	# Ipl 
	if self.ipl_create: 
		print 'Ipl'

		zone = 'belly'

		product_id = self.env['product.template'].search([
															('x_name_short', '=', 'ipl_bel_dep_15m_six'),
											],
												#order='date_order desc',
												limit=1,
											).id
		#service_id = service.id
		#print service
		self.service_ipl_ids.create({
											'service': 		product_id, 
											'zone': 		zone, 
											'treatment': 	self.id, 
			})




	# Ndyag
	if self.ndy_create: 
		print 'Ndyag'

		zone = 'body_local'

		product_id = self.env['product.template'].search([
															('x_name_short', '=', 'ndy_bol_ema_15m_six'),
											],
												#order='date_order desc',
												limit=1,
											).id
		#service_id = service.id
		#print service
		self.service_ndyag_ids.create({
											'service': 		product_id, 
											'zone': 		zone, 
											'treatment': 	self.id, 
			})


	# Quick 
	if self.qui_create: 
		print 'Quick'
		product = self.env['product.template'].search([
															#('x_name_short', '=', 'quick_neck_hands_rejuvenation_1'),
															('x_name_short', '=', 'qui_nec-han_rej_30m_one'),
											],
												#order='date_order desc',
												limit=1,
											)
		
		#service_id = service.id
		
		product_id = product.id

		#print service
		self.service_quick_ids.create({
											'service': 		product_id, 
											'patient': 		self.patient.id, 
											'physician': 	self.physician.id, 
											'treatment': 	self.id, 

											#'price_applied': 	product.x_price_vip
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

			product_id = self.env['product.template'].search([
																#('x_name_short', '=', 'cri_faa_acn_ten'),
																('x_name_short', '=', short_name),
												],
													#order='date_order desc',
													limit=1,
												).id
			#service_id = service.id
			#print service

			self.service_medical_ids.create({
												'service': 		product_id, 
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
			
			product_id = self.env['product.template'].search([
																('x_name_short', '=', short_name),
												],
													#order='date_order desc',
													limit=1,
												).id
			#service_id = service.id

			#print service

			self.service_cosmetology_ids.create({
												'service': 		product_id, 
												'treatment': 	self.id, 
				})











# create_recommendations




# ----------------------------------------------------------- Create Order With Lines ------------------------------------------------------
	
# Create Order Procedure With Lines 
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
		
		self.product_create = False
		self.vip_create = False

		#self.ses_create = False
		#self.con_create = False

# clear 


# All  
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
		
		self.product_create = True
		self.vip_create = True

		#self.ses_create = True
		#self.con_create = True
# all 





# ----------------------------------------------------------- Reset Treatment ------------------------------------------------------

# Reset 
def reset_treatment(self):
	print 
	print 'Reset'


	# Card 
	card = self.env['openhealth.card'].search([
													('patient_name', '=', self.patient.name), 
												],
													#order='write_date desc',
													limit=1,
											)
	print card
	print card.patient_name
	#if card.name != False: 
		#card.unlink()



	# Consultation 
	self.consultation_ids.unlink()

	# Recos
	self.service_product_ids.unlink()
	#self.service_vip_ids.unlink()
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

	# Alta 
	self.treatment_closed = False


	# Orders 
	for order in self.order_ids:
		order.remove_myself()


	# Conter Decrease - Deprecated !!!
	#name_ctr = 'advertisement'
	#counter = self.env['openhealth.counter'].search([
	#														('name', '=', name_ctr), 
	#												],
														#order='write_date desc',
	#													limit=1,
	#												)
	#counter.decrease()
	#counter.decrease()

# reset
