# -*- coding: utf-8 -*-
"""
	Doctor Line - Dep ?

	Only Data model. No functions.

	Created: 			18 May 2018
	Last up: 			13 Feb 2019
"""
from __future__ import print_function

import collections
from openerp import models, fields, api
from . import mgt_vars

class DoctorLine(models.Model):
	"""
    Doctor line
	"""

	_name = 'openhealth.management.doctor.line'

	_inherit = 'openhealth.management.line'
	_order = 'amount desc'


# ----------------------------------------------------------- Relational --------------
	management_id = fields.Many2one(
			'openhealth.management',
		)

# ----------------------------------------------------------- Nex --------------
	# Day Line
	#day_line = fields.One2many(
	#		'openhealth.management.day.doctor.line',
	#		'doctor_id',
	#	)

# ------------------------------------------------------------- Relational -----
	# Sales
	order_line = fields.One2many(
			'openhealth.management.order.line',
			'doctor_id',
		)

	# Family
	family_line = fields.One2many(
			'openhealth.management.family.line',
			'doctor_id',
		)

	# Sub family
	sub_family_line = fields.One2many(
			'openhealth.management.sub_family.line',
			'doctor_id',
		)

# ----------------------------------------------------------- Primitives -------
	# Nr Families
	nr_consultations = fields.Integer(
			'Nr Consultas',
			default=0,
		)

	nr_products = fields.Integer(
			'Nr Productos',
			default=0,
		)

	nr_procedures = fields.Integer(
			'Nr Procedimientos',
			default=0,
		)

	# Nr Sub Families
	nr_procedures_co2 = fields.Integer(
			'Nr Co2',
			default=0,
		)

	nr_procedures_quick = fields.Integer(
			'Nr Quick',
			default=0,
		)

	nr_medicals = fields.Integer(
			'Nr Tratamientos Médicos',
			default=0,
		)

	nr_cosmetologies = fields.Integer(
			'Nr Cosmeatrias',
			default=0,
		)

	# Ratios
	ratio_pro_con = fields.Float(
			'Ratio Total %',
		)

	ratio_pro_con_co2 = fields.Float(
			'Ratio Co2 %',
		)

	ratio_pro_con_quick = fields.Float(
			'Ratio Quick %',
		)



# ----------------------------------------------------------- From Pl - Vars -----

# ----------------------------------------------------------- Relational -------
	# Day Line
	#day_line = fields.One2many(
	#		'openhealth.management.day.doctor.line',
	#		'doctor_id',
	#	)

	# Doctor daily
	doctor_daily = fields.One2many(
			'doctor.daily',
			'doctor_id',
		)
	# Sales
	order_line = fields.One2many(
			'openhealth.management.order.line',
			'doctor_id',
		)


# ----------------------------------------------------------- From Pl - Methods -----

# ----------------------------------------------------------- Update Daily -----
	@api.multi
	#def update_daily(self):
	def update_daily(self, management_id):
		"""
		Update daily for each Doctor
		Used by 
			Management
				update_daily
		"""
		print()
		print('X - Update Daily')

		# Init
		#self.day_line.unlink()
		self.doctor_daily.unlink()
		date_array = []

		# Clear - Nex
		#self.order_line.unlink()

		# For all lines in the doctors order line
		for line in self.order_line:
			# Get date
			date = line.x_date_created.split()[0]
			# Create
			if date not in date_array:
				# Apprend to date array
				date_array.append(date)

				# Create Doctor Daily
				day = self.doctor_daily.create({
													'date': date,
													'management_id': management_id,
													'doctor_id': self.id,
									})

				# Update weekday and duration
				day.update()

			# Update Lines
			day.update_line(line)

			# Price list 2019
			if line.product_id.pl_price_list in ['2019']:
				day.pl_update_macro()

			# Price list 2018
			elif line.product_id.pl_price_list in ['2018']:
				day.update_macro()

		# Endfor
		print(date_array)
	# update_daily

# ----------------------------------------------------------- Stats ------------
	# Stats
	@api.multi
	def pl_stats(self):
		"""
		Doctor Statistics
		Used by:
			Management
				update_doctor
					pl_update_stats
		"""
		print()
		print('X - Mgt Doctor Line - Stats')

		# Using collections - More Abstract !

		# Clear
		self.sub_family_line.unlink()
		self.family_line.unlink()

		# Init
		family_arr = []
		sub_family_arr = []
		self.nr_consultations = 0
		self.nr_procedures = 0
		self.nr_procedures_co2 = 0
		self.nr_procedures_quick = 0
		self.nr_products = 0
		self.nr_medicals = 0
		self.ratio_pro_con = 0
		self.ratio_pro_con_co2 = 0
		self.ratio_pro_con_quick = 0

		# Loop
		for line in self.order_line:
			# Family
			family_arr.append(line.family)
			# Sub family
			sub_family_arr.append(line.sub_family)

# Count and Create
		# Family - Using collections
		counter_family = collections.Counter(family_arr)
		for key in counter_family:
			count = counter_family[key]

			# Counters
			#print key
			#print count
			family = self.family_line.create({
												'name': key,
												'x_count': count,
												'doctor_id': self.id,
											})
			family.update()

			# Counters
			#print key

			# Families
			if key in ['consultation', 'consultation_gyn', 'consultation_0', 'consultation_100']:
				self.nr_consultations = self.nr_consultations + count

			#elif key in ['laser', 'medical', 'cosmetology']:
			elif key in ['laser', 'medical', 'cosmetology', 'echography', 'gynecology', 'promotion']:
				self.nr_procedures = self.nr_procedures + count

			#elif key in ['topical', 'card']:
			elif key in ['topical', 'card', 'kit']:
				self.nr_products = self.nr_products + count

			# Subfamilies
			if key == 'medical':
				self.nr_medicals = self.nr_medicals + count

			if key == 'cosmetology':
				self.nr_cosmetologies = self.nr_cosmetologies + count

		# Subfamily - Using collections
		counter_sub_family = collections.Counter(sub_family_arr)
		for key in counter_sub_family:

			count = counter_sub_family[key]
			sub_family = self.sub_family_line.create({
														'name': key,
														'x_count': count,
														'doctor_id': self.id,
												})
			sub_family.update()

			# Counters
			#print key
			if key == 'laser_co2':
				self.nr_procedures_co2 = count
			elif key == 'laser_quick':
				self.nr_procedures_quick = count

# Amounts and Percentages
		#print 'Amounts'
		# Family
		for family in self.family_line:
			amount = 0
			orders = self.env['openhealth.management.order.line'].search([
																			('family', '=', family.name),
																			('doctor_id', '=', self.id),
																	],
																		#order='x_serial_nr asc',
																		#limit=1,
																	)
			for order in orders:
				amount = amount + order.price_total

			family.amount = amount


			# Percentage
			if self.amount != 0:
				family.per_amo = family.amount / self.amount

			#print family.name
			#print amount
			#print

		# Sub Family
		for sub_family in self.sub_family_line:
			amount = 0
			orders = self.env['openhealth.management.order.line'].search([
																			('sub_family', '=', sub_family.name),
																			('doctor_id', '=', self.id),
																	],
																		#order='x_serial_nr asc',
																		#limit=1,
																	)

			for order in orders:
				amount = amount + order.price_total

			sub_family.amount = amount

			# Percentage
			if self.amount != 0:
				sub_family.per_amo = sub_family.amount / self.amount
			#print sub_family.name
			#print amount
			#print

		#self.update_fields()
		self.update()
	# stats
