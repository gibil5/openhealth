# 9 Dec 2019

# ----------------------------------------------------------- Update ------------------------------
	# Update
	@api.multi
	def update(self):  
		print('2018 - Update')
		self.update_patients()
		#self.update_sales()
		#self.update_recos()


# ----------------------------------------------------------- Update Patients ---------------------
	# Update Patients
	@api.multi
	def update_patients(self):  
		#print()
		print('Update Patients')


		# QC
		t0 = timer()
		now_0 = datetime.datetime.now()



		# Clear 
		self.patient_line.unlink()


		# Get Patients 
		mode = 'normal'
		patients,count = mkt_funcs.get_patients_filter(self, self.date_begin, self.date_end, mode)

		self.total_count = count


		# Loop 
		for patient in patients: 

			# Create 
			pat_line = self.patient_line.create({
														'patient': patient.id, 
														'date_create': patient.create_date,
														'date_record': patient.x_date_record,
														'sex': patient.sex, 
														'dob': patient.dob, 
														'age': patient.age, 
														'first_contact': patient.x_first_contact, 
														'education': patient.x_education_level, 
														'vip': patient.x_vip, 
														'country': patient.country_id.name, 
														'city': patient.city, 
														'district': patient.street2, 
														'function': patient.function, 

														'marketing_id': self.id, 
													})
			ret = pat_line.update_fields()



		# Set Stats 
		self.update_stats()

		# Update Vip Sales 
		self.update_vip_sales()



		# Build Histo
		lib_marketing.build_histogram(self)


		# Build Media
		lib_marketing.build_media(self)


		# Build Places
		lib_marketing.build_districts(self)
		lib_marketing.build_cities(self)



		t1 = timer()
		now_1 = datetime.datetime.now()
		self.delta_patients = t1 - t0

	# update_patients




# ----------------------------------------------------------- Update Sales ------------------------
	# Update Sales
	@api.multi
	def update_sales(self):  
		print()
		print('2018 - Update Sales')

		# QC
		t0 = timer()

		# Clean Macros 
		self.patient_budget_count = 0 
		self.patient_sale_count = 0 
		self.patient_consu_count = 0 
		self.patient_proc_count = 0 



		# Patient Lines 
		for pat_line in self.patient_line: 

			# Update Line
			pat_line.update_fields_mkt()




			# Budgets
			budgets = self.env['sale.order'].search([
															('state', '=', 'draft'),
															('patient', '=', pat_line.patient.name),
													],
														order='date_order asc',
														#limit=1,
												)
			# Clean 
			pat_line.budget_line.unlink()

			# Create
			for budget in budgets:

				doctor = budget.x_doctor

				for line in budget.order_line: 
					
					if True: 

						# Budgets 
						budget_line = pat_line.budget_line.create({
																	'name': line.name,
																	'doctor': doctor.id,
																	'product_id': line.product_id.id, 
																	'x_date_created': budget.date_order, 
																	'product_uom_qty': line.product_uom_qty, 
																	'price_unit': line.price_unit,
																	'patient_line_budget_id': pat_line.id, 
																	'marketing_id': self.id,
							})

			# Count
			self.patient_budget_count = self.patient_budget_count + len(pat_line.budget_line)

			# Update Nrs
			pat_line.update_nrs()





			# Orders 
			orders = self.env['sale.order'].search([
															('state', '=', 'sale'),
															('patient', '=', pat_line.patient.name),
													],
														order='date_order asc',
														#limit=1,
												)

			# Clean 
			pat_line.sale_line.unlink()
			pat_line.consu_line.unlink()
			pat_line.procedure_line.unlink()

			# Create
			for order in orders: 

				doctor = order.x_doctor

				for line in order.order_line: 
					
					prod = line.product_id

					# Sale
					sale_line = pat_line.sale_line.create({
															'name': line.name,
															'doctor': doctor.id,
															'product_id': line.product_id.id,
															'x_date_created': order.date_order,
															'product_uom_qty': line.product_uom_qty,
															'price_unit': line.price_unit,
															'patient_line_sale_id': pat_line.id, 
															'marketing_id': self.id, 
						})



					# Consultation
					if prod.x_family in ['consultation']:
						consu_line = pat_line.consu_line.create({
																	'name': line.name, 
																	'product_id': line.product_id.id, 
																	'x_date_created': order.date_order, 
																	'product_uom_qty': line.product_uom_qty, 
																	'price_unit': line.price_unit, 
																	'patient_line_consu_id': pat_line.id, 
																	'marketing_id': self.id, 
																})


					# Procedure
					if 	(prod.type not in ['product'])   and   (prod.x_family not in ['consultation']):
						procedure_line = pat_line.procedure_line.create({
																			'name': line.name, 
																			'product_id': line.product_id.id, 
																			'x_date_created': order.date_order, 
																			'product_uom_qty': line.product_uom_qty, 
																			'price_unit': line.price_unit, 
																			'patient_line_proc_id': pat_line.id, 
																			'marketing_id': self.id, 
																		})


			# Update Counts
			self.patient_sale_count = self.patient_sale_count + len(pat_line.sale_line)
			self.patient_consu_count = self.patient_consu_count + len(pat_line.consu_line)
			self.patient_proc_count = self.patient_proc_count + len(pat_line.procedure_line)

			# Update Nrs
			pat_line.update_nrs()


		# QC
		t1 = timer()
		self.delta_sales = t1 - t0

	# update_sales





