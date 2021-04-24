# -*- coding: utf-8 -*-
"""
	Management - Finance module

	Create a data model for the Management report.
	Define a Controller - the way the user interface reacts to user input.
	Define a Strategy - for resolving a problem (business logic).

	Created: 			28 may 2018
	Last up: 			16 apr 2021
"""
from __future__ import print_function
import collections
from openerp import models, fields, api

from .mgt_patient_line import MgtPatientLine
from .lib import mgt_funcs, prod_funcs, mgt_bridge, mgt_vars
from .sales_doctor import SalesDoctor

from .management_db import ManagementDb

# ------------------------------------------------------------------- Class -----------------------
class Management(models.Model):
	"""
	Finance module
	"""
	_name = 'openhealth.management'
	_order = 'date_begin desc'


# ----------------------------------------------------------- Getters --------------------------
	def get_name(self):
		return self.name

	def get_date_begin(self):
		return self.date_begin

	def get_date_end(self):
		return self.date_end

	def get_total_amount(self):
		return str(self.total_amount)

	def get_total_count(self):
		return str(self.total_count)


# ----------------------------------------------------------- Relational --------------------------

# ------------------------------------------------------------- One2many -------
	# Sales
	order_line = fields.One2many(
			'openhealth.management.order.line',
			'management_id',
		)

	# Sales
	#sale_line_tkr = fields.One2many(
	#		'openhealth.management.order.line',
	#		'management_tkr_id',
	#	)

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

	# Doctor line - For Update Daily
	doctor_line = fields.One2many(
			'openhealth.management.doctor.line',
			'management_id',
		)

	# Doctor Day
	doctor_daily = fields.One2many(
			'doctor.daily',
			'management_id',
		)

	# Productivity
	productivity_day = fields.One2many(
			'productivity.day',
			'management_id',
		)

	# Patient
	patient_line = fields.One2many(
			'openhealth.management.patient.line',
			'management_id',
		)

# ------------------------------------------------------------- Many2one -------
	# Report Sale Product
	#report_sale_product = fields.Many2one(
	#		'openhealth.report.sale.product'
	#	)


# ----------------------------------------------------------- Configurator - Dep -----
	# Default Configurator
	def _get_default_configurator(self):
		return self.env['openhealth.configurator.emr'].search([('x_type', 'in', ['emr']),], limit=1,)

	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
			default=_get_default_configurator,
		)



# ----------------------------------------------------------- PL - Natives -----
	mode = fields.Selection([('normal', 'Normal'),
							('test', 'Test'),
							#('legacy', 'Legacy'),
							],
		default='normal',
		required=True,
	)

	# All Year Max and Min
	pl_max = fields.Boolean('Max')

	pl_min = fields.Boolean('Min')

# ----------------------------------------------------------- PL - Natives -----
	# New Procedures

	# Echography
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

	# Gynecology
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

	# Promotions
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

# ----------------------------------------------------------- PL Natives -------
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

# ----------------------------------------------------------- PL - Admin -------
	admin_mode = fields.Boolean()

	nr_products_stats = fields.Integer()

	nr_consultations_stats = fields.Integer()

	nr_procedures_stats = fields.Integer()


# ----------------------------------------------------------- Fields -----------
	# Type Array
	type_arr = fields.Selection(
			selection=mgt_vars._type_arr_list,
			string='Type Array',
			required=True,
			#default='ticket_receipt,ticket_invoice',
			default='all',
		)

	state_arr = fields.Selection(
			selection=mgt_vars._state_arr_list,
		)

# ----------------------------------------------------------- PL - Fields ------
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
			selection=mgt_vars._month_order_list,
			string='Mes',
			#required=True,
		)

# ----------------------------------------------------------- QC ---------------
	year = fields.Selection(
			selection=mgt_vars._year_order_list,
			string='Año',
			default='2020',
			required=True,
		)

	delta_fast = fields.Float(
			'Delta Fast',
		)

	delta_doctor = fields.Float(
			'Delta Doctor',
		)

