# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Kardex(models.Model):

	#_inherit = 'openhealth.process'	
	_order = 'product'
	_name = 'openhealth.kardex'






	# Location 
	location = fields.Selection(
			[	
				('all', 			'Todo'),

				('general', 		'General'),
				('platform', 		'Plataforma'),
				('laser_2', 		'Laser 2'),
			], 
		)



	# Stock Move Ids
	stock_move_ids = fields.One2many(

			'openhealth.kardex.move', 

			'kardex_id', 
		)
















	# Name 
	name = fields.Char(

			compute='_compute_name', 
		)


	@api.multi
	def _compute_name(self):

		for record in self:

			if record.product.x_name_short != False: 
				record.name = record.product.x_name_short








	product = fields.Many2one(
			'product.product', 
			'Producto', 
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




			if self.location == 'platform':
	
				moves = self.env['stock.move'].search([
															('product_id', '=', product_id),			
															('state', '=', 'done'),		


															#('location_id', 'like', 'Cremas Despacho'),		
															#('location_id', '=', 'AL/General/Cremas Despacho'),		
														],
														#order='start_date desc',
														#limit=1,
														)



			elif self.location == 'general': 

				moves = self.env['stock.move'].search([
															('product_id', '=', product_id),			
															('state', '=', 'done'),		


															#('location_id', 'not like', 'Cremas Despacho'),		


															#('location_id', 'like', 'Cremas Despacho'),		
															#('location_id', '=', 'AL/General/Cremas Despacho'),		
															#('location_id', 'like', 'General'),		
															#('location_id', '=', 'General'),		
														],
														#order='start_date desc',
														#limit=1,
														)


			elif self.location == 'all': 

				moves = self.env['stock.move'].search([
															('product_id', '=', product_id),			
															('state', '=', 'done'),		
														],
														#order='start_date desc',
														#limit=1,
														)






			print moves


			for move in moves: 
			
				#print move.name
				#print move.product_id
				#print move.date
				#print move.product_uom_qty





				smove = self.stock_move_ids.create({
																
																#'name': move.name,
																'name': move.picking_id.name,

																'product_id': move.product_id.id,

																'date': move.date,
																
																'product_uom_qty': move.product_uom_qty, 

																'kardex_id': kardex_id,


																'location_dest': move.location_dest_id.name, 

																'location_source': move.location_id.name, 


																'location': self.location, 
														})

				if smove.coeff == 0:
					smove.unlink()












	# Total 
	amount_total = fields.Float(
			
			'Cantidad Total', 
			
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


