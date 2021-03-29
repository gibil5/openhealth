# -*- coding: utf-8 -*-
"""
 	Family Line 

	Created: 			20 Aug 2018
	Last up: 			24 mar 2021
"""
from __future__ import print_function
from openerp import models, fields, api

#from . import mgt_vars
from lib import mgt_vars


class MgtFamilyLine(models.Model):
	"""
    Family line
	"""
	_name = 'openhealth.management.family.line'
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
		if self.name in mgt_vars._h_name: 
			self.name_sp = mgt_vars._h_name[self.name]
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


# Begin ----------------------------------- Inherited from mgt_line.py ----------------------------

# ----------------------------------------------------------- Interface --------
	management_id = fields.Many2one(
			'openhealth.management',
		)

	doctor_id = fields.Many2one(
			'openhealth.management.doctor.line',
			ondelete='cascade',
		)

# ----------------------------------------------------------- Primitive --------
	name = fields.Char(
			'Name',
		)

	name_sp = fields.Char(
			'Nombre',
		)

	meta = fields.Char(
			'Meta',
		)

	meta_sp = fields.Char(
			'Meta',
		)

	idx = fields.Integer(
			'Idx',
		)

	x_count = fields.Integer(
			'Nr',
		)

	amount = fields.Float(
			'Monto',
			digits=(16, 1),
		)

	per_amo = fields.Float(
			'% Monto',
		)

	per_nr = fields.Float(
			'% Nr',
		)

#----------------------------------------------------------- Method ------------
	@api.multi
	def open_line_current(self):
		"""
		Open line current
		"""
		res_id = self.id
		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Order Current',
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': res_id,
				'target': 'current',
				'flags': {
						'form': {'action_buttons': True, }
						},
				'context': {}
		}
	# open_line_current

# End ----------------------------------- Inherited from mgt_line.py ------------------------------
