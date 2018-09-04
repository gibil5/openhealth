

# 30 Aug 2018 



# ----------------------------------------------------------- Test - Vars ------------------------------------------------------

	# Nr Deltas 
	nr_delta = fields.Integer(
			'Nr Deltas', 
			#default=-1, 
		)


	# Test 
	test = fields.Boolean(
			'Test', 
		)

	prod_test = fields.Boolean(
			'Prod', 
		)

	consu_test = fields.Boolean(
			'Consu', 
		)

	laser_test = fields.Boolean(
			'Laser', 
		)

	medi_test = fields.Boolean(
			'Med', 
		)

	cosme_test = fields.Boolean(
			'Cos', 
		)

	other_test = fields.Boolean(
			'Otros', 
		)


# ----------------------------------------------------------- Test - Clear ------------------------------------------------------
	# Clear 
	#@api.multi
	def clear(self, patient_name, doctor_name): 
		#print 
		#print 'Clear'

		# Treatment 
		treatment = self.env['openhealth.treatment'].search([
																('patient', '=', patient_name),
																('physician', '=', doctor_name),
											],
												order='start_date desc',
												limit=1,
											)
		for order in treatment.order_ids: 
			order.remove_myself()
		treatment.appointment_ids.unlink()
		treatment.procedure_ids.unlink()


	# Test Clear 
	@api.multi
	def test_clear(self):  
		# Init 
		patient_name = 'TOTTI TOTTI FRANCESCO'
		doctor_name = 'Dr. Chavarri'
		# Clear 
		self.clear(patient_name, doctor_name)			




# ----------------------------------------------------------- Test - Integration ------------------------------------------------------
	# Test
	@api.multi
	def test_integration(self):  
		#print 
		#print 'Test'
		if self.test: 

			# Init 
			#patient_name = 'REVILLA RONDON JOSE JAVIER'
			patient_name = 'TOTTI TOTTI FRANCESCO'
			doctor_name = 'Dr. Chavarri'

			# Clear 
			self.clear(patient_name, doctor_name)			

			
			# Products 
			products = [
							# Products 
							('acneclean', 	1, 'product'), 

							# Consultations 
							('con_med', 	1, 'consultation'), 
							('con_gyn', 	1, 'consultation'), 

							# Laser 
							('co2_nec_rn1_one', 	1, 'laser'), 
							('exc_bel_alo_15m_one', 1, 'laser'), 
							('ipl_bel_dep_15m_six', 1, 'laser'), 
							('ndy_bol_ema_15m_six', 1, 'laser'), 
							('quick_neck_hands_rejuvenation_1', 1, 'laser'), 
							
							# Cosmeto
							('car_bod_rfa_30m_six', 1, 'cosmetology'), 

							# Other 
							('other', 	1, 'other'), 

							# Medical
							('bot_1zo_rfa_one', 1, 'medical'), 	# Bot
							('cri_faa_acn_ten', 1, 'medical'), 	# Crio
							('hac_1hy_rfa_one', 1, 'medical'), 	# Hial
							('infiltration_scar', 1, 'medical'), 	# Infil
							('infiltration_keloid', 1, 'medical'), 	# Infil
							('ivc_na_na_one', 1, 'medical'), 		# Intra
							('lep_faa_acn_one', 1, 'medical'), 		# Lep
							('pla_faa_rfa', 1, 'medical'), 			# Pla
							('men_faa_rfa', 1, 'medical'), 			# Meso
							('scl_leg_var_one', 1, 'medical'), 		# Escl
						]

			type_arr = [
							'product', 
							'consultation', 
							'laser', 
							'medical', 
							'cosmetology', 
							'other', 
			]


			# Create 
			print 'Create'
			order = self.create_order(patient_name, doctor_name, products, type_arr)

			# Pay
			order.pay_myself()


			# Update
			print 'Update'
			self.update_sales()
			self.update_stats()
			self.update_counters()
			#self.update_qc()




