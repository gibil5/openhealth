# -*- coding: utf-8 -*-
#
#
# 		*** Product Selector 
# 
# Created: 				25 Jan 2018
# Last updated: 	 	Id


from openerp import models, fields, api

import openerp.addons.decimal_precision as dp

from . import prodvars



class ProductSelector(models.Model):
	
	#_inherit = 'res.partner'

	#_order = 'write_date desc'

	_name = 'openhealth.product.selector'

	_description = 'Product Selector'







# ----------------------------------------------------------- Actions ------------------------------------------------------

	@api.multi
	def create_orderline(self):  

		print 
		print 'jx'
		print 'Create Orderline'


		ret = self.order_id.order_line.create({

													'product_id': self.product_id.id,

													'name': self.name,
															
													'order_id': self.order_id.id,

													'product_uom_qty': self.product_uom_qty, 


													#'price_subtotal': line.price_subtotal,
			
												})

		print ret
		print 







# ----------------------------------------------------------- Primitives ------------------------------------------------------

	name = fields.Text(
			string='Description', 
			required=True,

			compute='_compute_name', 
		)


	@api.multi
	#@api.depends('partner_id')

	def _compute_name(self):
		for record in self:

			if record.product_id.name != False: 
				record.name = record.product_id.name 





	treatment = fields.Selection(

			selection=[

							('laser_quick',		'Quick'), 
							('laser_co2',		'Co2'), 
							('laser_excilite',	'Excilite'), 
							('laser_ipl',		'IPL'), 
							('laser_ndyag',		'NDYAG'), 

				],

			string='Tratamiento', 
		)

	@api.onchange('treatment')
	
	def _onchange_treatment(self):

		print 'jx'
		print 'On change treatment'

		if self.treatment != False: 

			if self.x_type == 'service': 

				return {
						'domain': {'product_id': [
													
													('type', '=', self.x_type),
													('x_origin', '=', False),
													('x_family', '=', self.family),
													('x_treatment', '=', self.treatment),
									]},
				}









	zone = fields.Selection(

			#selection=[
			#				('laser_quick',		'Quick'), 
			#	],

			selection=prodvars._zone_list,
			
			string='Zona', 
		)

	@api.onchange('zone')
	
	def _onchange_zone(self):

		print 'jx'
		print 'On change zone'

		if self.zone != False: 

			if self.x_type == 'service': 

				return {
						'domain': {'product_id': [
													('type', '=', self.x_type),
													('x_origin', '=', False),
													('x_family', '=', self.family),
													('x_treatment', '=', self.treatment),
													('x_zone', '=', self.zone),

									]},
				}












	family = fields.Selection(

			selection=[
							# Service 
							('consultation',	'Consultas'), 
							('laser',			'Láser'),
							('medical',			'Tratamientos Médicos'), 
							('cosmetology',		'Cosmiatría'),


							# Product
							#('topical',			'Tópico'),
							#('kit',				'Kit'),
							#('card',			'Tarjeta'),
							#('none',		'none'),
				],

			string='Familia', 
		)

	@api.onchange('family')
	
	def _onchange_family(self):

		print 'jx'
		print 'On change family'

		if self.family != False: 


			if self.x_type == 'service': 

				return {
						'domain': {'product_id': [
													
													('type', '=', self.x_type),
													('x_origin', '=', False),
													('x_family', '=', self.family),
									]},
				}






















	x_type= fields.Selection(

			selection=[
							#('emr', 				'Historias'),
							('service', 				'Servicio'),
							('product', 				'Producto'),
						], 

			string='Tipo', 
			#required=True,
		)

	@api.onchange('x_type')
	
	def _onchange_x_type(self):

		print 'jx'
		print 'On change x_type'

		if self.x_type != False: 


			if self.x_type == 'product': 

				return {
						'domain': {'product_id': [
													#('x_treatment', '=', self.laser),
													#('x_zone', '=', self.zone),
													#('x_pathology', '=', self.pathology)
													('type', '=', self.x_type),
													('x_origin', '=', False),
													('categ_id', '=', 'Cremas'),
									]},
				}


			elif self.x_type == 'service': 

				return {
						'domain': {'product_id': [
													#('x_treatment', '=', self.laser),
													#('x_zone', '=', self.zone),
													#('x_pathology', '=', self.pathology)
													('type', '=', self.x_type),
													('x_origin', '=', False),
													#('x_family', 'in', ['laser','medical']),
									]},
				}






	default_code = fields.Char(
			string="Código", 
		)

	@api.onchange('default_code')
	def _onchange_default_code(self):

		print 'jx'
		print 'On change default_code'

		if self.default_code != False: 


			default_code = self.default_code


			product = self.env['product.product'].search([
																	#('name', '=', 'Paul Canales'),
																	('default_code', '=', default_code),
													],
													#order='date desc',
													limit=1,
												)
			print product
			print product.name 


			if product.name != False:
				self.product_id = product.id








	product_id = fields.Many2one(
			'product.product', 
			string='Product', 
			domain=[('sale_ok', '=', True)], 
			change_default=True, 
			ondelete='restrict', 
			required=True,
		)




	product_uom_qty = fields.Float(
			string='Quantity', 

			#digits=dp.get_precision('Product Unit of Measure'), 
			digits=(16, 0), 
			
			required=True, 
			
			#default=1.0,
		)


	price_unit = fields.Float(
			'Unit Price', 
			required=True, 
			digits=dp.get_precision('Product Price'), 
			default=0.0,
		)


	price_subtotal = fields.Monetary(
			#compute='_compute_amount', 
			string='Subtotal', 
			readonly=True, 
			store=True,
		)

	currency_id = fields.Many2one(
			related='order_id.currency_id', 
			store=True, 
			string='Currency', 
			readonly=True
		)



	order_id = fields.Many2one(
			'sale.order', 
			string='Order Reference', 
			required=True, 
			ondelete='cascade', 
			index=True, 
			copy=False, 
		)


