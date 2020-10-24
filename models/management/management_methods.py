# -*- coding: utf-8 -*-
"""
	Management - Methods

	Created: 			28 may 2018
	Last updated: 		23 oct 2020
"""
from __future__ import print_function
from timeit import default_timer as timer
import datetime
import collections
from openerp import models, fields, api

# Lib
#from lib import stats
#from lib import mgt_line_funcs
from lib import mgt_funcs
from lib import prod_funcs

class Management(models.Model):
	"""
	Contains only methods.
	"""
	_inherit = 'openhealth.management'


# -------------------------------------------------------------------------------------------------
# First Level - Update Buttons
# -------------------------------------------------------------------------------------------------

# ----------------------------------------------------------- Update Fast ------
	@api.multi
	def update_fast(self):
		"""
		Update Macros
		Used also by Django
		"""
		print()
		print('Update Fast')

		# Go
		t0 = timer()
		self.update_sales_fast()
		self.update_year()
		t1 = timer()
		self.delta_fast = t1 - t0
		#print self.delta_fast
		#print
		print()

		return 1 	# For Django
	# update_fast


# --------------------------------------------------------- Update Patients ----
	# Update Patients
	@api.multi
	def update_patients(self):
		"""
		Update Patients. 
		"""
		print()
		print('Update Patients')

		# Go
		orders, count = mgt_funcs.get_orders_filter_fast(self, self.date_begin, self.date_end)
		#print(orders)
		#print(count)

		# Create
		for order in orders:
			patient = order.patient
			patient_id = order.patient.id

			#if patient.name not in ['REVILLA RONDON JOSE JAVIER']:			
			if self.mode in ['test'] or self.mode in ['normal'] and patient.name not in ['REVILLA RONDON JOSE JAVIER']:
				#print(patient)
				#print(patient_id)

				# Count
				pat_count = self.env['openhealth.management.patient.line'].search_count([
																						('patient', '=', patient_id),
																						('management_id', '=', self.id),
																				],
																					#order='x_serial_nr asc',
																					#limit=1,
																				)
				#print(pat_count)

				if pat_count in [0]:
					patient_line = self.patient_line.create({
																'patient': patient_id,
																'management_id': self.id,
						})

		# Update
		for patient_line in self.patient_line:
			patient_line.update()

		print()

		return 1	# For Django
	# update_patients


# ---------------------------------------------------------- Update Doctors ----
	@api.multi
	def update_doctors(self):
		"""
		Update Doctors
		"""
		print()
		print('X - Update Doctors')

		# Go
		t0 = timer()

		# Sales by Doctor
		self.pl_update_sales_by_doctor()

		# Stats
		#stax.update_stats(self)
		self.update_stats()

		t1 = timer()
		self.delta_doctor = t1 - t0

		print()

		return 1	# For Django
	# update_doctors


# ----------------------------------------------------------- Update Prod ------
	# Update Productivity
	@api.multi
	def update_productivity(self):
		"""
		Update productivity
		Used also by Django
		"""
		print()
		print('X - Update Productivity')
		
		# Go
		prod_funcs.create_days(self)
		
		# Update cumulative and average
		prod_funcs.pl_update_day_cumulative(self)
		prod_funcs.pl_update_day_avg(self)

		print()

		return 1	# For Django
	# update_productivity

# ---------------------------------------------------------- Update Daily ------
	# Update Daily
	@api.multi
	def update_daily(self):
		"""
		Update daily sales for each doctor

		Used by Django. Last Test

		self.doctor_line
			'openhealth.management.doctor.line',
		"""
		print()
		print('Update Daily Sales')

		# For each doctor line
		for doctor in self.doctor_line:
			print(doctor.name)
			
			#doctor.update_daily() 	# Here !
			doctor.update_daily(self.id) 	# Here !
		print()

		# For Django
		self.date_test = datetime.datetime.now() 
		return 1	
	# update_daily


