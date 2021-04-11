# -*- coding: utf-8 -*-
"""
	Management Patient Line
	Should contain class methods

	Created: 			20 Jun 2019
	Last up: 			27 oct 2020
"""
from __future__ import print_function
from openerp import models, fields, api
from openerp.addons.openhealth.models.patient import pat_vars
from .management_db import ManagementDb


class MgtPatientLine(models.Model):
	"""
	Patient line
	"""
	_name = 'openhealth.management.patient.line'
	_order = 'amount_total desc'


# ----------------------------------------------------- Const ------------------
	_MODEL = "openhealth.management.patient.line"


# ----------------------------------------------------- Class methods ----------
	# Create
	@classmethod
	#def create_oh(cls, patient_id, management_id, env):
	def create_oh(cls, patient, management_id, env):
		#print('Class method - create')
		#print(cls)
		#print(patient_id, management_id)
		# create
		patient_line = env.create({
									'patient': patient.id,
									'management_id': management_id,
		})
		#cls.sex = patient.sex
		#cls.age = patient.age
		return patient_line


	# Count
	@classmethod
	def count_oh(cls, patient_id, management_id, env):
		#print('Class method - count')
		#print(cls)
		#print(patient_id, management_id)
		# count
		count = env.search_count([
									('patient', '=', patient_id),
									('management_id', '=', management_id),
			],
			#order='x_serial_nr asc',
			#limit=1,
		)
		return count


# ----------------------------------------------------------- Handles ----------
	# Management 
	management_id = fields.Many2one(
			'openhealth.management',
			ondelete='cascade',
		)

	# Patient
	patient = fields.Many2one(
			'oeh.medical.patient',
			#string='Paciente',
		)

# -------------------------------------------------------------- Vars ----------
	amount_total = fields.Float()

	count_total = fields.Integer()

	age = fields.Char(
			#string="Edad",
		)

	sex = fields.Selection(
			selection=pat_vars.get_sex_type_list(),
			#string="Sexo",
			#required=False,
		)

# ----------------------------------------------------------- Update -------------------------
	# Update
	@api.multi
	def update(self):
		"""
		Update 
		"""
		print()
		print('** MgtPatientLine - Update')

		# Update vars
		self.sex = self.patient.sex
		self.age = self.patient.age

		# Calc Amount total - All sales ever
		self.amount_total = 0
		self.count_total = 0

		# Get Orders
		#orders, count = mgt_db.get_orders_filter_by_patient_fast(self, self.patient.id)
		orders, count = ManagementDb.get_orders_filter_by_patient(self, self.patient.id)

		for order in orders:
			self.amount_total = self.amount_total + order.x_amount_flow
			for line in order.order_line:
				self.count_total = self.count_total + line.product_uom_qty
