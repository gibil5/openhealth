# -*- coding: utf-8 -*-
"""
 		*** Product Min

 		Created: 			 07 Mar 2019
		Last up: 	 		 07 Mar 2019
"""
from __future__ import print_function
from openerp.exceptions import ValidationError
from openerp import models, fields, api

class ProductMin(models.Model):
	"""
	high level support for doing this and that.
	"""

	# DB constraints for:
	# Prices
	_sql_constraints = [
				#('price', 'Check(price!=0)', 'SQL Warning: price diff zero !'),
				#('x_serial_nr','unique(x_serial_nr)', 'SQL Warning: x_serial_nr must be unique !'),
				#('x_serial_nr', 'Check(1=1)', 'SQL Warning: x_serial_nr must be unique !'),
			]



# ----------------------------------------------------------- Primitives ------------------------------
	_name = 'openhealth.product.min'


	_order = 'name'

	#_inherit = 'product.template'


	name = fields.Char(
			required=True,
		)

	code = fields.Char(
		)






	x_type = fields.Selection(
			[
				('service', 'Service'),
				('product', 'Product'),
			],
		)

	family = fields.Selection(
			[
				('topical', 'Topical'),

				('laser', 'Laser'),
			],
		)


	subfamily = fields.Selection(
			[
				('chavarri', 'Chavarri'),
				('commercial', 'Commercial'),

				('co2', 'co2'),
				('excilite', 'excilite'),
				('quick', 'quick'),
				('m22', 'm22'),
			],
		)




	manufacturer = fields.Selection(
			[
				('CLINICA CHAVARRI', 	'CLINICA CHAVARRI'),
				('HILDA', 				'HILDA'),
				('LA COOPER', 			'LA COOPER'),
				('ELIAS OCHANTE', 		'ELIAS OCHANTE'),
				('BOTICA FRANCESA', 	'BOTICA FRANCESA'),
				('BOTICA VILLEGAS', 	'BOTICA VILLEGAS'),
				('BOTICA SANTA TERESA', 'BOTICA SANTA TERESA'),
				('EURODERMA', 			'EURODERMA'),
				('MEDISCIENCE', 		'MEDISCIENCE'),
				('JEUNESSE', 			'JEUNESSE'),
				('DROGUERIA ZOMAX', 	'DROGUERIA ZOMAX'),
				('AKRON', 				'AKRON'),
				#('chavarri', 'Chavarri'),
			],
		)

	brand = fields.Selection(
			[
				('CLINICA CHAVARRI', 	'CLINICA CHAVARRI'),
				('BOTICA SANTA TERESA', 'BOTICA SANTA TERESA'),
				('EURODERMA', 			'EURODERMA'),
				('MEDISCIENCE', 		'MEDISCIENCE'),
				('JEUNESSE', 			'JEUNESSE'),
				('DROGUERIA ZOMAX', 	'DROGUERIA ZOMAX'),
				('AKRON', 				'AKRON'),
			],
		)


	new = fields.Boolean(
		)



# ----------------------------------------------------------- Lasers ------------------------------

	treatment = fields.Selection(
			[
				('LASER CO2 FRACCIONAL', 				'LASER CO2 FRACCIONAL'),
				('QUICKLASER', 				'QUICKLASER'),
				('LASER EXCILITE', 				'LASER EXCILITE'),
				('LASER M22 IPL', 				'LASER M22 IPL'),
				('LASER M22 ND YAG', 				'LASER M22 ND YAG'),
			],
		)
	zone = fields.Selection(
			[
				('Todo Rostro', 		'Todo Rostro'),
				('Pomulos', 			'Pomulos'),
				('Cuello', 				'Cuello'),
				('Manos', 				'Manos'),
				('Localizado Rostro', 	'Localizado Rostro'),
				('Localizado Cuerpo', 	'Localizado Cuerpo'),
				('Vagina', 				'Vagina'),
				#('AKRON', 				'AKRON'),
			],
		)

	pathology = fields.Selection(

			[
				('Rejuvenecimiento Facial', 	'Rejuvenecimiento Facial'),
				('Acne y Secuelas', 			'Acne y Secuelas'),
				('Manchas', 					'Manchas'),
				('Rejuvenecimiento Cuello', 	'Rejuvenecimiento Cuello'),
				('Rejuvenecimiento Manos', 		'Rejuvenecimiento Manos'),
				('Manchas', 					'Manchas'),
				('Queratosis', 					'Queratosis'),
				('Lunar', 						'Lunar'),
				('Quiste', 						'Quiste'),
				('Verruga', 					'Verruga'),
				('Cicatriz', 					'Cicatriz'),
				('Tatuaje', 					'Tatuaje'),
				('Lunares Congenitos', 			'Lunares Congenitos'),
			],
		)




	level = fields.Selection(
			[
				#('1', 				'1'),
				#('2', 				'2'),
				#('3', 				'3'),
				#('4', 				'4'),
				#('5', 				'5'),

				('Grado 1', 		'Grado 1'),
				('Grado 2', 		'Grado 2'),
				('Grado 3', 		'Grado 3'),
				('Grado 4', 		'Grado 4'),
				('Grado 5', 		'Grado 5'),
			],
		)



	sessions = fields.Selection(
			[
				#('1', 				'1'),
				#('5', 				'5'),
				#('6', 				'6'),

				('1 sesion', 				'1 sesion'),
				('5 sesiones', 				'5 sesiones'),
				('6 sesiones', 				'6 sesiones'),
			],
		)


	time = fields.Selection(
			[
				('2 min', 				'2 min'),
				('5 min', 				'5 min'),
				('15 min', 				'15 min'),
				('30 min', 				'30 min'),
			],
		)




# ----------------------------------------------------------- Prices ------------------------------

	price = fields.Float(
			required=True,
			default=-1,
		)

	price_company = fields.Float(
			required=True,
			default=-1,
		)

	price_vip = fields.Float(
			#required=True,
			#default=-1,
		)





# ----------------------------------------------------------- Prices - Constraints ------
	# Check price
	@api.constrains('price')
	def _check_price(self):
		self.check_price()

	# Check price - Uniqueness
	def check_price(self):

		# Loop 
		for record in self:

			# Content 
			if record.price in [0, -1]:
				raise ValidationError("Check Warning: Price not valid: %s" % record.price)

		# all records passed the test, don't return anything




	# Check price_company
	@api.constrains('price_company')
	def _check_price_company(self):
		self.check_price_company()


	# Check price_company - Uniqueness
	def check_price_company(self):

		# Loop 
		for record in self:

			# Content 
			#if record.price_company in [0, -1]:
			if record.price_company in [-1]:
				raise ValidationError("Check Warning: price_company not valid: %s" % record.price_company)

		# all records passed the test, don't return anything





