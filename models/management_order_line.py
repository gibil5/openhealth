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


	state = fields.Selection(
			selection = ord_vars._state_list, 
			string='Estado',	
			readonly=False,
			default='draft',
		)




	# Family 
	family = fields.Selection(

			string = "Familia", 	

			selection = [
							('product','Producto'), 

							('consultation','Consulta'), 
							
							('procedure','Procedimiento'), 
							
							('cosmetology','Cosmiatría'), 

							('medical','Tratamiento Médico'), 
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





# ----------------------------------------------------------- Actions ------------------------------------------------------

	_h_family = {
					'laser': 		'procedure', 		
					'medical': 		'medical', 		
					'consultation': 'consultation', 		
					'cosmetology': 'cosmetology', 	
					False: False, 	
	}






	# Update Fields
	@api.multi
	def update_fields(self):  


		# Product 
		#if self.product_id.type == 'product': 
		if self.product_id.type in ['product','consu']: 


			# Family 
			self.family = 'product'

			# Sub family
			#self.sub_family = self._h_subfamily['product']
			self.sub_family = 'product'



		# Service 
		else: 


			# Family 
			self.family = self._h_family[self.product_id.x_family]




			# Sub family 

			# Cosmetology 
			if self.product_id.x_family == 'cosmetology': 

				#self.sub_family = self._h_subfamily['cosmetology']
				self.sub_family = 'cosmetology'


			# Medical
			#elif self.product_id.x_family == 'medical': 
			else: 

				#self.sub_family = self._h_subfamily[self.product_id.x_treatment]
				self.sub_family = self.product_id.x_treatment 


			# Laser 
			#else: 
			#	if self.product_id.x_treatment in self._h_subfamily:
			#		self.sub_family = self._h_subfamily[self.product_id.x_treatment]
			#	else: 
			#		self.sub_family = self.product_id.x_treatment 




