# -*- coding: utf-8 -*-
"""
	Management Report

	Created: 			28 May 2018
	Last updated: 		 4 May 2019
"""
from __future__ import print_function

import os
import collections
import datetime
from timeit import default_timer as timer
from openerp import models, fields, api
from openerp.addons.openhealth.models.order import ord_vars
from . import mgt_funcs
from . import mgt_vars

class Management(models.Model):
	"""
	Management Report (Gerencia)
	Reports Sales, for a time period. From a Star Date to an End Date.
	Allows several analysis like:
		- Doctor Sale analysis,
		- Patient Purchase analysis,
		- Productivity analysis,
		- Daily Sales, per Doctor,
		- Statistics, 
		- Report Validation.
	"""
	_name = 'openhealth.management'

	_inherit = 'openhealth.repo'

	#_order = 'date_begin asc'
	_order = 'date_begin desc'




# ----------------------------------------------------------- DEP ----------------------

	# State Array - Dep !
	#state_arr = fields.Char()

	#state_arr = fields.Selection(
	#		selection=mgt_vars._state_arr_list,
	#		string='State Array',
	#		default='sale',
	#		required=True,
	#	)

	# Time Line
	#base_dir = fields.Char()





# ----------------------------------------------------------- PL - Natives ----------------------
	# All Year Max and Min
	pl_max = fields.Boolean(
			'Max',
		)

	pl_min = fields.Boolean(
			'Min',
		)

# ----------------------------------------------------------- PL - Relational ----------------------
	# Doctor
	doctor_line = fields.One2many(
			'openhealth.management.doctor.line',
			'management_id',
		)

	# Doctor
	#doctor_line = fields.One2many(
	#		'openhealth.management.doctor.line',
	#		'management_id',
	#	)


# ----------------------------------------------------------- PL - Natives ----------------------

	# New Procedures

	# New - Echography
	nr_echo = fields.Integer(
			'Nr Ecografia',
		)
	amo_echo = fields.Float(
			'Monto Ecografia',
		)
	per_amo_echo = fields.Float(
			'% Monto Ecografia',
		)
	avg_echo = fields.Float(
			'Precio Prom. Ecografia',
		)


	# New - Gynecology
	nr_gyn = fields.Integer(
			'Nr Ginecologia',
		)
	amo_gyn = fields.Float(
			'Monto Ginecologia',
		)
	per_amo_gyn = fields.Float(
			'% Monto Ginecologia',
		)
	avg_gyn = fields.Float(
			'Precio Prom. Ginecologia',
		)


	# New - Promotions
	nr_prom = fields.Integer(
			'Nr Promocion',
		)
	amo_prom = fields.Float(
			'Monto Promocion',
		)
	per_amo_prom = fields.Float(
			'% Monto Promocion',
		)
	avg_prom = fields.Float(
			'Precio Prom. Promocion',
		)






# ----------------------------------------------------------- PL Natives -------------------------

	# Credit Notes
	per_amo_credit_notes = fields.Float(
		)


	# Consultations
	nr_sub_con_med = fields.Integer(
			'Nr Cons Med',
		)

	amo_sub_con_med = fields.Float(
			'Monto Cons Med',
		)
	
	per_amo_sub_con_med = fields.Float(
			'% Monto Cons Med',
		)


	# Gynecology
	nr_sub_con_gyn = fields.Integer(
			'Nr Cons Gin',
		)

	amo_sub_con_gyn = fields.Float(
			'Monto Cons Gin',
		)
	
	per_amo_sub_con_gyn = fields.Float(
			'% Monto Cons Gin',
		)


	# Chavarri Brand
	nr_sub_con_cha = fields.Integer(
			'Nr Cons Dr. Chav',
		)

	amo_sub_con_cha = fields.Float(
			'Monto Cons Dr. Chav',
		)
	
	per_amo_sub_con_cha = fields.Float(
			'% Monto Sub Cons Dr. Chav',
		)



	# Families and Sub Families
	per_amo_families = fields.Float(
			'% Monto Familias',
		)

	per_amo_subfamilies = fields.Float(
			'% Monto Sub Familias',
		)

	#per_amo_subfamilies_products = fields.Float(
	#		'% Monto Sub Familias Productos',
	#	)

	#per_amo_subfamilies_procedures = fields.Float(
	#		'% Monto Sub Familias Procedimientos',
	#	)



	# Report Sale Product
	report_sale_product = fields.Many2one(
			'openhealth.report.sale.product'
		)

	rsp_count = fields.Integer(
			'RSP Nr',
		)

	rsp_total = fields.Float(
			'RSP Monto',
		)

	rsp_count_delta = fields.Integer(
			'RSP Nr Delta',
		)

	rsp_total_delta = fields.Float(
			'RSP Total Delta',
		)




