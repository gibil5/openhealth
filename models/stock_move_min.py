# -*- coding: utf-8 -*-

from openerp import models, fields, api




class StockMoveMin(models.Model):
	
	_name = 'stock.move.min'

	_description = "Stock Move Min"

	_order = 'product_id'





	name = fields.Char(
			string='Name',
		)





	stock_move_all_id = fields.Many2one(
		'stock.move.all', 
	)








	product_id = fields.Many2one(
			'product.product', 
			
			'Product', 
			#required=True, 
			select=True, 
			domain=[('type', 'in', ['product', 'consu'])], 
			#states={'done': [('readonly', True)]}
		)



	date = fields.Datetime(
			string="Date", 
		)


	picking = fields.Char(
			string="Reference", 
		)



	qty = fields.Float(
			string="Qty", 
		)




	source = fields.Char(
			'Source', 
		)

	destination = fields.Char(
			'Destination', 
		)