# -------------------------------------------------------------------------------------------------
# Second Level - Update Buttons
# -------------------------------------------------------------------------------------------------

	def update_sales_fast(self):
		"""
		Update Sales
			Steps
				Clean
				Get orders
				Loop 
					Line analysis
		"""
		print()
		print('Update Sales Fast')

		# Clean
		self.reset_macro()

		# Get Orders
		if self.type_arr in ['all']:
			orders, count = mgt_funcs.get_orders_filter_fast(self, self.date_begin, self.date_end)
		else:
			orders, count = mgt_funcs.get_orders_filter(self, self.date_begin, self.date_end, self.state_arr, self.type_arr)

# Loop
		tickets = 0
		for order in orders:
			tickets = tickets + 1

			# Filter Block
			if not order.x_block_flow:

				# If sale
				if order.state in ['sale']:  	
					# Line Analysis
					for line in order.order_line:
						self.line_analysis(line)

				# If credit Note - Do Amount Flow
				elif order.state in ['credit_note']:
					self.nr_credit_notes = self.nr_credit_notes + 1
					self.amo_credit_notes = self.amo_credit_notes + order.x_amount_flow


# Analysis - Setters
# Must be Abstract - To Hide Implementation

		# Set Averages
		mgt_funcs.set_averages(self)

		# Set Ratios
		mgt_funcs.set_ratios(self)

		# Set Totals
		mgt_funcs.set_totals(self, tickets)

		# Set Percentages
		mgt_funcs.set_percentages(self)

	# update_sales_fast