# ----------------------------------------------------------- PL - Admin ---------------------------------------------

	admin_mode = fields.Boolean()

	nr_products_stats = fields.Integer()

	nr_consultations_stats = fields.Integer()

	nr_procedures_stats = fields.Integer()



# ----------------------------------------------------------- PL - Fields ----------------------
	# Owner
	owner = fields.Selection(
			[
				('month', 'Month'),
				('year', 'Year'),
				('account', 'Account'),
				('aggregate', 'Aggregate'),
			],
			default='month',
			required=True,
		)


	month = fields.Selection(
			#selection=pl_mgt_vars._month_order_list,
			
			selection=mgt_vars._month_order_list,
			
			string='Mes',
			required=True,
		)

	#month = fields.Selection(
	#		selection=ord_vars._month_order_list,
	#		string='Mes',
	#		required=True,
	#	)





# ----------------------------------------------------------- PL - Dummy -------------------------
	# patient
	#patient_line = fields.One2many(
	patient_line = fields.Char(
	#		'openhealth.management.patient.line',
	#		'management_id',
	)





# ----------------------------------------------------------- Configurator ------------------------

	# Default Configurator
	def _get_default_configurator(self):
		configurator = self.env['openhealth.configurator.emr'].search([
																			('x_type', 'in', ['emr']),
																		],
																			#order='date_begin,name asc',
																			limit=1,
			)
		return configurator

	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
			
			default=_get_default_configurator,
		)




# ----------------------------------------------------------- Update Doctors ----------------------
	# Update
	@api.multi
	def update_doctors(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update Doctors')
		t0 = timer()

		self.update_sales_by_doctor()

		self.update_stats()

		#self.update_counters()
		#self.update_qc()
		t1 = timer()
		self.delta_doctor = t1 - t0
		#print self.delta_doctor
		#print
	# update_doctors



# ----------------------------------------------------------- Update Sales - By Doctor ------------

	# Update Sales
	def update_sales_by_doctor(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update Sales - By Doctor')

		# Clean
		self.doctor_line.unlink()

		# Init vars
		total_amount = 0
		total_count = 0
		total_tickets = 0

		# Create Doctors
		doctors = [
					'Dr. Chavarri',
					'Dr. Canales',
					'Dr. Gonzales',
					'Dr. Monteverde',
					'Eulalia',
					'Dr. Abriojo',
					'Dr. Castillo',
					'Dr. Loaiza',
					'Dr. Escudero',
					'Clinica Chavarri',
				]


		# Loop
		for doctor in doctors:
			doctor = self.doctor_line.create({
												'name': doctor,

												'management_id': self.id,
										})



		# Create Sales - By Doctor
		for doctor in self.doctor_line:

			#print(doctor.name)

			# Clear
			doctor.order_line.unlink()


#jx
			# Orders
			# Must include Credit Notes
			orders, count = mgt_funcs.get_orders_filter_by_doctor\
															(self, self.date_begin, self.date_end, doctor.name)

			#print(orders)
			#print(count)



			# Init Loop
			amount = 0
			count = 0
			tickets = 0


			# Loop
			for order in orders:

				# Tickets
				tickets = tickets + 1

				# Filter Block
				if not order.x_block_flow:


					# Parse Data

					# Amount
					#amount = amount + order.amount_total

					# Amount with State
					if order.state in ['credit_note']:
						#amount = amount - order.amount_total
						#amount = amount - order.amount_total
						#amount = amount - order.x_credit_note_amount
						
						amount = amount + order.x_amount_flow
						
						print('Gotcha !')
						print(amount)

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




					# Sale
					if order.state in ['sale']:  	# Sale - Do Line Analysis

						# Order Lines
						for line in order.order_line:

							count = count + 1

							
							# State
							#if order.state in ['credit_note']:
							#	price_unit = -line.price_unit
							#elif order.state in ['sale']:
							#	price_unit = line.price_unit

							
							# Price
							price_unit = line.price_unit
							

							# Here !!!
							#jx
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
																})
							order_line.update_fields()
						# Line Analysis - End
					# Conditional State Sale - End



					# Credit Note
					elif order.state in ['credit_note']:

						# Price
						price_unit = order.x_amount_flow

						# Here !!!
						#jx
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
																#'product_id': 			product_id.id,
																'product_uom_qty': 		1,

																# Price
																'price_unit': 			price_unit,
															})

						order_line.update_fields()
					# Conditional State CN - End

				# Filter Block - End

			# Loop - End



			# Stats
			doctor.amount = amount
			doctor.x_count = count
			# Percentage
			if self.total_amount != 0: 
				doctor.per_amo = (doctor.amount / self.total_amount)


			# Totals - Dep !
			#total_amount = total_amount + amount
			#total_count = total_count + count
			#total_tickets = total_tickets + tickets

	# update_sales_by_doctor







