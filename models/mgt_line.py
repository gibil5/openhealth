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
	#_order = 'amount desc'
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
			'Family',
		)

	meta_sp = fields.Char(
			'Familia',
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
	def update_fields(self):  

		#print 
		#print 'Update fields - Mgt Line'
		#print 

		if self.name in mgt_vars._h_name: 
			self.name_sp = mgt_vars._h_name[self.name]
		else: 
			self.name_sp = self.name




	#----------------------------------------------------------- Quick Button ------------------------------------------------------------

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




# ----------------------------------------------------------- Family ------------------------------------------------------
class FamilyLine(models.Model):	

	_inherit = 'openhealth.management.line'
	
	#_name = 'openhealth.management.family.line'
	_name = 'openhealth.management.family.line'
	
	#_order = 'idx asc'


	#doctor_id = fields.Many2one(
	#		'openhealth.management.doctor.line'
	#	)




	# Update Fields
	@api.multi
	def update_fields(self):  

		#print 
		#print 'Update fields - Mgt Line - Family'
		#print 


		_h_idx = {

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



		# Name sp 
		if self.name in mgt_vars._h_name: 
			self.name_sp = mgt_vars._h_name[self.name]
		else: 
			self.name_sp = self.name


		# Idx 
		self.idx = _h_idx[self.name]




		# Meta 
		if self.name in ['consultation', 'consultation_gyn', 'consultation_0', 'consultation_100']: 

			self.meta = 'consultation'
			self.meta_sp = 'Consulta'


		elif self.name in ['laser', 'medical', 'cosmetology']: 

			self.meta = 'procedure'
			self.meta_sp = 'Procedimiento'


		elif self.name in ['topical', 'card']: 

			self.meta = 'product'
			self.meta_sp = 'Producto'







# ----------------------------------------------------------- Subfamily ------------------------------------------------------
class SubFamilyLine(models.Model):	

	_inherit = 'openhealth.management.line'
	
	#_name = 'openhealth.management.sub_family.line'
	_name = 'openhealth.management.sub_family.line'
	
	#_order = 'idx asc'


	#doctor_id = fields.Many2one(
	#		'openhealth.management.doctor.line'
	#	)



