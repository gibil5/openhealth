# -*- coding: utf-8 -*-
"""
# 	Management Line
#
# Created: 				18 May 2018
"""
from openerp import models, fields, api

class ManagementLine(models.Model):
	"""
	high level support for doing this and that.
	"""

	_name = 'openhealth.management.line'



	_order = 'idx asc'



#----------------------------------------------------------- Dep - Update -------------------------
	# Update Fields
	#def update(self):
		#print
		#print 'Update fields - Mgt Line'
	#	if self.name in mgt_vars._h_name:
	#		self.name_sp = mgt_vars._h_name[self.name]
	#	else:
	#		self.name_sp = self.name
	# update



# ----------------------------------------------------------- Relational --------------------------

	management_id = fields.Many2one(
			'openhealth.management',

			#ondelete='cascade',
		)

	doctor_id = fields.Many2one(
			'openhealth.management.doctor.line',

			ondelete='cascade',
		)


# ----------------------------------------------------------- Primitive ---------------------------

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
			#digits=(16, 1),
		)

	per_nr = fields.Float(
			'% Nr',
		)




#----------------------------------------------------------- Open Line Current --------------------
	@api.multi
	def open_line_current(self):
		"""
		high level support for doing this and that.
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
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				'context': {}
		}
	# open_line_current
