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

		
		print self.product_id
		print self.name
		print self.order_id
		print self.product_uom_qty



		ret = self.order_id.order_line.create({

													'product_id': self.product_id.id,

													'name': self.name,
															
													'order_id': self.order_id.id,

													'product_uom_qty': self.product_uom_qty, 



													'x_price_manual': self.price_manual, 



													#'price_subtotal': line.price_subtotal,
												})

		print ret
		print 







# ----------------------------------------------------------- Primitives ------------------------------------------------------


	price_manual_flag = fields.Boolean(
			
			string="Precio manual",
			
			required=False, 
		)




	# Price manual
	price_manual = fields.Float(
			
			string="Valor",
			
			required=False, 
		)
	




	# Zone 
	zone = fields.Many2one(

			'openhealth.zone', 
			
			string='Zona', 
		)




	zone_co2 = fields.Many2one(

			'openhealth.zone.co2', 
			
			string='Zona Co2', 
		)


	zone_quick = fields.Many2one(

			'openhealth.zone.quick', 
			
			string='Zona quick', 
		)


	zone_excilite = fields.Many2one(

			'openhealth.zone.excilite', 
			
			string='Zona excilite', 
		)







	# Name 
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



	# Code 
	default_code = fields.Char(
			string="Código", 
		)




	# Treatment 
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




	# Family  
	family = fields.Selection(
			selection=[
							# Service 
							('consultation',	'Consultas'), 
							('laser',			'Láser'),
							('medical',			'Tratamientos Médicos'), 
							('cosmetology',		'Cosmiatría'),
				],

			string='Familia', 
		)


	# Type 
	x_type= fields.Selection(
			selection=[
							#('emr', 				'Historias'),
							('service', 				'Servicio'),
							('product', 				'Producto'),
						], 

			string='Tipo', 
			#required=True,
		)



# ----------------------------------------------------------- On changes ------------------------------------------------------



	# Zone 
	@api.onchange('zone')
	
	def _onchange_zone(self):

		print 'jx'
		print 'On change zone'

		if self.zone != False: 

			if self.x_type == 'service': 


				return {

							'domain': {

										'product_id': [
														('x_origin', '=', False),

														('type', '=', self.x_type),
														('x_family', '=', self.family),
														('x_treatment', '=', self.treatment),

														('x_zone', '=', self.zone.name_short),
													], 
									},
				}










	# Treatment 
	@api.onchange('treatment')
	
	def _onchange_treatment(self):

		print 'jx'
		print 'On change treatment'

		if self.treatment != False: 


			print self.treatment


			if self.x_type == 'service': 

				return {
						'domain': {

									'product_id': [
													
													('type', '=', self.x_type),
													('x_origin', '=', False),
													('x_family', '=', self.family),
													('x_treatment', '=', self.treatment),
												], 

									'zone': [
													('treatment', '=', self.treatment),
												], 

								},
				}

















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

			#required=True,
			required=False,
		)




	product_uom_qty = fields.Float(
			string='Quantity', 

			#digits=dp.get_precision('Product Unit of Measure'), 
			digits=(16, 0), 
			
			required=True, 
			
			default=1.0,
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


