# -*- coding: utf-8 -*-
#
# 	Order Line
# 

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp



class sale_order_line(models.Model):
	_inherit='sale.order.line'
	#_name = 'openhealth.order_line'






	@api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
	def _compute_amount(self):
		"""
		Compute the amounts of the SO line.
		"""
		for line in self:

			price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
			
			taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_id)
			
			line.update({
				'price_tax': taxes['total_included'] - taxes['total_excluded'],
				
				'price_total': taxes['total_included'],

				'price_subtotal': taxes['total_excluded'],
			})



	# Price Subtotal 
	#price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal - jx', readonly=True, store=True)


	#price_subtotal = fields.Float(
	#		string="Precio Vip",
	#		required=False, 

	#		compute='_compute_price_subtotal', 
	#	)







	# Price Unit
	price_unit = fields.Float(
		'Unit Price', 
		required=True, 
		digits=dp.get_precision('Product Price'), 
		default=0.0, 
	
		compute='_compute_price_unit', 
	)

	@api.multi
	def _compute_price_unit(self):

		for record in self:

			if record.x_comeback: 
				record.price_unit = record.product_id.x_price_vip_return

			else:		

				#if True: 
				#if record.order_id.pricelist_id.name == 'VIP': 
				if record.order_id.pricelist_id.name == 'VIP'		and 	record.x_price_vip != 0: 
					record.price_unit = record.x_price_vip

				else: 
					record.price_unit = record.x_price_std






	x_price_subtotal = fields.Monetary(
	#x_price_subtotal = fields.Float(
			string='Subtotal - jx', 
			readonly=True, 
			#store=True, 

			compute='_compute_x_price_subtotal', 
		)

	@api.multi
	def _compute_x_price_subtotal(self):
		for record in self:

			if record.x_comeback: 
				#record.price_subtotal = record.product_id.price_subtotal
				#record.price_subtotal = record.product_id.x_price_vip_return
				record.x_price_subtotal = record.product_id.x_price_vip_return
			

			else:		
				#record.price_subtotal = record.product_id.price_subtotal
				#record.price_subtotal = 55
				record.x_price_subtotal = 55











	# Price std
	x_price_std = fields.Float(
			string="Precio Std",
			required=False, 

			compute='_compute_price_std', 
		)


	@api.multi

	def _compute_price_std(self):

		for record in self:
			record.x_price_std = record.product_id.list_price





	# Price Vip
	x_price_vip = fields.Float(
			string="Precio Vip",
			required=False, 

			compute='_compute_price_vip', 
		)


	@api.multi

	def _compute_price_vip(self):

		for record in self:
			record.x_price_vip = record.product_id.x_price_vip






	# Price Vip
	x_price_vip_return = fields.Float(
			string="Precio Vip Return",
			required=False, 

			compute='_compute_price_vip_return', 
		)


	@api.multi

	def _compute_price_vip_return(self):

		for record in self:
			record.x_price_vip_return = record.product_id.x_price_vip_return









	# Comeback 
	x_comeback = fields.Boolean(
			string='Regreso', 		

			compute='_compute_comeback', 
		)


	@api.multi

	def _compute_comeback(self):

		for record in self:

			record.x_comeback = False


			for service in record.order_id.patient.x_service_quick_ids:

				if service.service.name == record.name  	and 	service.comeback: 
				
					record.x_comeback = True











	x_test = fields.Char(

			compute='_compute_test', 
		)


	@api.multi

	def _compute_test(self):

		for record in self:

			#record.x_test = record.order_id.partner_id.name
			#record.x_test = record.order_id.patient.name

			record.x_test = 'x'

			for service in record.order_id.patient.x_service_quick_ids:

				if service.service.name == record.name  	and 	service.comeback: 
				
					record.x_test = 'GOTCHA !'





	product_uom_qty = fields.Float(
		string='Quantity', 

		#required=True, 

		#digits=dp.get_precision('Product Unit of Measure'), 		
		#digits=(16, 1), 
		digits=(16, 0), 

		required=False,
		default=1.0
	)




	product_uom = fields.Many2one(
		'product.uom', 
		string='Unit of Measure', 
		#required=True
		required = False,
	)

#product_uom_qty = fields.Float(string='Quantity', digits=dp.get_precision('Product Unit of Measure'), required=True, default=1.0)
#product_uom = fields.Many2one('product.uom', string='Unit of Measure', required=True)


	customer_lead = fields.Float(
		'Delivery Lead Time', 

		#required=True, 
		required=False, 

		default=0.0,
		help="Number of days between the order confirmation and the shipping of the products to the customer", oldname="delay")



	order_id = fields.Many2one('sale.order', string='Order Reference', 
		
		#required=True, 
		required=False, 
		
		ondelete='cascade', index=True, copy=False)











