# -*- coding: utf-8 -*-
"""
	Management - Methods

	Created: 			28 may 2018
	Last up: 			28 oct 2020
"""
from __future__ import print_function
from timeit import default_timer as timer
import datetime
import collections
from openerp import models, fields, api

from lib import mgt_funcs
from lib import prod_funcs
from lib import mgt_db

from mgt_patient_line import MgtPatientLine
from management_order_line import MgtOrderLine


# --------------------------------------------------------------- Constants ----
_MODEL_MGT = "openhealth.management"


# ------------------------------------------------------------------- Class ----
class Management(models.Model):
	"""
	Contains only methods.
	"""
	_inherit = _MODEL_MGT


# -------------------------------------------------------------------------------------------------
# First Level - Update Buttons
# -------------------------------------------------------------------------------------------------

# ----------------------------------------------------------- Update Fast ------
	@api.multi
	def update_fast(self):
		"""
		Update Macros values
		Does not update:
			patients, doctors, productivity, daily.
		"""
		print()
		print('*** Update Fast')

		# Go
		self.update_sales()
		self.update_year()

	# update_fast


# --------------------------------------------------------- Update Patients ----
	# Update Patients
	@api.multi
	def update_patients(self):
		"""
		Update Patients
		Creates a Patient line, for each patient in month sales.
		"""
		print()
		print('*** Update Patients')

		#  Init
		env = self.env['openhealth.management.patient.line']

		# Get orders
		# Should be a class method
		orders, count = mgt_db.get_orders_filter_fast(self, self.date_begin, self.date_end)
		#print(orders)
		#print(count)
		
		# Create
		for order in orders:
			
			# Init
			#patient_id = order.patient.id
			patient = order.patient

			if self.mode in ['normal']:

				# Count
				count = MgtPatientLine.count_oh(patient.id, self.id, env)
				
				# Create
				if count == 0:
					#self.patient_line = MgtPatientLine.create_oh(patient_id, self.id, env)
					self.patient_line = MgtPatientLine.create_oh(patient, self.id, env)
					print(self.patient_line)

		# Update
		for patient_line in self.patient_line:
			patient_line.update()
		#print()

	# update_patients


# ---------------------------------------------------------- Update Doctors ----
	@api.multi
	def update_doctors(self):
		"""
		Update Doctors
		"""
		print()
		print('*** Update Doctors')

		# Go
		#t0 = timer()

		# Sales by Doctor
		self.update_sales_by_doctor()

		# Stats
		self.update_stats()

		#t1 = timer()
		#self.delta_doctor = t1 - t0

		print()

		#return 1	# For Django
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
		print('*** Update Productivity')
		
		# Go
		prod_funcs.create_days(self)
		
		# Update cumulative and average
		prod_funcs.update_day_cumulative(self)
		prod_funcs.update_day_avg(self)

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
		print('*** Update Daily Sales')

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
	def update_sales(self):
		"""
		Update Sales Macros
			Steps
				Clean
				Get orders
				Loop 
					Line analysis
		"""
		print()
		print('** Update Sales Fast')

		# Clean
		self.reset_macro()

		# Get Orders
		if self.type_arr in ['all']:
			orders, count = mgt_db.get_orders_filter_fast(self, self.date_begin, self.date_end)
		else:
			orders, count = mgt_db.get_orders_filter(self, self.date_begin, self.date_end, self.state_arr, self.type_arr)

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
					self.credit_note_analysis()

# Analysis - Setters

		# Set Averages
		self.set_averages()

		# Set Ratios
		self.set_ratios()

		# Set Totals
		total_amount = self.set_totals(tickets)

		# Set Percentages
		mgt_funcs.set_percentages(self, total_amount)

	# update_sales