# ----------------------------------------------------------- QC ----------------------------------

	year = fields.Selection(
			selection=ord_vars._year_order_list,
			string='Año',
			default='2019',
			required=True,
		)


	delta_fast = fields.Float(
			'Delta Fast',
		)

	delta_doctor = fields.Float(
			'Delta Doctor',
		)



# ----------------------------------------------------------- Fields ----------------------



	# Type Array
	type_arr = fields.Selection(
			selection=mgt_vars._type_arr_list,
			string='Type Array',
			#default='ticket_receipt,ticket_invoice',
			default='all',
			required=True,
		)


# ----------------------------------------------------------- Relational --------------------------

	# Sales
	order_line = fields.One2many(
			'openhealth.management.order.line',
			'management_id',
		)

	# Sales
	sale_line_tkr = fields.One2many(
			'openhealth.management.order.line',
			'management_tkr_id',
		)


	# Family
	family_line = fields.One2many(
			'openhealth.management.family.line',
			'management_id',
		)

	# Sub_family
	sub_family_line = fields.One2many(
			'openhealth.management.sub_family.line',
			'management_id',
		)

	# Daily
	day_line = fields.One2many(
			'openhealth.management.day.line',
			'management_id',
		)


# ----------------------------------------------------------- Totals ------------------------------
	# Sales
	total_count = fields.Integer(
			#'Nr Líneas',
			'Nr Ventas',
			readonly=True, 
		)

	# Ticket
	total_tickets = fields.Integer(
			#'Nr Ventas',
			'Nr Tickets',
			readonly=True,
		)

	# Ratios
	ratio_pro_con = fields.Float(
			'Ratio (proc/con) %',
		)


# ----------------------------------------------------------- Percentages -------------------------

	#per_amo_other = fields.Float(
	#		'Porc Monto',
	#	)

	per_amo_products = fields.Float(
			#'Porc Monto',
			'% Monto Productos',
		)

	per_amo_consultations = fields.Float(
			#'Porc Monto',
			'% Monto Consultas',
		)

	per_amo_procedures = fields.Float(
			#'Porc Monto',
			'% Monto Procedimientos',
		)

	per_amo_other = fields.Float(
			'Porc Monto',
		)





	per_nr_products = fields.Float(
			'Porc Nr',
		)

	per_nr_consultations = fields.Float(
			'Porc Nr',
		)

	per_nr_procedures = fields.Float(
			'Porc Nr',
		)

	per_nr_other = fields.Float(
			'Porc Nr',
		)



	per_amo_co2 = fields.Float(
			'% Monto Co2',
		)

	per_amo_exc = fields.Float(
			'% Monto Exc',
		)

	per_amo_ipl = fields.Float(
			'% Monto Ipl',
		)

	per_amo_ndyag = fields.Float(
			'% Monto Ndyag',
		)

	per_amo_quick = fields.Float(
			'% Monto Quick',
		)

	per_amo_medical = fields.Float(
			'% Monto TM',
		)

	per_amo_cosmetology = fields.Float(
			'% Monto Cosmiatria',
		)

	per_amo_topical = fields.Float(
			'% Monto Cremas',
		)

	per_amo_card = fields.Float(
			'% Monto Vip',
		)

	per_amo_kit = fields.Float(
			'% Monto Kits',
		)


