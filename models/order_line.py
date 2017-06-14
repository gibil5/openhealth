# -*- coding: utf-8 -*-
#
# 	Order Line
# 
#

from openerp import models, fields, api

import math
import jxvars



class sale_order_line(models.Model):

	_inherit='sale.order.line'
	#_name = 'openhealth.order_line'



	name = fields.Text(

			#string='Description', 
			string='Descripción', 

			required=True
		)


	product_id = fields.Many2one(
			'product.product', 
		
			#string='Product', 
			string='Producto', 
		
			domain=[('sale_ok', '=', True)], 
			change_default=True, 
			ondelete='restrict', 
			required=True
		)


	product_uom_qty = fields.Float(

			#string='Quantity', 
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


	#x_partner_vip = fields.Boolean(
	#		'Vip', 
			#readonly=True
	#		default=False, 
			#compute="_compute_partner_vip",
	#		)



	x_price_vip = fields.Float(
			string="Precio Vip",
		)




	price_total = fields.Float(	
			string="Total",
			compute="_compute_price_total",
		)

	#@api.multi
	@api.depends('price_unit', 'x_price_vip')
	
	def _compute_price_total(self):

		#print 
		#print 'Compute - Price Total'
		
		for record in self:

			if record.order_id.x_partner_vip  	and  	record.x_price_vip != 0.0:
				record.price_total = record.x_price_vip * record.product_uom_qty

			else: 
				record.price_total = record.price_unit * record.product_uom_qty





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




	#price_total = fields.Float(			
	#		string="Total",
			#compute="_compute_price_total",
	#	)








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


