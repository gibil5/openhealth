# -*- coding: utf-8 -*-

from openerp import models, fields, api

import openerp.addons.decimal_precision as dp



class StockMove(models.Model):
	
	_inherit = 'stock.move'

	_description = "Stock Move"


	#_order = 'create_date desc'
	#_order = 'date desc'
	#_order = 'date_expected desc'

	#_name = "stock.move"
	#_description = "Stock Move"
	#_order = 'picking_id, sequence, id'





# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Corrected Quantity 
	x_qty = fields.Float(
	
			'Qty - Corr', 
			
			digits=(16, 0), 


			compute='_compute_x_qty', 
		)

	@api.multi

	def _compute_x_qty(self):
		
		#print 'jx'
		#print 'compute x_qty'

		for record in self:

			coeff = -1

			record.x_qty = record.product_uom_qty * coeff









	x_note = fields.Char()




	x_categ_id = fields.Many2one(
			'product.category',
			'Internal Category', 
			#required=True, 
			#change_default=True, 
			#domain="[('type','=','normal')]" ,
			#help="Select category for the current product"


			store=True, 
			compute='_compute_x_categ_id', 
		)



	#@api.multi
	#@api.depends('__last_update')
	#@api.depends('name')
	@api.depends('x_note')

	
	def _compute_x_categ_id(self):
		#print 'jx'
		#print 'compute x_categ_id'
		for record in self:
			record.x_categ_id = record.product_id.categ_id
			print record.x_categ_id  





	# Quantity 
	product_uom_qty = fields.Float(
			'Quantity', 
			
			#digits_compute=dp.get_precision('Product Unit of Measure'),
			digits=(16, 0), 

			required=True, 			
			states={'done': [('readonly', True)]},
			help="jx ", 
		)












	#'state': fields.selection([
	#								('draft', 'New'),
	#								('cancel', 'Cancelled'),
	#							   	('waiting', 'Waiting Another Move'),
	#							   	('confirmed', 'Waiting Availability'),
	#							   	('assigned', 'Available'),
	#							   	('done', 'Done'),
	#						], 
	#	'Status', readonly=True, select=True, copy=False,
	#	help= "* New: When the stock move is created and not yet confirmed.\n"\
	#				   "* Waiting Another Move: This state can be seen when a move is waiting for another one, for example in a chained flow.\n"\
	#				   "* Waiting Availability: This state is reached when the procurement resolution is not straight forward. It may need the scheduler to run, a component to me manufactured...\n"\
	#				   "* Available: When products are reserved, it is set to \'Available\'.\n"\
	#				   "* Done: When the shipment is processed, the state is \'Done\'."
	#	),