# ---------------------------------------------------------- Get Averages ------
	def set_averages(self):

		vector = [	
					# Families
					('prod', self.amo_products, self.nr_products),
					('serv', self.amo_services, self.nr_services),
					('cons', self.amo_consultations, self.nr_consultations),
					('proc', self.amo_procedures, self.nr_procedures),
					('othe', self.amo_other, self.nr_other),

					# Sub families

					# Prod
					('top', self.amo_topical, self.nr_topical),
					('car', self.amo_card, self.nr_card),
					('kit', self.amo_kit, self.nr_kit),

					# Laser
					('co2', self.amo_co2, self.nr_co2),
					('exc', self.amo_exc, self.nr_exc),
					('ipl', self.amo_ipl, self.nr_ipl),
					('ndy', self.amo_ndyag, self.nr_ndyag),
					('qui', self.amo_quick, self.nr_quick),

					# Medical
					('med', self.amo_medical, self.nr_medical),
					('cos', self.amo_cosmetology, self.nr_cosmetology),
					('gyn', self.amo_gyn, self.nr_gyn),
					('ech', self.amo_echo, self.nr_echo),
					('pro', self.amo_prom, self.nr_prom),
		]

		# Functional - call to pure function
		result = mgt_funcs.averages_pure(vector)

		self.upack_vector_avg(result)

		
# ---------------------------------------------------------- Set Averages ------
	def upack_vector_avg(self, result):
		for avg in result: 
			tag = avg[0]
			value = avg[1]
			self.bridge_avg(tag, value)


# ------------------------------------------------------- Bridge Averages ------
	def bridge_avg(self, tag, value):

		#dic = {
		#		'prod': 	self.avg_products,
		#		'ser': 		self.avg_services,
		#		'con': 		self.avg_consultations,
		#		'proc': 	self.avg_procedures,
		#		'oth': 		self.avg_other,
		#	}

		# Families
		if tag == 'prod':
			self.avg_products  = value
			return

		if tag == 'serv':
			self.avg_services = value
			return
		
		if tag == 'cons':
			self.avg_consultations = value
			return

		if tag == 'proc':
			self.avg_procedures = value
			return
		
		if tag == 'othe':
			self.avg_other = value
			return

		# Sub Families

		# Prod
		if tag == 'top':
			self.avg_topical = value
			return

		if tag == 'car':
			self.avg_card = value
			return

		if tag == 'kit':
			self.avg_kit = value
			return

		# Laser
		if tag == 'co2':
			self.avg_co2 = value
			return

		if tag == 'exc':
			self.avg_exc = value
			return

		if tag == 'ipl':
			self.avg_ipl = value
			return

		if tag == 'ndy':
			self.avg_ndyag = value
			return

		if tag == 'qui':
			self.avg_quick = value
			return

		# Medical
		if tag == 'med':
			self.avg_medical = value
			return

		if tag == 'cos':
			self.avg_cosmetology = value
			return

		if tag == 'ech':
			self.avg_echo = value
			return

		if tag == 'gyn':
			self.avg_gyn = value
			return

		if tag == 'pro':
			self.avg_prom = value
			return


