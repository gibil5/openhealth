# -*- coding: utf-8 -*-
"""
	Price Line - Openhealth

	Created: 			 1 Apr 2019
	Last mod: 			11 Aug 2020
"""
from __future__ import print_function
from openerp import models, fields, api

class CartLine(models.Model):
	"""
	Cart line class
	"""
	_name = 'price_list.cart_line'
	_description = 'Cart Line'

# ---------------------------------------------- Fields - Chars ----------------
	name = fields.Char(
			#required=True,
		)
		
	price = fields.Float(
			#required=True,
		)

	qty = fields.Integer(
			#required=True,
		)

# ----------------------------------------------------------- Product ----------
	product = fields.Many2one(		
		#'product.template',
		'product.product',
		string='Product',
		domain=[
					#('sale_ok', '=', True),
					#('pl_price_list', '=', '2019'),
				],
		#change_default=True,
		#ondelete='restrict',
		#required=True,
		required=False,
	)

	# Treatment
	treatment = fields.Many2one(
			'openhealth.treatment',
			ondelete='cascade',
			string="Tratamiento",
		)
