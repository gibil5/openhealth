# -*- coding: utf-8 -*-
"""
 	Family Line 

	Created: 			20 Aug 2018
	Last up: 			18 Dec 2020
"""
from __future__ import print_function
from openerp import models, fields, api
from . import mgt_vars

from management import Management

#class FamilyLine(models.Model):
class MgtFamilyLine(models.Model):
	"""
	Only Data model. No functions.

	Should not be inherited
	"""
	_name = 'openhealth.management.family.line'

	_inherit = 'openhealth.management.line'

	_order = 'amount desc'

# ----------------------------------------------------------- Update -----------
	def update(self):
		print()
		print('X - Update - Family')

		# Idx 
		_h_idx = {
					'gynecology': 	10, 		
					'echography': 	10, 		
					'promotion': 	10, 		
					'kit': 			3, 		

					# 7 Feb 2019
					'credit_note': 	10,

					# 13 Jul 2018 
					'other': 	40, 		
					False: 0, 		
					'consultation': 	10, 		
					'consultation_gyn': 11, 		
					'consultation_0': 	12,
					'consultation_100': 13,
					#'product': 		3, 	
					#'kit': 			3, 		
					'topical': 			20, 		
					'card': 			21, 		
					#'procedure': 	2, 		
					'laser': 			30,
					'medical': 			31,
					'cosmetology': 		32,
		}
		self.idx = _h_idx[self.name]

		# Get Name Spanish
		if self.name in Management._h_name: 
			self.name_sp = Management._h_name[self.name]
		else: 
			self.name_sp = self.name

		# Meta
		if self.name in ['consultation', 'consultation_gyn', 'consultation_0', 'consultation_100']:
			self.meta = 'consultation'
			self.meta_sp = 'Consulta'

		#elif self.name in ['laser', 'medical', 'cosmetology']:
		elif self.name in ['laser', 'medical', 'cosmetology', 'echography', 'gynecology', 'promotion']:
			self.meta = 'procedure'
			self.meta_sp = 'Procedimiento'

		#elif self.name in ['topical', 'card']:
		elif self.name in ['topical', 'card', 'kit']:
			self.meta = 'product'
			self.meta_sp = 'Producto'

		elif self.name in ['other']:
			self.meta = 'other'
			self.meta_sp = 'Otros'

	# update_fields