# ----------------------------------------------------------- Update Recommendations --------------
	# Update Recos
	@api.multi
	def update_recos(self):  
		print()
		print('2018 - Update Recos')


		# QC
		t0 = timer()


		# Clean 
		self.patient_reco_count = 0 

		# Patient Lines 
		for pat_line in self.patient_line: 

			# Clean 
			pat_line.reco_line.unlink()

			# Recommendations
			patient = pat_line.patient


			# Loop 
			for treatment in patient.treatment_ids: 

				# Co2 
				for reco in treatment.service_co2_ids: 
					reco_line = pat_line.reco_line.create({
																'product_id': reco.service.id, 
																'sub_family': reco.service.x_treatment, 
																'x_date_created': reco.create_date, 
																'doctor': reco.physician.id, 
																'price': reco.price, 
																'price_vip': reco.price_vip, 
																'price_manual': reco.price_manual, 
																'price_applied': reco.price_applied,
																'patient_line_id': pat_line.id, 
																'marketing_id': self.id, 
															})

				# Exc 
				for reco in treatment.service_excilite_ids: 
					reco_line = pat_line.reco_line.create({
																'product_id': reco.service.id, 
																'sub_family': reco.service.x_treatment, 
																'x_date_created': reco.create_date, 
																'doctor': reco.physician.id, 
																'price': reco.price, 
																'price_vip': reco.price_vip, 
																'price_manual': reco.price_manual, 
																'price_applied': reco.price_applied, 
																'patient_line_id': pat_line.id, 
																'marketing_id': self.id, 
															})


				# Ipl 
				for reco in treatment.service_ipl_ids:
					reco_line = pat_line.reco_line.create({
																'product_id': reco.service.id, 
																'sub_family': reco.service.x_treatment, 
																'x_date_created': reco.create_date, 
																'doctor': reco.physician.id, 
																'price': reco.price, 
																'price_vip': reco.price_vip, 
																'price_manual': reco.price_manual, 
																'price_applied': reco.price_applied, 
																'patient_line_id': pat_line.id, 
																'marketing_id': self.id, 
															})


				# Ndyag 
				for reco in treatment.service_ndyag_ids:
					reco_line = pat_line.reco_line.create({
																'product_id': reco.service.id, 
																'sub_family': reco.service.x_treatment, 
																'x_date_created': reco.create_date, 
																'doctor': reco.physician.id, 
																'price': reco.price, 
																'price_vip': reco.price_vip, 
																'price_manual': reco.price_manual, 
																'price_applied': reco.price_applied, 
																'patient_line_id': pat_line.id, 
																'marketing_id': self.id, 
															})



				# Medical 
				for reco in treatment.service_medical_ids:
					reco_line = pat_line.reco_line.create({
																'product_id': reco.service.id, 
																'sub_family': reco.service.x_treatment, 
																'x_date_created': reco.create_date, 
																'doctor': reco.physician.id, 
																'price': reco.price, 
																'price_vip': reco.price_vip, 
																'price_manual': reco.price_manual, 
																'price_applied': reco.price_applied, 
																'patient_line_id': pat_line.id, 
																'marketing_id': self.id, 
															})


				# Quick 
				for reco in treatment.service_quick_ids:
					reco_line = pat_line.reco_line.create({
																'product_id': reco.service.id, 
																'sub_family': reco.service.x_treatment, 
																'x_date_created': reco.create_date, 
																'doctor': reco.physician.id, 
																'price': reco.price, 
																'price_vip': reco.price_vip, 
																'price_manual': reco.price_manual, 
																'price_applied': reco.price_applied, 
																'patient_line_id': pat_line.id, 
																'marketing_id': self.id, 
															})


				# Vip 
				for reco in treatment.service_vip_ids:
					reco_line = pat_line.reco_line.create({
																'product_id': reco.service.id, 
																'sub_family': reco.service.x_treatment, 
																'x_date_created': reco.create_date, 
																'doctor': reco.physician.id, 
																'price': reco.price, 
																'price_vip': reco.price_vip, 
																'price_manual': reco.price_manual, 
																'price_applied': reco.price_applied, 
																'patient_line_id': pat_line.id, 
																'marketing_id': self.id, 
															})

			# Update 
			pat_line.update_nrs()

			# Counts 
			self.patient_reco_count = self.patient_reco_count + len(pat_line.reco_line)


		# QC
		t1 = timer()
		self.delta_recos = t1 - t0

	# update_recos