# -------------------------------------------------------------------------------------------------
# Functional vars
# -------------------------------------------------------------------------------------------------

	vec_amount = fields.Float(
		'Todos',
	)
	vec_count = fields.Integer(
		'.',
	)

	vec_products_amount = fields.Float(
		'Productos',
	)
	vec_products_count = fields.Integer(
		'.',
	)

	vec_services_amount = fields.Float(
		'Servicios',
	)
	vec_services_count = fields.Integer(
		'.',
	)


	# Sub
	vec_co2_amount = fields.Float(
		'Co2',
	)
	vec_co2_count = fields.Integer(
		'.',
	)

	vec_exc_amount = fields.Float(
		'Exc',
	)
	vec_exc_count = fields.Integer(
		'.',
	)

	vec_ipl_amount = fields.Float(
		'Ipl',
	)
	vec_ipl_count = fields.Integer(
		'.',
	)

	vec_ndy_amount = fields.Float(
		'Ndyag',
	)
	vec_ndy_count = fields.Integer(
		'.',
	)

	vec_qui_amount = fields.Float(
		'Quick',
	)
	vec_qui_count = fields.Integer(
		'.',
	)


	# Medical
	vec_med_amount = fields.Float(
		'Medical',
	)
	vec_med_count = fields.Integer(
		'.',
	)

	vec_cos_amount = fields.Float(
		'Cosmeto',
	)
	vec_cos_count = fields.Integer(
		'.',
	)

	vec_gyn_amount = fields.Float(
		'Gyn',
	)
	vec_gyn_count = fields.Integer(
		'.',
	)

	vec_ech_amount = fields.Float(
		'Echo',
	)
	vec_ech_count = fields.Integer(
		'.',
	)

	vec_pro_amount = fields.Float(
		'Promo',
	)
	vec_pro_count = fields.Integer(
		'.',
	)

	# Prod
	vec_top_amount = fields.Float(
		'Topical',
	)
	vec_top_count = fields.Integer(
		'.',
	)

	vec_vip_amount = fields.Float(
		'Vip',
	)
	vec_vip_count = fields.Integer(
		'.',
	)

	vec_kit_amount = fields.Float(
		'Kit',
	)
	vec_kit_count = fields.Integer(
		'.',
	)


# ----------------------------------------------------------- Repo -------------
	# Name 
	name = fields.Char(
			string="Nombre", 		
			required=True, 
		)

	# Amount Total Year
	total_amount_year = fields.Float(
			'Monto Total Año',
			default=0,
		)

	# Dates
	date_begin = fields.Date(
			string="Fecha Inicio",
			default=fields.Date.today,
			required=True,
		)

	date_end = fields.Date(
			string="Fecha Fin",
			default=fields.Date.today,
			required=True,
		)

	# Amount
	total_amount = fields.Float(
			#'Total Monto',
			#'Total',
			'Monto Total',
			readonly=True,
			default=0,
		)

	# Date Test
	date_test = fields.Datetime(
			string="Fecha Test", 
		)

	# Percentage Total Amount Year
	per_amo_total = fields.Float(
			'Porc Monto Año',
		)

	# State
	state = fields.Selection(			
			selection=[
							('stable', 'Estable'),
							('unstable', 'Inestable'),
			],
			string='Estado',
			#readonly=False,
			default='unstable',
			#index=True,
		)


	# Spacing
	vspace = fields.Char(
			' ', 
			readonly=True
		)

# ----------------------------------------------------------- Totals -----------
	# Sales
	total_count = fields.Integer(
			'Nr Ventas',
			readonly=True,
		)

	# Ticket
	total_tickets = fields.Integer(
			'Nr Tickets',
			readonly=True,
		)

	# Ratios
	ratio_pro_con = fields.Float(
			'Ratio (proc/con) %',
		)

