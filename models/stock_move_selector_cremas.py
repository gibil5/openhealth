# -*- coding: utf-8 -*-
#
#
# 		*** Stock Move Selector Cremas   
# 
#

from openerp import models, fields, api



class StockMoveSelectorCremas(models.Model):
	
	_inherit = 'stock.move.selector'

	_name = 'stock.move.selector.cremas'

	_description = 'Stock Move Selector Cremas'

	#_order = 'write_date desc'




	product_id = fields.Many2one(
			'product.product',
			#'product.template',

			'Producto', 

			domain = [
						('type', '=', 'product'),
						('x_origin', '=', False),
						('sale_ok', '=', True),

						#('categ_id', '=', 'Consumibles'),						
						('categ_id', '=', 'Cremas'),						
					],



			required=True, 
		)