# ----------------------------------------------------------- Update Stats ------------------------
	# Set Stats
	@api.multi
	def update_stats(self):  
		print()
		print('2018 - Update Stats')


		# Init vars 

		# Sex 
		count_m = 0
		count_f = 0
		count_u = 0


		# Age 
		count_a = 0
		age_min = 100 
		age_max = 0 
		count_age_u = 0


		# First Contact 
		how_u = 0 
		how_none = 0 
		how_reco = 0 
		how_tv = 0
		how_radio = 0 
		how_inter = 0 
		how_web = 0 
		how_mail = 0 


		# Education 
		edu_u = 0
		edu_fir = 0
		edu_sec = 0
		edu_tec = 0
		edu_uni = 0
		edu_mas = 0


		# Vip 
		vip_true = 0 
		vip_false = 0 


		# Collections
		country_arr = []



		# Loop 
		for line in self.patient_line: 

			# Sex
			if line.sex == 'Male': 
				count_m = count_m + 1
			elif line.sex == 'Female': 
				count_f = count_f + 1
			else: 
				count_u = count_u + 1


			# Age Max and Min 
			if line.age_years not in[ -1, 0]: 			# Not an Error 
				count_a = count_a + line.age_years 
				if line.age_years > age_max: 
					age_max = line.age_years
				if line.age_years < age_min: 
					age_min = line.age_years
			else: 										# Error 
				count_age_u = count_age_u + 1


			# First Contact 
			if line.first_contact == 'none': 
				how_none = how_none + 1

			elif line.first_contact == 'recommendation': 
				how_reco = how_reco + 1

			elif line.first_contact == 'tv': 
				how_tv = how_tv + 1

			elif line.first_contact == 'radio': 
				how_radio = how_radio + 1

			elif line.first_contact == 'internet': 
				how_inter = how_inter + 1

			elif line.first_contact == 'website':
				how_web = how_web + 1

			elif line.first_contact == 'mail_campaign':
				how_mail = how_mail + 1

			else: 
				how_u = how_u + 1


			# Education 
			if line.education == 'first': 
				edu_fir = edu_fir + 1

			elif line.education == 'second': 
				edu_sec = edu_sec + 1

			elif line.education == 'technical': 
				edu_tec = edu_tec + 1

			elif line.education == 'university': 
				edu_uni = edu_uni + 1

			elif line.education == 'masterphd': 
				edu_mas = edu_mas + 1

			else: 
				edu_u = edu_u + 1


			# Vip 
			if line.vip: 
				vip_true = vip_true + 1

			else: 
				vip_false = vip_false + 1



			# Address - Using collections

			# Countries 
			country_arr.append(line.country)




		# Update Object 


		# Sex 
		# Absolutes 
		self.sex_male = count_m
		self.sex_female = count_f
		self.sex_undefined = count_u

		# Per
		#if self.total_count != 0: 
			#self.sex_male_per = ( float(self.sex_male) / float(self.total_count) ) * 100
			#self.sex_female_per = ( float(self.sex_female) / float(self.total_count) ) * 100
			#self.sex_undefined_per = ( float(self.sex_undefined) / float(self.total_count) ) * 100
		self.sex_male_per = mkt_funcs.get_per(self, self.sex_male, self.total_count)
		self.sex_female_per = mkt_funcs.get_per(self, self.sex_female, self.total_count)
		self.sex_undefined_per = mkt_funcs.get_per(self, self.sex_undefined, self.total_count)




		# Ages 
		self.age_min = age_min
		self.age_max = age_max
		self.age_undefined = count_age_u
		
		if self.total_count != 0: 
			self.age_mean = count_a / self.total_count
			self.age_undefined_per = ( float(self.age_undefined) / float(self.total_count) ) * 100


		# First Contact
		self.how_none = how_none
		self.how_reco = how_reco
		self.how_tv = how_tv
		self.how_radio = how_radio		
		self.how_inter = how_inter
		self.how_web = how_web
		self.how_mail = how_mail
		self.how_u = how_u

		# Per
		self.how_none_per = mkt_funcs.get_per(self, how_none, self.total_count)
		self.how_reco_per = mkt_funcs.get_per(self, how_reco, self.total_count)
		self.how_tv_per = mkt_funcs.get_per(self, how_tv, self.total_count)
		self.how_radio_per = mkt_funcs.get_per(self, how_radio, self.total_count)
		self.how_inter_per = mkt_funcs.get_per(self, how_inter, self.total_count)
		self.how_web_per = mkt_funcs.get_per(self, how_web, self.total_count)
		self.how_mail_per = mkt_funcs.get_per(self, how_mail, self.total_count)
		self.how_u_per = mkt_funcs.get_per(self, how_u, self.total_count)


		# Education 
		self.edu_fir = edu_fir
		self.edu_sec = edu_sec
		self.edu_tec = edu_tec
		self.edu_uni = edu_uni
		self.edu_mas = edu_mas
		self.edu_u = edu_u

		# Per 
		self.edu_fir_per = mkt_funcs.get_per(self, edu_fir, self.total_count)
		self.edu_sec_per = mkt_funcs.get_per(self, edu_sec, self.total_count)
		self.edu_tec_per = mkt_funcs.get_per(self, edu_tec, self.total_count)
		self.edu_uni_per = mkt_funcs.get_per(self, edu_uni, self.total_count)
		self.edu_mas_per = mkt_funcs.get_per(self, edu_mas, self.total_count)
		self.edu_u_per = mkt_funcs.get_per(self, edu_u, self.total_count)


		# Vip 
		self.vip_true = vip_true
		self.vip_false = vip_false

		 # Per 
		self.vip_true_per = mkt_funcs.get_per(self, vip_true, self.total_count)
		self.vip_false_per = mkt_funcs.get_per(self, vip_false, self.total_count)




		# Using collections		
		# Country
		counter_country = collections.Counter(country_arr)




		# Clear 
		self.country_line.unlink()
		self.city_line.unlink()
		self.district_line.unlink()



		# Country
		#print 'Create Country Line '
		for key in counter_country: 
			count = counter_country[key]
			country = self.country_line.create({
													'name': key, 
													'count': count,
													'marketing_id': self.id, 
												})
			#print country
		#print self.country_line
		#print 

	# update_stats



