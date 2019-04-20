# -*- coding: utf-8 -*-

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp




# ----------------------------------------------------------- StockMove ------------------------------------------------------
class StockMove(models.Model):
	_inherit = 'stock.move'
	_description = "Stock Move"



	# Corrected Quantity 
	x_qty = fields.Float(
			'Qty - Corr', 
			digits=(16, 0), 

			compute='_compute_x_qty', 
		)

	@api.multi
	def _compute_x_qty(self):
		for record in self:
			coeff = -1
			record.x_qty = record.product_uom_qty * coeff


	x_note = fields.Char()


	x_categ_id = fields.Many2one(
			'product.category',
			'Internal Category', 
			store=True, 
			compute='_compute_x_categ_id', 
		)



	#@api.multi
	@api.depends('x_note')	
	def _compute_x_categ_id(self):
		for record in self:
			record.x_categ_id = record.product_id.categ_id



	# Quantity 
	product_uom_qty = fields.Float(
			'Quantity', 
			#digits_compute=dp.get_precision('Product Unit of Measure'),
			digits=(16, 0), 
			required=True, 			
			states={'done': [('readonly', True)]},
			help="jx ", 
		)







# ----------------------------------------------------------- StockMoveMin ------------------------------------------------------

class StockMoveMin(models.Model):	
	_name = 'stock.move.min'
	_description = "Stock Move Min"
	_order = 'product_id,date desc'



	name = fields.Char(
			string='Descripción',
		)

	x_type = fields.Selection(
			[	
				('topical', 		'Cremas'),
				('consumable', 		'Consumibles'),
			], 
			string='Tipo',
		)

	stock_move_all_id = fields.Many2one(
		'stock.move.all', 
	)

	product_id = fields.Many2one(
			'product.product', 			
			'Producto', 
			select=True, 
			domain=[('type', 'in', ['product', 'consu'])], 
		)

	date = fields.Datetime(
			string="Fecha", 
		)

	picking = fields.Char(
			string="Referencia", 
		)

	qty = fields.Float(
			string="Cantidad", 
		)

	source = fields.Char(
			'Origen', 
		)

	destination = fields.Char(
			'Destino', 
		)







# ----------------------------------------------------------- StockMoveAll ------------------------------------------------------

class StockMoveAll(models.Model):
	_name = 'stock.move.all'
	_description = "Stock Move All"



	name = fields.Selection(
			[	
				('topical', 		'Cremas'),
				('consumable', 		'Consumibles'),
			], 
			string='Nombre',
			required=True, 
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
			domain=[
						('type', 'in', ['product', 'consu']), 
						('categ_id', '=', 'Cremas'), 

					], 
		)



	@api.onchange('product_id')
	def _onchange_product_id(self):
		if self.product_id != False: 
				return {
							'domain': {'stock_move_min_ids': [
																('product_id', '=', self.product_id.name),
										]},
				}





	# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Reset 
	@api.multi 
	def reset(self):

		self.stock_move_min_ids.unlink()		
		self.product_id = False 


		# Stock move mins - Unlink !
		stock_move_mins = self.env['stock.move.min'].search([
																('x_type','=',self.name)
														],
																#order='write_date desc',
																#limit=1,
														)
		stock_move_mins.unlink()




	_hac = {
				'consumable': 			'Consumibles', 
				'topical': 				'Cremas', 
		}



	# Create Kardex 
	@api.multi 
	def create_kardex(self):

		#print 'jx'
		#print 'Create Kardex'

		self.reset()


 		moves = self.env['stock.move'].search([
													('state','=','done')
											],
												#order='write_date desc',
												#limit=1,
											)
 		#print moves 
 		#print 


 		for move in moves:
			source = move.location_id.name
			destination = move.location_dest_id.name

 			if move.product_id.categ_id.name == self._hac[self.name]: 

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



					# Coeff Negative !!!
					if (						
							(source=='General' and destination=='Inventory loss')				or
							(source=='Existencias' and destination=='Pérdidas de inventario')	or
							(source=='General' and destination=='Cremas Despacho')				or
							(source=='Existencias' and destination=='Cremas Despacho')			or
							(source=='General' and destination=='Rebaja')						or
							(source=='Existencias' and destination=='Rebaja')					or
							(source=='General' and destination=='Sala Láser 2')					or
							(source=='Existencias' and destination=='Sala Láser 2')				#or
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
																		'x_type': self.name, 
																		'stock_move_all_id': self.id, 
		 			})

		 			#print stock_move_min
		 			#print 


