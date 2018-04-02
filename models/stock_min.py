# -*- coding: utf-8 -*-

from openerp import models, fields, api




class StockMin(models.Model):
	
	_name = 'openhealth.stock.min'

	_description = "Stock Min"

	#_order = 'product_id,date desc'

	#_inherit = 'stock.min'




	name = fields.Char(
		)

