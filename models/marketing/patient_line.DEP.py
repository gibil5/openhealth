# 11 Dec 2019





# ----------------------------------------------------------- Update Fields ------------------------------------------------------

	# Update Fields
	@api.multi
	def update_fields_mkt(self):  
		#print
		#print 'Update Fields - Mkt'


		self.emr = self.patient.x_id_code

		self.phone_2 = self.patient.phone 

		self.phone_1 = self.patient.mobile

		self.email = self.patient.email




		self.treatment = self.env['openhealth.treatment'].search([
																	('patient','=', self.patient.name),
														],
														#order='create_date desc',
														order='start_date desc',
														limit=1,)





		self.consultation = self.env['openhealth.consultation'].search([
																		#('name','=', self.patient.name),
																		('treatment','=', self.treatment.id),
														],
														#order='create_date desc',
														order='evaluation_start_date desc',
														limit=1,)




		self.chief_complaint = self.treatment.chief_complaint

		self.diagnosis = self.consultation.x_diagnosis



		#self.budget_amount = 

		#self.budget_date = 







# ----------------------------------------------------------- Update Fields ------------------------------------------------------

	# Update Fields
	@api.multi
	def update_fields(self):  
		#print
		#print 'Update Fields - Patient'


		# Age 
		if self.age.split()[0] != 'No': 
			self.age_years = self.age.split()[0]
			ret = 1
		else:
			ret = -1



		# Places
		if self.city != False: 
			self.city = self.city.title()

		if self.district != False: 
			self.district = self.district.title()


		

		# Measures

		# Sex 
		if self.sex == 'Male': 
			self.mea_m = 1
		elif self.sex == 'Female':
			self.mea_f = 1
		else:
			self.mea_u = 1

		# Vip 
		if self.vip: 
			self.mea_vip = 1
		else: 
			self.mea_vip_no	= 1


		# Education
		if self.education == 'first': 
			self.mea_first = 1

		elif self.education == 'second': 
			self.mea_second = 1

		elif self.education == 'technical': 
			self.mea_technical = 1

		elif self.education == 'university': 
			self.mea_university = 1

		elif self.education == 'masterphd': 
			self.mea_masterphd = 1 

		else: 
			self.mea_edu_u = 1			


		# First Contact 
		if self.first_contact == 'recommendation': 
			self.mea_recommendation = 1

		elif self.first_contact == 'tv': 
			self.mea_tv = 1

		elif self.first_contact == 'radio': 
			self.mea_radio = 1

		elif self.first_contact == 'internet': 
			self.mea_internet = 1

		elif self.first_contact == 'website': 
			self.mea_website = 1

		elif self.first_contact == 'mail_campaign': 
			self.mea_mail_campaign = 1

		elif self.first_contact == 'none': 
			self.mea_how_none = 1

		else: 
			self.mea_how_u = 1

	
		return ret 

	# update_fields






# ----------------------------------------------------------- Update Fields Vip ------------------------------------------------------

	# Update fields Vip
	@api.multi
	def update_fields_vip(self):  
		#print 
		#print 'Update fields - Vip'
		

		# Nr Lines Vip 
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_id_vip','=', self.id),
																			]) 
		self.nr_lines_vip = count

	# update_fields_vip






# ----------------------------------------------------------- Update Fields Proc ------------------------------------------------------

	# Update fields Proc
	@api.multi
	def update_nrs(self):  
		#print 
		#print 'Update fields - Nrs'
		#print 



		# Sales 
		for line in self.sale_line: 
			# Doctor 
			if self.doctor.name == False: 
				self.doctor = line.doctor.id 





		# Budgets
		self.budget_amount = ''
		self.budget_prod = ''
		for line in self.budget_line: 


			# Doctor 
			if self.doctor.name == False: 
				self.doctor = line.doctor.id 



		
			# Budget Amount 
			self.budget_amount = self.budget_amount + str(line.price_total) + ', '

			# Budget Flag 
			if line.price_total >= 1500: 
				self.budget_flag = True



			# Budget Prod
			if line.product_id.x_treatment != False: 
				if line.product_id.x_treatment in prodvars._h_subfamily: 
					self.budget_prod = self.budget_prod + prodvars._h_subfamily[line.product_id.x_treatment] + ', '
				else: 
					self.budget_prod = self.budget_prod + line.product_id.x_treatment + ', '




		# Amount and Prod 
		self.budget_amount = self.budget_amount[:-2]
		self.budget_prod = self.budget_prod[:-2]




		# Nr Budgets
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_budget_id','=', self.id),
																			]) 
		self.nr_budget = count




		# Nr Sale
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_sale_id','=', self.id),
																			]) 
		self.nr_sale = count




		# Nr Consu 
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_consu_id','=', self.id),
																			]) 
		self.nr_consu = count




		# Nr Product
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_product_id','=', self.id),
																			]) 
		self.nr_products = count





		# Nr Proc 
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_proc_id','=', self.id),
																			]) 
		self.nr_proc = count





		# Nr Reco 
		count = self.env['openhealth.marketing.recom.line'].search_count([
																				('patient_line_id','=', self.id),
																			]) 
		self.nr_reco = count

	# update_nrs

