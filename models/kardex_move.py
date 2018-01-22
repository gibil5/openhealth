# -*- coding: utf-8 -*-

from openerp import models, fields, api




class KardexMove(models.Model):
	
	#_inherit = 'stock.move'

	_description = "Kardex Move"

	_name = "openhealth.kardex.move"





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


	location_source = fields.Char(
			'Orígen', 
		)






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
			#'Quantity', 
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

			#'Date', 
			'Fecha', 
		
			required=True, 
			#select=True, 
			#help="Move date: scheduled date until move is done, then date of actual move processing", 
			#states={'done': [('readonly', True)]}
		)
	



	product_id = fields.Many2one(
			'product.product', 


			#'Product', 
			'Producto', 


			required=True, 
			#select=True, 

			#domain=[('type', 'in', ['product', 'consu'])], 
			domain=[('type', 'in', ['product'])], 
			
			#states={'done': [('readonly', True)]}
		)
	


	product_uom_qty = fields.Float(

			#'Quantity', 
			'Cantidad T', 
		
			#digits_compute=dp.get_precision('Product Unit of Measure'),
			required=True, 
			#states={'done': [('readonly', True)]},
		)

	
