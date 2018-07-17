# -*- coding: utf-8 -*-
#
#
# 	Management Order Line 
# 

from openerp import models, fields, api


#import openerp.addons.decimal_precision as dp
import ord_vars
import prodvars


class management_order_line(models.Model):



	_inherit='openhealth.line'

	_name = 'openhealth.management.order.line'

	_description = "Openhealth Management Order Line"





# ----------------------------------------------------------- Inheritable ------------------------------------------------------

	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient', 
			string="Paciente", 
		)


	# Doctor 
	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
		)




	# Serial Number 
	serial_nr = fields.Char(
			'Serial Nr',
		)


	# Delta 
	delta = fields.Integer(
			'Delta',
		)






	# Family 
	family = fields.Selection(

			string = "Familia", 	

			selection = [
							# 13 Jul 2018 
							('other',	'Otros'), 


							('topical',	'Cremas'), 
							('card',	'Tarjeta'), 
							('kit',		'Kit'), 
							('product',	'Producto'), 


							('consultation',		'Consulta'), 
							('consultation_gyn',	'Consulta Ginecológica'), 
							('consultation_100',	'Consulta 100'), 
							('consultation_0',		'Consulta Gratuita'), 
							#('consultation',		'consultation'), 
							#('consultation_gyn',	'consultation_gyn'), 
							#('consultation_100',	'consultation_100'), 
							#('consultation_0',		'consultation_0'), 


							('procedure',	'Procedimiento'), 
							('laser',		'Laser'), 
							
							('cosmetology',	'Cosmiatría'), 

							('medical',		'Tratamiento Médico'), 
			], 

			required=False, 
		)




	# Sub Family
	#sub_family = fields.Selection(
	sub_family = fields.Char(

			string = "Sub-familia",

			selection=prodvars._treatment_list,

			required=False,
		)	






	# State 
	state = fields.Selection(
			selection = ord_vars._state_list, 
			string='Estado',	
			readonly=False,
			default='draft',
		)



# ----------------------------------------------------------- Handles ------------------------------------------------------
	
	# Doctor 
	doctor_id = fields.Many2one(			

			'openhealth.management.doctor.line',
		
			ondelete='cascade', 			
		)





	# Management 
	management_id = fields.Many2one(			
			
			'openhealth.management',

			ondelete='cascade', 			
		)



	# Sales TKR
	management_tkr_id = fields.Many2one(			
			
			'openhealth.management',

			ondelete='cascade', 			
		)




# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update Fields
	@api.multi
	def update_fields(self):  

		#print 
		#print 'Update Fields - Order'
		#print 


		# Set Family and Sub Family 

		#_h_family = {
						#'laser': 			'procedure', 		
		#				'laser': 			'laser', 		
					
		#				'medical': 			'medical', 		
		#				'consultation': 	'consultation', 		
		#				'cosmetology': 		'cosmetology', 	
		#				False: False, 	
		#}




		# If Product 
		if self.product_id.type in ['product','consu']: 	# Products and Consumables 

			# Family 
			if self.product_id.x_family in ['kit']: 	# Kits 
				self.family = 'topical'
			else: 										# Vip and Topical 
				self.family = self.product_id.x_family


			#if self.family == False: 			# Error Condition 
			#	print 
			#	print 'Gotcha !'
			#	print self.product_id.name 
			#	print self.product_id.x_family
			#	print 


			# Sub family
			self.sub_family = 'product'




		# If Service 
		else: 

			# Family 
			self.family = self.product_id.x_family



			# Correct 
			if (self.product_id.x_family  == 'consultation'): 

				if self.price_unit  == 100: 
					#print 'Gotcha 1 !'
					#print self.product_id.name 
					#print self.price_unit
					#print 
					self.family = 'consultation_100'
			
				elif self.price_unit  == 0: 
					#print 'Gotcha 2 !'
					#print self.product_id.name 
					#print self.price_unit
					#print 
					self.family = 'consultation_0'





			# Sub family 
			# Cosmetology 
			if self.product_id.x_family == 'cosmetology': 

				self.sub_family = 'cosmetology'




			# Medical, Other 
			else: 
				self.sub_family = self.product_id.x_treatment 




			# Laser 
			#else: 
			#	if self.product_id.x_treatment in self._h_subfamily:
			#		self.sub_family = self._h_subfamily[self.product_id.x_treatment]
			#	else: 
			#		self.sub_family = self.product_id.x_treatment 


	# update_fields


