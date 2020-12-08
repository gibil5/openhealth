# -*- coding: utf-8 -*-
"""
	Management - Business logic

	SRP
		Responsibility of this class:
		Provide service buttons to the UI.

	Created: 			 6 dec 2020
	Last up: 			 6 dec 2020
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
		vector_obj = self.init_vector(TYPES)
		vector_sub = self.init_vector(SUBFAMILIES)

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

			#doctor.update_daily() 	# Here !
			doctor.update_daily(self.id) 	# Here !
		print()

		# For Django
		#self.date_test = datetime.datetime.now()
		#return 1


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
		#self.validate_external()  	# Dep ?


# ----------------------------------------------------------- Reset ------------
	# Reset
	@api.multi
	def reset(self):
		"""
		Reset Button.
		"""
		print('*** Reset')
		self.reset_macro()
		self.reset_relationals()
	# reset