# ----------------------------------------------------------- Amounts -----------------------------

	amo_products = fields.Float(
			'Monto Productos',
		)

	amo_procedures = fields.Float(
			'Monto Procedimientos',
		)

	amo_consultations = fields.Float(
			'Monto Consultas',
		)


	amo_other = fields.Float(
			'Monto Otros',
		)

	amo_credit_notes = fields.Float(
			'Monto Notas de Credito',
		)



	amo_co2 = fields.Float(
			'Monto Co2',
		)

	amo_exc = fields.Float(
			'Monto Exc',
		)

	amo_ipl = fields.Float(
			'Monto Ipl',
		)

	amo_ndyag = fields.Float(
			'Monto Ndyag',
		)

	amo_quick = fields.Float(
			'Monto Quick',
		)

	amo_medical = fields.Float(
			'Monto TM',
		)

	amo_cosmetology = fields.Float(
			'Monto Cosmiatria',
		)

	amo_services = fields.Float(
			'Monto Servicios',
		)

	amo_topical = fields.Integer(
			'Monto Cremas',
		)

	amo_card = fields.Integer(
			'Monto Vip',
		)

	amo_kit = fields.Integer(
			'Monto Kits',
		)


# ----------------------------------------------------------- Numbers -----------------------------

	nr_procedures = fields.Integer(
			#'Nr Procedimientos',
			'Nr Procs',
		)

	nr_consultations = fields.Integer(
			'Nr Consultas',
		)

	nr_products = fields.Integer(
			'Nr Productos',
		)

	nr_other = fields.Integer(
			'Nr Otros',
		)

	nr_credit_notes = fields.Integer(
			'Nr Notas de Credito',
		)


	# Procedures
	nr_co2 = fields.Integer(
			'Nr Co2',
		)

	nr_exc = fields.Integer(
			'Nr Exc',
		)

	nr_ipl = fields.Integer(
			'Nr Ipl',
		)

	nr_ndyag = fields.Integer(
			'Nr Ndyag',
		)

	nr_quick = fields.Integer(
			'Nr Quick',
		)

	nr_medical = fields.Integer(
			'Nr TM',
		)

	nr_cosmetology = fields.Integer(
			'Nr Cosmiatria',
		)

	# Nr Services
	nr_services = fields.Integer(
			'Nr Servicios',
		)

	# Prods
	nr_topical = fields.Integer(
			'Nr Cremas',
		)

	nr_card = fields.Integer(
			'Nr Vip',
		)

	nr_kit = fields.Integer(
			'Nr Kits',
		)


# ----------------------------------------------------------- Avg ---------------------------------

	avg_other = fields.Float(
			'Precio Prom. Otros',
		)

	avg_products = fields.Float(
			'Precio Prom. Productos',
		)

	avg_consultations = fields.Float(
			'Precio Prom. Consultas',
		)

	avg_procedures = fields.Float(
			'Precio Prom. Procedimientos',
		)

	avg_services = fields.Float(
			'Precio Prom. Servicios',
		)


	# Products
	avg_topical = fields.Float(
			'Precio Prom. Cremas',
		)

	avg_card = fields.Float(
			'Precio Prom. Vip',
		)

	avg_kit = fields.Float(
			'Precio Prom. Kits',
		)


	# Procedures
	avg_co2 = fields.Float(
			'Precio Prom. Co2',
		)

	avg_exc = fields.Float(
			'Precio Prom. Exc',
		)

	avg_ipl = fields.Float(
			'Precio Prom. Ipl',
		)

	avg_ndyag = fields.Float(
			'Precio Prom. Ndyag',
		)

	avg_quick = fields.Float(
			'Precio Prom. Quick',
		)

	avg_medical = fields.Float(
			'Precio Prom. TM',
		)

	avg_cosmetology = fields.Float(
			'Precio Prom. Cosmiatria',
		)


