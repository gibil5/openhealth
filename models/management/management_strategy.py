# -*- coding: utf-8 -*-
"""
	Management - Strategy

	SRP
		Responsibility of this class:
		Define a strategy for resolving a problem (business logic).

	Interface
		def update_sales(self, vector_obj, vector_sub):
		def update_sales_by_doctor(self):
		def update_stats(self):

		def line_analysis(self, line):

		def create_doctor_data(self, doctor_name, orders):

		def set_averages(self):
		def set_ratios(self):
		def upack_vector_avg(self, result):
		def bridge_avg(self, tag, value):

	Created: 			28 may 2018
	Last up: 			11 dec 2020
"""
from __future__ import print_function
import collections

from openerp import models

from physician import Physician
from mgt_order_line import MgtOrderLine
from lib import mgt_funcs, mgt_db, mgt_bridge

# ------------------------------------------------------------------- Class -----------------------
class ManagementStrategy(models.Model):
	"""
	Using vectors and functional programming.
	"""
	_inherit = 'openhealth.management'
	#_name = 'openhealth.management.implementation'
	#_order = 'date_begin desc'


# -------------------------------------------------------------------------------------------------
# Second Level - Update Buttons
# -------------------------------------------------------------------------------------------------

# ----------------------------------------------------------- Update Fast ------
	def update_sales(self, vector_obj, vector_sub):
		"""
		Update Sales Macros
		Responsibilites:
			- Clean
			- Get orders
			- Loop on sales - Line analysis
			- Update stats
		"""
		print()
		print('** Update Sales')

		# Clean
		self.reset_macro()

		# Get Orders
		if self.type_arr in ['all']:
			orders, count = mgt_db.get_orders_filter_fast(self, self.date_begin, self.date_end)
		else:
			orders, count = mgt_db.get_orders_filter(self, self.date_begin, self.date_end, self.state_arr, self.type_arr)

		# Loop on sales
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
						#self.line_analysis_obj(line, vector_obj)
						#self.line_analysis_sub(line, vector_sub)
						mgt_funcs.line_analysis_obj(line, vector_obj)
						mgt_funcs.line_analysis_sub(line, vector_sub)

				# If credit Note - Do Amount Flow
				elif order.state in ['credit_note']:
					self.credit_note_analysis(order)

# Analysis - Setters

		# Set Averages
		self.set_averages()

		# Set Ratios
		self.set_ratios()

		# Set Totals
		vector = [self.amo_products, self.amo_services, self.amo_other, self.amo_credit_notes]
		self.total_amount = mgt_funcs.get_sum_pure(vector)

		vector = [self.nr_products, self.nr_services]
		self.total_count = mgt_funcs.get_sum_pure(vector)

		self.total_tickets = tickets

		# Set Percentages
		#mgt_funcs.set_percentages(self, total_amount)
		#results = mgt_funcs.percentages_pure(vector, self.total_amount)

		# Test
		#print('Vector obj - Test')
		#for obj in vector_obj:
		#	print(obj.name)
		#	print(obj.amount)
		#	print(obj.count)
		#	print()

		# Set macros
		# Bridges
		mgt_bridge.set_totals(self, vector_obj)
		mgt_bridge.set_types(self, vector_obj)
		mgt_bridge.set_subfamilies(self, vector_sub)

	# update_sales


# ---------------------------------------------------------- Get Averages ------
	def set_averages(self):
		"""
		Set averages
		"""
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
		"""
		Unpack vecto average
		"""
		for avg in result:
			tag = avg[0]
			value = avg[1]
			self.bridge_avg(tag, value)


# ------------------------------------------------------- Bridge Averages ------
	def bridge_avg(self, tag, value):
		"""
		Bridge average
		"""

		#dic = {
		#		'prod': 	self.avg_products,
		#		'ser': 		self.avg_services,
		#		'con': 		self.avg_consultations,
		#		'proc': 	self.avg_procedures,
		#		'oth': 		self.avg_other,
		#	}

		# Families
		if tag == 'prod':
			self.avg_products = value
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


		# Get - Should be static method
		env = self.env['oeh.medical.physician']
		doctors = Physician.get_doctors(env)
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
		"""
		Create doctor data
		"""
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
		"""
		if self.nr_consultations != 0:
			self.ratio_pro_con = (float(self.nr_procedures) / float(self.nr_consultations))
	# set_ratios


# ----------------------------------------------------------- Line Analysis ----
	def line_analysis(self, line):
		"""
		Parses order lines
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