# ----------------------------------------------------------- Test - Create Order ------------------------------------------------------
	
	# Create Order 
	@api.multi
	def create_order(self, patient_name, doctor_name, products, type_arr):  
		#print 
		#print 'Create Order'

		# Treatment 
		treatment = self.env['openhealth.treatment'].search([
																('patient', '=', patient_name),
																('physician', '=', doctor_name),
											],
												order='start_date desc',
												limit=1,
											)
		# Patient
		patient = self.env['oeh.medical.patient'].search([
																('name', '=', patient_name),
											],
												order='create_date desc',
												limit=1,
											)
		# Doctor
		doctor = self.env['oeh.medical.physician'].search([
																('name', '=', doctor_name),
											],
												order='create_date desc',
												limit=1,
											)
		# Partner
		partner = self.env['res.partner'].search([
																('name', '=', patient_name),
											],
												order='create_date desc',
												limit=1,
											)
		# Pricelist 
 		pricelist = self.env['product.pricelist'].search([
															('name', '=', 'Public Pricelist'), 
													],
														#order='write_date desc',
														limit=1,
													)
		# Create Order 
		order = self.env['sale.order'].create({
													'patient': patient.id,	
													'pricelist_id': pricelist.id, 
													'partner_id': partner.id,
													'x_doctor': doctor.id,	
													'state':'draft',
													'treatment': treatment.id,
												}
											)

		# Order line 
		for product in products: 
			name = 	product[0]
			qty = 	product[1]
			x_type = product[2]
			if 	(x_type == 'product' and self.prod_test) or 		\
				(x_type == 'consultation' and self.consu_test) or 	\
				(x_type == 'laser' and self.laser_test) or 			\
				(x_type == 'medical' and self.medi_test) or			\
				(x_type == 'cosmetology' and self.cosme_test) or  	\
				(x_type == 'other' and self.other_test):

				# Product
				product = self.env['product.product'].search([
																('x_name_short', '=', name),
													],
														order='create_date desc',
														limit=1,
													)
				# Order line 
				order_line = order.order_line.create({
														'product_id': product.id,
														'product_uom_qty': qty, 

														'order_id': order.id,
										})
		return order 




