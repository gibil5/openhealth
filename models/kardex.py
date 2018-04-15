# -*- coding: utf-8 -*-
#
#
from openerp import models, fields, api

import unidecode			# Centos: yum install python-unidecode
import kardex_vars 




# ----------------------------------------------------------- Kardex ------------------------------------------------------

class Kardex(models.Model):

	_name = 'openhealth.kardex'
	_order = 'product'




	# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Dates all
	date_all = fields.Boolean(
			string="Todo", 
			default=False, 
		)

	# Date Begin 
	date_begin = fields.Date(
			string="Fecha Inicio", 
			default = fields.Date.today, 
		)

	# Date End
	date_end = fields.Date(
			string="Fecha Final", 
			default = fields.Date.today, 
		)

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

	vspace = fields.Char(
			' ', 
			readonly=True
		)




	# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Generate 
	@api.multi 
	def generate_kardex(self):
		self.remove_kardex()
		self.update_kardex()



	# Remove 
	@api.multi 
	def remove_kardex(self):
		self.stock_move_ids.unlink()



	# Update 
	@api.multi 
	def update_kardex(self):

		#print 'jx'
		#print 'Update'


		if self.product.name != False: 

			product_id = self.product.id 
			kardex_id = self.id 


			if self.location == 'platform':	
				moves = self.env['stock.move'].search([
															('product_id', '=', product_id),			
															('state', '=', 'done'),		
														],
														#order='start_date desc',
														#limit=1,
														)

			elif self.location == 'general': 
				#if self.date_all: 
				if True: 
					moves = self.env['stock.move'].search([

															('product_id', '=', product_id),			
															('state', '=', 'done'),		

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
			
				smove = self.stock_move_ids.create({
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
				total = total + move.qty 
			record.amount_total = total








# ----------------------------------------------------------- KardexMove ------------------------------------------------------

class KardexMove(models.Model):
	
	_name = "openhealth.kardex.move"
	_description = "Kardex Move"



	# Location 
	location = fields.Selection(
			[	
				('all', 			'Todo'),
				('general', 			'General'),
				('platform', 			'Plataforma'),
				('laser_2', 			'Laser 2'),
			], 
		)


	location_dest = fields.Char(
			'Destino', 
		)


	location_dest_tra = fields.Char(
			'Destino t', 

			compute='_compute_location_dest_tra', 
		)

	@api.multi
	def _compute_location_dest_tra(self):
		
		#print 'jx'
		#print 'Compute Location dest Tra'

		for record in self:
			foo = record.location_dest
			bar = " ".join(foo.split())
			bar = unidecode.unidecode(bar)
			dest = bar 
			if dest in kardex_vars._hlo: 
				dest_tra = kardex_vars._hlo[dest]
				record.location_dest_tra = dest_tra


	# Source 
	location_source = fields.Char(
			'Orígen', 
		)


	location_source_tra = fields.Char(
			'Orígen t', 

			compute='_compute_location_source_tra', 
		)

	@api.multi
	def _compute_location_source_tra(self):
		
		#print 'jx'
		#print 'Compute Location Source Tra'

		for record in self:
			foo = record.location_source
			bar = " ".join(foo.split())
			bar = unidecode.unidecode(bar)
			source = bar 
			if source in kardex_vars._hlo: 
				source_tra = kardex_vars._hlo[source]
				record.location_source_tra = source_tra



	coeff = fields.Float(
			'Coef', 
			default="1", 
			
			compute='_compute_coeff', 
		)


	@api.multi
	def _compute_coeff(self):
		for record in self:
			coeff = 0 
			if record.location == 'general': 
				if record.name != False:

					if record.location_source == 'General'		or 	record.location_source == 'Existencias': 
							coeff = -1

					elif record.location_source == 'Vendors'	or 	record.location_source == 'Vendedores': 
							coeff = 1


				elif (record.location_source == 'Inventory loss' and record.location_dest == 'General')  or  (record.location_source == 'Pérdidas de inventario' and record.location_dest == 'Existencias'): 
					coeff = 1


				elif (record.location_source == 'General' and record.location_dest == 'Inventory loss')  or  (record.location_source == 'Existencias' and record.location_dest == 'Pérdidas de inventario'): 
					coeff = -1


				if (record.location_source == 'General' and record.location_dest == 'Customers')  or  (record.location_source == 'Existencias' and record.location_dest == 'Clientes'): 
					coeff = 0


			elif record.location == 'platform': 
				coeff = 0 
				if record.name != False:
					if record.location_source == 'Cremas Despacho': 
						coeff = -1
					elif 'INT' in record.name: 
						coeff = 1

			elif record.location == 'all': 
				coeff = 1


			record.coeff = coeff






	qty = fields.Float( 
			'Cantidad', 

			compute='_compute_qty', 
		)

	@api.multi
	def _compute_qty(self):
		for record in self:
			record.qty = record.product_uom_qty * record.coeff



	name = fields.Char(
			'Nombre', 
		)


	kardex_id = fields.Many2one(
			'openhealth.kardex', 
		)


	date = fields.Datetime(
			'Fecha', 
			required=True, 
		)
	

	product_id = fields.Many2one(
			'product.product', 
			'Producto', 
			required=True, 
			domain=[('type', 'in', ['product'])], 
		)
	

	product_uom_qty = fields.Float(
			'Cantidad T', 
			required=True, 
		)

	




