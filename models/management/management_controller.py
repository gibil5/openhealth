# -*- coding: utf-8 -*-
"""
	Management - Controller

	Define a Controller - the way the user interface reacts to user input.
	Define a Strategy - for resolving a problem (business logic).

	Created: 			 3 apr 2021
	Last up: 			 4 apr 2021
"""
from __future__ import print_function
from __future__ import absolute_import

import collections
from openerp import models, fields, api
from .mgt_patient_line import MgtPatientLine
from .management_db import ManagementDb

#from sales_doctor import SalesDoctor

from .lib import mgt_funcs, prod_funcs, mgt_bridge, mgt_vars

_pre = '\n\n----------------------------------------------- '
_pos = ' -----'


# ------------------------------------------------------------------- Class -----------------------
class Management(models.Model):
	"""
	Finance module
	"""
	#_name = 'openhealth.management'
	_order = 'date_begin desc'
	_inherit = 'openhealth.management'





	# -----------------------------------------------------------------------------------------------------------
	# 	Strategy - Define a strategy for resolving a problem (business logic).
	#
	#   Interface
	#   ----------
	#	def update_sales(self, vector_obj, vector_sub):
	#	def update_stats(self):
	#	def line_analysis(self, line):
	#	def set_averages(self):
	#	def set_ratios(self):
	#	def upack_vector_avg(self, result):
	#	def bridge_avg(self, tag, value):
	# -----------------------------------------------------------------------------------------------------------


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

        Called by: update_fast
		"""
		print()
		print('** Update Sales')

		# Clean
		self.reset_macro()

		# Get Orders
		if self.type_arr in ['all']:
			#orders, count = mgt_db.get_orders_filter_fast(self, self.date_begin, self.date_end)
			orders, count = ManagementDb.get_orders_filter_fast(self, self.date_begin, self.date_end)
		else:
			#orders, count = mgt_db.get_orders_filter(self, self.date_begin, self.date_end, self.state_arr, self.type_arr)
			orders, count = ManagementDb.get_orders_filter(self, self.date_begin, self.date_end, self.state_arr, self.type_arr)

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
                        
                        # Dep !
						#self.line_analysis(line)

						mgt_funcs.line_analysis_type(line, vector_obj)
						mgt_funcs.line_analysis_sub(line, vector_sub)


				# If credit Note - Do Amount Flow
				elif order.state in ['credit_note']:
					self.credit_note_analysis(order)


# After the loop
# Analysis - Setters

		# Set Averages
		#self.set_averages()
		mgt_funcs.set_averages_vector(vector_obj)
		mgt_funcs.set_averages_vector(vector_sub)


# Data model 
		# Set Totals
		self.total_tickets = tickets
		self.total_amount, self.total_count = mgt_funcs.get_totals(vector_obj)

		# Set Percentages
		#mgt_funcs.set_percentages(self, total_amount)
		#results = mgt_funcs.percentages_pure(vector, self.total_amount)
		mgt_funcs.set_percentages_vector(vector_obj, self.total_amount)
		mgt_funcs.set_percentages_vector(vector_sub, self.total_amount)


		# Set Ratios
		#self.set_ratios()
		#mgt_funcs.set_ratios_vector(vector_obj)
		#mgt_funcs.set_ratios_vector(vector_sub)
		#mgt_funcs.set_ratios_vector(nr_consultations, nr_procedures, vector_obj)

		#self.ratio_pro_con = mgt_funcs.set_ratios_vector(vector_fam)
		self.ratio_pro_con = mgt_funcs.set_ratios_vector(vector_sub)


		# Set macro vectors 
		# Bridges
		mgt_bridge.set_totals(self, vector_obj)
		mgt_bridge.set_types(self, vector_obj)
		mgt_bridge.set_subfamilies(self, vector_sub)



		# Test
		print(_pre + 'Vectors - Test' + _pos)

		vecs = [vector_obj, vector_sub]

		for vector in vecs:
			for obj in vector:
			    print(obj.name)
			    print(obj.count)
			    print(obj.amount)
			    print(obj.average)
			    print(obj.percentage)
			    print()

	# update_sales




# ----------------------------------------------------------- Update Stats -----
	def update_stats(self):
		"""
		Update Stats
			Doctors,
			Families,
			Sub-families

        Called by:
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




