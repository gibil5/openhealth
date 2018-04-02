# -*- coding: utf-8 -*-

from openerp import models, fields, api




class InventoryLine(models.Model):
	
	_inherit = 'openhealth.stock.min'

	_name = 'openhealth.stock.min.inventory.line'

	_description = "Stock Min Inventory Line"


	_order = 'code asc'






	categ = fields.Selection(

			[
				('topical', 	'Cremas'),		
				('consumable', 	'Consumible'),		
			],

			default='consumable', 
		)





	state = fields.Selection(
		
			[
				('draft', 	'Draft'),		
				('done', 	'Done'),		
			],

			default='draft', 
		)


	product_id = fields.Many2one(
			'product.template', 
		)




	name = fields.Char(
		)

	#date = fields.Datetime(
	#		string="Fecha", 
	#	)



	code = fields.Char(
		)

	description = fields.Char(
		)

	qty = fields.Float(
		)

	units = fields.Char(
		)



	inventory_id = fields.Many2one(
		'openhealth.stock.min.inventory', 
		#string='Order Reference', 		
		#required=False, 
		ondelete='cascade', 
		#index=True, 
		#copy=False
	)