# ----------------------------------------------------------- Update Year ------
	@api.multi
	def update_year(self):
		"""
		Update Yearly total amounts
		"""
		print()
		print('** Update Year')

		# Mgts
		mgts = self.env[_MODEL_MGT].search([
												('owner', 'in', ['month']),
												('year', 'in', [self.year]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		# Count
		count = self.env[_MODEL_MGT].search_count([
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



# ----------------------------------------------------------- Update -------------------------------

# ----------------------------------------------- Update Sales - By Doctor -----

	def update_sales_by_doctor(self):
		"""
		Update Sales by Doctor
		"""
		print()
		print('Update Sales - By Doctor')

		# Clean - Important 
		self.doctor_line.unlink()

		# Init vars
		total_amount = 0
		total_count = 0
		total_tickets = 0

		# Doctors Inactive
		doctors_inactive = self.env['oeh.medical.physician'].search([
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

			# Get Orders - Must include Credit Notes
			orders, count = mgt_db.get_orders_filter_by_doctor(self, self.date_begin, self.date_end, doctor.name)
			#print(orders)
			#print(count)

			if count > 0:
				self.create_doctor_data(doctor.name, orders)

			#print()
	# update_sales_by_doctor


# ----------------------------------------------------------- Create Doctor Data ------------
	def create_doctor_data(self, doctor_name, orders):
		print()
		print('** Create Doctor Data')

		#  Init
		env = self.env['openhealth.management.order.line']

		# Init Loop
		amount = 0
		count = 0
		#tickets = 0

		# Create
		doctor = self.doctor_line.create({
											'name': doctor_name,
											'management_id': self.id,
										})

		# Loop
		for order in orders:

			# For loop
			#tickets = tickets + 1

			# Filter Block
			if not order.x_block_flow:

				# For loop
				amount = amount + order.amount_total

				# State equal to Sale
				if order.state in ['sale']:

					# Order Lines
					for line in order.order_line:

						# For loop
						count = count + 1

						# Create- Should be a class method
						print('*** Create Doctor Order Line !')
						order_line = MgtOrderLine.create_oh(order, line, doctor, self, env)

					# Line Analysis Sale - End
				# Conditional State Sale - End
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
		mgts = self.env[_MODEL_MGT].search([
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
		mgt = self.env[_MODEL_MGT].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
															('month', 'not in', [False]),
														],
														order='total_amount asc',
														limit=1,
													)
		mgt.pl_min = True


		# Max
		mgt = self.env[_MODEL_MGT].search([
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
		mgts = self.env[_MODEL_MGT].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
														],
														order='date_begin asc',
														#limit=1,
													)
		# Count
		count = self.env[_MODEL_MGT].search_count([
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
		#print()
		#print('Reset Macros')

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
		print('*** Update Stats !')

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


# ------------------------------------------------------------- Set Ratios -----
	def set_ratios(self):
		"""
		Set Ratios
		Used by 
			Management
		"""
		if self.nr_consultations != 0:
			self.ratio_pro_con = (float(self.nr_procedures) / float(self.nr_consultations))
	# set_ratios


# ----------------------------------------------------------- Set Totals -------
	def set_totals(self, tickets):
		"""
		Set Totals
		Used by 
			Management
		"""
		self.total_amount = self.amo_products + self.amo_services + self.amo_other + self.amo_credit_notes
		self.total_count = self.nr_products + self.nr_services
		self.total_tickets = tickets

		return self.total_amount
	# set_totals


# ----------------------------------------------------------- Line Analysis ----
	#def line_analysis(self, line, verbose=False):
	def line_analysis(self, line):
		"""
		Analyses order lines 
		Updates counters
		"""
		#print('Line analysis')

		# Init
		prod = line.product_id

		#print('name: ', prod.name)
		#print('treatment: ', prod.pl_treatment)
		#print('family: ', prod.pl_family)
		#print('sub_family: ', prod.pl_subfamily)
		#print()


		# Products
		if prod.type in ['product']:
			self.nr_products = self.nr_products + line.product_uom_qty
			self.amo_products = self.amo_products + line.price_subtotal

			# Topical
			if prod.pl_family in ['topical']:
				self.nr_topical = self.nr_topical + line.product_uom_qty
				self.amo_topical = self.amo_topical + line.price_subtotal
				return

			# Card
			elif prod.pl_family in ['card']:
				self.nr_card = self.nr_card + line.product_uom_qty
				self.amo_card = self.amo_card + line.price_subtotal
				return

			# kit
			elif prod.pl_family in ['kit']:
				self.nr_kit = self.nr_kit + line.product_uom_qty
				self.amo_kit = self.amo_kit + line.price_subtotal
				return

		# Services
		else:
			self.nr_services = self.nr_services + line.product_uom_qty
			self.amo_services = self.amo_services + line.price_subtotal

			# Consultations
			if prod.pl_treatment in ['CONSULTA MEDICA']:
				self.nr_sub_con_med = self.nr_sub_con_med + line.product_uom_qty
				self.amo_sub_con_med = self.amo_sub_con_med + line.price_subtotal
				return

			# Procedures
			else:
				self.nr_procedures = self.nr_procedures + line.product_uom_qty
				self.amo_procedures = self.amo_procedures + line.price_subtotal

				# By Treatment
				# Co2
				if prod.pl_treatment in ['LASER CO2 FRACCIONAL']:
					self.nr_co2 = self.nr_co2 + line.product_uom_qty
					self.amo_co2 = self.amo_co2 + line.price_subtotal
					return

				# Exc
				elif prod.pl_treatment in ['LASER EXCILITE']:
					self.nr_exc = self.nr_exc + line.product_uom_qty
					self.amo_exc = self.amo_exc + line.price_subtotal
					return

				# Quick
				elif prod.pl_treatment in ['QUICKLASER']:
					self.nr_quick = self.nr_quick + line.product_uom_qty
					self.amo_quick = self.amo_quick + line.price_subtotal
					return

				# Ipl
				elif prod.pl_treatment in ['LASER M22 IPL']:
					self.nr_ipl = self.nr_ipl + line.product_uom_qty
					self.amo_ipl = self.amo_ipl + line.price_subtotal
					return

				# Ndyag
				elif prod.pl_treatment in ['LASER M22 ND YAG']:
					self.nr_ndyag = self.nr_ndyag + line.product_uom_qty
					self.amo_ndyag = self.amo_ndyag + line.price_subtotal
					return

				# Medical
				elif prod.pl_family in ['medical']:
					self.nr_medical = self.nr_medical + line.product_uom_qty
					self.amo_medical = self.amo_medical + line.price_subtotal
					return

				# Cosmeto
				elif prod.pl_family in ['cosmetology']:
					self.nr_cosmetology = self.nr_cosmetology + line.product_uom_qty
					self.amo_cosmetology = self.amo_cosmetology + line.price_subtotal
					return

				# Echo
				elif prod.pl_family in ['echography']:
					self.nr_echo = self.nr_echo + line.product_uom_qty
					self.amo_echo = self.amo_echo + line.price_subtotal
					return

				# Gyn
				elif prod.pl_family in ['gynecology']:
					self.nr_gyn = self.nr_gyn + line.product_uom_qty
					self.amo_gyn = self.amo_gyn + line.price_subtotal
					return

				# Prom
				elif prod.pl_family in ['promotion']:
					self.nr_prom = self.nr_prom + line.product_uom_qty
					self.amo_prom = self.amo_prom + line.price_subtotal
					return

	# line_analysis


# ------------------------------------------------------------- CN Analysis ----
	def credit_note_analysis(self):
		self.nr_credit_notes = self.nr_credit_notes + 1
		self.amo_credit_notes = self.amo_credit_notes + order.x_amount_flow


# ------------------------------------------------------- Validate Internal ----
	# Validate
	@api.multi
	def validate(self):
		"""
		Validates the content. 
		For internal Data Coherency - internal and external. 
		"""
		print()
		print('Validate the content !')

		# Internal
		out = self.validate_internal()

		# External
		#self.validate_external()  	# Dep !

		# Django
		return out
	# validate


# ------------------------------------------------------- Validate Internal ----
	# Validate
	@api.multi
	def validate_internal(self):
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


# ------------------------------------------------------- Validate external ----
	# Validate
	@api.multi
	def validate_external(self):
		"""
		Validates Data Coherency - External. 
		Looks for data coherency between reports.
		Builds a Report Sale Product for the month. 
		Compares it to Products stats.
		"""
		#print()
		#print('Validate External')

		if self.report_sale_product.name in [False]:
			date_begin = self.date_begin
			self.report_sale_product = self.env['openhealth.report.sale.product'].create({
																							'name': date_begin,
																							'management_id': self.id,
																						})
		rsp = self.report_sale_product
		#print(rsp)
		#print(rsp.name)

		rsp.update()

		self.rsp_count = rsp.total_qty
		self.rsp_total = rsp.total
		self.rsp_count_delta = self.nr_products - self.rsp_count
		self.rsp_total_delta = self.amo_products - self.rsp_total

