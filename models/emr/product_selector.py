# -*- coding: utf-8 -*-
"""
	Product Selector - 		Highly Deprecated 2019

	Created: 				25 Jan 2018
 	Last up: 	 			24 April 2019

	Used by: Order

	24 Apr 2019:			Cleanup after 2019 PL. Must disappear:
							- Onchanges. 
"""
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp

class ProductSelector(models.Model):
	
	#_inherit = 'res.partner'

	#_order = 'write_date desc'

	_name = 'openhealth.product.selector'

	_description = 'Product Selector'



# ----------------------------------------------------------- Relational - Dep ------------------------------
	# Zone 
	#zone = fields.Many2one(
	#		'openhealth.zone',
	#		string='Zona', 
			#create_edit=False, 
	#	)



# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Create Order Line 
	@api.multi
	def create_orderline(self):  
		#print 
		#print 'Create Orderline'

		# Create 
		ret = self.order_id.order_line.create({
													'product_id': self.product_id.id,
													'name': self.name,
													'order_id': self.order_id.id,
													'product_uom_qty': self.product_uom_qty, 
													'x_price_manual': self.price_manual, 
												})
		# Prints 
		#print self.product_id
		#print self.name
		#print self.order_id
		#print self.product_uom_qty
		#print ret
		#print 


# ----------------------------------------------------------- Fields ------------------------------------------------------

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


	# Price manual flag 
	price_manual_flag = fields.Boolean(			
			string="Precio manual",
			required=False, 
		)


	# Price manual
	price_manual = fields.Float(			
			string="Valor",
			required=False, 
		)
	



	# Product 
	product_id = fields.Many2one(
			'product.product', 
			string='Product', 
			domain=[('sale_ok', '=', True)], 
			change_default=True, 
			ondelete='restrict', 
			required=False,
			#create_edit=False, 
		)



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
		)



	# Qty 
	product_uom_qty = fields.Float(
			string='Quantity', 
			digits=(16, 0), 
			required=True, 
			default=1.0,
		)


	# Price Unit 
	price_unit = fields.Float(
			'Unit Price', 
			required=True, 
			digits=dp.get_precision('Product Price'), 
			default=0.0,
		)


	# Price Sub
	price_subtotal = fields.Monetary(
			string='Subtotal', 
			readonly=True, 
			store=True,
		)


	# Currency 
	currency_id = fields.Many2one(
			related='order_id.currency_id', 
			store=True, 
			string='Currency', 
			readonly=True
		)


	# Order 
	order_id = fields.Many2one(
			'sale.order', 
			string='Order Reference', 
			required=True, 
			ondelete='cascade', 
			index=True, 
			copy=False, 
		)



# ----------------------------------------------------------- On Changes ------------------------------------------------------

	# Zone 
	@api.onchange('zone')	
	def _onchange_zone(self):
		#print 'jx'
		#print 'On change zone'
		if self.zone != False: 
			if self.x_type == 'service': 
				return {	'domain': {	'product_id': [
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
		#print 'jx'
		#print 'On change treatment'
		if self.treatment != False: 
			#print self.treatment
			if self.x_type == 'service': 
				return {	'domain': {	'product_id': [
														('type', '=', self.x_type),
														('x_origin', '=', False),
														('x_family', '=', self.family),
														('x_treatment', '=', self.treatment),
												], 
										'zone': 	[
														('treatment', '=', self.treatment),
													], 
								},
				}


	# Family 
	@api.onchange('family')
	def _onchange_family(self):
		#print 'jx'
		#print 'On change family'
		if self.family != False: 
			if self.x_type == 'service': 
				return {	'domain': {	'product_id': [			
														('type', '=', self.x_type),
														('x_origin', '=', False),
														('x_family', '=', self.family),
									]},
				}


	# Type 
	@api.onchange('x_type')
	def _onchange_x_type(self):
		#print 'jx'
		#print 'On change x_type'
		if self.x_type != False: 
			if self.x_type == 'product': 
				return {	'domain': {'product_id': [
														('type', '=', self.x_type),
														('x_origin', '=', False),
														('categ_id', '=', 'Cremas'),
									]},
				}
			elif self.x_type == 'service': 
				return {	'domain': {'product_id': [
														('type', '=', self.x_type),
														('x_origin', '=', False),
									]},
				}


	# Default Code 
	@api.onchange('default_code')
	def _onchange_default_code(self):
		#print 'jx'
		#print 'On change default_code'
		if self.default_code != False: 
			default_code = self.default_code
			product = self.env['product.product'].search([
																	('default_code', '=', default_code),
													],
													#order='date desc',
													limit=1,
												)
			#print product
			#print product.name 
			if product.name != False:
				self.product_id = product.id

