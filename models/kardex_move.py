# -*- coding: utf-8 -*-

from openerp import models, fields, api




class KardexMove(models.Model):
	
	#_inherit = 'stock.move'

	_description = "Kardex Move"

	_name = "openhealth.kardex.move"



	name = fields.Char(
		)


	kardex_id = fields.Many2one(
			'openhealth.kardex', 
		)




	date = fields.Datetime(
			'Date', 
			required=True, 
			#select=True, 
			#help="Move date: scheduled date until move is done, then date of actual move processing", 
			#states={'done': [('readonly', True)]}
		)
	

	product_id = fields.Many2one(
			'product.product', 
			'Product', 
			required=True, 
			#select=True, 

			#domain=[('type', 'in', ['product', 'consu'])], 
			domain=[('type', 'in', ['product'])], 
			
			#states={'done': [('readonly', True)]}
		)
	


	product_uom_qty = fields.Float(
			'Quantity', 
			#digits_compute=dp.get_precision('Product Unit of Measure'),
			required=True, 
			#states={'done': [('readonly', True)]},
		)

	
