# -*- coding: utf-8 -*-
"""
	Management - Controller 

	SRP
		Responsibility of this class:
		Controller - defines the way the user interface reacts to user input.

	Interface
		def reset_macro(self):
		def reset_relationals(self):
		def validate_internal(self):

	Created: 			 6 dec 2020
	Last up: 			11 dec 2020
"""
from __future__ import print_function
import datetime

from openerp import models, api

from lib import mgt_funcs, prod_funcs, mgt_db, mgt_bridge
from mgt_patient_line import MgtPatientLine

# --------------------------------------------------------------- Constants ----
TYPES = [
		# Types
		'products',
		'services',
]

#FAMILIES = [
		# Families
		#'consultations',
		#'procedures',
		#'credit_notes',
		#'other',
#]

SUBFAMILIES = [
		# Sub Families
		'co2',
		'exc',
		'ndy',
		'ipl',
		'qui',
		'med',
		'cos',
		'ech',
		'gyn',
		'pro',
		'top',
		'vip',
		'kit',
]


# ------------------------------------------------------------------- Class -----------------------
class ManagementBusiness(models.Model):
	"""
    Management - Business logic.
    Contains the BL of the company.
	"""
	_inherit = 'openhealth.management'

# -------------------------------------------------------------------------------------------------
# First Level - Update Buttons
# -------------------------------------------------------------------------------------------------

# ----------------------------------------------------------- Update Fast ------
	@api.multi
	def update_fast(self):
		"""
		Updates Macro values
		Does not update: patients, doctors, productivity, daily.
		"""
		print()
		print('*** Update Fast')

		#  Init vectors
		vector_obj = mgt_funcs.init_vector(TYPES)
		vector_sub = mgt_funcs.init_vector(SUBFAMILIES)

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
		orders, count = mgt_db.get_orders_filter_fast(self, self.date_begin, self.date_end)
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
		self.update_sales_by_doctor()

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
		prod_funcs.create_days(self)

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
		self.reset_macro()
		self.reset_micro()
	# reset

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
