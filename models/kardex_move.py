# -*- coding: utf-8 -*-

from openerp import models, fields, api




class KardexMove(models.Model):
	
	#_inherit = 'stock.move'

	_description = "Kardex Move"

	_name = "openhealth.kardex.move"





	location_dest = fields.Char(
		)


	location = fields.Char(
		)






	coeff = fields.Float(

			default="1", 
			
			compute='_compute_coeff', 
		)


	@api.multi
	def _compute_coeff(self):

		for record in self:


			if record.name != False:

				#if 'OUT' in record.name: 
				if 'OUT' in record.name  	or   'INT' in record.name: 
					record.coeff = -1

				else:
					record.coeff = 1


			elif record.location == 'Inventory loss' and record.location_dest == 'General': 
				record.coeff = 1

			elif record.location == 'General' and record.location_dest == 'Inventory loss': 
				record.coeff = -1






	qty = fields.Float(
			'Quantity', 

			compute='_compute_qty', 
		)

	@api.multi
	def _compute_qty(self):

		for record in self:

			record.qty = record.product_uom_qty * record.coeff








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

	
