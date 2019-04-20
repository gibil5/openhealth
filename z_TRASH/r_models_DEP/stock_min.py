# -*- coding: utf-8 -*-
#

from openerp import models, fields, api
import stock_min_funcs  




class StockMin(models.Model):	
	_name = 'openhealth.stock.min'
	_description = "Stock Min"
	#_order = 'product_id,date desc'
	#_inherit = 'stock.min'

	name = fields.Char(
		)




class Inventory(models.Model):	
	_inherit = 'openhealth.stock.min'
	_name = 'openhealth.stock.min.inventory'
	_description = "Stock Min Inventory"
	#_order = 'product_id,date desc'



	# Primitives 
	name = fields.Char(
		)

	date = fields.Datetime(
			string="Fecha", 
		)

	author = fields.Many2one(
			'res.partner'
		)

	inventory_line = fields.One2many(
			'openhealth.stock.min.inventory.line', 
			'inventory_id',
		)



	#  Update 
	@api.multi
	def update_lines(self):  
		lines = self.env['openhealth.stock.min.inventory.line'].search([
																		('state', '=', 'draft'),
			
											],
												order='code asc',
												#limit=1,
											)
		for line in lines:
			line.inventory_id = self.id 
			line.product_id = stock_min_funcs.get_product_id(self, line.code, line.description, line.categ)






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
		ondelete='cascade', 
	)

