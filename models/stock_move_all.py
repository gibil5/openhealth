# -*- coding: utf-8 -*-

from openerp import models, fields, api


class StockMoveAll(models.Model):
	
	_name = 'stock.move.all'

	_description = "Stock Move All"




# ----------------------------------------------------------- Primitives ------------------------------------------------------

	name = fields.Char(
			string='Nombre',
		)




	stock_moves = fields.Many2many(
			'stock.move.min',
			'stock_move_all_id', 
		)




	stock_move_min_ids = fields.One2many(
			'stock.move.min',
			'stock_move_all_id', 
		)



	product_id = fields.Many2one(
			'product.product', 
			
			'Producto', 

			#select=True, 
			domain=[
					
						('type', 'in', ['product', 'consu']), 

						('categ_id', '=', 'Cremas'), 

					], 
		)




	@api.onchange('product_id')
	
	def _onchange_product_id(self):

		print 'jx'
		print 'On change product_id'

		if self.product_id != False: 



				return {
							'domain': {'stock_move_min_ids': [
													
																#('type', '=', self.x_type),
																#('x_origin', '=', False),

																('product_id', '=', self.product_id.name),
									]},
				}





# ----------------------------------------------------------- Actions ------------------------------------------------------


	# Reset 
	@api.multi 
	def reset(self):

		print 'jx'
		print 'Reset'

		self.stock_move_min_ids.unlink()
		
		self.product_id = False 



		# Stock move mins 		
		stock_move_mins = self.env['stock.move.min'].search([
																#('state','=','done')
											],
												#order='write_date desc',
												#limit=1,
											)
		print stock_move_mins
		stock_move_mins.unlink()
		print stock_move_mins
		print









	# Create Kardex 
	@api.multi 
	def create_kardex(self):

		print 'jx'
		print 'Create Kardex'


		

		self.reset()





 		moves = self.env['stock.move'].search([

													('state','=','done')

													#('patient', '=', self.patient.name),
													#('product_id','like','protector')
											],
												#order='write_date desc',
												#limit=1,
											)
 		


 		print moves 
 		print 


 		for move in moves:

			source = move.location_id.name
			destination = move.location_dest_id.name




 			#if move.product_id.default_code == '01': 
 			if move.product_id.categ_id.name == 'Cremas': 


 				if not ( 

 							(source=='Inventory loss'  and  destination=='Cremas Despacho') 	or 
 							(source=='Cremas Despacho'  and  destination=='Customers') 			or
 							(source=='General'  and  destination=='Customers') 					or
 							(source=='Cremas Despacho'  and  destination=='Inventory loss') 	or 
 					
 							(source=='Pérdidas de inventario'  and  destination=='Cremas Despacho') 	or 
 							(source=='Cremas Despacho'  and  destination=='Clientes') 			or
 							(source=='Existencias'  and  destination=='Clientes') 				or
 							(source=='Cremas Despacho'  and  destination=='Pérdidas de inventario') 	#or 
 						): 


					#print move
					#print move.name
					#print move.product_id
					#print move.date 
					#print 


					# Coeff Negative !!!
					if (
						
							(source=='General' and destination=='Inventory loss')				or
							(source=='Existencias' and destination=='Pérdidas de inventario')	or

							(source=='General' and destination=='Cremas Despacho')				or
							(source=='Existencias' and destination=='Cremas Despacho')			or

							(source=='General' and destination=='Rebaja')						or
							(source=='Existencias' and destination=='Rebaja')					#or
						
						): 
						coeff = -1 

					else:
						coeff = 1





					# Create 
		 			stock_move_min = self.stock_move_min_ids.create({
																		'name': move.name,
																		'product_id': move.product_id.id, 
																		'date': move.date,


																		'qty': move.product_uom_qty * coeff, 

																		'source': move.location_id.name, 
																		'destination': move.location_dest_id.name, 
																		'picking': move.picking_id.name, 


																		'stock_move_all_id': self.id, 
		 			})

		 			print stock_move_min
		 			print 



		 			#stock_move = self.stock_moves.create({
					#													'name': move.name,
					#													'product_id': move.product_id.id, 
					#													'date': move.date,

					#													'stock_move_all_id': self.id, 
		 			#})
		 			#print stock_move
		 			#print 



