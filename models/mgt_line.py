# -*- coding: utf-8 -*-
#
# 	Management Line 
# 
# Created: 				18 May 2018
#

from openerp import models, fields, api

import mgt_vars



class ManagementLine(models.Model):
	
	#_inherit = 'openhealth.management.line'

	_name = 'openhealth.management.line'

	#_order = 'x_count desc'
	_order = 'amount desc'



	# ----------------------------------------------------------- Relational ------------------------------------------------------

	management_id = fields.Many2one(
			'openhealth.management'
		)




	# ----------------------------------------------------------- Primitive ------------------------------------------------------
	name = fields.Char(
			'Name',
		)

	name_sp = fields.Char(
			'Nombre',
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
	def update_fields(self):  

		if self.name in mgt_vars._h_name: 
			self.name_sp = mgt_vars._h_name[self.name]
		else: 
			self.name_sp = self.name




	#----------------------------------------------------------- Quick Button ------------------------------------------------------------

	# For quick access
	@api.multi
	def open_line_current(self):  

		#consultation_id = self.id 
		res_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Order Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,

				#'res_id': consultation_id,
				'res_id': res_id,
				
				'target': 'current',
				'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				'context': {}
		}




# ----------------------------------------------------------- Family ------------------------------------------------------
class FamilyLine(models.Model):	

	_inherit = 'openhealth.management.line'
	
	#_name = 'openhealth.management.family.line'
	_name = 'openhealth.management.family.line'
	
	#_order = 'idx asc'


	doctor_id = fields.Many2one(
			'openhealth.management.doctor.line'
		)




# ----------------------------------------------------------- Subfamily ------------------------------------------------------
class SubFamilyLine(models.Model):	

	_inherit = 'openhealth.management.line'
	
	#_name = 'openhealth.management.sub_family.line'
	_name = 'openhealth.management.sub_family.line'
	
	#_order = 'idx asc'


	doctor_id = fields.Many2one(
			'openhealth.management.doctor.line'
		)