# ----------------------------------------------------------- Update Year ------
	@api.multi
	def update_year(self):
		"""
		Update Year
		"""
		print()
		print('Update Year')

		# Mgts
		mgts = self.env['openhealth.management'].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		# Count
		count = self.env['openhealth.management'].search_count([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		#print(mgts)
		#print(count)

		total = 0		
		for mgt in mgts:
			total = total + mgt.total_amount

		self.total_amount_year = total

		if self.total_amount_year != 0:
			self.per_amo_total = self.total_amount / self.total_amount_year
	# update_year


# ------------------------------------------------------- Validate Internal ----
	# Validate
	@api.multi
	def validate(self):
		"""
		Validates the content. 
		For internal Data Coherency - internal and external. 
		"""
		print()
		print('X - Validate the content !')

		# Internal
		out = self.pl_validate_internal()

		# External
		#self.pl_validate_external()  	# Dep !

		# Django
		return out
	# validate


# ------------------------------------------------------- Validate Internal ----
	# Validate
	@api.multi
	def pl_validate_internal(self):
		"""
		Validates Data Coherency - internal. 
		"""
		print()
		print('Validate Internal')

		# Families
		self.per_amo_families = self.per_amo_products + self.per_amo_consultations + self.per_amo_procedures + self.per_amo_other + self.per_amo_credit_notes
		print(self.per_amo_families)

		# Sub Families
		self.per_amo_subfamilies = self.per_amo_sub_con_med + self.per_amo_sub_con_gyn + self.per_amo_sub_con_cha + \
									self.per_amo_co2 + self.per_amo_exc + self.per_amo_quick + self.per_amo_ipl + self.per_amo_ndyag + \
									self.per_amo_medical + self.per_amo_cosmetology + \
									self.per_amo_echo + self.per_amo_gyn + self.per_amo_prom + \
									self.per_amo_topical + self.per_amo_card + self.per_amo_kit + \
									self.per_amo_credit_notes
		print(self.per_amo_subfamilies)

		return self.per_amo_families, self.per_amo_subfamilies


# ----------------------------------------------------------- Validate external -------------------------
	# Validate
	@api.multi
	def pl_validate_external(self):
		"""
		Validates Data Coherency - External. 
		Builds a Report Sale Product for the month. 
		Compares it to Products stats.
		"""
		print()
		print('X - Validate External')

		if self.report_sale_product.name in [False]:

			date_begin = self.date_begin


			self.report_sale_product = self.env['openhealth.report.sale.product'].create({
																							'name': date_begin,
																							'management_id': self.id,
																						})

		rsp = self.report_sale_product
		print(rsp)
		print(rsp.name)


		rsp.update()

		self.rsp_count = rsp.total_qty
		self.rsp_total = rsp.total
		self.rsp_count_delta = self.nr_products - self.rsp_count
		self.rsp_total_delta = self.amo_products - self.rsp_total





# ----------------------------------------------------------- Update -------------------------------

# ----------------------------------------------- Update Sales - By Doctor -----

	def pl_update_sales_by_doctor(self):
		"""
		Pl - Update Sales
		"""
		print()
		print('X - Update Sales - By Doctor')

		# Clean - Important 
		self.doctor_line.unlink()

		# Init vars
		total_amount = 0
		total_count = 0
		total_tickets = 0

		# Doctors Inactive
		doctors_inactive = self.env['oeh.medical.physician'].search([
																	#('x_type', 'in', ['emr']),
																	('active', '=', False),
															],
															#order='date_begin,name asc',
															#limit=1,
													)
		#print(doctors_inactive)

		# Doctors Active
		doctors_active = self.env['oeh.medical.physician'].search([
																	('active', '=', True),
															],
															#order='date_begin,name asc',
															#limit=1,
													)
		#print(doctors_active)

		doctors = doctors_inactive + doctors_active
		#print(doctors)

		# Create Sales - By Doctor - All 
		for doctor in doctors:
			#print(doctor.name)
			#print(doctor.active)

			# Clear
			#doctor.order_line.unlink()

			# Orders
			# Must include Credit Notes
			orders, count = mgt_funcs.get_orders_filter_by_doctor(self, self.date_begin, self.date_end, doctor.name)
			#print(orders)
			#print(count)


			if count in [0]:
				#print()
				jx = 5
			else:
				#print('Gotcha')
				self.create_doctor_data(doctor.name, orders)

			#print()
	# update_sales_by_doctor

# ----------------------------------------------------------- Create Doctor Data ------------
	def create_doctor_data(self, doctor_name, orders):
		print()
		print('X - Create Doctor Data')


		# Init Loop
		amount = 0
		count = 0
		tickets = 0
		doctor = self.doctor_line.create({
											'name': doctor_name,
											'management_id': self.id,
										})

		# Loop
		for order in orders:

			# Tickets
			tickets = tickets + 1

			# Filter Block
			if not order.x_block_flow:


				# Parse Data


				# Amount with State
				if order.state in ['credit_note']:
					amount = amount + order.x_amount_flow

				elif order.state in ['sale']:
					amount = amount + order.amount_total


				# Id Doc
				if order.x_type in ['ticket_invoice', 'invoice']:
					receptor = order.patient.x_firm.upper()
					id_doc = order.patient.x_ruc
					id_doc_type = 'ruc'
					id_doc_type_code = '6'
				else:
					receptor = order.patient.name
					id_doc = order.patient.x_id_doc
					id_doc_type = order.patient.x_id_doc_type
					id_doc_type_code = order.patient.x_id_doc_type_code

					# Pre-Electronic
					if id_doc_type is False or id_doc is False:
						id_doc = order.patient.x_dni
						id_doc_type = 'dni'
						id_doc_type_code = '1'






				# State equal to Sale
				if order.state in ['sale']:  	# Sale - Do Line Analysis

					#print('SALE')

					# Order Lines
					for line in order.order_line:

						count = count + 1

						# Price
						price_unit = line.price_unit						



						# Families
						family = line.product_id.get_family()
						sub_family = line.product_id.get_subsubfamily()



						# Create
						order_line = doctor.order_line.create({
																'date_order_date': order.date_order,
																'x_date_created': order.date_order,

																'name': order.name,
																'receptor': 	receptor,
																'patient': 		order.patient.id,
																'doctor': order.x_doctor.id,
																'serial_nr': order.x_serial_nr,

																# Type of Sale
																'type_code': 	order.x_type_code,
																'x_type': 		order.x_type,

																# Id Doc
																'id_doc': 				id_doc,
																'id_doc_type': 			id_doc_type,
																'id_doc_type_code': 	id_doc_type_code,

																# State
																'state': order.state,

																# Handles
																'doctor_id': doctor.id,
																'management_id': self.id,

																# Line
																'product_id': 			line.product_id.id,
																'product_uom_qty': 		line.product_uom_qty,

																# Price
																'price_unit': 			price_unit,

																# Families
																'family': family, 
																'sub_family': sub_family, 
															})

						#print(line)
						#print(line.product_id)
						#print(line.product_id.name)


						# Deprecated !
						# Update Families
						#if line.product_id.pl_price_list in ['2019']:
						#	order_line.pl_update_fields()

						#elif line.product_id.pl_price_list in ['2018']:
						#	order_line.update_fields()



					# Line Analysis Sale - End

				# Conditional State Sale - End




				# State equal to Credit Note
				elif order.state in ['credit_note']:

					#print('CREDIT NOTE')


					# Order Lines
					for line in order.order_line:

						# Families
						family = line.product_id.get_family()
						sub_family = line.product_id.get_subsubfamily()


						# Price
						price_unit = order.x_amount_flow

						# Create
						order_line = doctor.order_line.create({
																'date_order_date': order.date_order,
																'x_date_created': order.date_order,

																'name': order.name,
																'receptor': 	receptor,
																'patient': 		order.patient.id,
																'doctor': order.x_doctor.id,
																'serial_nr': order.x_serial_nr,

																# Type of Sale
																'type_code': 	order.x_type_code,
																'x_type': 		order.x_type,

																# Id Doc
																'id_doc': 				id_doc,
																'id_doc_type': 			id_doc_type,
																'id_doc_type_code': 	id_doc_type_code,

																# State
																'state': order.state,

																# Handles
																'doctor_id': doctor.id,
																'management_id': self.id,

																# Line
																'product_uom_qty': 		1,

																# Price
																'price_unit': 			price_unit,


																# Families
																'family': family, 
																'sub_family': sub_family, 
															})


						#print(line)
						#print(line.product_id)
						#print(line.product_id.name)



						# Deprecated !
						#if line.product_id.pl_price_list in ['2019']:
						#	order_line.pl_update_fields()

						#elif line.product_id.pl_price_list in ['2018']:
						#	order_line.update_fields()



					# Line Analysis Credit Note - End

				# Conditional State - End


			# Filter Block - End
		# Loop - End



		# Stats
		doctor.amount = amount
		doctor.x_count = count

		# Percentage
		if self.total_amount != 0: 
			doctor.per_amo = (doctor.amount / self.total_amount)

	# create_doctor_data





# ----------------------------------------------------------- Update Max -----------------------
	@api.multi
	def update_max(self):
		"""
		Update Year All
		"""
		print()
		print('X - Update Max')

		# Clear
		mgts = self.env['openhealth.management'].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
														],
														order='date_begin asc',
														#limit=1,
													)
		for mgt in mgts:
			#print(mgt.name)
			mgt.pl_max = False
			mgt.pl_min = False


		# Max
		mgt = self.env['openhealth.management'].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
															('month', 'not in', [False]),
														],
														order='total_amount asc',
														limit=1,
													)
		mgt.pl_min = True


		# Max
		mgt = self.env['openhealth.management'].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
															('month', 'not in', [False]),
														],
														order='total_amount desc',
														limit=1,
													)
		mgt.pl_max = True