# ----------------------------------------------------------- Update Vip Sales --------------------
	@api.multi
	def update_vip_sales(self):  
		print()
		print('2018 - Vip Sales')

		# Patient Lines 
		for pl in self.patient_line: 

			if pl.vip: 
				
				# Clean 
				pl.order_line.unlink()
				pl.order_line_vip.unlink()

				# Orders 
				orders = self.env['sale.order'].search([
															('state', '=', 'sale'),
															('patient', '=', pl.patient.name),
													],
														order='date_order asc',
														#limit=1,
												)


				# Find Vip Date - First Method 
				for order in orders: 
					for ol in order.order_line: 
						if ol.product_id.default_code == '495': 		# Vip Card 
							pl.vip_date = order.date_order


				# Find Vip Date - Second Method - Legacy 
				if pl.vip_date == False:
					card = self.env['openhealth.card'].search([
																	('patient_name', '=', pl.patient.name),
														],
															#order='x_serial_nr asc',
															limit=1,
													)
					pl.vip_date = card.create_date



				# Order Lines - Create Order Line 
				for order in orders: 

					# Create Vip 
					for ol in order.order_line:
						pl_ol = pl.order_line.create({
														'name': ol.name, 
														'product_id': ol.product_id.id, 
														'x_date_created': order.date_order, 
														'product_uom_qty': ol.product_uom_qty, 
														'price_unit': ol.price_unit, 
														'patient_line_id': pl.id, 
							})
						#print pl_ol



						# Create - Vip sale 
						if pl.vip_date != False: 
							if order.date_order >= pl.vip_date and ol.product_id.type in ['service']: 

								pl_ol_vip = pl.order_line_vip.create({
																		'name': ol.name, 
																		'product_id': ol.product_id.id, 
																		'x_date_created': order.date_order, 
																		'product_uom_qty': ol.product_uom_qty, 
																		'price_unit': ol.price_unit, 
																		'patient_line_id_vip': pl.id, 
									})
								#print pl_ol

				pl.update_fields_vip()

	# update_vip_sales






