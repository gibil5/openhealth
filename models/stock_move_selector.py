
from openerp import models, fields, api




class StockMoveSelector(models.Model):
	
	_name = 'stock.move.selector'

	_description = "Stock Move Selector"




	sms_active_id = fields.Integer(
			default=7,
		)




	name = fields.Char(

			'Name',

			required="0", 

			compute="_compute_name",
		)

	@api.multi
	#@api.depends('')

	def _compute_name(self):
		for record in self:
			record.name = 'SMS-' + str(record.id).zfill(8)





	product_id = fields.Many2one(
			
			'product.product',
			#'product.template',

			'Producto', 

			domain = [
						('type', '=', 'product'),
						('x_origin', '=', False),
					],


			required="0", 
		)


# ----------------------------------------------------------- Actions ------------------------------------------------------



	# Open Myself
	@api.multi 
	def open_stock_moves(self):



		#product_id = self.product_id 



		return {

			# Mandatory 
			'type': 'ir.actions.act_window',

			'name': 'Open Stock Moves',


			# Window action 
			'res_model': 'stock.move',

			#'res_id': treatment_id,


			# Views 
			#"views": [[False, "form"]],
			"views": [[False, "tree"]],

			#'view_mode': 'form',
			'view_mode': 'tree',
			

			'target': 'current',


			#'view_id': view_id,
			#'auto_search': False, 


			'flags': {
					'form': {'action_buttons': True, }
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
			},			




			"domain": 	[
							["product_id", "=", self.product_id.id], 
							#['state', '=', 'done'],
						],




			'context':   {}
		}
	# open_myself