# ----------------------------------------------------------- Update Year all -----------------------
	@api.multi
	def update_year_all(self):
		"""
		Update Year All
		"""
		print()
		print('X - Update Year All')

		# Mgts
		mgts = self.env['openhealth.management'].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
														],
														order='date_begin asc',
														#limit=1,
													)
		# Count
		count = self.env['openhealth.management'].search_count([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
														],
															#order='x_serial_nr asc',
															#limit=1,
														)
		print(mgts)
		print(count)

		for mgt in mgts:
			print(mgt.name)
			mgt.update_year()


# ----------------------------------------------------------- Reset -------------------------------
	# Reset
	@api.multi
	def reset(self):
		"""
		Reset Button.
		"""
		#print()
		print('X - Reset')

		# Go
		self.reset_macro()
		self.reset_relationals()
	# reset

# ----------------------------------------------------------- Reset -------------------------
	# Reset Macros
	def reset_macro(self):
		"""
		Reset Macro
			All self fields
		"""
		print()
		print('X - Reset Macros')

		# Deltas
		self.delta_fast = 0
		self.delta_doctor = 0

		# Relational
		if self.patient_line not in [False]:
			self.patient_line.unlink()

		#self.report_sale_product = False
		self.report_sale_product.unlink()
		self.rsp_count = 0
		self.rsp_count_delta = 0
		self.rsp_total = 0
		self.rsp_total_delta = 0

		# Clear
		self.total_amount_year = 0
		self.total_amount = 0
		self.total_count = 0
		self.total_tickets = 0

		# Nr - 1st level
		self.nr_products = 0
		self.nr_services = 0
		self.nr_consultations = 0
		self.nr_procedures = 0

		# Nr - 2nd level
		self.nr_topical = 0
		self.nr_card = 0
		self.nr_kit = 0
		self.nr_co2 = 0
		self.nr_exc = 0
		self.nr_ipl = 0
		self.nr_ndyag = 0
		self.nr_quick = 0
		self.nr_medical = 0
		self.nr_cosmetology = 0
		self.nr_echo = 0
		self.nr_gyn = 0
		self.nr_prom = 0
		self.nr_credit_notes = 0
		self.nr_other = 0
		self.nr_sub_con_med = 0
		self.nr_sub_con_gyn = 0
		self.nr_sub_con_cha = 0

		# Amo - 1st Level
		self.amo_products = 0
		self.amo_services = 0
		self.amo_consultations = 0
		self.amo_procedures = 0
		self.amo_credit_notes = 0
		self.amo_other = 0

		# Amo - 2nd Level
		self.amo_topical = 0
		self.amo_card = 0
		self.amo_kit = 0
		self.amo_co2 = 0
		self.amo_exc = 0
		self.amo_ipl = 0
		self.amo_ndyag = 0
		self.amo_quick = 0
		self.amo_medical = 0
		self.amo_cosmetology = 0
		self.amo_echo = 0
		self.amo_gyn = 0
		self.amo_prom = 0
		self.amo_sub_con_med = 0
		self.amo_sub_con_gyn = 0
		self.amo_sub_con_cha = 0

		# Per Amo
		self.per_amo_total = 0
		self.per_amo_families = 0
		self.per_amo_subfamilies = 0

		self.per_amo_sub_con_med = 0
		self.per_amo_sub_con_gyn = 0
		self.per_amo_sub_con_cha = 0

		self.per_amo_echo = 0
		self.per_amo_gyn = 0
		self.per_amo_prom = 0

		self.per_amo_other = 0
		self.per_amo_credit_notes = 0
		self.per_amo_topical = 0
		self.per_amo_card = 0
		self.per_amo_kit = 0
		self.per_amo_products = 0
		self.per_amo_services = 0
		self.per_amo_consultations = 0
		self.per_amo_procedures = 0
		self.per_amo_co2 = 0
		self.per_amo_exc = 0
		self.per_amo_ipl = 0
		self.per_amo_ndyag = 0
		self.per_amo_quick = 0
		self.per_amo_medical = 0
		self.per_amo_cosmetology = 0

		# Avg
		self.avg_echo = 0
		self.avg_gyn = 0
		self.avg_prom = 0

		self.avg_other = 0
		self.avg_topical = 0
		self.avg_kit = 0
		self.avg_card = 0
		self.avg_products = 0
		self.avg_services = 0
		self.avg_consultations = 0
		self.avg_procedures = 0
		self.avg_co2 = 0
		self.avg_exc = 0
		self.avg_ipl = 0
		self.avg_ndyag = 0
		self.avg_quick = 0
		self.avg_medical = 0
		self.avg_cosmetology = 0

		# Ratios
		self.ratio_pro_con = 0
	# reset_macro

	# Reset Relationals
	def reset_relationals(self):
		"""
		Reset Micro
			All Relational
				Doctors, Families, Sub-families
		"""
		print()
		print('X - Reset Micros')

		# Productivity Days
		self.productivity_day.unlink()

		# Order Lines
		self.order_line.unlink()

		# Doctor lines
		#self.doctor_line.unlink()        # Too complex

		# Family lines
		self.family_line.unlink()
		self.sub_family_line.unlink()
	# reset_micro

