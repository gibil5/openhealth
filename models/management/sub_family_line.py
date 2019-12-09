# -*- coding: utf-8 -*-
"""
	Sub Family Line 

	Only Data model. No functions.

	Created: 			20 Aug 2018
	Last up: 			 9 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api
from . import mgt_vars

class SubFamilyLine(models.Model):	
	"""
	Sub Family Line
	"""
	#_inherit = 'openhealth.management.line'  	# Dep
	
	_name = 'openhealth.management.sub_family.line'
	
	_order = 'amount desc'



# ----------------------------------------------------------- Relational --------------------------
	management_id = fields.Many2one(
			'openhealth.management',
			#ondelete='cascade',
		)

	doctor_id = fields.Many2one(
			'openhealth.management.doctor.line',
			ondelete='cascade',
		)


# ----------------------------------------------------------- Fields ---------------------------
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
			#digits=(16, 1),
		)


	per_nr = fields.Float(
			'% Nr',
		)




#----------------------------------------------------------- Open Line Current --------------------
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
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				'context': {}
		}
	# open_line_current

