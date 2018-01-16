# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Kardex(models.Model):

	#_inherit = 'openhealth.process'	
	#_order = 'write_date desc'

	_name = 'openhealth.kardex'



	name = fields.Char(
		)


	stock_move_ids = fields.One2many(

			#'stock.move', 
			'openhealth.kardex.move', 

			'kardex_id', 
		)






	# Total 
	amount_total = fields.Float(
			'Total S/.', 
			default='0', 

			compute='_compute_amount_total', 
		)


	@api.multi

	def _compute_amount_total(self):
				
		for record in self:		

			total = 0 

			for move in record.stock_move_ids: 

				total = total + move.product_uom_qty 

			record.amount_total = total


