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



		# Idx 
		_h_idx = {
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



		# Name sp 
		if self.name in mgt_vars._h_name: 
			self.name_sp = mgt_vars._h_name[self.name]
		else: 
			self.name_sp = self.name



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


		elif self.name in ['other']: 

			self.meta = 'other'
			self.meta_sp = 'Otros'








# ----------------------------------------------------------- Subfamily ------------------------------------------------------
class SubFamilyLine(models.Model):	

	_inherit = 'openhealth.management.line'
	
	#_name = 'openhealth.management.sub_family.line'
	_name = 'openhealth.management.sub_family.line'
	
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


		# Name Sp 
		if self.name in mgt_vars._h_name: 
			self.name_sp = mgt_vars._h_name[self.name]
		else: 
			self.name_sp = self.name



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


		#elif self.name in ['criosurgery', 'botulinum_toxin', 'hyaluronic_acid', '']: 
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





