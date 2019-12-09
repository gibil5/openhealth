# 9 Dec 2019

	# Family 
	family = fields.Selection(
			string = "Familia - 9 Dec", 	
			selection = [
							('credit_note',	'Notas de Credito'),

							('other',	'Otros'), 
							('topical',	'Cremas'), 
							('card',	'Tarjeta'), 
							('kit',		'Kit'), 
							('product',	'Producto'), 
							('consultation',		'Consulta'), 
							('consultation_gyn',	'Consulta Ginecológica'), 
							('consultation_100',	'Consulta 100'), 
							('consultation_0',		'Consulta Gratuita'), 
							('procedure',	'Procedimiento'), 
							('laser',		'Laser'), 							
							('cosmetology',	'Cosmiatría'), 
							('medical',		'Tratamiento Médico'), 
			], 
			#required=False, 
			required=True, 
		)





# ----------------------------------------------------------- Actions - Dep !!! ------------------------------------------------------
	
	# Update Fields
	@api.multi
	def update_fields(self):
		print()
		print('2018 - Update Fields - Order')


		# If Product 
		if self.product_id.type in ['product','consu']: 	# Products and Consumables 
			# Family 
			if self.product_id.x_family in ['kit']: 	# Kits 
				self.family = 'topical'
			else: 										# Vip and Topical 
				self.family = self.product_id.x_family
			# Sub family
			self.sub_family = 'product'


		# If Service 
		else: 
			# Family 
			self.family = self.product_id.x_family

			# Correct 
			if (self.product_id.x_family  == 'consultation'): 
				if self.price_unit  == 100: 
					self.family = 'consultation_100'			
				elif self.price_unit  == 0: 
					self.family = 'consultation_0'

			# Sub family 
			# Cosmetology 
			if self.product_id.x_family == 'cosmetology': 
				self.sub_family = 'cosmetology'

			# Medical, Other 
			else: 
				self.sub_family = self.product_id.x_treatment 

	# update_fields









