# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Kardex(models.Model):

	#_inherit = 'openhealth.process'	
	
	_order = 'product'

	_name = 'openhealth.kardex'



	name = fields.Char(

			compute='_compute_name', 
		)


	@api.multi
	def _compute_name(self):

		for record in self:

			if record.product.x_name_short != False: 
				record.name = record.product.x_name_short






	stock_move_ids = fields.One2many(

			#'stock.move', 
			'openhealth.kardex.move', 

			'kardex_id', 
		)


	product = fields.Many2one(
			'product.product'
		)


# ----------------------------------------------------------- Generate ------------------------------------------------------

	# Generate 
	@api.multi 
	def generate_kardex(self):
		
		print 'jx'
		print 'Generate'

		self.remove_kardex()
		
		#res_id = self.create_kardex()

		self.update_kardex()






	# Remove 
	@api.multi 
	def remove_kardex(self):

		print 'jx'
		print 'Remove'

		self.stock_move_ids.unlink()






	# Update 
	@api.multi 
	def update_kardex(self):

		print 'jx'
		print 'Update'


		if self.product.name != False: 


			product_id = self.product.id 

			kardex_id = self.id 


			moves = self.env['stock.move'].search([

															('product_id', '=', product_id),			
															('state', '=', 'done'),			
				
													],
													#order='start_date desc',
													#limit=1,
													)
			print moves


			for move in moves: 
			
				print move.name
				print move.product_id
				print move.date
				print move.product_uom_qty


				ret = self.stock_move_ids.create({
																
																#'name': move.name,
																'name': move.picking_id.name,

																'product_id': move.product_id.id,

																'date': move.date,
																
																'product_uom_qty': move.product_uom_qty, 

																'kardex_id': kardex_id,


																'location_dest': move.location_dest_id.name, 

																'location': move.location_id.name, 


			#													'price_subtotal': line.price_subtotal,
			#													'x_date_created': line.create_date,
																#'move_id': self.x_kardex.id,
														})















	# Total 
	amount_total = fields.Float(
			
			'Total', 
			
			default='0', 

			compute='_compute_amount_total', 
		)


	@api.multi

	def _compute_amount_total(self):
				
		for record in self:		

			total = 0 

			for move in record.stock_move_ids: 

				#total = total + move.product_uom_qty 
				total = total + move.qty 


			record.amount_total = total


