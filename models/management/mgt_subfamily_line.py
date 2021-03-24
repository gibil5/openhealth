# -*- coding: utf-8 -*-
"""
	Sub Family Line 

	Created: 			20 Aug 2018
	Last up: 			24 mar 2021
"""
from __future__ import print_function
from openerp import models, fields, api
from . import mgt_vars

class MgtSubfamilyLine(models.Model):	
	"""
	Subfamily Line
	"""	
	_name = 'openhealth.management.sub_family.line'
	_order = 'amount desc'


# ----------------------------------------------------------- Relational -------
	management_id = fields.Many2one(
			'openhealth.management',
			#ondelete='cascade',
		)

	doctor_id = fields.Many2one(
			'openhealth.management.doctor.line',
			ondelete='cascade',
		)

# ----------------------------------------------------------- Fields -----------
	name = fields.Char(
			'Name',
			required=True,
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


# ----------------------------------------------------------- Update -----------
	def update(self):  
		#print()
		#print('X - Update - Sub Family')

		# Idx 
		_h_idx = {
					False: 0, 		
					'laser_co2': 			10,
					'laser_excilite': 		11,
					'laser_ipl': 			12,
					'laser_ndyag': 			13,
					'laser_quick': 			14,
					'criosurgery' : 	31, 		
					'botulinum_toxin' : 32, 		
					'hyaluronic_acid' : 33, 		
					'cosmetology': 		70,
					'product': 			80, 	
					'consultation': 	90, 		
		}

		# Medical 
		medical_arr = [
							'botulinum_toxin', 		# Bot
							'criosurgery', 			# Crio
							'hyaluronic_acid', 		# Hial
							'infiltration_scar', 	# Infil
							'infiltration_keloid', 	# Infil
							'intravenous_vitamin', 		# Intra
							'lepismatic', 				# Lep
							'plasma', 				# Pla
							'mesotherapy_nctf', 	# Meso
							'sclerotherapy', 		# Escl
		]

		# Idx
		if self.name in _h_idx: 
			self.idx = _h_idx[self.name]
		else: 
			self.idx = 100

		# Meta 
		if self.name in ['laser_co2', 'laser_excilite', 'laser_ipl', 'laser_ndyag', 'laser_quick']:
			self.meta = 'laser'
			self.meta_sp = 'Laser'

		elif self.name in medical_arr:
			self.meta = 'medical'
			self.meta_sp = 'TM'

		elif self.name in ['cosmetology']:
			self.meta = 'cosmetology'
			self.meta_sp = 'Cosmiatria'

		elif self.name in ['consultation']:
			self.meta = 'consultation'
			self.meta_sp = 'Consulta'

		elif self.name in ['product']:
			self.meta = 'product'
			self.meta_sp = 'Producto'

		elif self.name in ['other']:
			self.meta = 'other'
			self.meta_sp = 'Otros'
	# update

#----------------------------------------------------------- Method ------------
	@api.multi
	def open_line_current(self):
		"""
		Open line current
		"""
		res_id = self.id
		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Subfamily Current',
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

