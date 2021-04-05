# -*- coding: utf-8 -*-
"""
	Management - Tools

	Define a Controller - the way the user interface reacts to user input.
	Define a Strategy - for resolving a problem (business logic).

	Created: 			 3 apr 2021
	Last up: 			 3 apr 2021
"""
from __future__ import print_function
import collections
from openerp import models, fields, api
from mgt_patient_line import MgtPatientLine
from sales_doctor import SalesDoctor
from management_db import ManagementDb

from lib import mgt_funcs, prod_funcs, mgt_bridge, mgt_vars

# ------------------------------------------------------------------- Class -----------------------
class Management(models.Model):
	"""
	Finance module
	"""
	#_name = 'openhealth.management'
	_order = 'date_begin desc'
	_inherit = 'openhealth.management'



# -------------------------------------------------------------------------------------------------
# 	Third Level - Tools
# -------------------------------------------------------------------------------------------------

# ---------------------------------------------------------- Set Averages ------
	#def set_averages_vector(self, vector_obj):
	#	"""
	#	Set averages vector
	#	"""


# ------------------------------------------------------------- Set Ratios -----
	def set_ratios(self):
		"""
		Set Ratios
		"""
		if self.nr_consultations != 0:
			self.ratio_pro_con = (float(self.nr_procedures) / float(self.nr_consultations))
	# set_ratios


# ---------------------------------------------------------- Set Averages ------
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
		result = mgt_funcs.averages_pure_tag(vector)

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
		#        'prod':     self.avg_products,
		#        'ser':         self.avg_services,
		#        'con':         self.avg_consultations,
		#        'proc':     self.avg_procedures,
		#        'oth':         self.avg_other,
		#    }

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



