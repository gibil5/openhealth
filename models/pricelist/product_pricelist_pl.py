# -*- coding: utf-8 -*-
"""
	Pricelist - Product

	Created: 			 1 Apr 2019
	Last mod: 			 8 Apr 2019
"""
from __future__ import print_function
from openerp import models, fields, api

from . import px_vars

class PriceListProduct(models.Model):
	"""
	Is Used by PL Container
	"""
	#_name = 'price_list.product'
	_description = 'Product'	
	_order = 'idx_int'
	
	_inherit = 'openhealth.product.pricelist'


# ---------------------------------------------- Fields - Chars -----------------------
	family = fields.Selection(
			selection=px_vars._family_list,
			required=True,
		)

	subfamily = fields.Selection(
			selection=px_vars._subfamily_list,
			required=True,
		)

	treatment = fields.Selection(
			selection=px_vars._treatment_list,
			required=True,
		)




# ---------------------------------------------- Fields - Chars -----------------------
	name = fields.Char(
			required=True,
		)

	name_short = fields.Char(
			required=True,
		)

	prefix = fields.Char(
			required=True,
		)

	idx = fields.Char(
			required=True,
		)

	code = fields.Char(
		)

	idx_int = fields.Integer(
			'Idx I',
		)

	time_stamp = fields.Char(
			required=False,
		)


# ---------------------------------------------- Fields - Categorized ---------
	
	manufacturer = fields.Selection(
			selection=px_vars._manufacturer_list,
			string='Manufacturer',
		)

	brand = fields.Selection(
			selection=px_vars._brand_list,		
			string='brand',
		)


	x_type = fields.Selection(
			selection=px_vars._type_list,
			required=True,
		)


	price_list = fields.Selection(
			selection=px_vars._price_list_list,
			string='Price list',
			default='2019',
			required=True,
		)


	zone = fields.Selection(
			selection=px_vars._zone_list,
			required=True,
		)

	pathology = fields.Selection(
			selection=px_vars._pathology_list,
			required=True,
		)

	level = fields.Selection(
			selection=px_vars._level_list,

			required=False,
		)

	sessions = fields.Selection(
			selection=px_vars._sessions_list,
			required=True,
		)

	time = fields.Selection(
			selection=px_vars._time_list,
			required=False,
		)


# ---------------------------------------------- Fields - Floats -----------------------
	price = fields.Float()

	price_vip = fields.Float()

	price_company = fields.Float()

	price_session = fields.Float()

	price_session_next = fields.Float()

	price_max = fields.Float()




# ----------------------------------------------------------- Update ----------------------------------------------------
	@api.multi
	def update(self):
		"""
		Update
		"""
		print('Product Pricelist - Update')
		self.idx_int = int(self.idx)
		print(self.name)
		print(self.idx)
		print(self.idx_int)



# ----------------------------------------------------------- Handle ------------------------------

	# Used by Container
	#container_id = fields.Many2one(		
	#		'price_list.container',
	#		ondelete='cascade',
	#	)

