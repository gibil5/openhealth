# -*- coding: utf-8 -*-
#
# 	Management Line 
# 
# Created: 				18 May 2018
#
from openerp import models, fields, api
from . import mgt_vars

class ManagementLine(models.Model):

	_name = 'openhealth.management.line'

	_order = 'idx asc'



	# ----------------------------------------------------------- Relational ------------------------------------------------------

	management_id = fields.Many2one(
			'openhealth.management'
		)

	doctor_id = fields.Many2one(
			'openhealth.management.doctor.line'
		)


	# ----------------------------------------------------------- Primitive ------------------------------------------------------
	
	name = fields.Char(
			'Name',
		)

	name_sp = fields.Char(
			'Nombre',
		)

	meta = fields.Char(
			#'Family',
			'Meta',
		)

	meta_sp = fields.Char(
			#'Familia',
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
			digits=(16,1), 
		)



	#----------------------------------------------------------- Actions ------------------------------------------------------------

	# Update Fields
	@api.multi
	#def update_fields(self):  
	def update(self):  

		#print 
		#print 'Update fields - Mgt Line'
		#print 
		if self.name in mgt_vars._h_name: 
			self.name_sp = mgt_vars._h_name[self.name]
		else: 
			self.name_sp = self.name
	# update_fields



	#----------------------------------------------------------- Open Line Current ------------------------------------------------------------

	# For quick access
	@api.multi
	def open_line_current(self):  

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
