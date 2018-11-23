# -*- coding: utf-8 -*-

from openerp import models, fields, api



class StockMoveSelector(models.Model):	
	_name = 'stock.move.selector'
	_description = "Stock Move Selector"


	# ----------------------------------------------------------- Primitives ------------------------------------------------------
	
	# Name 
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


	# Product 
	product_id = fields.Many2one(			
			'product.product',
			'Producto', 
			required=True, 
			domain = [
						('type', '=', 'product'),
						('x_origin', '=', False),
						('sale_ok', '=', True),
					],
		)


	sms_active_id = fields.Integer(
			default=7,
		)


	# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Create Kardex 
	@api.multi 
	def create_kardex(self):

		# Init 
		context = self._context.copy()
		location = context['location']
		product_name = self.product_id.name
		product_id = self.product_id.id
			
		kardex = self.env['openhealth.kardex'].search([
														('product', '=', product_name),			
														('location', '=', location),
												],
												#order='start_date desc',
												limit=1,
												)
		# Search 
		if kardex.name == False: 
			kardex = self.env['openhealth.kardex'].create({
															'product': product_id, 
															'location': location, 
														})

		# Generate 
		kardex.generate_kardex()
		kardex_id = kardex.id

		return {
			'type': 'ir.actions.act_window',
			'name': 'Open Kardex',
			'res_model': 'openhealth.kardex',
			'res_id': kardex_id,
			# Views 
			"views": [[False, "form"]],
			#"views": [[False, "tree"]],
			'view_mode': 'form',
			#'view_mode': 'tree',
			'target': 'current',
			#'view_id': view_id,
			#'auto_search': False, 
			'flags': {
						'form': {'action_buttons': True, }
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
			},			
			#"domain": [
			#			["product_id", "=", self.product_id.id], 
						#['state', '=', 'done'],
			#		],

			'context':   {}
		}
	# create_kardex




#
# 		*** Stock Move Selector Consu   
# 
class StockMoveSelectorConsu(models.Model):	
	_inherit = 'stock.move.selector'
	_name = 'stock.move.selector.consu'
	_description = 'Stock Move Selector consu'
	#_order = 'write_date desc'


	product_id = fields.Many2one(
			'product.product',
			'Producto', 
			domain = [
						('type', '=', 'product'),
						('x_origin', '=', False),
						('sale_ok', '=', False),
						('categ_id', '=', 'Consumibles'),
					],
			required=True, 
		)


#
# 		Stock Move Selector Cremas   
#
class StockMoveSelectorCremas(models.Model):	
	_inherit = 'stock.move.selector'
	_name = 'stock.move.selector.cremas'
	_description = 'Stock Move Selector Cremas'
	#_order = 'write_date desc'


	product_id = fields.Many2one(
			'product.product',
			'Producto', 
			domain = [
						('type', '=', 'product'),
						('x_origin', '=', False),
						('sale_ok', '=', True),
						('categ_id', '=', 'Cremas'),						
					],
			required=True, 
		)

