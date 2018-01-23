# -*- coding: utf-8 -*-
#
#
# 		*** Stock Move Selector Consu   
# 
#

from openerp import models, fields, api



class StockMoveSelectorConsu(models.Model):
	
	_inherit = 'stock.move.selector'

	_name = 'stock.move.selector.consu'

	_description = 'Stock Move Selector consu'

	#_order = 'write_date desc'




	product_id = fields.Many2one(
			'product.product',
			#'product.template',

			'Producto', 

			domain = [
						('type', '=', 'product'),
						('x_origin', '=', False),
						
						('sale_ok', '=', False),

						('categ_id', '=', 'Consumibles'),						
						#('categ_id', '=', 'Cremas'),						
					],



			required=True, 
		)
