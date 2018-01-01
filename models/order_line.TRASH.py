# -*- coding: utf-8 -*-
#
# 	Order Line
# 
#

from openerp import models, fields, api
import math


from . import jxvars



class sale_order_line(models.Model):

	_inherit='sale.order.line'
	#_name = 'openhealth.order_line'



	name = fields.Text(
			string='Descripción', 
			required=True
		)



	product_id = fields.Many2one(

			'product.product', 		
		
			string='Producto', 

			#domain=[('sale_ok', '=', True)], 

			
			domain=[
						('sale_ok', '=', True), 
					], 


			change_default=True, 
			ondelete='restrict', 
			required=True
		)



	product_uom_qty = fields.Float(
			string='Cantidad', 

			#digits=dp.get_precision('Product Unit of Measure'), 
			#required=True, 
			#default=1.0
		)


	#price_unit = fields.Float('Unit Price', required=True, digits=dp.get_precision('Product Price'), default=0.0)
	price_unit = fields.Float(
			'Precio', 
			required=True, 
			#digits=dp.get_precision('Product Price'), 
			default=0.0
		)

	#price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal', readonly=True, store=True)
	#price_tax = fields.Monetary(compute='_compute_amount', string='Taxes', readonly=True, store=True)
	#price_total = fields.Monetary(compute='_compute_amount', string='Total', readonly=True, store=True)








	order_id=fields.Many2one(

		'sale.order',
		
		string='Order',
		)



	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 
		)



	procedure_created = fields.Boolean(
			default=False,
		)



	_state_list = [
        			#('pre-draft', 'Pre-Quotation'),

        			('draft', 'Quotation'),
        			('sent', 'Quotation Sent'),
        			('sale', 'Sale Order'),
        			('done', 'Done'),
        			('cancel', 'Cancelled'),
        		]

	state = fields.Selection(
				selection = _state_list, 
				
				string="State",

				)







# ---------------------------------------------- Prices --------------------------------------------------------





	x_price_vip = fields.Float(
			string="Precio Vip",
		)





	#x_partner_vip = fields.Boolean(
	#		'Vip', 
			#readonly=True
	#		default=False, 
			#compute="_compute_partner_vip",
	#		)

	# Price total - Deprecated ? 
	#price_total = fields.Float(	
	#		string="Total",
	#		compute="_compute_price_total",
	#	)

	#@api.multi
	#@api.depends('price_unit', 'x_price_vip')
	
	#def _compute_price_total(self):
		
	#	for record in self:
	#		if record.order_id.x_partner_vip  	and  	record.x_price_vip != 0.0:
	#			record.price_total = record.x_price_vip * record.product_uom_qty
	#		else: 
	#			record.price_total = record.price_unit * record.product_uom_qty





	# Price subtotal 
	price_subtotal = fields.Float(	
			string="jx Sub-Total",
			compute="_compute_price_subtotal",
		)


	#@api.multi
	@api.depends('price_unit', 'x_price_vip')
	
	def _compute_price_subtotal(self):

		#print 
		#print 'Compute - Price Subtotal'
		
		for record in self:
		
			#if True: 
			#if record.x_partner_vip  	and  	record.x_price_vip != 0.0:
			if record.order_id.x_partner_vip  	and  	record.x_price_vip != 0.0:

					record.price_subtotal = record.x_price_vip * record.product_uom_qty


			else: 
				record.price_subtotal = record.price_unit * record.product_uom_qty












# ---------------------------------------------- Type --------------------------------------------------------

	# Type - Deprecated ?

	_x_type_list = [
						('service','Servicio'), 
						('consu','Producto'), 
					]


	x_type = fields.Selection(
			selection = _x_type_list, 

			string="Tipo",			
			compute='_compute_x_type', 			
			)
	
	#@api.multi
	@api.depends('product_id')

	def _compute_x_type(self):
		for record in self:
			record.x_type = record.product_id.type




#sale_order_line













# 31 Dec 2017


	@api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
	def _compute_amount(self):
		"""
		Compute the amounts of the SO line.
		"""
		for line in self:
			

			if line.x_comeback == True: 
				
				#price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
				price = line.x_price_vip_return * (1 - (line.discount or 0.0) / 100.0)
			
			else: 
				#price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
				price = 55
			



			taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_id)
			
			line.update({
				'price_tax': taxes['total_included'] - taxes['total_excluded'],
				'price_total': taxes['total_included'],
				'price_subtotal': taxes['total_excluded'],
			})






	@api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
	def _compute_amount(self):
		"""
		Compute the amounts of the SO line.
		"""
		for line in self:
			
			if line.x_comeback == True: 
				
				#price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
				price = line.x_price_vip_return * (1 - (line.discount or 0.0) / 100.0)
			
			else: 
				#price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
				price = 77
			



			taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_id)
			
			line.update({
				'price_tax': taxes['total_included'] - taxes['total_excluded'],
				'price_total': taxes['total_included'],
				'price_subtotal': taxes['total_excluded'],
			})




	#price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal - jx', readonly=True, store=True)
	
	price_subtotal = fields.Monetary(
		compute='_compute_amount', 
		string='Subtotal - jx', 
		readonly=True, 
		#store=True
	)



			
