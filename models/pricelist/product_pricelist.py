# -*- coding: utf-8 -*-
"""
	Openhealth Product Pricelist

	Created: 			 2 Sep 2019
	Last mod: 			 2 Sep 2019
"""
from __future__ import print_function
from openerp import models, fields, api

#class PriceListProduct(models.Model):
class ProductPricelist(models.Model):

	"""
	Used by Container Pricelist
	"""
	_name = 'openhealth.product.pricelist'
	
	_description = 'Openhealth Product Pricelist'
	
	#_order = 'idx_int'



# ----------------------------------------------------------- Handle ------------------------------
	
	#container_id = fields.Char()
	
	container_id = fields.Many2one(		
			'openhealth.container.pricelist',
			ondelete='cascade',
		)