# ----------------------------------------------------------- Update Stats -----
	def update_stats(self):
		"""
		Update Stats
			Doctors, 
			Families, 
			Sub-families
		Used by
			update_doctors
		"""
		print()
		print('X - Update Stats')

		# Using collections - More Abstract !

		# Clean
		self.family_line.unlink()
		self.sub_family_line.unlink()

		# Init
		family_arr = []
		sub_family_arr = []
		_h_amount = {}
		_h_sub = {}

	# All
		# Loop - Doctors
		for doctor in self.doctor_line:

			# Loop - Order Lines
			for line in doctor.order_line:

				# Family
				family_arr.append(line.family)

				if line.family in [False, '']:
					print()
					print('Error: Family')
					print(line.product_id.name)

				# Sub family
				sub_family_arr.append(line.sub_family)

				if line.sub_family in [False, '']:
					print()
					print('Error: Subfamily')
					print(line.product_id.name)

				# Amount - Family
				if line.family in _h_amount:
					_h_amount[line.family] = _h_amount[line.family] + line.price_total

				else:
					_h_amount[line.family] = line.price_total

				# Amount - Sub Family
				if line.sub_family in _h_sub:
					_h_sub[line.sub_family] = _h_sub[line.sub_family] + line.price_total

				else:
					_h_sub[line.sub_family] = line.price_total

			# Doctor Stats - openhealth.management.doctor.line
			doctor.pl_stats()


	# By Family
		# Count
		counter_family = collections.Counter(family_arr)

		# Create
		for name in counter_family:
			print(name)
			count = counter_family[name]
			amount = _h_amount[name]
			family = self.family_line.create({
													'name': name,
													'x_count': count,
													'amount': amount,
													'management_id': self.id,
												})
			family.update()

			# Percentage
			if self.total_amount != 0:
				family.per_amo = family.amount / self.total_amount


	# Subfamily
		# Count
		counter_sub_family = collections.Counter(sub_family_arr)

		# Create
		for name in counter_sub_family:
			count = counter_sub_family[name]
			amount = _h_sub[name]
			sub_family = self.sub_family_line.create({
														'name': name,
														'name_sp': name,
														'x_count': count,
														'amount': amount,
														'management_id': self.id,
												})
			# Percentage
			if self.total_amount != 0:
				sub_family.per_amo = sub_family.amount / self.total_amount
	# update_stats


