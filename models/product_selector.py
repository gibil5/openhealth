# -*- coding: utf-8 -*-
#
#
# 		*** Product Selector 
# 
# Created: 				25 Jan 2018
# Last updated: 	 	Id


from openerp import models, fields, api

import openerp.addons.decimal_precision as dp



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






	type= fields.Selection(

			#_get_product_template_type_wrapper, 

			selection=[
							#('emr', 				'Historias'),
							('service', 				'Servicio'),
							('product', 				'Producto'),
						], 

			string='Product Type', 
			#required=True,
		)









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