# ----------------------------------------------------------- Percentages -------------------------
	per_amo_products = fields.Float(
			'% Monto Productos',
		)

	per_amo_consultations = fields.Float(
			'% Monto Consultas',
		)

	per_amo_procedures = fields.Float(
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

# ----------------------------------------------------------- Numbers ----------
	nr_procedures = fields.Integer(
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

# ----------------------------------------------------------- Avg --------------
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



# -----------------------------------------------------------------------------------------------------------
# 	Controller - defines the way the user interface reacts to user input.
# -----------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# 	Level Zero - Update all
# -------------------------------------------------------------------------------------------------

# ----------------------------------------------------------- Update All ------
	@api.multi
	def update(self):
		"""
		Updates All
		fast, patients, doctors, productivity, daily.
		"""
		print()
		print('*** Update')
		self.update_fast()
		self.update_patients()
		self.update_doctors()
		self.update_productivity()
		self.update_daily()


# -------------------------------------------------------------------------------------------------
# 	First Level - Update Buttons
# -------------------------------------------------------------------------------------------------

# ----------------------------------------------------------- Update Fast ------
	@api.multi
	def update_fast(self):
		"""
		Updates Macro values
		Does not update: patients, doctors, productivity, daily.
		Uses vectors. 
			The content of vectors is dynamic. 
			They can change if there is a new typologie (type, familiy or sub-family). 
		"""
		print()
		print('*** Update Fast')

		#  Init vectors
		
		# Vector of types (products, services)
		vector_obj = mgt_funcs.init_vector(mgt_vars.TYPES)
		
		# Vector of sub-families (co2, exc, pro...)
		vector_sub = mgt_funcs.init_vector(mgt_vars.SUBFAMILIES)

		# Update sales
		self.update_sales(vector_obj, vector_sub)



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
		#orders, count = mgt_db.get_orders_filter_fast(self, self.date_begin, self.date_end)
		orders, count = ManagementDb.get_orders_filter_fast(self, self.date_begin, self.date_end)
		#print(orders)
		#print(count)

		# Create
		for order in orders:

			# Init
			patient = order.patient

			if self.mode in ['normal']:

				# Count
				count = MgtPatientLine.count_oh(patient.id, self.id, env)

				# Create
				if count == 0:
					self.patient_line = MgtPatientLine.create_oh(patient, self.id, env)
					print(self.patient_line)

		# Update
		for patient_line in self.patient_line:
			patient_line.update()


# ---------------------------------------------------------- Update Doctors ----
	@api.multi
	def update_doctors(self):
		"""
		Update Doctors
		"""
		print()
		print('*** Update Doctors')

		# Sales by Doctor
		#self.update_sales_by_doctor()


		obj = SalesDoctor(self, self.date_begin, self.date_end, self.doctor_line, self.total_amount)
		obj.update()

		# Stats
		self.update_stats()


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
		#prod_funcs.create_days(self)

		# Get Holidays - From config
		self.productivity_day.unlink()
		days_inactive = self.configurator.get_inactive_days()					# Respects the LOD !

		#prod_funcs.create_days(self, days_inactive)
		#prod_funcs.create_productive_days(self, self.date_begin, self.date_end, days_inactive)
		prod_funcs.create_productive_days(self.date_begin, self.date_end, days_inactive, self.productivity_day, self.id)

		# Update cumulative and average
		prod_funcs.update_day_cumulative(self)
		prod_funcs.update_day_avg(self)


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

			doctor.update_daily(self.id) 	# Here !
		print()


# -------------------------------------------------------------- Validate ------
	# Validate
	@api.multi
	def validate(self):
		"""
		Button
		Validates the content.
		For internal Data Coherency - internal and external.
		"""
		print()
		print('*** Validate the content !')
		# Internal
		out = self.validate_internal()

		# External
		#self.validate_external()

# ------------------------------------------------------- Validate Internal ----
	# Validate
	def validate_internal(self):
		"""
		Validates Data Coherency - Internal.
		"""
		print()
		print('** Validates internal')

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



# ----------------------------------------------------------- Reset ------------
	# Reset
	@api.multi
	def reset(self):
		"""
		Reset Button.
		"""
		print('*** Reset')
		self.reset_vector()
		self.reset_macro()
		self.reset_micro()
	# reset

# ----------------------------------------------------------- Reset Vector -----
	# Reset Vector
	def reset_vector(self):
		"""
		Reset Vector - All self fields
		"""
		print('reset_vector')

		# Macros 
		self.vec_amount = 0
		self.vec_count = 0
		self.vec_products_amount = 0
		self.vec_products_count = 0
		self.vec_services_amount = 0
		self.vec_services_count = 0

		# Laser 
		self.vec_co2_amount = 0.
		self.vec_co2_count = 0.
		self.vec_exc_amount = 0.
		self.vec_exc_count = 0.
		self.vec_ipl_amount = 0.
		self.vec_ipl_count = 0.
		self.vec_ndy_amount = 0.
		self.vec_ndy_count = 0.
		self.vec_qui_amount = 0.
		self.vec_qui_count = 0.

		# Med
		self.vec_med_amount = 0.
		self.vec_med_count = 0.
		self.vec_cos_amount = 0.
		self.vec_cos_count = 0.
		self.vec_gyn_amount = 0.
		self.vec_gyn_count = 0.
		self.vec_ech_amount = 0.
		self.vec_ech_count = 0.
		self.vec_pro_amount = 0.
		self.vec_pro_count = 0.

		# Prod
		self.vec_top_amount = 0.
		self.vec_top_count = 0.
		self.vec_vip_amount = 0.
		self.vec_vip_count = 0.
		self.vec_kit_amount = 0.
		self.vec_kit_count = 0.

		# Reset vector 
		vec = [
			# Totals 
			self.vec_amount,
			self.vec_count,
			self.vec_products_amount,
			self.vec_products_count,
			self.vec_services_amount,
			self.vec_services_count,

			# Laser 
			self.vec_co2_amount,
			self.vec_co2_count,
			self.vec_exc_amount,
			self.vec_exc_count,
			self.vec_ipl_amount,
			self.vec_ipl_count,
			self.vec_ndy_amount,
			self.vec_ndy_count,
			self.vec_qui_amount,
			self.vec_qui_count,

			# Med
			self.vec_med_amount,
			self.vec_med_count,
			self.vec_cos_amount,
			self.vec_cos_count,
			self.vec_gyn_amount,
			self.vec_gyn_count,
			self.vec_ech_amount,
			self.vec_ech_count,
			self.vec_pro_amount,
			self.vec_pro_count,

			# Prod
			self.vec_top_amount,
			self.vec_top_count,
			self.vec_vip_amount,
			self.vec_vip_count,
			self.vec_kit_amount,
			self.vec_kit_count,
		]
		
		#mgt_funcs.reset_vector(vec)



# ----------------------------------------------------------- Reset Macros -----
	# Reset Macros
	def reset_macro(self):
		"""
		Reset Macro - All self fields
		"""
		#print()
		#print('Reset Macros')

		# Deltas
		self.delta_fast = 0
		self.delta_doctor = 0

		# Relational
		#if self.patient_line not in [False]:
		self.patient_line.unlink()
		#self.report_sale_product.unlink()
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
	def reset_micro(self):
		"""
		Reset Micro
			All Relational:
				Doctors, Families, Sub-families
		"""
		#print()
		#print('X - Reset Micros')

		# Productivity Days
		self.productivity_day.unlink()

		# Order Lines
		self.order_line.unlink()

		# Doctor lines
		self.doctor_line.unlink()        # Too complex

		# Family lines
		self.family_line.unlink()
		self.sub_family_line.unlink()

	# reset_micro



# ----------------------------------------------------------- Serializer --------------------------
	# Contains the Finance report serialized in json or xml 
	# name, date_begin, date_end, total_amount, total_count, total_tickets
	#report_serial = fields.Char()

	#@api.multi
	#def serialize(self):
	#	self.report_serial = "{	'name': " + self.get_name() + \
	#							", 'date_begin': " + self.get_date_begin() + \
	#							", 'date_end': " + self.get_date_end() + \
	#							", 'total_amount': " + self.get_total_amount() + \
	#						"}"