# ----------------------------------------------------------- Line Analysis ----
	def line_analysis(self, line, verbose=False):
		"""
		Analyses order lines 
		Updates counters
		"""

		# Init
		prod = line.product_id
		if verbose:
			print(prod.name)
			print(prod.pl_treatment)
			print(prod.pl_family)
			print(prod.pl_subfamily)

		# Services
		if prod.type in ['service']:
			self.nr_services = self.nr_services + line.product_uom_qty
			self.amo_services = self.amo_services + line.price_subtotal

			# Consultations
			if prod.pl_subfamily in ['consultation']:
				self.nr_consultations = self.nr_consultations + line.product_uom_qty
				self.amo_consultations = self.amo_consultations + line.price_subtotal

				if prod.pl_treatment in ['CONSULTA MEDICA']:
					self.nr_sub_con_med = self.nr_sub_con_med + line.product_uom_qty
					self.amo_sub_con_med = self.amo_sub_con_med + line.price_subtotal
					
				elif prod.pl_treatment in ['CONSULTA GINECOLOGICA']:
					self.nr_sub_con_gyn = self.nr_sub_con_gyn + line.product_uom_qty
					self.amo_sub_con_gyn = self.amo_sub_con_gyn + line.price_subtotal

				elif prod.pl_treatment in ['CONSULTA MEDICA DR. CHAVARRI']:
					self.nr_sub_con_cha = self.nr_sub_con_cha + line.product_uom_qty
					self.amo_sub_con_cha = self.amo_sub_con_cha + line.price_subtotal

			# Procedures
			else:
				self.nr_procedures = self.nr_procedures + line.product_uom_qty
				self.amo_procedures = self.amo_procedures + line.price_subtotal

				# By Family
				# Echo
				if prod.pl_family in ['echography']:
					self.nr_echo = self.nr_echo + line.product_uom_qty
					self.amo_echo = self.amo_echo + line.price_subtotal

				# Gyn
				elif prod.pl_family in ['gynecology']:
					self.nr_gyn = self.nr_gyn + line.product_uom_qty
					self.amo_gyn = self.amo_gyn + line.price_subtotal

				# Prom
				elif prod.pl_family in ['promotion']:
					self.nr_prom = self.nr_prom + line.product_uom_qty
					self.amo_prom = self.amo_prom + line.price_subtotal

				# By Sub Family
				# Co2
				elif prod.pl_subfamily in ['co2']:
					self.nr_co2 = self.nr_co2 + line.product_uom_qty
					self.amo_co2 = self.amo_co2 + line.price_subtotal

				# Exc
				elif prod.pl_subfamily in ['excilite']:
					self.nr_exc = self.nr_exc + line.product_uom_qty
					self.amo_exc = self.amo_exc + line.price_subtotal

				# Quick
				elif prod.pl_subfamily in ['quick']:
					self.nr_quick = self.nr_quick + line.product_uom_qty
					self.amo_quick = self.amo_quick + line.price_subtotal


				# By Treatment
				# Ipl
				elif prod.pl_treatment in ['LASER M22 IPL']:
					self.nr_ipl = self.nr_ipl + line.product_uom_qty
					self.amo_ipl = self.amo_ipl + line.price_subtotal

				# Ndyag
				elif prod.pl_treatment in ['LASER M22 ND YAG']:
					self.nr_ndyag = self.nr_ndyag + line.product_uom_qty
					self.amo_ndyag = self.amo_ndyag + line.price_subtotal

				else:
					# Medical
					if prod.pl_family in ['medical']:
						self.nr_medical = self.nr_medical + line.product_uom_qty
						self.amo_medical = self.amo_medical + line.price_subtotal

					# Cosmeto
					elif prod.pl_family in ['cosmetology']:
						self.nr_cosmetology = self.nr_cosmetology + line.product_uom_qty
						self.amo_cosmetology = self.amo_cosmetology + line.price_subtotal

		# Products
		elif prod.type in ['product']:
			self.nr_products = self.nr_products + line.product_uom_qty
			self.amo_products = self.amo_products + line.price_subtotal

			# Topical
			if prod.pl_family in ['topical']:
				self.nr_topical = self.nr_topical + line.product_uom_qty
				self.amo_topical = self.amo_topical + line.price_subtotal

			# Card
			elif prod.pl_family in ['card']:
				self.nr_card = self.nr_card + line.product_uom_qty
				self.amo_card = self.amo_card + line.price_subtotal

			# kit
			elif prod.pl_family in ['kit']:
				self.nr_kit = self.nr_kit + line.product_uom_qty
				self.amo_kit = self.amo_kit + line.price_subtotal

		return False
	# line_analysis