# ----------------------------------------------------------- Update Counters ------------------------------------------------------

	# Update counters
	def update_counters(self):  
		#print 
		#print 'Update counters'

		# Init 
		self.nr_consultations = 0 
		self.nr_products = 0 
		self.nr_procedures = 0 

		self.amo_consultations = 0 
		self.amo_products = 0 
		self.amo_procedures = 0 

		self.avg_consultations = 0 
		self.avg_products = 0 
		self.avg_procedures = 0 

		self.ratio_pro_con = 0 


		self.nr_co2 = 0 
		self.nr_exc = 0 
		self.nr_ipl = 0 
		self.nr_ndyag = 0 
		self.nr_quick = 0 
		self.nr_medical = 0 
		self.nr_cosmetology = 0 

		self.amo_co2 = 0 
		self.amo_exc = 0 
		self.amo_ipl = 0 
		self.amo_ndyag = 0 
		self.amo_quick = 0 
		self.amo_medical = 0 
		self.amo_cosmetology = 0 

		self.avg_co2 = 0 
		self.avg_exc = 0 
		self.avg_ipl = 0 
		self.avg_ndyag = 0 
		self.avg_quick = 0 
		self.avg_medical = 0 
		self.avg_cosmetology = 0 




		
		# Loop - Families 
		for family in self.family_line: 

			# Consultations 
			if family.meta == 'consultation': 
				self.nr_consultations = self.nr_consultations +  family.x_count
				self.amo_consultations = self.amo_consultations + family.amount

			# Products 
			elif family.meta == 'product': 
				self.nr_products = self.nr_products +  family.x_count
				self.amo_products = self.amo_products + family.amount

			# Procedures 
			elif family.meta == 'procedure': 
				self.nr_procedures = self.nr_procedures +  family.x_count
				self.amo_procedures = self.amo_procedures + family.amount


		

		# Loop - Subfamilies 
		for sub_family in self.sub_family_line: 

			if sub_family.name == 'laser_co2': 				
				self.nr_co2 = self.nr_co2 +  sub_family.x_count
				self.amo_co2 = self.amo_co2 + sub_family.amount

			elif sub_family.name == 'laser_excilite': 
				self.nr_exc = self.nr_exc +  sub_family.x_count
				self.amo_exc = self.amo_exc + sub_family.amount

			elif sub_family.name == 'laser_ipl': 
				self.nr_ipl = self.nr_ipl +  sub_family.x_count
				self.amo_ipl = self.amo_ipl + sub_family.amount

			elif sub_family.name == 'laser_ndyag': 
				self.nr_ndyag = self.nr_ndyag +  sub_family.x_count
				self.amo_ndyag = self.amo_ndyag + sub_family.amount

			elif sub_family.name == 'laser_quick': 
				self.nr_quick = self.nr_quick +  sub_family.x_count
				self.amo_quick = self.amo_quick + sub_family.amount

			elif sub_family.name == 'cosmetology': 
				self.nr_cosmetology = self.nr_cosmetology +  sub_family.x_count
				self.amo_cosmetology = self.amo_cosmetology + sub_family.amount

			# Special Case, by Meta !
			elif sub_family.meta == 'medical': 
				self.nr_medical = self.nr_medical +  sub_family.x_count
				self.amo_medical = self.amo_medical + sub_family.amount



		# Calc. Avoid division by zero !		

		# Ratios	
		if self.nr_consultations != 0:
			self.ratio_pro_con = (float(self.nr_procedures) / float(self.nr_consultations)) * 100 



		# Average prices 
		
		# Families 
		if self.nr_consultations != 0:
			self.avg_consultations = self.amo_consultations / self.nr_consultations

		if self.nr_products != 0: 
			self.avg_products = self.amo_products / self.nr_products


		if self.nr_procedures != 0: 
			self.avg_procedures = self.amo_procedures / self.nr_procedures


		# Subfamilies
		if self.nr_co2 != 0: 
			self.avg_co2 = self.amo_co2 / self.nr_co2

		if self.nr_exc != 0: 
			self.avg_exc = self.amo_exc / self.nr_exc

		if self.nr_ipl != 0: 
			self.avg_ipl = self.amo_ipl / self.nr_ipl

		if self.nr_ndyag != 0: 
			self.avg_ndyag = self.amo_ndyag / self.nr_ndyag

		if self.nr_quick != 0: 
			self.avg_quick = self.amo_quick / self.nr_quick

		if self.nr_medical != 0: 
			self.avg_medical = self.amo_medical / self.nr_medical

		if self.nr_cosmetology != 0: 
			self.avg_cosmetology = self.amo_cosmetology / self.nr_cosmetology

		#print 'Done !'

	# update_counters




# ----------------------------------------------------------- Update Qc ------------------------------------------------------

	# Update Qc
	def update_qc(self):  
		#print 
		#print 'Update Qc'

		# Checksum 

		# Orders 
		orders,count = mgt_funcs.get_orders_filter_all(self, self.date_begin, self.date_end)

		# All 
		for order in orders: 
			order.check_payment_method()
			order.check_sum()


		# Serial Number 

		# Init 
		serial_nr_last = 0 
		self.nr_delta = 0 

		# Orders 
		x_type = 'ticket_receipt'
		orders,count = mgt_funcs.get_orders_filter_type(self, self.date_begin, self.date_end, x_type)
		#print count
		#print orders
		
		# All 
		for order in orders: 
		
			# Serial Nr
			serial_nr = int(order.x_serial_nr.split('-')[1])
			if serial_nr_last != 0:
				delta = serial_nr - serial_nr_last
			else:
				delta = 1
			if delta == 2: 
				self.nr_delta = self.nr_delta + 1
			order.x_delta = delta
			serial_nr_last = serial_nr

			# Prints 
			#print order 
			#print order.x_serial_nr
			#print serial_nr
			#print serial_nr_last			
			#print delta 
			#print 

		#print 'Done !'
		
	# update_qc




