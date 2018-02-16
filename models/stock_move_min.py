# -*- coding: utf-8 -*-

from openerp import models, fields, api




class StockMoveMin(models.Model):
	
	_name = 'stock.move.min'

	_description = "Stock Move Min"

	_order = 'product_id,date desc'





	name = fields.Char(
			string='Descripción',
		)



	x_type = fields.Selection(

			[	
				('topical', 		'Cremas'),
				('consumable', 		'Consumibles'),
			], 


			string='Tipo',
		)







	stock_move_all_id = fields.Many2one(
		'stock.move.all', 
	)



	product_id = fields.Many2one(
			'product.product', 
			
			'Producto', 

			#required=True, 
			select=True, 
			domain=[('type', 'in', ['product', 'consu'])], 
			#states={'done': [('readonly', True)]}
		)



	date = fields.Datetime(
			string="Fecha", 
		)


	picking = fields.Char(
			string="Referencia", 
		)



	qty = fields.Float(
			string="Cantidad", 
		)




	source = fields.Char(
			'Origen', 
		)

	destination = fields.Char(
			'Destino', 
		)