# ----------------------------------------------------------- Update Stats ------------------------

	def update_stats(self):
		"""
		Update Stats - Doctors, Families, Sub-families
		"""
		#print()
		#print('Update Stats')

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

				# Sub family
				sub_family_arr.append(line.sub_family)

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

			# Doctor Stats
			doctor.stats()


	# By Family

		# Count
		counter_family = collections.Counter(family_arr)

		# Create
		for key in counter_family:
			count = counter_family[key]
			amount = _h_amount[key]
			family = self.family_line.create({
													'name': key,
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
		for key in counter_sub_family:
			count = counter_sub_family[key]
			amount = _h_sub[key]
			sub_family = self.sub_family_line.create({
														'name': key,
														'x_count': count,
														'amount': amount,
														'management_id': self.id,
												})
			sub_family.update()

			# Percentage
			if self.total_amount != 0:
				sub_family.per_amo = sub_family.amount / self.total_amount

	# update_stats




# ----------------------------------------------------------- Update Sales - Fast -----------------
	# Update Sales - Fast
	def update_sales_fast(self):
		"""
		high level support for doing this and that.
		"""
		#print()
		#print('Update Sales Fast')

		# Clean
		self.reset_macro()

		# Orders
		if self.type_arr in ['all']:
			orders, count = mgt_funcs.get_orders_filter_fast(self, self.date_begin, self.date_end)
		else:
			orders, count = mgt_funcs.get_orders_filter\
													(self, self.date_begin, self.date_end, self.state_arr, self.type_arr)

		#print orders
		#print count

		# Init Loop
		tickets = 0


# Loop
		for order in orders:
			tickets = tickets + 1

			# Filter Block
			if not order.x_block_flow:


				# Sale
				if order.state in ['sale']:  	# Sale - Do Line Analysis

					# Lines
					for line in order.order_line:

						# Line Analysis
						mgt_funcs.line_analysis(self, line)


				# Credit Note
				elif order.state in ['credit_note']:  									# CN - Do Amount Flow
					self.nr_credit_notes = self.nr_credit_notes + 1
					self.amo_credit_notes = self.amo_credit_notes + order.x_amount_flow


# Analysis

		# Averages

		# Families
		if self.nr_other != 0:
			self.avg_other = self.amo_other / self.nr_other

		if self.nr_products != 0:
			self.avg_products = self.amo_products / self.nr_products

		if self.nr_services != 0:
			self.avg_services = self.amo_services / self.nr_services

		if self.nr_consultations != 0:
			self.avg_consultations = self.amo_consultations / self.nr_consultations

		if self.nr_procedures != 0:
			self.avg_procedures = self.amo_procedures / self.nr_procedures


		# Subfamilies
		if self.nr_topical != 0:
			self.avg_topical = self.amo_topical / self.nr_topical

		if self.nr_card != 0:
			self.avg_card = self.amo_card / self.nr_card

		if self.nr_kit != 0:
			self.avg_kit = self.amo_kit / self.nr_kit

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





		# Ratios
		if self.nr_consultations != 0:
			self.ratio_pro_con = (float(self.nr_procedures) / float(self.nr_consultations)) * 100




		# Totals
		#self.total_amount = self.amo_products + self.amo_services + self.amo_other - self.amo_credit_notes
		self.total_amount = self.amo_products + self.amo_services + self.amo_other + self.amo_credit_notes
		
		self.total_count = self.nr_products + self.nr_services
		self.total_tickets = tickets




		# Percentages

		# Year - Dep !!!
		#if self.total_amount_year != 0:
		#		self.per_amo_total = self.total_amount / self.total_amount_year


		# Month
		if self.total_amount != 0:

			self.per_amo_other = (self.amo_other / self.total_amount)

			self.per_amo_products = (self.amo_products / self.total_amount)
			self.per_amo_consultations = (self.amo_consultations / self.total_amount)
			self.per_amo_procedures = (self.amo_procedures / self.total_amount)

			self.per_amo_topical = (self.amo_topical / self.total_amount)
			self.per_amo_card = (self.amo_card / self.total_amount)
			self.per_amo_kit = (self.amo_kit / self.total_amount)

			self.per_amo_co2 = (self.amo_co2 / self.total_amount)
			self.per_amo_exc = (self.amo_exc / self.total_amount)
			self.per_amo_ipl = (self.amo_ipl / self.total_amount)
			self.per_amo_ndyag = (self.amo_ndyag / self.total_amount)
			self.per_amo_quick = (self.amo_quick / self.total_amount)
			self.per_amo_medical = (self.amo_medical / self.total_amount)
			self.per_amo_cosmetology = (self.amo_cosmetology / self.total_amount)

	# update_sales_fast


# ----------------------------------------------------------- Update - Fast -----------------------
	# Update
	@api.multi
	def update_fast(self):
		"""
		high level support for doing this and that.
		"""
		#print()
		#print('Update Fast')
		t0 = timer()
		self.update_sales_fast()
		t1 = timer()
		self.delta_fast = t1 - t0
		#print self.delta_fast
		#print
	# update


# ----------------------------------------------------------- Reset -------------------------------
	# Reset
	@api.multi
	def reset(self):
		"""
		high level support for doing this and that.
		"""
		#print()
		print('Reset')
		self.reset_macro()
		self.reset_micro()
	# reset


	# Reset Macros
	def reset_macro(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Reset Macros'

		# Clear
		self.total_amount_year = 0

		self.total_amount = 0
		self.total_count = 0
		self.total_tickets = 0

		# Nr
		self.nr_credit_notes = 0
		self.nr_other = 0
		self.nr_products = 0
		self.nr_services = 0
		self.nr_consultations = 0
		self.nr_procedures = 0
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

		# Amo
		self.per_amo_total = 0
		self.amo_credit_notes = 0
		self.amo_other = 0
		self.amo_products = 0
		self.amo_services = 0
		self.amo_consultations = 0
		self.amo_procedures = 0
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

		# Per Amo
		self.per_amo_other = 0
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



	# Reset Micro (Doctors, Families, Sub-families)
	def reset_micro(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Reset Doctors'
		self.order_line.unlink()

		self.doctor_line.unlink()

		self.family_line.unlink()
		self.sub_family_line.unlink()
	# reset_micro


# ----------------------------------------------------------- Update ------------------------------
	# Update
	@api.multi
	def update(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Management - Update')
		t0 = timer()
		now_0 = datetime.datetime.now()
		self.reset()
		self.update_fast()
		self.update_doctors()
		t1 = timer()
		now_1 = datetime.datetime.now()
		delta = t1 - t0
		print()
		#print(t0)
		#print(t1)
		print(now_0)
		print(now_1)
		print(delta)
		print()
	# update


# -------------------------------------------------------------------------------------------------
# 																Productivity                       
# -------------------------------------------------------------------------------------------------

# ----------------------------------------------------------- Update Averages ---------------------
	# Update Averages
	@api.multi
	def update_day_avg(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update - Average')

		# Update
		for day in self.day_line:
			#print(day.date)
			day.update_avg()
			day.update_projection()

	# update_day_avg


# ----------------------------------------------------------- Update Cumulative -------------------
	# Update Cumulative
	@api.multi
	def update_day_cumulative(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update - Cumulative')

		# Init
		amount_total = 0
		duration_total = 0

		# Clean
		#for day in self.day_line:
		#	if day.amount in [0]:
				#day.duration = 0
		#		day.unlink()

		# Update Cumulative and Nr Days
		for day in self.day_line:
			#print(day.name)
			#print(day.date)
			amount_total = amount_total  + day.amount
			day.cumulative = amount_total
			duration_total = duration_total + day.duration
			day.nr_days = duration_total

		# Update Nr Days Total
		for day in self.day_line:
			day.nr_days_total = duration_total

	# update_day_cumulative


# ----------------------------------------------------------- Create Days -------------------------
	# Create Days
	@api.multi
	def create_days(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Create Days')

		# Clean
		self.day_line.unlink()


		# Holidays
		days_inactive = []
		if self.configurator.name not in [False]:
			for day in self.configurator.day_line:
				if day.holiday:
					days_inactive.append(day.date)
		#print(days_inactive)


		# Create
		#date_format = "%Y-%m-%d %H:%M:%S"
		date_format = "%Y-%m-%d"
		date_end_dt = datetime.datetime.strptime(self.date_end, date_format)
		date_begin_dt = datetime.datetime.strptime(self.date_begin, date_format)
		delta = date_end_dt - date_begin_dt
		
		#print(delta)


		# Create
		for i in range(delta.days + 1):

		    date_dt = date_begin_dt + datetime.timedelta(i)
		    weekday = date_dt.weekday()
		    weekday_str = ord_vars._dic_weekday[weekday]
		    #print(date_dt, weekday)


		    # Duration
		    if weekday in [5]:
		    	duration = 0.5
		    else:
		    	duration = 1


		    # Not Sunday
		    if weekday in [0, 1, 2, 3, 4, 5]:


		    	#date_date = date_dt.split()[0]
		    	#date_date = date_dt.day
		    	#date_date = date_dt.date
				date_s = date_dt.strftime(date_format)
				
				#print(date_s)


				if date_s not in days_inactive:

			    	# Create
					day = self.day_line.create({
												'date': date_dt,

												'name': weekday_str,
												'weekday': weekday_str,
												'duration': duration,
												'management_id': self.id,
									})


					day.update_amount()		# Important !


					#print(date_dt, weekday, weekday_str)
					#print(date_dt)
					#print(date_s)

	# create_days

# ----------------------------------------------------------- Update Prod -------------------------
	# Update Days
	@api.multi
	def update_productivity(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update Productivity')
		
		self.create_days()
		#print(self.day_line)

		self.update_day_cumulative()
		
		self.update_day_avg()


# ----------------------------------------------------------- Update Daily -------------------------
	# Update Daily
	@api.multi
	def update_daily(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update daily')
		for doctor in self.doctor_line:
			doctor.update_daily()
